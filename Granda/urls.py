from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView


urlpatterns = [
	url(r'^jet/', include('jet.urls', 'jet')),
	url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
	url(r'^admin/', admin.site.urls),
	url(r'^ingresar/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^registro/$', auth_views.logout, {'template_name': 'registro.html'}, name='registro'),



	url(r'', include("reservaciones.urls")),



]
