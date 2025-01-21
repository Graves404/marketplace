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

def upload_file(file_name: str, file_content: bytes, content_type: str):
    blob = bucket.blob(f"images/{file_name}")
    blob.upload_from_string(file_content, content_type)
    blob.make_public()
    public_url = blob.public_url

    firebase_db.collection("files").add({
        "file_name": file_name,
        "url": public_url,
        "content_type": content_type,
    })
    return {"msg": "Done"}

def delete_files(urls: list[str]):
    for url in urls:
        try:
            correct_url = url.replace(settings.BASE_URL, "")
            blob = bucket.blob(correct_url)
            blob.delete()
        except Exception as e:
            return f"Error {e}"

    return {"msg": "images delete"}
