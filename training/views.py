from django.shortcuts import render, redirect
from .models import Training , Trainee
from.forms import TrainingModelForm
from django.contrib import messages


def all_trainings(request):
    from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
    all_trainings_list = Training.objects.all()
    total_training_nos=len(all_trainings_list)
    trainings_per_page = 20
    paginator = Paginator(all_trainings_list, trainings_per_page)
    page = request.GET.get('page')
    try:
        trainings = paginator.page(page)
    except PageNotAnInteger:
        trainings = paginator.page(1)
    except EmptyPage:
        trainings = paginator.page(paginator.num_pages)
    context = {'trainings': trainings,'total_training_nos':total_training_nos}
    return render(request, 'training/all.html', context)

def trainees(request):
    trainees=Trainee.objects.filter(training__id=request.GET.get('training_id'))
    training=Training.objects.get(id=request.GET.get('training_id'))
    return render(request, 'training/trainees.html', {'trainees':trainees,'training':training})

def add_training(request):
    if request.method == 'POST':
        form = TrainingModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Training added successfully")
            return redirect('/training')
    else:
        form = TrainingModelForm()
    return render(request, 'training/add_training.html', {'form': form})

def edit_training(request):
    training = Training.objects.get(id=request.GET['training_id'])
    if request.method == 'POST':
        form = TrainingModelForm(request.POST, request.FILES, instance=training)
        if form.is_valid():
            form.save()
            messages.success(request, "training updated successfully")
            return redirect('/training')
    else:
        form = TrainingModelForm(instance=training)
    return render(request, 'training/edit_training.html', {'form': form})