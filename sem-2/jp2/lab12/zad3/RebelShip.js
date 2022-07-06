"use strict";

import { Ship } from "./Ship";

export class RebelShip extends Ship {
  constructor(position, strength, health) {
    super("Rebel Alliance", position, strength, health);
  }

  hyperSpeed() {
    this.position = undefined;
  }
}
