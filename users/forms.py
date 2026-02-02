
from django import forms
from .models import CustomUser, Student, Professor
from django import forms
from .models import CustomUser, Branch, Batch
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class BatchForm(forms.ModelForm):
    class Meta:
        model = Batch
        fields = ['batch']

    def __init__(self, *args, **kwargs):
        super(BatchForm, self).__init__(*args, **kwargs)
        self.fields['batch'].required = True

class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = ['branch']

    def __init__(self, *args, **kwargs):
        super(BranchForm, self).__init__(*args, **kwargs)
        self.fields['branch'].required = True

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Student, Professor, Branch, Batch

# Custom User Registration Form
class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

# Student Registration Form
class StudentRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    # Fields for Student registration
    batch = forms.ModelChoiceField(queryset=Batch.objects.all(), required=True)
    branch = forms.ModelChoiceField(queryset=Branch.objects.all(), required=True)

    class Meta:
        model = Student
        fields = ['usn', 'batch', 'branch', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data

# Professor Registration Form
class ProfessorRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput(), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Confirm Password')
    
    # Fields for Professor registration
    department = forms.ModelChoiceField(queryset=Branch.objects.all(), required=True)

    class Meta:
        model = Professor
        fields = ['empid', 'department', 'email', 'first_name', 'last_name']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
