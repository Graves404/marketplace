import FooterComponent from "../Footer/FooterComponent";
import HeaderComponent from "../Header/HeaderComponent";
import type { FormProps } from 'antd';
import { Button, Form, Input, Card, notification } from 'antd';


type FieldType = {
    email?: string;
  };

  const errorNotification = (value:string) => {
    notification.error({
        message : "Ошибка",
        description : `Почта ${value} не найдена`,
        placement: "topRight"
    }) 
}

const successNotification = (value:string) => {
    notification.success({
        message: "Успешно!",
        description : `Ha электронную почту ${value} отправлено письмо для восстановление пароля`,
        placement : "topRight"
    })
}
  
const ForgetPassComponent: React.FC = () => {

    const [ form ] = Form.useForm();


    const onFinish = async (value:FieldType) => {
        try {
            const response = await fetch("http://127.0.0.1:8000/user/forget_password/"+value.email, {
                method : "POST",
            })
            if(response.ok){
                successNotification(value.email || "");
                form.resetFields();
            } else {
                errorNotification(value.email || "");
            }
        } catch (error) {
            console.error(error);
        }
      };
      
      const onFinishFailed: FormProps<FieldType>['onFinishFailed'] = (errorInfo) => {
        console.log('Failed:', errorInfo);
      };    

    return (
        <div className="min-h-screen flex flex-col">
            <div>
                <HeaderComponent />
            </div>
            <div className="flex-1 flex justify-center items-center">
                <Card title="Find your account" style={{ width: 500 }}>
                    <p>Please enter your email to search for your account.</p>
                    <Form
                        form={form}
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
                            label="Email"
                            name="email"
                            rules={[{ required: true, message: 'Please input your email!' }]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item label={null}>
                            <Button type="primary" htmlType="submit">
                                Reset password
                            </Button>
                        </Form.Item>
                    </Form>
                </Card>
            </div>
            <div className="mt-auto">
                <FooterComponent />
            </div>
        </div>
    );
}

export default ForgetPassComponent;