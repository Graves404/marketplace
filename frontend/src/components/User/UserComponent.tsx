import { useEffect } from "react";
import FooterComponent from "../Footer/FooterComponent";
import HeaderComponent from "../Header/HeaderComponent";
import Cookies from "js-cookie";

const UserComponent: React.FC = () => {
    
    const getSecretData = async () => {
        try {
          const token = Cookies.get("mne_market_accesses_token"); 
      
          const response = await fetch("http://127.0.0.1:8000/user/test/", {
            method: "GET",
            headers: {
              "Content-Type": "application/json",
              "Authorization": `Bearer ${token}`,
              "Cookie": `mne_market_accesses_token=${token}`
            },
            credentials: "include"
          });
      
          if (response.ok) {
            const data = await response.json();
            console.log("Данные получены:", data);
          } else {
            console.error("Ошибка запроса:", response.status, response.statusText);
          }
        } catch (error) {
          console.error("Ошибка запроса:", error);
        }
      };
      
    useEffect(()=> {
      getSecretData()
    });

    return(
        <div>
            <HeaderComponent/>
            <p>User Component</p>
            <FooterComponent/>
        </div>
    )
}

export default UserComponent;