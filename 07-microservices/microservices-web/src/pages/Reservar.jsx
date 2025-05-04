import React, { useState } from 'react';
import styles from '../styles/Reservar.module.css';
import AlertModal from '../components/Modal';

console.log("styles: ", styles);

function Reservar() {
  const [name, setName] = useState('');
  const [phone, setPhone] = useState('');
  const [service, setService] = useState('');
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  const [errors, setErrors] = useState({});

  const [modalOpen, setModalOpen] = useState(false);
  const [modalType, setModalType] = useState('success'); 
  const [modalTitle, setModalTitle] = useState('');
  const [modalDesc, setModalDesc] = useState('');


  const validate = () => {
    const newErrors = {};

    if (!name.trim()) {
      newErrors.name = 'El nombre es obligatorio.';
    }

    if (!phone.trim()) {
      newErrors.phone = 'El número de contacto es obligatorio.';
    } else if (!/^\d{10}$/.test(phone)) {
      newErrors.phone = 'El número de contacto debe tener 10 dígitos.';
    }

    if (!service) {
      newErrors.service = 'Debes seleccionar un servicio.';
    }

    if (!date) {
      newErrors.date = 'Debes seleccionar una fecha.';
    }

    if (new Date(date) < new Date().setHours(0, 0, 0, 0)) {
      newErrors.date = 'La fecha no puede ser en el pasado.';
    }
    
    if (!time) {
      newErrors.time = 'Debes seleccionar una hora.';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
  
    if (!validate()) return;
  
    let userId;
    try {
      const userResponse = await fetch('http://localhost:4002/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nombre: name, telefono: phone }),
      });
  
      if (!userResponse.ok) throw new Error('Error al crear usuario');
  
      const userData = await userResponse.json();
      userId = userData.id;
  
      const reservaResponse = await fetch('http://localhost:4002/reservas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          servicio: service,
          fecha: date,
          hora: time,
          user_id: userId,
        }),
      });
  
      if (!reservaResponse.ok) throw new Error('Error al crear reserva');

      const reservaData = await reservaResponse.json();
      const codigoConfirmacion = reservaData.codigo;
  
      // Muestra modal de éxito
      setModalType('success');
      setModalTitle('¡Reserva exitosa!');
      setModalDesc(`Tu cita fue registrada correctamente. Código de confirmación: ${codigoConfirmacion}`);
      setModalOpen(true);
    } catch (error) {
      console.error(error);
      // Muestra modal de error
      setModalType('error');
      setModalTitle('Error al reservar');
      setModalDesc('Ocurrió un problema al hacer la reserva. Inténtalo más tarde.');
      setModalOpen(true);
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
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          {errors.name && <p className={styles['error-message']}>{errors.name}</p>}
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="phone">Número de contacto</label>
          <input
            type="tel"
            id="phone"
            name="phone"
            placeholder="Ingresa tu número"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
          />
          {errors.phone && <p className={styles['error-message']}>{errors.phone}</p>}
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="service">Servicio</label>
          <select
            id="service"
            name="service"
            value={service}
            onChange={(e) => setService(e.target.value)}
          >
            <option value="">Selecciona un servicio</option>
            <option value="corte">Corte de cabello</option>
            <option value="disenio_barba">Diseño de barba</option>
            <option value="afeitado">Afeitado con toalla caliente</option>
          </select>
          {errors.service && <p className={styles['error-message']}>{errors.service}</p>}
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="date">Fecha</label>
          <input
            type="date"
            id="date"
            name="date"
            value={date}
            onChange={(e) => setDate(e.target.value)}
          />
          {errors.date && <p className={styles['error-message']}>{errors.date}</p>}
        </div>
        <div className={styles['form-group']}>
          <label htmlFor="time">Hora</label>
          <input
            type="time"
            id="time"
            name="time"
            value={time}
            onChange={(e) => setTime(e.target.value)}
          />
          {errors.time && <p className={styles['error-message']}>{errors.time}</p>}
        </div>
        <button type="submit" className={styles['submit-button']}>Reservar</button>
      </form>

      {modalOpen && (
        <AlertModal
          isOpen={modalOpen}
          onClose={() => setModalOpen(false)}
          title={modalTitle}
          description={modalDesc}
          type={modalType}
          onConfirm={() => {
            setModalOpen(false);
            if (modalType === 'success') {
              window.location.href = '/'; 
            }
          }}
        />
      )}

    </div>
    
  );
}

export default Reservar;