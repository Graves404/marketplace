import HeaderComponent from "../Header/HeaderComponent";
import FooterComponent from "../Footer/FooterComponent";
import type { FormProps } from 'antd';
import { Button, Checkbox, Form, Input } from 'antd';
import { Link, useNavigate } from 'react-router';
import Cookies from 'js-cookie';
import axios from 'axios';

type FieldType = {
    email?: string;
    password?: string;
    remember?: string;
    data?: string;
  };
  
  const AuthComponent: React.FC = () => {
    const navigate = useNavigate();

    const onFinish: FormProps<FieldType>['onFinish'] = async (user: FieldType) => {
        try {
            const response = await axios.post<FieldType>(`http://127.0.0.1:8000/authentication/check_user?email_=${user.email}&pass_=${user.password}`);
            if (response.data) {
                Cookies.set("mne_market_accesses_token:", response.data, {expires : 1});
                navigate('/my_profile');
            }
        } catch (error) {
            alert("Inncorect E-mail or Password")
            console.error(error);
        }
    }
    const onFinishFailed: FormProps<FieldType>['onFinishFailed'] = (errorInfo) => {
        console.log('Failed:', errorInfo);
    }

    return (
        <div className="min-h-screen flex flex-col">
            <HeaderComponent />
            <div className="flex flex-1 items-center justify-center">
                <Form
                    name="basic"
                    labelCol={{ span: 8 }}
                    wrapperCol={{ span: 16 }}
                    style={{ maxWidth: 600 }}
                    initialValues={{ remember: true }}
                    onFinish={onFinish}
                    onFinishFailed={onFinishFailed}
                    autoComplete="off"
                >
                    <Form.Item<FieldType>
                        label="Email"
                        name="email"
                        rules={[{ required: true, message: 'Please input your email!' }]}
                    >
                        <Input />
                    </Form.Item>
                    <Form.Item<FieldType>
                        label="Password"
                        name="password"
                        rules={[{ required: true, message: 'Please input your password!' }]}
                    >
                        <Input.Password />
                    </Form.Item>

                    <div className="flex justify-between items-center">
                        <Form.Item<FieldType> name="remember" valuePropName="checked" label={null}>
                            <Checkbox>Remember me</Checkbox>
                        </Form.Item>
                    </div>
                    <div className="flex justify-between items-center">
                        <Form.Item label={null} >
                            <Button type="primary" htmlType="submit">
                                Login
                            </Button>
                        </Form.Item>
                        <Link to={`/registration`} className="flex items-center"> 
                            <Button>
                                Registration
                            </Button>
                        </Link>
                    </div>
                </Form>
            </div>
            <FooterComponent />
        </div>
    );
};
export default AuthComponent;