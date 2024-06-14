import datetime
from kavenegar import *
from config.settings import Kavenegar_API
from random import randint

from .models import CustomUser


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI(Kavenegar_API)
        params = {
            'sender': '10008663',
            'receptor': phone_number,
            'message': f'Your Verify Code: {code}'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


def get_random_otp():
    return randint(1000, 9999)


def check_otp_expiration(phone_number):
    try:
        user = CustomUser.objects.get(phone_number=phone_number)
        now = datetime.datetime.now()
        otp_time = user.otp_code_created
        diff_time = now - otp_time
        print(f'otptime: {diff_time}')
        if diff_time.seconds > 120:
            return False
        return True

    except CustomUser.DoesNotExist:
        return False
