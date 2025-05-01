import { Link } from 'react-router-dom';
import styles from '../styles/NavBar.module.css'; 

function Navbar() {
    return (
      <nav className={styles.navbar}>
        <div className={styles.logo}>Barbería Élite</div>
        <ul className={styles.navLinks}>
          <li><a href="#inicio">Inicio</a></li>
          <li><a href="#reservar">Reservar</a></li>
          <li><a href="#gestionar">Gestionar</a></li>
        </ul>
      </nav>
    );
  }

export default Navbar;