import { useState } from 'react';
import styles from '../styles/Gestionar.module.css';

function Gestionar() {
  const [codigo, setCodigo] = useState('');
  const [reserva, setReserva] = useState(null);

  const handleBuscar = (e) => {
    e.preventDefault();
    // Simulación de búsqueda de reserva
    if (codigo === '12345') {
      setReserva({
        nombre: 'Juan Pérez',
        servicio: 'Corte de cabello',
        fecha: '2025-05-01',
        hora: '15:00',
      });
    } else {
      setReserva(null);
      alert('No se encontró ninguna reserva con ese código.');
    }
  };

  const handleCancelar = () => {
    alert('Reserva cancelada exitosamente.');
    setReserva(null);
  };

  return (
    <div className={styles['gestionar-container']}>
      <h1 className={styles['title']}>Gestionar Reserva</h1>
      <form className={styles['gestion-form']} onSubmit={handleBuscar}>
        <div className={styles['form-group']}>
          <label htmlFor="codigo">Código de Reserva</label>
          <input
            type="text"
            id="codigo"
            name="codigo"
            placeholder="Ingresa tu código"
            value={codigo}
            onChange={(e) => setCodigo(e.target.value)}
            required
          />
        </div>
        <button type="submit" className={styles['buscar-button']}>
          Buscar
        </button>
      </form>

      {reserva && (
        <div className={styles['reserva-detalles']}>
          <h2>Detalles de la Reserva</h2>
          <p><strong>Nombre:</strong> {reserva.nombre}</p>
          <p><strong>Servicio:</strong> {reserva.servicio}</p>
          <p><strong>Fecha:</strong> {reserva.fecha}</p>
          <p><strong>Hora:</strong> {reserva.hora}</p>
          <button className={styles['cancelar-button']} onClick={handleCancelar}>
            Cancelar Reserva
          </button>
        </div>
      )}
    </div>
  );
}

export default Gestionar;