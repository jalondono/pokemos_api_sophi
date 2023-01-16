from rest_framework import serializers
from core.models.user import Account
from core.utils import check_password_complexity, check_email_format


class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password']

    def create(self, validated_data):

        email = validated_data['email']
        password = validated_data['password']

        if Account.objects.filter(email=email):
            raise serializers.ValidationError(f"The email {email} already exist")

        if not check_password_complexity(password):
            raise serializers.ValidationError("Password is not strong enough - Your password must have: "
                                              "at least 8 characters, a lowercase (a to z), an uppercase (A to Z), "
                                              "a number (0 to 9), a special character (e.g. !@#$%^&*()_+-=.)")
        if not check_email_format(email):
            raise serializers.ValidationError("The Email does not have a valid format- Your email must have: "
                                              "Two parts by @ symbol, (a to z) and a domain,"
                                              "that is personal_info@domain.com")

        account = Account(email=email)
        account.set_password(password)
        account.save()
        return account
