"use strict";

import { Vector2 } from "./Vector2";
import { Ship } from "./Ship";

// Vector2
const vector = new Vector2(10, 20);

vector.diff([0, 5]);
console.log(vector.toString());
vector.multiplyBy(5);
console.log(vector.toString());

// Ship
const allyShip = new Ship("ally", new Vector2(0, 0), 10, 50);
const enemyShip = new Ship("enemy", new Vector2(50, 10), 20, 50);

allyShip.getDistance(enemyShip);
allyShip.makeDamage(enemyShip);
allyShip.getDamage(50);
