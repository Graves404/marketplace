import  ImageData  from "./ImageData"
import User from './User';
export default interface Item {
    id: number,
    title: string,
    description: string,
    price: number,
    city: string,
    images: ImageData[],
    user_id: number
    user: User
}