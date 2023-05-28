from firebase_admin import firestore
import db


def getDocument():
    db = firestore.client()
    users_ref = db.collection(u'mina-1')
    docs = users_ref.get()

    return docs