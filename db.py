import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

if not firebase_admin._apps:
    firebase_admin.initialize_app(credential=credentials.Certificate('clave.json'))