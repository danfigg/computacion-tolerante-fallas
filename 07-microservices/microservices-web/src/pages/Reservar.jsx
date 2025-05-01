import styles from '../styles/Reservar.module.css';

function Reservar() {
  return (
    <div className={styles['reservar-container']}>
      <h1 className={styles['title']}>Reserva tu cita</h1>
      <form className={styles['reservation-form']}>
        <div className={`${styles['form-group']} ${styles['full-width']}`}>
          <label htmlFor="name">Nombre completo</label>
          <input type="text" id="name" name="name" placeholder="Ingresa tu nombre" required />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="phone">Número de contacto</label>
          <input type="tel" id="phone" name="phone" placeholder="Ingresa tu número" required />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="service">Servicio</label>
          <select id="service" name="service" required>
            <option value="">Selecciona un servicio</option>
            <option value="corte">Corte de cabello</option>
            <option value="barba">Diseño de barba</option>
            <option value="afeitado">Afeitado con toalla caliente</option>
          </select>
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="date">Fecha</label>
          <input type="date" id="date" name="date" required />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="time">Hora</label>
          <input type="time" id="time" name="time" required />
        </div>
        <button type="submit" className={styles['submit-button']}>Reservar</button>
      </form>
    </div>
  );
}

export default Reservar;