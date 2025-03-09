import HeaderComponent from "../Header/HeaderComponent";
import FooterComponent from "../Footer/FooterComponent";
import type { FormProps } from "antd";
import { Button, Form, Input, notification } from "antd";
import { Link, useNavigate } from "react-router";
import Cookies from "js-cookie";
import axios from "axios";

type FieldType = {
  email?: string;
  password?: string;
  remember?: string;
  data?: string;
};

type AuthResponse = {
  token?: string;
};

const AuthComponent: React.FC = () => {
  const navigate = useNavigate();

  const errorNotification = () => {
    notification.error({
      message: "Ошибка входа",
      description: "Неверный логин или пароль.",
      placement: "topRight",
    });
  };

  const successNotification = () => {
    notification.success({
      message: "Успешно!",
      description: "Вы успешно вошли в аккаунт",
      placement: "topRight",
    });
  };

  const onFinish: FormProps<FieldType>["onFinish"] = async (
    user: FieldType,
  ) => {
    try {
      const response = await axios.post<AuthResponse>(
        "http://127.0.0.1:9090/user/login",
        {
          email: user.email,
          password: user.password,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        },
      );
      if (response.data) {
        Cookies.set("mne_market_accesses_token", String(response.data.token), {
          expires: 1,
          sameSite: "None",
          secure: true,
        });
        successNotification();
        setTimeout(() => {
          navigate("/my_profile");
        }, 500);
      }
    } catch (error) {
      errorNotification();
      console.error(error);
    }
  };
  const onFinishFailed: FormProps<FieldType>["onFinishFailed"] = (
    errorInfo,
  ) => {
    notification.error({
      message: `Failed ${errorInfo}`,
      placement: "topRight",
    });
  };

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
            rules={[{ required: true, message: "Please input your email!" }]}
          >
            <Input />
          </Form.Item>
          <Form.Item<FieldType>
            label="Password"
            name="password"
            rules={[{ required: true, message: "Please input your password!" }]}
          >
            <Input.Password />
          </Form.Item>
          <div className="flex justify-between items-center w-full">
            <div className="flex">
              <Button type="primary" htmlType="submit">
                Sign In
              </Button>
            </div>
            <div className="flex">
              <Link to={`/registration`} className="flex items-center">
                <Button>Sign Up</Button>
              </Link>
            </div>
          </div>
          <div className="flex justify-center mt-6">
            <Link to={`/forget_email`}>forget password</Link>
          </div>
        </Form>
      </div>
      <div className="mt-auto">
        <FooterComponent />
      </div>
    </div>
  );
};
export default AuthComponent;
