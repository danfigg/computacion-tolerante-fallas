import { Link } from 'react-router-dom';
import styles from '../styles/NavBar.module.css'; 

function Navbar() {
    return (
      <nav className={styles.navbar}>
        <div className={styles.logo}><Link to="/">Barbería Élite</Link></div>
        <ul className={styles.navLinks}>
          <li><Link to="/">Inicio</Link></li>
          <li><Link to="/reservar">Reservar</Link></li>
          <li><Link to="/gestionar">Gestionar</Link></li>
        </ul>
      </nav>
    );
  }

export default Navbar;