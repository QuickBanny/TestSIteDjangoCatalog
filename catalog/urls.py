from django.urls import path, include
from django.views.generic import ListView, DetailView
from django.conf.urls.static import static
from catalog.models import Image
from testsite import settings
from . import views
from catalog.views import ImageDetailView, ImageSearchListView, ImageEditViews, ImageDeleteViews

urlpatterns = [
	path('', views.index, name='index'),
	path('catalog/', ListView.as_view(queryset=Image.objects.all().order_by("-date")[:25],
										template_name='catalog/image_list.html')),
	path('catalog/<int:pk>/', ImageDetailView.as_view(), name='image_detail_views'),
	path('catalog/search/', ImageSearchListView.as_view()),
	path('catalog/add/', views.model_form_upload, name='catalog/add_modal.html'),
	path('catalog/<int:pk>/edit/', ImageEditViews.as_view(), name="image_edit_views"),
	path('catalog/<int:pk>/delet/', ImageDeleteViews.as_view(), name="image_delete_views")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)