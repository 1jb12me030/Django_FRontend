from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student,Class

class StudentRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    image = forms.ImageField()
    student_class = forms.ModelChoiceField(queryset=Class.objects.all(), empty_label="Select a Class")

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'status', 'image', 'student_class']

# from django import forms
# from django.contrib.auth import authenticate

# class StudentLoginForm(forms.Form):
#     phone = forms.CharField(max_length=15, required=True)
#     password = forms.CharField(widget=forms.PasswordInput, required=True)

#     def clean(self):
#         cleaned_data = super().clean()
#         phone_number = cleaned_data.get('phone_number')
#         password = cleaned_data.get('password')

#         if phone_number and password:
#             student = authenticate(phone_number=phone_number, password=password)

#             if student is None:
#                 raise forms.ValidationError("Invalid phone number or password.")


from django import forms
from .models import Student

class StudentProfileUpdateForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 'image', 'student_class']
