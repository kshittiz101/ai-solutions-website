from django.urls import path
from .views import home, contact, case_study_list, case_studies_details, blogs_page, blogs_details, events_details
urlpatterns = [
    path('', home, name="home"),
    path('contact/', contact, name='contact'),
    path("case-study/", case_study_list, name="case-study"),
    path('case-studies/<slug:slug>/', case_studies_details,
         name="case_studies_details"),

    path('blogs/', blogs_page, name="blogs"),
    path('blogs/<slug:slug>/', blogs_details, name="blogs_details"),
    path('events/<slug:slug>/', events_details, name="events_details"),
]
