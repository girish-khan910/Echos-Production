from django.urls import path, include

urlpatterns = [
    path('api/contact/', include('contact.urls')),
]
