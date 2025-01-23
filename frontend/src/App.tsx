import axios from "axios"
import ListItem from "./components/ListItem"
import { useEffect, useState } from "react"
import { Item } from "./models/Item"
import { Breadcrumb, Layout, theme } from 'antd';

const { Header, Content, Footer } = Layout;

export default function App() {

  const [items, setItems] = useState<Item[]>([]);

  const {
    token: { colorBgContainer, borderRadiusLG },
  } = theme.useToken()

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
          <Layout>
      <Header style={{ display: 'flex', alignItems: 'center' }}>
        <div className="demo-logo" />
        
      </Header>
      <Content style={{ padding: '0 48px' }}>
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>Home</Breadcrumb.Item>
          <Breadcrumb.Item>List</Breadcrumb.Item>
          <Breadcrumb.Item>App</Breadcrumb.Item>
        </Breadcrumb>
        <div
          style={{
            background: colorBgContainer,
            minHeight: 280,
            padding: 24,
            borderRadius: borderRadiusLG,
          }}
        >
          <ListItem urls={items}/>
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Market ©{new Date().getFullYear()} Created by Ant UED
      </Footer>
    </Layout>
    </>
  )
}

