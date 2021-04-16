from django.contrib import admin
from django.urls import path, include
import teamplapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', teamplapp.views.index, name="index"),
    path('project/', include('project.urls')),
    path('account/', include('account.urls')),
]
