import json
import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

from smartequ.models import InternshipEnrollment

from .forms import RequestCallForm



# ======================================
# BASIC PAGES
# ======================================

# def index(request):
#     return render(request, 'user/index.html')

def home(request):
    return render(request, 'user/home.html')

def about(request):
    return render(request, 'user/about.html')

def training(request):
    return render(request, 'user/training.html')

def data_science(request):
    return render(request, 'user/data_science.html')

def python(request):
    return render(request, 'user/python.html')

def java(request):
    return render(request, 'user/java.html')

def cloud(request):
    return render(request, 'user/cloud.html')

def internship(request):
    return render(request, 'user/internship.html')

def internship_details(request):
    return render(request, 'user/internship_details.html')

# ======================================
# REQUEST CALL FORM
# ======================================

def request_call(request):

    if request.method == "POST":
        form = RequestCallForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "✅ We will call you shortly!")
            return redirect('request_call')

    else:
        form = RequestCallForm()

    return render(request, 'user/request_call.html', {'form': form})


def enroll_internship(request):
    """
    Handle internship enrollment form submission and save data to database.
    """
    if request.method == 'POST':
        program_name = request.POST.get('program_name')
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message', '')  # Get message field, default empty string

        # Validate that required fields are provided
        if program_name and full_name and email and mobile:
            try:
                # Save to database with optional message
                enrollment = InternshipEnrollment(
                    program_name=program_name,
                    full_name=full_name,
                    email=email,
                    mobile=mobile,
                    message=message  # Save the optional message
                )
                enrollment.save()
                
                messages.success(request, '✅ Your enrollment request has been submitted successfully! Our team will contact you within 24 hours.')
            except Exception as e:
                messages.error(request, f'❌ An error occurred: {str(e)}')
        else:
            messages.error(request, '❌ Please fill all the required fields.')

        return redirect('home')

    # If not POST, redirect back to internship list
    return redirect('home')