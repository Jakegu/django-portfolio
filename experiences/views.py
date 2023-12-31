from django.shortcuts import render, redirect
from .forms import ExperienceForm
from .models import Experience

def experience_list(request):
    experiences = Experience.objects.all()
    return render(request, 'experiences/experience_list.html', {'experiences': experiences})

#Homework
#Display the form in the html

def experience_new(request):
    if request.method == 'POST':
        form = ExperienceForm(request.POST, request.FILES)
        if form.is_valid():
            experience = form.save()
            return redirect('experience_list')


    else:
        form = ExperienceForm()


    return render(request, 'experiences/experience_new.html', {
        'form': form
    })
