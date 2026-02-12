from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.contact_list,name='home'),
    path('add/',views.add_contact,name='addcontact'),
    path('update/<int:contact_id>/',views.edit_contact,name='edit'),
    path('delete/<int:contact_id>/',views.delete_contact,name='delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)