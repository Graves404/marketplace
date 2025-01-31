import React, { useEffect, useState } from 'react';
import { Breadcrumb, Layout, Menu, theme, Card, notification, Avatar, Modal } from 'antd';
import { UserOutlined, SettingOutlined, LogoutOutlined, PlusCircleOutlined } from '@ant-design/icons';
import type { MenuProps } from 'antd';
import { useNavigate } from "react-router"
import FooterComponent from '../Footer/FooterComponent';
import HeaderComponent from '../Header/HeaderComponent';
import AddItemComponent from '../Item/AddItemComponent';
import Cookies from "js-cookie";

const { Content, Sider } = Layout;

type MenuItem = Required<MenuProps>['items'][number];

const UserComponent: React.FC = () => {
    const {token: { colorBgContainer, borderRadiusLG }} = theme.useToken();
    
    const navigate = useNavigate();

    const [ userData, setUserData ] = useState<any>(null);

    const [isModalOpen, setIsModalOpen] = useState(false);

    const showModal = () => {
      setIsModalOpen(true);
    };

    const handleOk = () => {
      setIsModalOpen(false);
    };
  
    const handleCancel = () => {
      setIsModalOpen(false);
    };

    const handleLogout = () => {
      Cookies.remove("mne_market_accesses_token");
      notification.info({
        message : "Выход из аккаунта",
        description : "Вы успешно вышли из аккаунта.",
        placement: "topRight"
      });
      navigate("/")
    }  

    const items: MenuItem[] = [
      { key: '1', icon: <PlusCircleOutlined />, label: 'Add new item', onClick: showModal },
      { key: '2', icon: <SettingOutlined />, label: 'Settings' },
      { key: '3', icon: <LogoutOutlined />, label: 'Log out',  onClick: handleLogout},
    ]

    const getSecretData = async () => {
        try {
          const token = Cookies.get("mne_market_accesses_token");       
          const response = await fetch("http://127.0.0.1:8000/user/my_profile/", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${token}`,
            },
            credentials: "include"
          })
          
          const data = await response.json()
          setUserData(data);
        } catch (error) {
          console.error("Ошибка запроса:", error);
        }
    };
      
    useEffect(()=> { getSecretData() },[]);

    return(
        <div>
          <Layout style={{ minHeight: '100vh', background: colorBgContainer }}>
            <HeaderComponent/>
            <Layout style={{ background : colorBgContainer}}>
              <Sider width={200} style={{ height: '100vh' }}>
              <div style={{ width: 200 }}>
                <Menu
                  defaultSelectedKeys={['1']}
                  defaultOpenKeys={['sub1']}
                  mode="inline"
                  theme="dark"
                  items={items}
                />
              </div>
                <Modal title="Create a new item" open={isModalOpen} onOk={handleOk} onCancel={handleCancel}>
                  <AddItemComponent onSuccess={handleOk}/>
                </Modal>
              </Sider>
              <Layout style={{ padding: '0 24px 24px', flex: 1 }}>
                <Breadcrumb
                  items={[{ title: 'My Profile' }]}
                  style={{ margin: '16px 0' }}
                />
                <Content
                  style={{
                    padding: 24,
                    margin: 0,
                    minHeight: 280,
                    background: colorBgContainer,
                    borderRadius: borderRadiusLG,
                  }}
                >
                  <div>
                    {userData ? (
                      <div>
                        <div>
                          <Avatar size={64} icon={<UserOutlined />} />
                        </div>
                        <p><strong>Name:</strong> {userData.name} {userData.surname}</p>
                        <p><strong>Email:</strong> {userData.email}</p>
                        <p><strong>Phone:</strong> {userData.phone}</p>
                        <p><strong>City:</strong> {userData.city}</p>
                        {userData.items && userData.items.length > 0 ? (
                          <div>
                            {userData.items.map((item:any,index:number) => (
                              <Card key={index} title={item.title} extra={<a href="#">More</a>} style={{ width: 300, margin:16 }}>
                                <p>{item.description}</p>
                                <p>{item.price} $</p>
                                <p>{item.city}</p>
                              </Card>
                            ))}
                          </div>
                        ):(
                          <p>No items available</p>
                        )}
                      </div>
                  ) : (
                      <p>Loading...</p>
                  )}
                  </div>
                </Content>
              </Layout>
            </Layout>
          </Layout>
          <FooterComponent/>
        </div>
    )
}

export default UserComponent;