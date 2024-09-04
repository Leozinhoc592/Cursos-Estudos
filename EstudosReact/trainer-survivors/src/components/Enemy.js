import React from 'react';

const Enemy = ({ position }) => {
  return (
    <div
      className="enemy"
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: 20, // Largura da hitbox
        height: 20, // Altura da hitbox
        backgroundColor: 'red', // Para diferenciar visualmente
      }}
    />
  );
};

export default Enemy;