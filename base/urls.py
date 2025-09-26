from django.urls import path
from .views import home, contact, case_studies_details, articles_details, events_details
urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name='contact'),
    path('case-studies/<slug:slug>/', case_studies_details,
         name="case_studies_details"),
    path('articles/<slug:slug>/', articles_details, name="articles_details"),
    path('events/<slug:slug>/', events_details, name="events_details"),
]
