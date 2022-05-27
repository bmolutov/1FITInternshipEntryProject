from django.urls import path
from .views import * 
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


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
    path('review/companies/<int:company_id>/<int:rating>/', CompanyReviewsListFiltered.as_view()),  # get

    # EXTRA: 
    # editing reviews, 
    # sorted list of companies, sorted by avg rating
    path('review/edit/<int:pk>/', ReviewEditing.as_view()), # put
    path('companies/sorted/', CompaniesListSorted().as_view()), # get
]


urlpatterns += [
    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
