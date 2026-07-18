import { NavLink } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="navbar">
      <NavLink to="/" className="navbar-brand">PixSoftPay</NavLink>
      <div className="navbar-links">
        <NavLink to="/" end className={({ isActive }) => isActive ? 'active' : ''}>Dashboard</NavLink>
        <NavLink to="/create" className={({ isActive }) => isActive ? 'active' : ''}>Nouveau QR</NavLink>
        <NavLink to="/history" className={({ isActive }) => isActive ? 'active' : ''}>Historique</NavLink>
      </div>
    </nav>
  );
}
