import React from 'react';

const Player = ({ position }) => {
  return (
    <div
      className="player"
      style={{
        position: 'absolute',
        left: position.x,
        top: position.y,
        width: 20, // Largura da hitbox
        height: 20, // Altura da hitbox
        backgroundColor: 'blue', // Para diferenciar visualmente
      }}
    />
  );
};

export default Player;