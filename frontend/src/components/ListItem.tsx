import { Card, List } from 'antd';
import { Item } from '../models/Item';
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
                    <Card title={item.title}>
                        <p>{item.description}</p>
                        <p>{item.price}</p>
                        <p>{item.city}</p>
                        {item.images.length > 0 ? (
                            <ImagesComponent image={item.images[0]}/>
                        ) : (
                            <img src="../error.png"/>
                        )}
                    </Card>
                </List.Item>
            )}
            />
        </div>
    )
}

export default ListItem