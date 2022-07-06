"use strict";
import { Vector2 } from "./Vector2.js";

export class Ship {
  constructor(faction, position, strength, health) {
    this.faction = faction;
    this.position = position;
    this.strength = strength;
    this.health = health;
  }
  getDistance(enemyShip) {
    try {
      return [
        this.position.x - enemyShip.position.x,
        this.position.y - enemyShip.position.y,
      ];
    } catch (err) {
      console.log(err);
    }
  }
  checkHealth() {
    if (this.health <= 0) console.log("Statek został zniszczony!");
  }
  getDamage(amount) {
    this.health -= amount;
    this.checkHealth();
  }
  makeDamage(enemyShip) {
    enemyShip.health -= this.strength;
    enemyShip.checkHealth();
  }
}
