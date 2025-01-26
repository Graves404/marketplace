import axios from 'axios';
import { useEffect, useState } from 'react';
import { useParams } from 'react-router';
import Item from '../../models/Item';

import { Layout, theme, Image } from 'antd';
import HeaderComponent from '../Header/HeaderComponent';
import FooterComponent from '../Footer/FooterComponent';
import UserInformationComponent from './UserInformationComponent';

const { Content } = Layout;

const ItemComponent: React.FC = () => {
    
    const { id } = useParams<{ id: string }>();
    
    const [item, setItem] = useState<Item>();

    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken()
    
    const fetchItem = async () => {
        try {
          const response = await axios.get<Item>(`http://127.0.0.1:8000/items/get_item/${id}?id_=${id}`); 
          setItem(response.data);
        } catch (error) {
          console.error(error);
        }
      }
    
      useEffect(()=> {
      fetchItem()
    }, [id]);  

        return (
        <div className="flex flex-col min-h-screen">
            <Layout className="flex flex-col flex-grow">
                <HeaderComponent />
                <Content
                    style={{
                        padding: "0 48px",
                        display: "flex", // Для корректного растягивания
                        flexDirection: "column",
                    }}
                    className="flex-grow"
                >
                    <div
                        style={{
                            background: colorBgContainer,
                            minHeight: "100%", // Растягиваем контент на всю высоту
                            padding: 24,
                            borderRadius: borderRadiusLG,
                        }}
                        className="flex justify-center items-center flex-grow"
                    >
                        <div className="flex flex-col text-center">
                            <p className="font-mono">{item?.title}</p>
                            <Image.PreviewGroup>
                                <div className="flex space-x-4">
                                    {item?.images.map((img) => {
                                        return <Image key={img.id} src={img.url_photo} width={200} />;
                                    })}
                                </div>
                            </Image.PreviewGroup>
                            <p>{item?.price} EUR</p>
                            <p>{item?.description}</p>
                            <p>{item?.city}</p>
                            <UserInformationComponent/>
                        </div>
                    </div>
                </Content>
                <FooterComponent />
            </Layout>
        </div>
        )
}

export default ItemComponent;