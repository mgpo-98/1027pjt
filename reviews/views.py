import re
from django.shortcuts import render, redirect
from reviews.forms import ReviewForm
from reviews.models import Review

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)

            review.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }
    return render(request,'reviews/form.html', context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    context = {
        'review' : review,
    }
    return render(request, 'reviews/detail.html', context)
    
