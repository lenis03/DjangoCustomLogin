# DjangoCustomLogin

## Overview
This project is a Django application that implements user authentication using OTP (One-Time Password) codes. The application allows users to log in using their phone numbers, which are verified through OTP codes sent to their phones.

## Features
- User login with phone number.
- OTP generation and verification.
- Session management for storing phone numbers temporarily.
- Error handling for invalid and expired OTPs.

## Prerequisites
- Python 3.x
- Django 3.x or higher

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/lenis03/DjangoCustomLogin.git
    cd DjangoCustomLogin
    ```

2. **Create a virtual environment using pipenv:**
    ```bash
    pip install pipenv
    pipenv install
    pipenv shell
    ```

3. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

4. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

### Login View

The `LoginView` handles displaying the login form, generating OTPs, and managing user sessions. When a user submits their phone number, the view checks if the user exists, generates an OTP, and sends it to the user's phone. If the user does not exist, it creates a new inactive user and sends the OTP.

### OTP Verification View

The `verify_otp_view` handles the OTP verification process. It retrieves the user's phone number from the session, verifies the OTP, checks for expiration, and activates the user upon successful verification. If the OTP is incorrect or expired, it displays an error message.

## Helper Functions

The helper functions include generating a random OTP, sending OTP to the user's phone number, and checking OTP expiration.

## Forms

The form used for logging in is defined in `forms.py` and includes a single field for the phone number.

## Models

The `CustomUser` model extends the default Django user model to include phone number and OTP code fields.

## Templates

- `accounts/login.html`: Template for the login page.
- `accounts/verify.html`: Template for the OTP verification page.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Contact

For any questions or inquiries, please contact fardintorkamand83@gmail.com

---
