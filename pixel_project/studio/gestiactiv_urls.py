"""URLconf de l'espace GestiActiv (sous-domaine gestiactiv.*).

Servi par `studio.middleware.GestiActivHostMiddleware` : les requêtes du
sous-domaine sont routées ici, avec SSO (même session) que le site principal.
"""
from django.conf import settings
from django.http import HttpResponse
from django.urls import path, re_path
from django.views.generic.base import RedirectView
from django.views.static import serve as static_serve
from django.contrib.staticfiles.storage import staticfiles_storage

from . import views


def robots(request):
    return HttpResponse("User-agent: *\nDisallow: /\n", content_type="text/plain")


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(
        url=staticfiles_storage.url('favicon.svg'), permanent=True)),
    path('robots.txt', robots),

    # Accueil / authentification
    path('', views.gestiactiv_home, name='gestiactiv_home'),
    path('login/', views.gestiactiv_login, name='gestiactiv_login'),
    path('connexion/', views.gestiactiv_login, name='gestiactiv_login_alias'),
    path('register/', views.gestiactiv_register, name='gestiactiv_register'),
    path('inscription/', views.gestiactiv_register, name='gestiactiv_register_alias'),
    path('logout/', views.gestiactiv_logout, name='gestiactiv_logout'),
    path('deconnexion/', views.gestiactiv_logout, name='gestiactiv_logout_alias'),
    path('onboarding/', views.gestiactiv_onboarding, name='gestiactiv_onboarding'),

    # Espace client
    path('dashboard/', views.gestiactiv_espace, name='gestiactiv_espace'),

    # Backends métiers (par activité)
    path('auto-ecole/', views.gestion_auto_ecole, name='g_auto_ecole'),
    path('sante/', views.gestion_sante, name='g_sante'),
    path('hotel/', views.gestion_hotel, name='g_hotel'),
    path('commerce/', views.gestion_commerce, name='g_commerce'),
    path('juridique/', views.gestion_juridique, name='g_juridique'),
    path('comptabilite/', views.gestion_comptabilite, name='g_comptabilite'),
    path('rh/', views.gestion_rh, name='g_rh'),
    path('restaurant/', views.gestion_restaurant, name='g_restaurant'),
    path('patisserie/', views.gestion_patisserie, name='g_patisserie'),

    # API (JSON, réutilisées du site principal)
    path('api/connexion/', views.api_connexion, name='g_api_connexion'),
    path('api/inscription/', views.api_inscription, name='g_api_inscription'),
    path('api/deconnexion/', views.api_deconnexion, name='g_api_deconnexion'),
]

# Fichiers media servis quel que soit DEBUG (embarqués dans l'image Docker).
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', static_serve, {'document_root': settings.MEDIA_ROOT}),
]
