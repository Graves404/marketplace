import firebase from "firebase/compat/app";
import { getDownloadURL, getStorage, listAll, ref } from "firebase/storage";

const firebaseConfig = {
    storageBucket : "market-479da.firebasestorage.app" 
};
const app = firebase.initializeApp(firebaseConfig);

const storage = getStorage(app)

type PhotoURLs = string[]

const listRef = ref(storage, "images/")

async function getPhotoURLs() : Promise<PhotoURLs> {
    try {
        const photoList = await listAll(listRef);
        const photoURLs = await Promise.all(
            photoList.items.map((itemRef) => getDownloadURL(itemRef))
        );
        return photoURLs;
    } catch (error) {
        console.error(error);
        return []
    }
}

export { storage, getPhotoURLs }