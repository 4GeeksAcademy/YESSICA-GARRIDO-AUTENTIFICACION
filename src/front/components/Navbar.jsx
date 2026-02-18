import { Link } from "react-router-dom";

export const Navbar = () => {

	return (
		<nav className="navbar navbar-light bg-white">
		<div className="container">
			<Link to="home/">
				<span className="navbar-brand mb-0 fs-1 fw-bold">Rigo</span>
			</Link>

			<div className="d-flex gap-2">
				<Link to="/login">
					<button className="btn btn-primary me-2">Iniciar Sesión</button>
				</Link>
				<Link to="/registro">
					<button className="btn btn-primary">Registrarme</button>
				</Link>
			</div>
		</div>
	</nav>
	);
};