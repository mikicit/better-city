# Create a Firebase user with custom claims.
# For development purposes only.

import argparse
import os
import firebase_admin
from firebase_admin import credentials, auth


def initialize_firebase_app(token_path):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    key_path = os.path.join(script_directory, token_path)
    cred = credentials.Certificate(key_path)
    firebase_admin.initialize_app(cred)


def create_firebase_user(email, password, user_type, token_path):
    initialize_firebase_app(token_path)

    user = auth.create_user(
        email=email,
        email_verified=True,
        password=password,
    )

    claims = {'role': user_type, 'status': 'ACTIVE'}
    auth.set_custom_user_claims(user.uid, claims)

    user = auth.get_user(user.uid)
    print("Custom claims:")
    print(user.custom_claims)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a Firebase user with custom claims.")
    parser.add_argument("email", type=str, help="User email address")
    parser.add_argument("password", type=str, help="User password")
    parser.add_argument("user_type", type=str, help="User type (e.g., 'ADMIN'...)")
    parser.add_argument("token_path", type=str, help="Absolute path to the Firebase token file")

    args = parser.parse_args()
    create_firebase_user(args.email, args.password, args.user_type, args.token_path)
