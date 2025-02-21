import { useParams } from 'react-router';
import FooterComponent from "../Footer/FooterComponent";
import HeaderComponent from "../Header/HeaderComponent";
import type { FormProps } from 'antd';
import { Button, Form, Input, Card, notification } from 'antd';
import axios from 'axios';


type FieldType = {
    email?:string;
    password?: string;
    confirm_password?: string
  };

  const errorNotification = () => {
    notification.error({
        message : "Ошибка",
        description : "He получилось поменять пороль, обратиться в поддежку",
        placement: "topRight"
    }) 
}

const successNotification = () => {
    notification.success({
        message: "Успешно!",
        description : "Вы поменяли пороль.",
        placement : "topRight"
    })
}

const ResetPassComponent: React.FC = () => {
    const { email } = useParams<{ email : string }>();

    const onFinish = async (user:FieldType) => {
        try {
            const response = await axios.post<FieldType>("http://127.0.0.1:8000/user/reset_password",
                {
                    "email" : email,
                    "password" : user.password,
                    "confirm_password" : user.confirm_password
                },
                {
                    headers: {
                        "Content-Type": "application/json"
                    }
                })
            if (response.data) {
                successNotification();
            } else {
                errorNotification();
            }
        } catch (error) {
            console.error(error);
        }
      };

      const onFinishFailed: FormProps<FieldType>['onFinishFailed'] = (errorInfo) => {
        console.log('Failed:', errorInfo);
      };
    
    
    return(
        <div className="min-h-screen flex flex-col">
            <div>
                <HeaderComponent/>
            </div>
            <div className="flex-1 flex justify-center items-center">
                <Card title="Input a new password" variant="borderless" style={{ width: 500 }}>
                    <Form
                        name="basic"
                        labelCol={{ span: 8 }}
                        wrapperCol={{ span: 16 }}
                        style={{ maxWidth: 600, margin: 10 }}
                        initialValues={{ remember: true }}
                        onFinish={onFinish}
                        onFinishFailed={onFinishFailed}
                        autoComplete="off"
                    >
                        <Form.Item<FieldType>
                            label="New password"
                            name="password"
                            rules={[{ required: true, message: 'Please input new password!' }]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item<FieldType>
                            label="Confirm password"
                            name="confirm_password"
                            rules={[{ required: true, message: 'Please input confirm password!' }]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item label={null}>
                            <Button type="primary" htmlType="submit">
                                Update password
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>
            </div>
            <div className="mt-auto">
                <FooterComponent/>
            </div>
        </div>
    )
}

export default ResetPassComponent;