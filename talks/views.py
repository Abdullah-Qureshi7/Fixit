from django.shortcuts import render
from .models import talks
from .forms import talksform, UserRegistrationForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'index.html')

def talk_list(request):
    talks_All = talks.objects.all().order_by('-created_at')
    return render(request,'talks_list.html', {'talks': talks_All})

@login_required
def talk_create(request):
    if request.method == "POST":
       form = talksform(request.POST, request.FILES)
       if form.is_valid():
          talk = form.save(commit=False)
          talk.user = request.user
          talk.save()
          return redirect ('talk_list')
    else:
        form = talksform()
    return render(request, 'talk_form.html', {'form': form})

@login_required
def talk_edit(request, talk_id):
    talk = get_object_or_404(talks, pk= talk_id, user = request.user)
    if request.method == 'POST':
        form = talksform(request.POST, request.FILES, instance=talk)
        if form.is_valid() :
            talk = form.save(commit=False)
            talk.user = request.user
            talk.save()
            return redirect('talk_list')
    else:
        form = talksform(instance= talk)
        return render(request, 'talk_form.html', {'form': form})

@login_required
def talk_delete (request, talk_id):
    talk = get_object_or_404(talks, pk = talk_id, user= request.user)
    if request.method == 'POST':
        talk.delete()
        return redirect('talk_list')
    return render (request, 'talk_confirm_delete.html', {'talk': talk})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('talk_list')
    else:
       form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})
