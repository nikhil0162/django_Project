from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import CarPost
from django.contrib import messages
from .forms import CarForm, CarUpdateForm
from django.views.generic import DetailView, ListView, CreateView, DeleteView, TemplateView, UpdateView
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# from django.conf.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from  tracking_analyzer.models import Tracker




# def send_mail_example()

def home(request):
	print(request.META.get('REMOTE_ADDR'))
	print(request.META.get('HTTP_X_FORWARDED_FOR'))
	return render(request, 'blog/home.html', {'title': 'Home'})

# class Home(TemplateView):



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

	def get_object(self, queryset=None):
		obj = super(CarPostDetailView, self).get_object(queryset)
		# Tracker.objects.create_from_request(self.request, obj)
		return obj

# import bleach
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

	# def render_to_response(self, context, **response_kwargs):
	# 	qs = CarPost.objects.all()
	# 	context = {
	# 		'cars': qs,

	# 	}
	# 	Tracker.objects.create_from_request(self.request, qs.first().name)
	# 	return render_to_response('blog/cars.html', context)

# from django.urls import reverse
class CarPostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = CarPost
	template_name = 'blog/car_detail.html'
	success_url = reverse_lazy('blog-cars')

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.posted_by:
			return True
		return False


class CarPostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = CarPost
	form_class = CarUpdateForm
	template_name = 'blog/carpost_update.html'
	success_url = reverse_lazy('blog-cars')

	def test_func(self):
		post = self.get_object()
		return self.request.user == post.posted_by





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


def send_mail_by_me(request):
	print("triggred")
	return render(request, 'blog/sms_sending.html')
