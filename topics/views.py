from django.shortcuts import render

# Create your views here.

def topics(request):
    return render(request, 'topics.html', {})