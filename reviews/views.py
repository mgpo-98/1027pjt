from django.shortcuts import render, redirect
from reviews.forms import CommentForm, ReviewForm
from reviews.models import Review, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html', context)

def create(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user 
            review.save()
            return redirect('reviews:index')
    else:
        review_form = ReviewForm()
    context = {
        'review_form' : review_form,
    }
    return render(request,'reviews/form.html', context)

def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user: 
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('reviews:detail', review.pk)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            'review_form': review_form
        }
        return render(request, 'reviews/form.html', context)
    else:
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('reviews:detail', review.pk)

def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')


def detail(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm()
    context = {
        'review' : review,
        'comments': review.comment_set.all(),
        'comment_form' : comment_form,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def like(request ,pk):
    review = Review.objects.get(pk=pk)
    if request.user in review.like_users.all() :
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('reviews:detail', pk)

@login_required
def comment_create(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect('reviews:detail', review.pk)


def comment_delete(request, pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    comment.delete()
    return redirect('reviews:detail', pk)