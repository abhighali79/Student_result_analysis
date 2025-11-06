
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from users.models import CustomUser
from .forms import StudentRegistrationForm, ProfessorRegistrationForm
from django.shortcuts import render
from .forms import BatchForm,BranchForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def index(request):
    return render(request, 'main.html')




# Student Registration View
def student_register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            # Create CustomUser instance first
            username = form.cleaned_data['usn']  # or use the username field
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create CustomUser object
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_student=True  # Set this to True for student registration
            )

            # Create Student object and associate with the user
            student = form.save(commit=False)  # Do not save yet
            student.user = user  # Link the student profile to the CustomUser
            student.save()  # Now save the student object
            
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('student_login')  # Redirect to login page after successful registration

    else:
        form = StudentRegistrationForm()

    return render(request, 'student_register.html', {'form': form})

# Professor Registration View
def professor_register(request):
    if request.method == 'POST':
        form = ProfessorRegistrationForm(request.POST)
        if form.is_valid():
            # Create CustomUser instance
            username = form.cleaned_data['empid']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            # Create the CustomUser object
            user = CustomUser.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                is_professor=True  # Set is_professor flag to True
            )

            # Create Professor instance and associate with the user
            professor = form.save(commit=False)  # Prevent saving immediately
            professor.user = user  # Link professor to the CustomUser
            professor.save()  # Save the Professor instance

            messages.success(request, 'Professor registered successfully!')
            return redirect('professor_login')  # Redirect to login after registration
        else:
            messages.error(request, 'There was an error in your form. Please check the details.')
    else:
        form = ProfessorRegistrationForm()
    return render(request, 'professor_register.html', {'form': form})

# Login View
def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']  # USN
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_student:
            login(request, user)
            request.session['usn'] = user.username
            messages.success(request, f"Welcome, {user.first_name}! You are logged in as a student.")
            return redirect('upload_file')  # Redirect to student dashboard
        else:
            messages.error(request, "Invalid login credentials or not a student account.")
            return render(request, 'student_login.html')
    return render(request, 'student_login.html')

def professor_login(request):
    if request.method == 'POST':
        username = request.POST['username']  # Employee ID
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_professor:
            login(request, user)
            request.session['empid'] = user.username
            messages.success(request, f"Welcome, {user.first_name}! You are logged in as a professor.")
            return redirect('professor_dashboard')  # Redirect to professor dashboard
        else:
            messages.error(request, "Invalid login credentials or not a professor account.")
            return render(request, 'professor_login.html')
    return render(request, 'professor_login.html')


