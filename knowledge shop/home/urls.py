from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('contact', views.contact),
    path('sell', views.sell),
    path('buy', views.buy),
    path('jee', views.jee),
    path('cbse', views.cbse),
    path('state', views.state),
    path('icse', views.icse),
    path('defence', views.defence),
    path('engg', views.engg),
    path('good', views.good),
    path('fibuy/<int:id>', views.fibuy),
    path('fibuy', views.final),

]
