import User from "../../models/User"

interface UserInformationProps {
    user: User;
}

const UserInformationComponent: React.FC<UserInformationProps> = ({ user }) => {
    return (
        <div>
            <p></p>
            <p>Salesman:</p>
            <p>{user.name}</p>
            <p>{user.surname}</p>
            <p>Tel: {user.phone}</p>
        </div>
    )
}

export default UserInformationComponent