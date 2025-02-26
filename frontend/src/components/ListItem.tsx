import { Card, List } from 'antd';
import  Item  from '../models/Item';
import { Link } from 'react-router'
import ImagesComponent from './ImagesComponent';

interface ListItemProps {
    urls: Item[]
}

const ListItem: React.FC<ListItemProps> = ({ urls }) => {
    
    return(
        <div>
            <List
            grid={{ gutter: 16, column: 4 }}
            dataSource={urls}
            renderItem={(item) => (
                    <List.Item>
                        <Link to={`/item/${item.id}`}>
                            <Card className="shadow-lg rounded-lg overflow-hidden">
                                <div className='flex flex-col'>
                                    <div className='w-full h-50 overflow-hidden'>
                                        {item.images.length > 0 ? (
                                            <ImagesComponent image={item.images[0]}/>
                                        ) : (
                                            <img src="../img/error.png"/>
                                        )}
                                    </div>
                                    <div className='p-4'>
                                        <div className='text-xl font-bold mb-2'>{item.title}</div>
                                        <div className='text-gray-700 text-base'>{item.price} €</div>
                                        <div className='text-gray-500 text-sm'>{item.city}</div>
                                    </div>
                                </div>
                            </Card>
                        </Link>
                    </List.Item>
            )}
            />
        </div>
    )
}

export default ListItem