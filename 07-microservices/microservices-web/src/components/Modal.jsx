import React from 'react';
import { FiCheckCircle, FiAlertCircle } from 'react-icons/fi'; 
import '../styles/Modal.css';

const AlertModal = ({ isOpen, onClose, title, description, onConfirm, type }) => {
  if (!isOpen) return null;

  const modalClass = type === 'success' ? 'modal-success' : 'modal-error';
  const icon = type === 'success' ? <FiCheckCircle size={48} /> : <FiAlertCircle size={48} />;
  const buttonClass = type === 'success' ? 'confirm-btn-success' : 'confirm-btn-error';

  return (
    <div className="modal-back">
      <div className={`modal ${modalClass}`}>
        <button className="close-btn" onClick={onClose}>&times;</button>
        <div className="modal-icon">{icon}</div>
        <h2 className="modal-title">{title}</h2>
        <p className="modal-desc">{description}</p>
        <button className={`confirm-btn ${buttonClass}`} onClick={onConfirm}>Aceptar</button>
      </div>
    </div>
  );
};

export default AlertModal;
