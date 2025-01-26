import { Link } from 'react-router';
import { Layout } from 'antd';

const { Header } = Layout;

const HeaderComponent: React.FC = () => {
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
                                <p className="text-white">Sign In / Sign Up</p>
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