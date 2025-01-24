import axios from 'axios';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router';
import Item from '../models/Item';

const ItemComponent: React.FC = () => {
    
    const { id } = useParams<{ id: string }>();
    
    const [item, setItem] = useState<Item>();
    
    const fetchItem = async () => {
        try {
          const response = await axios.get<Item>(`http://127.0.0.1:8000/items/get_item/${id}?id_=${id}`);
          console.log("Item fetched:", response.data); 
          setItem(response.data);
        } catch (error) {
          console.error(error);
        }
      }
    
      useEffect(()=> {
      fetchItem()
    }, [id]);  

        return (
            <div>
                <p>{item?.title} - НАЗВАНИЕ</p>
                
            </div>
        )
}

export default ItemComponent;