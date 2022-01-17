from django.shortcuts import render

# Create your views here.
from reviews.models import Review


def review_get(request):
    all_reviews = Review.objects.all().filter(is_confirm=1)
    return render(request, 'review.html', {'reviews': all_reviews})
