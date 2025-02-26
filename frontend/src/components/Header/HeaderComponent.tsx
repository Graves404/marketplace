import { Link } from 'react-router';
import { Layout } from 'antd';
import Cookies from 'js-cookie';
import { jwtDecode } from 'jwt-decode';
import { notification } from 'antd';

const { Header } = Layout;

const HeaderComponent: React.FC = () => {

    let canGoHomePageRender = false;

    const inforNotification = () => {
        notification.info({
            message: "Вы успешно вышли из аккаунта",
            description: "Вы успешно вышли из аккаунта",
            placement: "topRight"
        })
    }

    const isValidateToken = (token: string) => {
        try {
            const decoded = jwtDecode(token);
            const currentTime = Date.now() / 1000;
            return decoded.exp && decoded.exp > currentTime;
        } catch (error) {
            console.log(error);
        }
    }

    const token = Cookies.get("mne_market_accesses_token");
    if (token && isValidateToken(token)) {
        canGoHomePageRender = true;
    }

    const handleLogout = () => {
        Cookies.remove("mne_market_accesses_token");
        inforNotification();
    }
    return(
        <>
            <div>
                <Layout>
                    <Header>
                            <div className="flex justify-between items-center w-full">
                            <div className="flex-1 text-center">
                            <Link to={`/`}>
                                <p className="text-white">Home</p>
                            </Link>
                            </div>
                            <div className="flex-1 text-center">
                                {canGoHomePageRender ? (
                                    <div className='flex justify-between items-center'>
                                        <Link to={`/my_profile`}>
                                            <p className="text-white">My Profile</p>
                                        </Link>
                                        <Link to={`/`}>
                                            <p className='text-white' onClick={handleLogout}>Logout</p>
                                        </Link>
                                    </div>
                                ) : (                                
                                    <Link to={`/login`}>
                                        <p className="text-white">Sign In / Sign Up</p>
                                    </Link>
                                )}
                            </div>
                            <div className="flex-1 text-center">
                                <p className="text-white">Help</p>
                            </div>
                            </div>
                        </Header>
                </Layout>
            </div>
        </>
    )
};

export default HeaderComponent;