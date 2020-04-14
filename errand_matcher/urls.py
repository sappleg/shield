from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('volunteer', views.begin_signup, name='begin_signup'),
    path('confirmation', views.confirm_email, name='confirm_email'),
    path('activate/<uuid:token_id>', views.activate, name='activate'),
    path('health', views.health_and_safety, name='health_and_safety'),
    path('requestor', views.requestor_signup, name='requestor'),
    path('errand', views.request_errand, name='request_errand'),
]
