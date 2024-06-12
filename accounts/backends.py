from .models import CustomUser


class PhoneAuthenticationBackend:

    @staticmethod
    def authenticate(request, phone_number=None, password=None,):

        try:
            user = CustomUser.objects.get(phone_number=phone_number)
            return user

        except CustomUser.DoesNotExist:
            return None

    @staticmethod
    def get_user(user_id):

        try:
            return CustomUser.objects.get(pk=user_id)

        except CustomUser.DoesNotExist:
            return None
