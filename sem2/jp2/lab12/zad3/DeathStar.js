"use strict";

import { Ship } from "./Ship";

export class DeathStar extends Ship {
  constructor(position) {
    super("Empire", position, 100, 10000);

    this.deathRayAvailable = true;
  }

  makeDamage(enemyShip) {
    if (this.deathRayAvailable) {
      Ship.makeDamage(enemyShip);
      this.deathRayAvailable = false;

      setTimeout(() => {
        this.deathRayAvailable = true;
      }, 10000);
    } else console.log("Death Ray Unavailable");
  }
}
