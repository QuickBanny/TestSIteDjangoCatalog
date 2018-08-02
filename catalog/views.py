from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from catalog.models import Image
from catalog.form import ImageForm
from django.db.models import Q
from django.http import HttpResponseForbidden

class ImageDetailView(DetailView):
	model = Image
	context_object_name = 'image_details'
	template_name = 'catalog/image.html'

	def get_query_set(self):
		return get_object_or_404(Image, id=self.kwargs['spk'])

class ImageSearchListView(ListView):
	model = Image
	paginate_by = 100

	def get_queryset(self):
		res = super(ImageSearchListView, self).get_queryset()

		query = self.request.GET.get('q')
		query_date = self.request.GET.get('search_date')
		if query and query_date:
			res = res.filter(
				Q(name__startswith=query) | Q(desc__startswith=query)|
				Q(date=query_date))
		return res

class ImageEditViews(UpdateView):
	model = Image
	form_class = ImageForm
	template_name = 'catalog/edit.html'
	success_url = '/catalog/search/'

	def get_query_set(self):
		return get_object_or_404(Image, id=self.kwargs['spk'])



def model_form_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ImageForm()
    return render(request, 'catalog/add_modal.html', {
        'form': form
    })

class ImageDeleteViews(DeleteView):
    model = Image
    template_name = 'catalog/delet.html'
    success_url = '/catalog/search/'
    def get_query_set(self):
    	return get_object_or_404(Image, id=self.kwargs['spk'])

def index(request):
	return render(request, 'catalog/home.html')
