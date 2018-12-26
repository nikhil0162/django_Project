from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import CarPost
from django.contrib import messages
from .forms import CarForm
from django.views.generic import DetailView, ListView, CreateView, DeleteView
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse_lazy

def home(request):
    return render(request, 'blog/home.html', {'title': 'Home'})

import json
def apiJson(request):
	emp={
		'name': 'Ramanuj',
		'age': 25,
		'sal': 60000,
		'city': 'Rohtak',
	}
	representation = f"Name {emp['name']},<br> age {emp['age']}, <br>sal {emp['sal']}, <br>city {emp['city']}"
	rd = json.dumps(emp)
	return HttpResponse(rd)

class CarPostDetailView(DetailView):
	model = CarPost


class CarPostCreateView(CreateView):
	form_class = CarForm
	success_url = reverse_lazy('blog-cars')
	template_name = 'blog/carpost_form.html'

	def form_valid(self, form):
		form.instance.posted_by = self.request.user
		form.save()
		return super(CarPostCreateView, self).form_valid(form)


class CarPostListView(ListView):
	model = CarPost
	template_name = 'blog/cars.html'  # <app>/<model>_<viewtype>.html
	ordering = ['-date_posted']
	context_object_name = 'cars'


class CarPostDeleteView(DeleteView):
	model = CarPost
	template_name = 'blog/car_detail.html'
	success_url = reverse_lazy('blog-cars')


def search(request):
	if request.method == 'POST':
		srch = request.POST.get('q')

		if srch:
			match = CarPost.objects.filter(Q(company_name__icontains= srch) | Q(model_name__icontains= srch))

			if match:
				return render(request, 'blog/cars.html', {'cars':match})
			else:
				return HttpResponse("<h1>no result found!</h1>")
		else:
			return HttpResponseRedirect('/search_post/')
	return render(request, 'blog/cars.html')


