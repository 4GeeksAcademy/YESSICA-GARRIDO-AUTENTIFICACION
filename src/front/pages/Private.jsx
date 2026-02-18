import { useEffect } from "react";
import { useNavigate } from "react-router-dom";

export const Private = () => {
    const navigate = useNavigate();

    const logout = () => {
        sessionStorage.removeItem("token");
        navigate("/login");
    };

    useEffect(() => {
        const token = sessionStorage.getItem("token");

        if (!token) {
            navigate("/login");
        }
    }, []);

    return (
        <div className="container-sm w-25">
            <div className="row justify-content-md-center">
                <h1 className="my-4">Bienvenido Heiber</h1>
                <img src="/mi-imagen-2.jpg" className="w-100 rounded-3  mb-3" alt="Mi imagen 2" />
                
                <button onClick={logout} className="btn btn-primary">Cerrar sesión</button>
            </div>
        </div>
    );
};