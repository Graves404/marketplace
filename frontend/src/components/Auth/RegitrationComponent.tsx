import HeaderComponent from "../Header/HeaderComponent";
import { Button, Form, Input, notification } from 'antd';
import { useNavigate } from "react-router"

  const RegistrationComponent: React.FC = () => {
    const [form] = Form.useForm();
    const navigate = useNavigate();

    const openNotification = () => {
        notification.success({
            message : "Успешная регистрация!",
            description : "Вы были успешно зарегистрированы.",
            placement: "topRight"
        })
    }

    const onFinish = async (value:any) => {
        try {
            const response = await fetch("http://127.0.0.1:8000/user/registration_service", {
                method : "POST",
                headers : {
                    "Content-Type": "application/json",
                }, 
                body : JSON.stringify(value)
            });
            if (response.ok) {
                openNotification();
                form.resetFields();
                setTimeout(()=>{
                    navigate("/");
                }, 2000);                
            } else {
                console.error(response.statusText);
            }
        } catch (error) {
            console.error(error);
        }
    }


    return(
        <div>
            <HeaderComponent/>
            <div className="flex justify-center items-center h-screen">
                <Form form={form} onFinish={onFinish} className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg">
                    <div className="flex justify-center">
                        <p className="text-2xl">Regitration</p>
                    </div>
                    <br />
                    <Form.Item label="Name" name="name" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>
                    <Form.Item label="Surname" name="surname" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>
                    <Form.Item label="Email" name="email" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>

                    <Form.Item label="City" name="city" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>

                    <Form.Item
                        label="Phone Number"
                        name="phone"
                        rules={[{ required: true, message: 'Please input!' }]}
                    >
                        <Input />
                    </Form.Item>

                    <Form.Item label="Username" name="username" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>

                    <Form.Item label="Password" name="hash_pass" rules={[{ required: true, message: 'Please input!' }]}>
                        <Input />
                    </Form.Item>

                    <Form.Item className="flex justify-center" wrapperCol={{ offset: 6, span: 16 }}>
                        <Button type="primary" htmlType="submit">
                        Confirm
                        </Button>
                    </Form.Item>
                </Form>
            </div>
        </div>
    )
}

export default RegistrationComponent;

// {
//     "name": "string",
//     "surname": "string",
//     "email": "user@example.com",
//     "city": "string",
//     "phone": "string",
//     "username": "string",
//     "hash_pass": "string"
//   }