from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from api.serializers import *


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(token.key)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })


class GetUserInfo(APIView):

    def get(self, request):
        user = request.user

        if user.is_authenticated:
            serializer = UserInfoSerializer(user) 
            return Response(serializer.data)
        
        return Response({
            'error': 'not authenticated'
        })


class UserRegistration(APIView):

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'username': user.username,
        })


class UserLogout(APIView):

    def get(self, request):
        request.user.auth_token.delete()
        return Response({
            'message': 'logged out',
        })


class CompaniesList(APIView):

    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanyInfoSerializer(companies, many=True)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated, )


class CompaniesListFiltered(APIView):

    def get(self, request, type):
        companies = Company.objects.all()
        companies = [company for company in companies if company.type == type]
        serializer = CompanyInfoSerializer(companies, many=True)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated, )


class CompanyDetails(APIView):

    def getCompany(self, pk):
        try:
            return Company.objects.get(id=pk)
        except Exception:
            return Response({'message': 'An error occurred!'})

    def get(self, request, pk):
        company = self.getCompany(pk) 
        serializer = CompanyDetailInfoSerializer(company)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated, )


class ReviewLeaving(APIView):

    def post(self, request):
        serializer = ReviewInfoSerializer(data=request.data)
        author = request.data.get('author')

        leftReviews = Review.objects.all()
        leftReviews = [review for review in leftReviews if review.author.id == int(author)]
        
        companies = [review.company.id for review in leftReviews]
        company = request.data.get('company')

        if int(company) in companies:
            return Response({'error': 'You have already reviewed this company!'})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)    

    permission_classes = (IsAuthenticated, )


class CompanyReviewsList(APIView):

    def get(self, request, company_id):
        reviews = Review.objects.all()
        reviews = [review for review in reviews if review.company.id == company_id]

        serializer = ReviewDetailSerializer(reviews, many=True)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated, )


class CompanyReviewsListFiltered(APIView):

    def get(self, request, company_id, rating):
        reviews = Review.objects.all()
        reviews = [review for review in reviews if review.company.id == company_id and review.rating == rating]

        serializer = ReviewDetailSerializer(reviews, many=True)
        return Response(serializer.data)

    permission_classes = (IsAuthenticated, )
