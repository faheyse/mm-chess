from django.shortcuts import render
from .models import Testimonial

reviews = list(Testimonial.objects.all())

# Create your views here.
def home(request):

	context = {
	        	'name1': reviews[0].name,
	            'review1': reviews[0].review,
	            'name2': reviews[1].name,
	            'review2': reviews[1].review,
	            'name3': reviews[2].name,
	            'review3': reviews[2].review,
	            'name4': reviews[3].name,
	            'review4': reviews[3].review,
	            'name5': reviews[4].name,
	            'review5': reviews[4].review,
	            'name6': reviews[5].name,
	            'review6': reviews[5].review,
        	}

	return render(request, 'testimonials/home.html', context)

def about(request):
	return render(request, 'testimonials/about.html')
