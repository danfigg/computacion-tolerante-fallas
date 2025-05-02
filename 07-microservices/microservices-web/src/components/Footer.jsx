import styles from '../styles/Footer.module.css';

function Footer() {
  return (
    <footer className={styles.footer}>
      <p>&copy; {new Date().getFullYear()} Barbería Élite. Todos los derechos reservados.</p>
    </footer>
  );
}

export default Footer;
