import React, { useState } from 'react';
import styles from '../styles/Reservar.module.css';

function Reservar() {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [service, setService] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Paso 1: Verificar si el usuario existe o crear uno nuevo
    let userId;
    try {
      const userResponse = await fetch('http://localhost:4002/users', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ nombre: name, telefono: phone }),
      });

      if (!userResponse.ok) {
        throw new Error('Error al crear usuario');
      }

      const userData = await userResponse.json();
      userId = userData.id;

      // Paso 2: Crear la reserva asociada al usuario
      const reservaResponse = await fetch('http://localhost:4002/reservas', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          servicio: service,
          fecha: date,
          hora: time,
          user_id: userId, // Asociar la reserva al usuario creado
        }),
      });

      if (!reservaResponse.ok) {
        throw new Error('Error al crear reserva');
      }

      alert('Reserva creada exitosamente');
    } catch (error) {
      console.error(error);
      alert('Hubo un error al hacer la reserva');
    }
  };

  return (
    <div className={styles['reservar-container']}>
      <h1 className={styles['title']}>Reserva tu cita</h1>
      <form className={styles['reservation-form']} onSubmit={handleSubmit}>
        <div className={`${styles['form-group']} ${styles['full-width']}`}>
          <label htmlFor="name">Nombre completo</label>
          <input
            type="text"
            id="name"
            name="name"
            placeholder="Ingresa tu nombre"
            required
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="phone">Número de contacto</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            placeholder="Ingresa tu número"
            required
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="service">Servicio</label>
          <select
            id="service"
            name="service"
            required
            value={service}
            onChange={(e) => setService(e.target.value)}
          >
            <option value="">Selecciona un servicio</option>
            <option value="corte">Corte de cabello</option>
            <option value="disenio_barba">Diseño de barba</option>
            <option value="afeitado">Afeitado con toalla caliente</option>
          </select>
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="date">Fecha</label>
          <input
            type="date"
            id="date"
            name="date"
            required
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="time">Hora</label>
          <input
            type="time"
            id="time"
            name="time"
            required
            value={time}
            onChange={(e) => setTime(e.target.value)}
          />
        </div>
        <button type="submit" className={styles['submit-button']}>Reservar</button>
      </form>
    </div>
  );
}

export default Reservar;
