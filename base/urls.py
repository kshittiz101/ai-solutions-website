from django.urls import path
from .views import home, case_studies_details, articles_details
urlpatterns = [
    path('', home, name="home"),
    path('case-studies/<slug:slug>/', case_studies_details, name="case_studies_details"),
    path('articles/<slug:slug>/', articles_details, name="articles_details"),
]
