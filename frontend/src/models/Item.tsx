import { ImageData } from "./ImageData"
export interface Item {
    id: number,
    title: string,
    description: string,
    price: number,
    city: string,
    images: ImageData[],
    user_id: number
}