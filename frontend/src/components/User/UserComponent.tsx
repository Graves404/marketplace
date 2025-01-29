import Cookies from "js-cookie";
import { useEffect } from "react";

const UserComponent: React.FC = () => {

    const getSecretData = async () => {
        try {
          const token = Cookies.get("mne_market_accesses_token"); 

          console.log(token);
          
      
          const response = await fetch("http://127.0.0.1:8000/user/my_profile/", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${token}`,
            },
            credentials: "include"
          })
          
          const data = await response.json()
          console.log(data);
          
          
        } catch (error) {
          console.error("Ошибка запроса:", error);
        }
      };
      
    useEffect(()=> {
      getSecretData()
    });

    return(
        <div>
            <p>User Component</p>
        </div>
    )
}

export default UserComponent;