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
                            <Card title={item.title}>
                                <div className='flex'>
                                    <div>{item.price} €</div>
                                    <div>{item.city}</div>
                                    {item.images.length > 0 ? (
                                        <ImagesComponent image={item.images[0]}/>
                                    ) : (
                                        <img src="../img/error.png"/>
                                    )}
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