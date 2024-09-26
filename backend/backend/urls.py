"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from Todo import views
# import routers from the REST framework # it is necessary for routing
from rest_framework import routers
# create a router object
router = routers.DefaultRouter()
# register the router
router.register(r'tasks',views.TodoView, 'task')


urlpatterns = [
    path("admin/", admin.site.urls),
    # add another path to the url patterns
    # when you visit the localhost:8000/api
    # you should be routed to the django Rest framework
    path('api/', include(router.urls))
]
# Serve React frontend
urlpatterns += [
    path('', TemplateView.as_view(template_name='index.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve additional files if needed
urlpatterns += [
    path('build/<path:path>/', serve, {'document_root': settings.REACT_APP_BUILD_DIR}),
]
