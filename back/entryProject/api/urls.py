from django.contrib import admin
from django.urls import path
from .views import * 


urlpatterns = [
    # actions related to user
    path('login/', CustomAuthToken.as_view()), # post
    path('user/', GetUserInfo.as_view()), # get
    path('register/', UserRegistration.as_view()), # post
    path('logout/', UserLogout.as_view()), # get

    # actions related to Company model
    path('companies/', CompaniesList.as_view()), # get
    path('companies/filtered/<str:type>/', CompaniesListFiltered.as_view()), # get
    path('companies/<int:pk>/', CompanyDetails.as_view()), # get

    # actions related to Review model
    path('review/', ReviewLeaving.as_view()), # post
    path('review/companies/<int:company_id>/', CompanyReviewsList.as_view()), # get
    path('review/companies/<int:company_id>/<int:rating>/', CompanyReviewsListFiltered.as_view())  # get
]
