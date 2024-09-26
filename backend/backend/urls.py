from django.views.generic import TemplateView
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path, include
from Todo import views
from rest_framework import routers

# Create a router object
router = routers.DefaultRouter()
# Register the router
router.register(r'tasks', views.TodoView, 'task')

urlpatterns = [
    path("admin/", admin.site.urls),
    # Route for the Django REST framework
    path('api/', include(router.urls)),
    # Serve React frontend
    path('', TemplateView.as_view(template_name='index.html'), name='home'),  # Add a name for easier reference
    # Serve static files
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve additional files (React build)
urlpatterns += [
    path('build/<path:path>', serve, {'document_root': settings.REACT_APP_BUILD_DIR}),  # Remove trailing slash for consistency
]

# Serve manifest.json specifically if needed
urlpatterns += [
    path('manifest.json', serve, {'document_root': settings.REACT_APP_BUILD_DIR}),
]
