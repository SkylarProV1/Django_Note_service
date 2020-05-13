import requests 

headers={}

nome='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6InNreUB5YW5kZXgucnUiLCJleHAiOjE1ODkzMjI5MzMsImVtYWlsIjoic2t5QHlhbmRleC5ydSJ9.zrOG3dpkTb0ebKTT0u-ioKZGHR-Oa8YOLW5CyHMpJNs'
headers['Authorization']=f"JWT {nome}"

#r=requests.get('http://127.0.0.1:8000/api/notes' ,headers=headers)
#api/notes/21/edit/',headers=headers)
#data={"title":"BATYA","body":"<p>MAY</p>",'tags':['bay']}
#print(r.text)

r=requests.post('http://127.0.0.1:8000/api/register' ,data={"email":"skywayto@yandex.ru","password":"123"})
print(r.text)

"""
[{"id":21,"title":"Super","body":"<p>okss</p>","pub_date":"2020-04-30T12:17:55.015109+03:00","tags":["noce"]},{"id":24,"title":"Oksss","body":"<p>okss</p>","pub_date":"2020-05-02T16:05:53.735069+03:00","tags":["pass"]},{"id":25,"title":"Super","body":"<p>eeee</p>","pub_date":"2020-05-02T16:06:02.852909+03:00","tags":["eeee"]}]
"""