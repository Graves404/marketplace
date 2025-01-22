import axios from "axios"
import ListItem from "./components/ListItem"
import { useEffect, useState } from "react"
import { Item } from "./models/Item"

export default function App() {

  const [items, setItems] = useState<Item[]>([]);

  const fetchItems = async () => {
    try {
      const response = await axios.get<Item[]>("http://127.0.0.1:8000/items/all_items")
      setItems(response.data)
    } catch (error) {
      console.error(error);
    }
  }

  useEffect(()=> {
    fetchItems()
  }, []);
     
  return (
    <>
      <ListItem urls={items}/>
    </>
  )
}

