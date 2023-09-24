from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required  # Import the login_required decorator
from .forms import StudentRegistrationForm
from .models import *
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.models import Token

def student_registration(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            
            # Create and return an API token for the user
            #token, created = Token.objects.get_or_create(user=user)
            #print(f"Token created: {token.key}")
            
            login(request, user)
            return redirect('home')  # Redirect to the home page or wherever you want
    else:
        form = StudentRegistrationForm()
    
    return render(request, 'testapp/student_registration.html', {'form': form})
@login_required  # Use the login_required decorator to require login for accessing the home page
def home(request):
    # Example: Fetch some data from your database
    data_from_database = Student.objects.all()  # Replace YourModel with your actual model
    
    # Example: Create a variable to pass to the template
    welcome_message = "Welcome to our website!"
    
    context = {
        'data_from_database': data_from_database,
        'welcome_message': welcome_message,
        # Add other context data here as needed
    }
    return render(request, 'testapp/home.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages  # Import messages for displaying errors

def student_login(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        password = request.POST['password']
        
        user = authenticate(request, phone=phone, password=password)
        
        if user is not None:
            login(request, user)
            id = user.student_id  # Assuming you have a field named 'student_id' in your custom Student model
            return render(request, "testapp/student_login.html", {'id': id})
        else:
            messages.error(request, "Bad credentials!")
            return redirect('home')  # Replace 'home' with the URL where you want to redirect on login failure
    
    return render(request, 'testapp/student_login.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')
    
#students/views.pyfrom django.contrib.auth import authenticate, login
# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render

# @login_required
# def home(request):
#     return render(request, 'testapp/home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import StudentProfileUpdateForm

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = StudentProfileUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the profile page or wherever you want
    else:
        form = StudentProfileUpdateForm
    return render(request, 'testapp/update_profile.html', {'form': form})

@login_required
def home(request):
    return render(request, 'testapp/home.html')


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Student2
from .serializers import StudentSerializer

class CreateStudentView(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            # You can process the data or save it to the database here
            Student2.objects.create(name=name)
            return Response({"message": "Student created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer1

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile1(request):
    student = request.user

    if request.method == 'PUT':
        serializer = StudentSerializer1(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
