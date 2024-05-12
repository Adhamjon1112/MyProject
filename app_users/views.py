from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
from .models import Note

from .forms import UserRegistrationForm, NoteForm

User = get_user_model()


def user_registration(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        try:
            user = User.objects.get(email=email)
        except:
            user = None

        if password1 == password2 and not user:
            user = User.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                username=username,
                email=email,
            )
            user.set_password(password2)
            user.save()
            return redirect('login')


    form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'app_users/registration.html', context)


def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user_exists = user.check_password(password)
        except:
            user_exists = None
            user = None

        if user_exists:
            login(request, user)
            return redirect('notes_list')
    return render(request, 'app_users/login.html')



@login_required
def notes_list(request):
    notes = Note.objects.filter(owner=request.user)
    context={
        'notes': notes, 
        'owner': request.user
    }
    return render(request, 'app_users/notes.html', context)

@login_required
def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    return render(request, 'app_users/note.html', {'note': note})

@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    context={ 
        'form': form
    }    
    return render(request, 'app_users/form.html', context)

@login_required
def note_update(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm(instance=note)
    context={
        'form': form
    }
    return render(request, 'app_users/form.html', context)

@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id, owner=request.user)
    note.delete()
    return redirect('notes_list')

