from django.shortcuts import render
from django.db.models import Q
from .models import Person

# Create your views here.
def index(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # persons = Person.objects.filter(first__icontains=q)
        persons = Person.objects.filter(Q(first__icontains=q) | 
        Q(last__icontains=q)| 
        Q(age__icontains=q) | 
        Q(Country__icontains=q) )
    else:
        persons = Person.objects.all()

    context = {
        'persons':persons
    }
    return render(request, 'index.html', context=context)
