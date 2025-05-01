import styles from '../styles/Landing.module.css';
import { Link } from 'react-router-dom';

function Landing() {
  return (
    <div className={styles['landing-container']}>
      <div className={styles['landing-text']}>
        <h1>
          Bienvenido a <span className={styles['highlight']}>Barbería Élite</span>
        </h1>
        <p className={styles['tagline']}>
          Tu estilo comienza aquí. Cortes clásicos, modernos y siempre con actitud.
        </p>

        <p>
          En Barbería Élite, nos enorgullece ofrecer un servicio de calidad excepcional. Nuestro equipo de barberos profesionales está dedicado a brindarte una experiencia única, desde cortes de cabello personalizados hasta diseños de barba que reflejan tu estilo y personalidad.
        </p>

        <p>
          Además, contamos con productos de alta calidad para el cuidado de tu cabello y barba, asegurándonos de que siempre luzcas impecable. Ven y vive la experiencia de una barbería moderna con un toque clásico.
        </p>

        <div className={styles['services']}>
          <div className={styles['service']}>
            💈 <span>Cortes de cabello personalizados</span>
          </div>
          <div className={styles['service']}>
            🧔 <span>Diseño de barba profesional</span>
          </div>
          <div className={styles['service']}>
            ✂️ <span>Afeitados con toalla caliente</span>
          </div>
        </div>

        <Link to="/reservar" className={styles['cta-button']}>
          Reserva tu cita
        </Link>
      </div>

      <div className={styles['landing-image']}>
        <img
          src="https://plus.unsplash.com/premium_photo-1677444398670-4f5aaaef65eb?w=900&auto=format&fit=crop&q=60"
          alt="Barbero trabajando"
        />
      </div>
    </div>
  );
}

export default Landing;