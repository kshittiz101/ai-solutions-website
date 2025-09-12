from django.shortcuts import render, redirect
from .models import Inquiry, CaseStudy
from django.contrib import messages
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.contrib.messages import get_messages

# Phone number validator
phone_validator = RegexValidator(
    regex=r'^\+?[0-9\-\s()]{7,20}$',
    message="Enter a valid phone number with country code (e.g. +977-9812345678)."
)


def generate_toasts_from_messages(request):
    """
    Generate simple toast data from Django messages.
    """
    COLOR_MAP = {
        "success": "green",
        "error": "red",
        "warning": "yellow",
        "info": "blue",
    }

    toasts = []
    for m in get_messages(request):
        color = COLOR_MAP.get(getattr(m, "level_tag", ""), "gray")
        toasts.append({
            "text": str(m.message),
            "color": color,
        })
    return toasts

# handle inquiry submission


def handle_inquiry_submission(request):
    """Handles POST inquiry submission logic."""
    name = request.POST.get("name")
    email = request.POST.get("email")
    phone = request.POST.get("phone")
    company = request.POST.get("company")
    country = request.POST.get("country")
    job_title = request.POST.get("job_title")
    job_details = request.POST.get("job_details")

    # Check required fields
    if not all([name, email, phone, company, country, job_title, job_details]):
        messages.error(request, "Please fill all the fields")
        return False

    # Validate phone number
    try:
        phone_validator(phone)
    except ValidationError:
        messages.error(request, "Enter a valid phone number with country code")
        return False

    # Save inquiry
    Inquiry.objects.create(
        name=name,
        email=email,
        phone=phone,
        company_name=company,
        country=country,
        job_title=job_title,
        job_details=job_details,
    )

    messages.success(request, "Inquiry submitted successfully")
    return True


def home(request):
    # get the first 3 case studies
    case_studies = CaseStudy.objects.all()[:3]
    if request.method == "POST":
        handle_inquiry_submission(request)
        return redirect("home")

    # FIX: pass toasts to the template
    context = {"toasts": generate_toasts_from_messages(request), "case_studies": case_studies}
    return render(request, "base/index.html", context)


def case_studies_details(request, slug):
    case_study = CaseStudy.objects.get(slug=slug)
    return render(request, "base/case-study/case-studies-details.html", {"case_study": case_study})
