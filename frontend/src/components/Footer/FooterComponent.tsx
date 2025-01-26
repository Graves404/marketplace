import { Layout } from 'antd'

const { Footer } = Layout

const FooterComponent: React.FC = () => {
    return(
        <Layout>
            <Footer style={{ textAlign: "center" }}>
                Market ©{new Date().getFullYear()} Design created by Ant UED
            </Footer>
        </Layout>
    )
}

export default FooterComponent;