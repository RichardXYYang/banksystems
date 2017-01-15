from django.shortcuts import render
from bank.models import Musician
from bank.models import LoginForm

# Create your views here.

def home(request):
	content = {
		'message': 'welcome to my bank system'
		}
	musician = Musician(first_name='Richard', last_name='Richman', instrument='violin');
	musician.save(); 
	return render(request, 'login.html', content)
#branch
def login(request):
	username = "not logged in"
# 	username.upper();
 	if request.method == "POST":
 #Get the posted form
 		MyLoginForm = LoginForm(request.POST)
 		if MyLoginForm.is_valid():
 			username = MyLoginForm.cleaned_data['username']
			password =  MyLoginForm.cleaned_data['password']
			MyLoginForm = LoginForm(username=username, password=password);
		else:
			MyLoginForm = LoginForm(username=username, password='aaaa');
	return render(request, 'home.html', {"username" : username})
