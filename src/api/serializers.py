from rest_framework import serializers
from taggit.managers import TaggableManager
from notes.models import Note
from accounts.models import User
from django.contrib.auth import get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from accounts.tokens import account_activation_token
from django.core.mail import EmailMessage



class TagSerializerField(serializers.ListField):
	child = serializers.CharField()

	def to_representation(self, data):
		return data.values_list('name', flat=True)


class TagSerializer(serializers.ModelSerializer):

	tags = TagSerializerField()

	def create(self, validated_data):
		tags = validated_data.pop('tags')
		instance = super(TagSerializer, self).create(validated_data)
		instance.tags.set(*tags)
		return instance


class NoteSerializer(serializers.ModelSerializer):

	tags = TagSerializerField()

	def create(self, validated_data):
		tags = validated_data.pop('tags')
		instance = super(TagSerializer, self).create(validated_data)
		instance.tags.set(*tags)
		return instance

	def update(self, instance, validated_data):
		instance.title=validated_data.get('title', instance.title)
		instance.body=validated_data.get('body', instance.body)
		instance.tags=validated_data.get('tags', instance.tags)
		instance.public=validated_data.get('public', instance.public)
		instance.save()
		return instance

	class Meta:
		model = Note
		fields = ('id', 'title', 'body', 'pub_date','tags','public')


class PublicSerializer(serializers.ModelSerializer):

	"""
	def update(self, instance, validated_data):
		instance.title=validated_data.get('title', instance.title)
		instance.body=validated_data.get('body', instance.body)
		instance.public=validated_data.get('public', instance.public)
		instance.save()
		return instance
	"""

	class Meta:
		model = Note
		fields = ('id', 'title', 'body','public')


User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):

	password = serializers.CharField(write_only=True)

	def create(self, validated_data):

		user = User.objects.create(
            email=validated_data['email']
        )
		user.set_password(validated_data['password'])
		user.is_active=False

		#current_site = get_current_site(self)
		mail_subject = 'Activate your blog account.'
		message = render_to_string('acc_active_email.html', {
	                'user': user,
	                'domain': "127.0.0.1:8000",
	                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
	                'token': account_activation_token.make_token(user),
				})
				
		to_email = user.email
		email = EmailMessage(
			mail_subject, message, to=[to_email]
				)
		email.send()
		user.save()

		return user


	class Meta:
		model = User
		fields = ('id','email','password')




