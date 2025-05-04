import { useState } from 'react';
import styles from '../styles/Gestionar.module.css';
import AlertModal from '../components/Modal';

function Gestionar() {
  const [codigo, setCodigo] = useState('');
  const [reserva, setReserva] = useState(null);
  const [loading, setLoading] = useState(false);

  // Para el modal
  const [modalOpen, setModalOpen] = useState(false);
  const [modalType, setModalType] = useState('success'); 
  const [modalTitle, setModalTitle] = useState('');
  const [modalDesc, setModalDesc] = useState('');

  const handleBuscar = async (e) => {
    e.preventDefault();
    console.log('Buscando reserva...');
    setLoading(true);

    try {
      const response = await fetch(`http://localhost:4002/reservas?codigo=${codigo.trim()}`);
      
      if (!response.ok) {
        throw new Error('No se encontró ninguna reserva con ese código.');
      }
      const reservaArray = await response.json();
      const reservaData = reservaArray[0];
      
      setReserva({
        id: reservaData.id,
        servicio: reservaData.servicio,
        fecha: reservaData.fecha,
        hora: reservaData.hora,
        codigo: reservaData.codigo,
        user_id: reservaData.user_id,
      });

      const userResponse = await fetch(`http://localhost:4002/users/${reservaData.user_id}`);
      
      if (!userResponse.ok) {
        throw new Error('No se encontró el usuario asociado a la reserva.');
      }

      const userData = await userResponse.json();

      setReserva((prevReserva) => ({
        ...prevReserva,
        nombre: userData.nombre,
        telefono: userData.telefono,
      }));

    } catch (error) {
      console.error('Error:', error);
      setReserva(null);
      alert(error.message);
    } finally {
      setLoading(false);
    }
  };

  const handleCancelar = async () => {
    if (!reserva?.codigo) {
      setModalType('error');
      setModalTitle('Error');
      setModalDesc('No se puede cancelar la reserva: código no encontrado.');
      setModalOpen(true);
      return;
    }
  
    try {
      const response = await fetch(`http://localhost:4002/reservas/${reserva.id}`, {
        method: 'DELETE',
      });
  
      if (!response.ok) {
        throw new Error('No se pudo cancelar la reserva.');
      }
  
      // Mostrar modal de éxito
      setModalType('success');
      setModalTitle('Reserva cancelada');
      setModalDesc('La reserva fue cancelada exitosamente.');
      setModalOpen(true);
      setReserva(null);  // Limpiar reserva
    } catch (error) {
      console.error('Error al cancelar la reserva:', error);
      // Mostrar modal de error
      setModalType('error');
      setModalTitle('Error al cancelar');
      setModalDesc('Ocurrió un error al cancelar la reserva. Inténtalo más tarde.');
      setModalOpen(true);
    }
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
        <button
          type="submit"
          className={styles['buscar-button']}
          disabled={loading}
        >
          {loading ? 'Buscando...' : 'Buscar'}
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

      {/* Mostrar el modal si está abierto */}
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
              window.location.href = '/'; // Redirigir al inicio si es éxito
            }
          }}
        />
      )}
    </div>
  );
}

export default Gestionar;
