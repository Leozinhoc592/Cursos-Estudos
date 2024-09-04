import React from 'react';

const Projectile = ({ position }) => {
  const { x, y } = position;

  const projectileStyle = {
    position: 'absolute',
    top: y,
    left: x,
    width: '10px',
    height: '10px',
    backgroundColor: 'red',
    borderRadius: '50%',
  };

  return <div style={projectileStyle} />;
};

export default Projectile;