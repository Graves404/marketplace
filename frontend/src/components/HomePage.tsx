import axios from "axios"
import ListItem from "./ListItem"
import React, { useEffect, useState } from "react"
import { Item } from "../models/Item"
import { Layout, theme, Carousel } from 'antd';

const { Header, Content, Footer } = Layout;

const contentStyle: React.CSSProperties = {
  height: '560px',
  lineHeight: '160px',
  textAlign: 'center',
  background: '#364d79',
};

const HomePage: React.FC = () => {

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
        <div>
        <Layout>
          <Header>
            <div className="flex justify-between items-center w-full">
              <div className="flex-1 text-center">
                <p className="text-white">Home</p>
              </div>
              <div className="flex-1 text-center">
                <p className="text-white">Sign In / Sign Up</p>
              </div>
              <div className="flex-1 text-center">
                <p className="text-white">Help</p>
              </div>
            </div>
          </Header>
          <Carousel autoplay>
            <div className="w-full h-64">
              <div style={contentStyle}>
                <img className="object-fill" src="./img/ps5.webp" />
              </div>
            </div>
            <div className="w-full h-64">
              <div style={contentStyle}>
                <img className="w-full h-64 object-cover" src="./img/samsung.webp" />
              </div>
            </div>
            <div className="w-full h-64">
              <div style={contentStyle}>
                <img className="w-full h-64 object-cover" src="./img/iphone.jpg" />
              </div>
            </div>
            <div>
              <div style={contentStyle}>
                <img className="w-full h-64 object-cover" src="./img/ikea.avif" />
              </div>
            </div>
          </Carousel>
          <Content style={{ padding: "0 48px" }}>
            <div
              style={{
                background: colorBgContainer,
                minHeight: 280,
                padding: 24,
                borderRadius: borderRadiusLG,
              }}
            >
              <ListItem urls={items} />
            </div>
          </Content>
          <Footer style={{ textAlign: "center" }}>
            Market ©{new Date().getFullYear()} Design created by Ant UED
          </Footer>
        </Layout>
      </div>
    )
}

export default HomePage;