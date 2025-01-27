import FooterComponent from "../Footer/FooterComponent";
import HeaderComponent from "../Header/HeaderComponent";

const UserComponent: React.FC = () => {
    return(
        <div>
            <HeaderComponent/>
            <p>User Component</p>
            <FooterComponent/>
        </div>
    )
}

export default UserComponent;