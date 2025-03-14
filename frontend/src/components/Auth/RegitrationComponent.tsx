import HeaderComponent from "../Header/HeaderComponent";
import { Button, Form, Input, notification } from "antd";
import { useNavigate } from "react-router";
import FooterComponent from "../Footer/FooterComponent";
import RegistrationData from "../../models/RegistrationData";

const RegistrationComponent: React.FC = () => {
  const [form] = Form.useForm();
  const navigate = useNavigate();

  const openNotification = () => {
    notification.success({
      message: "Успешная регистрация!",
      description:
        "Вы были успешно зарегистрированы. Ha почту отправлен email для верификации",
      placement: "topRight",
    });
  };

  const errorNotification = (description: string) => {
    notification.error({
      message: "Ошибка",
      description: description,
      placement: "topRight",
    });
  };

  const onFinish = async (value: RegistrationData) => {
    try {
      const response = await fetch("http://127.0.0.1:9090/user/registration", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(value),
      });

      const data = await response.json();

      console.log(data);

      if (data.code === 389) {
        errorNotification("Пользователь c таким Email уже зарегистриван");
      } else {
        if (response.ok) {
          openNotification();
          form.resetFields();
          setTimeout(() => {
            navigate("/");
          }, 2000);
        } else {
          console.error(response.statusText);
        }
      }
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <HeaderComponent />
      <div className="flex justify-center items-center h-screen">
        <Form
          form={form}
          onFinish={onFinish}
          className="bg-white p-6 rounded-lg shadow-lg w-full max-w-lg"
        >
          <div className="flex justify-center">
            <p className="text-2xl">Regitration</p>
          </div>
          <br />
          <Form.Item
            label="Name"
            name="name"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Surname"
            name="surname"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item
            label="Email"
            name="email"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="City"
            name="city"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Phone Number"
            name="phone"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Username"
            name="username"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="hash_pass"
            rules={[{ required: true, message: "Please input!" }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            className="flex justify-center"
            wrapperCol={{ offset: 6, span: 16 }}
          >
            <Button type="primary" htmlType="submit">
              Confirm
            </Button>
          </Form.Item>
        </Form>
      </div>
      <div className="mt-auto">
        <FooterComponent />
      </div>
    </div>
  );
};

export default RegistrationComponent;
