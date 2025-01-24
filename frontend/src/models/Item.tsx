import  ImageData  from "./ImageData"
export default interface Item {
    id: number,
    title: string,
    description: string,
    price: number,
    city: string,
    images: ImageData[],
    user_id: number
}