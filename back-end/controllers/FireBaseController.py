import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import initialize_app
import json
import os

class FirebaseController:
    FireStoreClient = None
    Credentials = None
    AppReference = None
    def __init__(self):
        cert = {
                "type": "service_account",
                "project_id": "voicerecorderapp-6d1ca",
                "private_key_id": "e3ddf124548d5e655f455aa29a46c515b41ce0e0",
                "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDRSdKT2yQTGNjD\ncAWe32K7KfMqz5w4xfljG3ofB8mgh0z1LGiNU5Z/AWBXNA7OrUT/OvCHJ8Gy8zvX\nLTTtfpUpGZ43ckGHYEURy3OBJSjv3Zif0p3XhAEu0LasRR45Uu8MtS/j6wRj3Xo2\nfm/DuXdTghDRzCaZV0UAs/D6CTojP9rG1tPiNDhxqAxVSjupLp6wG1OcCOw00FfI\nX5cp04mf5XfLXUrEwF0geIqgpLoT7WBPTCiD3YCRZSF5nefOSgmtq+HH8pr6627d\n2Y2lEejmnLYCz/1aftT/CGEwiXCvYf2Hn3vPQMNPb0ZYGTupHTiZZ8+o/LKHUvOj\n4ghNU60LAgMBAAECggEARFQSRISMzBFWH8SQiTSMYufIxKbgbaaxC5rabYwY12il\nBvyXK+Do5xE3d3D/DpoCR0PiaHXh5v9Df7Z6K7mikDcVcSvD2iNjmXIvhS/xJBLY\ndAGK1+R4kGTC5w5v1i5N7nuvJX3Cwqn57xWrfp6sJx71R9Gbnn+f/yFAYRmnGf91\nRxcxg38arPUZEjJbfUWu4kfZ/BjHl7/CCeG+XaI/1hTiVgZCkJGPdx9n/XaCnD33\nHakbByroMUz685i7S6shfNlVimq04DuOAe2gqjms9D+DFSL/XBE7wrlwouuluR8D\nKAtUgg9UD0pbTH3GumR/vjB2gCzHLIdYWLWfd00CUQKBgQDtxUM3A+NOooFQqo61\nvrPi3Ii7Rx+ugOnB/8qyGD5FHO8Jzv0rcdidfSrESKlmP0TL6jPS58OXkTBRHBxP\nw1r7uj+ngYhZzxC4PUkq2ecbaaUihP9wMxqJwNBgTDoJjFLwIVlYV0vlpdOI0o5V\nYx9k7LcnRMZhHBZr7wvM/bJTEQKBgQDhVYnRikmWxLDkxg957o6qMOxkWKKIu3PA\nbHBmXw1kbdk2j6DZgbJ85bb3SU0cRSqeS0jqEBxJa7rYE1RknsNSddOoHmoelRuH\nUcmioeKl7ybCrY7uhVMUNmXDf07NjOysv77G1xUy3egRNzWpSC8t2WxTaVLeCOxe\nc68ipaHGWwKBgQDoLCjX/anlzPSsyf6UJWUN7v5ssKSVBzg6wQUyJk4XuosHbuDz\nnTVBg0lRZQpU1w7cdxKnrLvmslUVvnc+w6mCCHnDnM6Bs5nF7cIWX7Q1plEjhe7P\npncRb/+JKKW7URRjeoz9oDByTBxkjAWEB0hOin7Fj3iOtpiGSGOjhU6toQKBgAN6\nwqoNrJ07ZE/kDxEe8e0G3F+gTsI1ws/R3Np31UkbuSLyjNVO/2aWVYD0DNDG8KWJ\nHBMhNI6dr0Du63qySOnZD++kqJbYTpiEVszAGzPcwYh4DaD5RhMl0+R07s6VwoHY\nZCXF5Hnom1DIvXdjufbHSLjxA2qSULQUrTunuxvJAoGAPm9cT4igK67yUu8lya7a\nHw5EzbTsZbeyC9mB2L8Ccn7HxApzZMtgVYtMz20kFaNHNWDQjED3fNOdhK59eOMf\n44abiZ4skVLZ4t//I/WxyMd0m9Q5GVyEycphamu4rmC7O9FhsKjOoFQTBmOZNrhb\n/eKKZuioX8bccNQfuVKeF3U=\n-----END PRIVATE KEY-----\n",
                "client_email": "firebase-adminsdk-gm446@voicerecorderapp-6d1ca.iam.gserviceaccount.com",
                "client_id": "112421484406957363988",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://oauth2.googleapis.com/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-gm446%40voicerecorderapp-6d1ca.iam.gserviceaccount.com"
            }
        self.Credentials = credentials.Certificate(cert)
        self.AppReference = initialize_app(self.Credentials)
        self.FireStoreClient = firestore.client()