from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index,name='index'),
    path('addproduct/',views.add_product,name='addproduct')
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URLS,document_root=settings.MEDIA_URLS)