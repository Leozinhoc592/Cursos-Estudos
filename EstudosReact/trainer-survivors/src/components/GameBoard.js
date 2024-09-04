import React, { useState, useEffect } from 'react';
import Player from './Player';
import Enemy from './Enemy';
import Projectile from './Projectile';
import { isColliding } from '../utils/collision';

const GameBoard = () => {
  const [playerPosition, setPlayerPosition] = useState({ x: 50, y: 50, width: 20, height: 20 });
  const [enemies, setEnemies] = useState([{ x: 100, y: 100, width: 20, height: 20, health: 100 }]);
  const [projectiles, setProjectiles] = useState([]);
  const [keysPressed, setKeysPressed] = useState({});

  const movePlayer = () => {
    let newX = playerPosition.x;
    let newY = playerPosition.y;

    if (keysPressed.ArrowUp) newY -= 5;
    if (keysPressed.ArrowDown) newY += 5;
    if (keysPressed.ArrowLeft) newX -= 5;
    if (keysPressed.ArrowRight) newX += 5;

    setPlayerPosition({ ...playerPosition, x: newX, y: newY });
  };

  const shootProjectile = () => {
    const angle = keysPressed.ArrowRight ? 0 : keysPressed.ArrowLeft ? 180 : keysPressed.ArrowUp ? -90 : 90;
    const newProjectile = {
      x: playerPosition.x + playerPosition.width / 2,
      y: playerPosition.y + playerPosition.height / 2,
      angle: angle,
      speed: 10,
    };
    setProjectiles((prevProjectiles) => [...prevProjectiles, newProjectile]);
  };

  const moveProjectiles = () => {
    setProjectiles((prevProjectiles) =>
      prevProjectiles
        .map((projectile) => {
          const radians = (projectile.angle * Math.PI) / 180;
          return {
            ...projectile,
            x: projectile.x + Math.cos(radians) * projectile.speed,
            y: projectile.y + Math.sin(radians) * projectile.speed,
          };
        })
        .filter((projectile) => projectile.x >= 0 && projectile.x <= 500 && projectile.y >= 0 && projectile.y <= 500)
    );
  };

  useEffect(() => {
    const handleKeyDown = (e) => {
      setKeysPressed((prevKeys) => ({
        ...prevKeys,
        [e.key]: true,
      }));
      if (e.key === ' ') shootProjectile();
    };

    const handleKeyUp = (e) => {
      setKeysPressed((prevKeys) => ({
        ...prevKeys,
        [e.key]: false,
      }));
    };

    window.addEventListener('keydown', handleKeyDown);
    window.addEventListener('keyup', handleKeyUp);

    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      window.removeEventListener('keyup', handleKeyUp);
    };
  }, [keysPressed]);

  useEffect(() => {
    const interval = setInterval(() => {
      movePlayer();
      moveProjectiles();

      setEnemies((prevEnemies) =>
        prevEnemies
          .map((enemy) => {
            const dx = playerPosition.x - enemy.x;
            const dy = playerPosition.y - enemy.y;
            const angle = Math.atan2(dy, dx);

            const newEnemyPosition = {
              ...enemy,
              x: enemy.x + Math.cos(angle) * 2,
              y: enemy.y + Math.sin(angle) * 2,
            };

            projectiles.forEach((projectile) => {
              if (isColliding(projectile, newEnemyPosition)) {
                newEnemyPosition.health -= 20;
              }
            });

            return newEnemyPosition;
          })
          .filter((enemy) => enemy.health > 0)
      );
    }, 20);

    return () => clearInterval(interval);
  }, [keysPressed, playerPosition, projectiles]);

  useEffect(() => {
    const spawnEnemy = () => {
      const side = Math.floor(Math.random() * 4);
      let x, y;
      if (side === 0) {
        x = 0;
        y = Math.random() * 500;
      } else if (side === 1) {
        x = 500;
        y = Math.random() * 500;
      } else if (side === 2) {
        x = Math.random() * 500;
        y = 0;
      } else {
        x = Math.random() * 500;
        y = 500;
      }
      setEnemies((prevEnemies) => [...prevEnemies, { x, y, width: 20, height: 20, health: 100 }]);
    };

    const interval = setInterval(spawnEnemy, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="game-board">
      <Player position={playerPosition} />
      {projectiles.map((projectile, index) => (
        <Projectile key={index} position={projectile} />
      ))}
      {enemies.map((enemy, index) => (
        <Enemy key={index} position={enemy} />
      ))}
    </div>
  );
};

export default GameBoard;