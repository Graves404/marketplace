import { Card, List } from 'antd';
import { Item } from '../models/Item';

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
                    </Card>
                </List.Item>
            )}
            />
        </div>
    )
}

export default ListItem