from firebase_admin import firestore, credentials, storage
from fastapi import UploadFile
import firebase_admin

creds = credentials.Certificate("src/firebase_key.json")

firebase_app = firebase_admin.initialize_app(creds, {
    'databaseURL': "https://market-479da-default-rtdb.firebaseio.com/",
    'storageBucket': 'market-479da.firebasestorage.app'
})

firebase_db = firestore.client()

bucket = storage.bucket()

def upload_file(filename_: str, file_: UploadFile):
    blob = bucket.blob(f"images/{filename_}")
    blob.upload_from_file(file_.file, content_type=file_.content_type)
    blob.make_public()
    return blob.public_url

