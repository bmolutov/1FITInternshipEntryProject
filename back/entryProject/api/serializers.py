from rest_framework import serializers, validators
from api.models import * 


class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'dateOfBirth') 


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'email', 'dateOfBirth')

        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'required': True,
                'allow_blank': False,
                'validators': [
                    validators.UniqueValidator(
                        CustomUser.objects.all(), 'A user with that email already exists!'
                    )
                ]
            }
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        password = validated_data.get('password')
        email = validated_data.get('email')
        dateOfBirth = validated_data.get('dateOfBirth')

        user = CustomUser.objects.create(
            username=username,
            password=password,
            email=email,
            dateOfBirth=dateOfBirth,
        )
        user.set_password(password)
        user.save()

        return user


class CompanyInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('name', 'type', 'logo')


class CompanyDetailInfoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Company
        fields = ('name', 'type', 'logo', 'foundingDate')


class ReviewInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ('rating', 'reviewContent', 'date', 'author', 'company') 

    def create(self, validated_data):
        rating = validated_data.get('rating')
        reviewContent = validated_data.get('reviewContent')
        date = validated_data.get('date')
        author = validated_data.get('author')
        company = validated_data.get('company')

        review = Review.objects.create(
            rating=rating,
            reviewContent=reviewContent,
            date=date,
            author=author,
            company=company,
        )

        review.save()
        return review

    def update(self, instance, validated_data):
        instance.rating = validated_data.get('rating')
        instance.reviewContent = validated_data.get('reviewContent')
        instance.author = validated_data.get('author')
        instance.company = validated_data.get('company')
        instance.save()
        return instance


class ReviewDetailSerializer(serializers.ModelSerializer):

    author = UserInfoSerializer()

    class Meta:
        model = Review
        fields = ('rating', 'reviewContent', 'date', 'author')
