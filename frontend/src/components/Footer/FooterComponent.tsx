import { Layout } from 'antd'

const { Footer } = Layout

const FooterComponent: React.FC = () => {
    return(
        <Layout>
            <Footer style={{ textAlign: "center" }}>
                Kupi.mne ©{new Date().getFullYear()} Design created by Kupi.mne
            </Footer>
        </Layout>
    )
}

export default FooterComponent;