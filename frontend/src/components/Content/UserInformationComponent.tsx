import User from "../../models/User"

interface UserInformationProps {
    user: User;
}

const UserInformationComponent: React.FC<UserInformationProps> = ({ user }) => {
    return (
        <div>
            <p className="text-2xl font-bold">Salesman:</p>
            <p className="text-xl">{user.name}</p>
            <p className="text-xl">{user.surname}</p>
            <p className="text-xl">Tel: {user.phone}</p>
        </div>
    )
}

export default UserInformationComponent