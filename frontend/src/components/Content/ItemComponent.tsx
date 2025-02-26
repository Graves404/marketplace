import axios from 'axios';
import { useEffect, useState, useCallback } from 'react';
import { useParams } from 'react-router';
import Item from '../../models/Item';

import { Layout, theme, Image } from 'antd';
import HeaderComponent from '../Header/HeaderComponent';
import FooterComponent from '../Footer/FooterComponent';
import UserInformationComponent from './UserInformationComponent';
import PaymentComponent from '../Payment/PaymentComponent';
const { Content } = Layout;

const ItemComponent: React.FC = () => {
    
    const { id } = useParams<{ id: string }>();
    
    const [item, setItem] = useState<Item>();

    const {
        token: { colorBgContainer, borderRadiusLG },
    } = theme.useToken()
    
    const fetchItem = useCallback(async () => {
        try {
            const response = await axios.get<Item>(`http://127.0.0.1:8000/items/get_item/${id}?id_=${id}`); 
            setItem(response.data);
        } catch (error) {
            console.error(error);
        }
    }, [id]);
    
    useEffect(() => {
        fetchItem()
    }, [id, fetchItem]);  

    return (
        <div className="flex flex-col min-h-screen">
            <Layout className="flex flex-col flex-grow">
                <HeaderComponent />
                <Content
                    style={{
                        padding: "0 48px",
                        display: "flex",
                        flexDirection: "column",
                    }}
                    className="flex-grow"
                >
                    <div
                        style={{
                            background: colorBgContainer,
                            minHeight: "100%",
                            padding: 24,
                            borderRadius: borderRadiusLG,
                        }}
                        className="flex justify-center items-center flex-grow"
                    >
                        <div className="flex flex-col w-full max-w-4xl">
                            <p className="text-4xl font-bold mb-20" style={{ marginBottom: '2rem' }}>{item?.title}</p>
                            <div className="flex flex-row space-x-8">
                            <div className="flex space-x-4 flex-grow">
                                <Image.PreviewGroup>
                                    {item?.images.map((img) => (
                                        <Image
                                            key={img.id}
                                            src={img.url_photo}
                                            className="w-48 h-48 object-cover rounded-lg"
                                            width={200}
                                        />
                                    ))}
                                </Image.PreviewGroup>
                            </div>
                            <div className="w-64 flex-shrink-0 flex flex-col space-y-4">
                                <p className="text-3xl font-bold">{item?.price} $</p>
                                <div className="flex space-x-8">
                                    {item?.user && <UserInformationComponent user={item.user} />}
                                </div>
                                <div className="flex justify-center w-full">
                                    {item && <PaymentComponent title={item.title} price={item.price} />}
                                </div>
                            </div>
                        </div>
                            <div className="mb-6">
                                <p className="text-2xl font-bold mb-2">Location</p>
                                <p className='text-xl'>{item?.city}</p>
                            </div>
                            <div className="mb-6">
                                <p className="text-2xl font-bold mb-2">Description</p>
                                <p className='text-xl'>{item?.description}</p>
                            </div>
                        </div>
                    </div>
                </Content>
                <FooterComponent />
            </Layout>
        </div>
    );
}

export default ItemComponent;