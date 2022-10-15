
import firebase_admin
from firebase_admin import credentials, auth
#import pyrebase

import argparse
import json
import os
import requests
import pprint
'''
TODO : poder seleccionar app on posar les coses
TODO : separar usuaris per company a Firebase
'''
class FirebaseHelper (object):


    cred = credentials.Certificate("F:\\Programas\\Git\\owere_v2\\applications\\helper\\serviceAccountKey.json")
    app_instance = firebase_admin.initialize_app(credential=cred)

    FIREBASE_WEB_API_KEY = ""
    rest_api_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword"


    def createFirebaseUser(self, email, password):

        user = auth.create_user(email = email, password = password )
        print ("user created succesfully : {0}".format(user.uid))
        #print("user firebase_auth_token: {0}".format(user.firebase_auth_token))

    def loginFirebaseUser(self, email, password):

        user = auth.get_user_by_email(email)

        #user = auth.sign_in_with_email_and_password(email, password)
        print("user created succesfully : {0}".format(user.uid))
        print(self.sign_in_with_email_and_password(email, password))


    def changePassword(self):
        # TODO :
        return None


    def sign_in_with_email_and_password(self, email: str, password: str, return_secure_token: bool = True):
        payload = json.dumps({
            "email": email,
            "password": password,
            "returnSecureToken": return_secure_token
        })

        r = requests.post(self.rest_api_url,
                          params={"key": self.FIREBASE_WEB_API_KEY},
                          data=payload)

        return r.json()