from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login

from . models import CustomUser
from .forms import LoginForm
from . import helper


class LoginView(View):

    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):

        form = self.form_class(request.POST)
        otp = helper.get_random_otp()

        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']

            try:
                user = CustomUser.objects.get(phone_number=phone_number)
                helper.send_otp_code(phone_number, otp)
                user.otp_code = otp
                user.save()
                request.session['phone_number'] = phone_number
                return redirect('accounts:verify')

            except CustomUser.DoesNotExist:
                user = CustomUser(phone_number=phone_number)
                helper.send_otp_code(phone_number, otp)
                user.otp_code = otp
                user.is_active = False
                user.save()
                request.session['phone_number'] = phone_number
                return redirect('accounts:verify')

        return render(request, 'accounts/login.html', {'form': form})


# TODO: after login delete the session
def verify_otp_view(request):
    try:
        phone_number = request.session.get('phone_number')
        user = CustomUser.objects.get(phone_number=phone_number)
        if request.method == "POST":
            # check otp expiration
            if not helper.check_otp_expiration(phone_number):
                messages.error(request, 'OTP code is expired!, pleas try again.', 'danger')
                return redirect('accounts:verify')

            if user.otp_code != int(request.POST.get('otp')):
                messages.error(request, 'OTP code is incorrect!, pleas try again.', 'danger')
                return redirect('accounts:verify')
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home:home')
        return render(request, 'accounts/verify.html', {'phone_number': phone_number})
    except CustomUser.DoesNotExist:
        messages.error(request, 'Error accorded!, pleas try again.', 'danger')
        return redirect('accounts/login')
