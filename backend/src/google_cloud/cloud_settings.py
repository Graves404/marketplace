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

def upload_file(files: list[UploadFile]):
    upload_list_urls = []
    for file in files:
        try:
            blob = bucket.blob(f"images/{file.filename}")
            blob.upload_from_file(file.file, content_type=file.content_type)

            blob.make_public()
            upload_list_urls.append(blob.public_url)
        except Exception as e:
            print(f"Error uploading file {file.filename}: {e}")
    return upload_list_urls

