from unittest.mock import patch
from django.contrib import admin
from django.urls import path
from desafio.views import family, datfamily_template
from datefamily.views import create_family, list_datefamily

urlpatterns = [
    path('admin/', admin.site.urls),
    path("family/", family, name="family"),
    path("datfamily_template/", datfamily_template, name="datfamily_template"),
    path("create_family/", create_family, name ="create_family"),
    path("list_datefamily/", list_datefamily, name="list_datefamily")
    
]
