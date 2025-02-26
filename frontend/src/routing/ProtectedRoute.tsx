import { Navigate, Outlet } from 'react-router';
import { jwtDecode } from 'jwt-decode';

interface TokenPayload {
    exp: number;
}

const ProtectedRoute = () => {
        const checkAuth = () => {
        const token = localStorage.getItem('mne_market_accesses_token');

        if (!token) return false;

        try {
            const decoded = jwtDecode<TokenPayload>(token);
            const currentTime = Math.floor(Date.now() / 1000);
            return decoded.exp > currentTime
        } catch {
            return false;
        }
    };
    return checkAuth() ? <Outlet /> : <Navigate to="/login" replace/>;
}

export default ProtectedRoute;