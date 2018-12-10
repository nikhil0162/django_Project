from django.shortcuts import render
from .models import CarPost
from django.contrib import messages
from .forms import CarForm
from django.views.generic import DetailView, ListView, CreateView
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

class CarPostListView(ListView):
	model = CarPost
	template_name = 'blog/cars.html'  # <app>/<model>_<viewtype>.html
	ordering = ['-date_posted']
	context_object_name = 'cars'

class CarPostDetailView(DetailView):
	model = CarPost

class CarPostCreateView(CreateView):
	model = CarPost
	fields = ['company_name', 'model_name', 'image', 'launched_date']

	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		return super().form_valid(form)


def search(request):
	if request.method == 'POST':
		srch = request.POST.get('q')

		if srch:
			match = CarPost.objects.filter(Q(company_name__icontains= srch) | Q(model_name__icontains= srch))

			if match:
				return render(request, 'blog/cars.html', {'cars':match})
			else:
				return messages.error(request, "no result found!")
		else:
			return HttpResponseRedirect('/search_post/')
	return render(request, 'blog/cars.html')


def search_users(request):
	if request.method == 'POST':
		srch = request.POST.get('qname')
	else:
		srch = ''

	result = User.objects.filter(Q(username__icontains=srch))
	return render(request, 'blog/searching.html',{'results': result})
