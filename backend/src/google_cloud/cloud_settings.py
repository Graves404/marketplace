from firebase_admin import firestore, credentials, storage
from fastapi import UploadFile
from ..security.security_config import settings
import firebase_admin

creds = credentials.Certificate("src/firebase_key.json")

firebase_app = firebase_admin.initialize_app(creds, {
    'databaseURL': settings.DATA_BASE_URL_FIREBASE,
    'storageBucket': settings.STORAGE_BUCKET
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

def delete_files(urls: list[str]):
    for url in urls:
        try:
            correct_url = url.replace(settings.BASE_URL, "")
            blob = bucket.blob(correct_url)
            blob.delete()
        except Exception as e:
            print(f"Error {e}")

    return {"msg": "images delete"}
