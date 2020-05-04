from django.contrib.auth import authenticate, login
from django.views.generic import FormView
from .forms import UserCreationForm
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
#from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
#from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from .models import User

from django.utils.encoding import force_text


from django.urls import reverse_lazy


from django.contrib import messages

class RegisterView(FormView):

	
	template_name = 'registration/register.html' 
	form_class = UserCreationForm
	success_url = '/'


	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		email = request.POST['email']
		password = request.POST['password1']
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(self.request)
			mail_subject = 'Activate your blog account.'
			message = render_to_string('acc_active_email.html', {
	                'user': user,
	                'domain': current_site.domain,
	                'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode('utf-8'),
	                'token': account_activation_token.make_token(user),
				})
				
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
	                        mail_subject, message, to=[to_email]
				)
			print(message)
			print(email)
			email.send()
			messages.success(self.request, ('Please Confirm your email to complete registration.'))


			#return redirect('/')
			#return redirect('login')
			return HttpResponse('Please confirm your email address to complete the registration')# подкорректировать
		return redirect('/')
		#return super(RegisterView, self).form_valid(form)



class Activate(FormView):
	template_name = 'registration/login.html' 
	form_class = UserCreationForm

	def get(self, request, uidb64, token, *args, **kwargs):
		try:
			uid = urlsafe_base64_decode(uidb64).decode('utf-8')
			user = User.objects.get(pk=uid)
		except Exception as e :
			pritnt("OOOOOOOO",e)
			user = None

		if user is not None and account_activation_token.check_token(user, token):
			user.is_active = True
			#user.profile.email_confirmed = True
			user.save()
			login(request, user)
			messages.success(request, ('Your account have been confirmed.'))
			return redirect('/')
		else:
			messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
			return redirect('/')
