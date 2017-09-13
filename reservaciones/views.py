from django.shortcuts import render, redirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import Perfil

from reservaciones.forms import UsuarioForm
from .forms import RegisterForm

from django import forms

# Create your views here.
def mostrar_inicio(request):
	return render(request, 'aplicacion/index.html',{})

def mostrar_contactos(request):
	return render(request, 'aplicacion/contact.html',{})

def mostrar_quienes(request):
	return render(request, 'aplicacion/elements.html',{})

def mostrar_carro(request):
	return render(request, 'aplicacion/shopping-cart.html',{})

def mostrar_maquinaria(request):
	return render(request, 'aplicacion/maquinaria.html',{})


def mostrar_herramienta(request):
	return render(request, 'aplicacion/herramienta.html',{})


def mostrar_detalle(request):
	return render(request, 'aplicacion/checkout-billing-details.html',{})

def mostrar_login(request):
	return render(request, 'aplicacion/login.html',{})

def mostrar_alquiler(request):
	return render(request, 'aplicacion/index1.html',{})

class UserFormView(View):
	form_class = UserForm
	template_name = 'aplicacion/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user.set_password(password)
			user.save()

			user = authenticate(username=username, password=password)
			if user.is_active:
				login(request, user)
				return redirect('login')

		return render(request, self.template_name, {'form': form})


def usuario(request):
	if request.method=="POST":
		perfil_form= UsuarioForm(request.POST)

		if perfil_form.is_valid():
			try:
				user= perfil_form.save(commit=False)	
				usermane= perfil_form.cleaned_data['username']
				gmail= perfil_form.cleaned_data['gmail']
				first_name= perfil_form.cleaned_data['first_name']
				last_name= perfil_form.cleaned_data['last_name']
				password = perfil_form.cleaned_data['password']
				user.set_password(password)
				user= authenticate(username= username, password= password)
				user.save()
				if user.is_active:
					login(request, user)
					return redirect('login')

				perfil_form.save()
				return render( request, 'aplicacion/checkout-billing-details.html',{'perfil_form':perfil_form})
			except:
				return render(request , seft.template_name, {'perfil_form':perfil_form}
			)

	
	else:
		perfil_form= UsuarioForm()

	return render(request, 'aplicacion/registro.html' , {'perfil_form':perfil_form})


