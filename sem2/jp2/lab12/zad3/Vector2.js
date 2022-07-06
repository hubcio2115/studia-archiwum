"use strict";

export class Vector2 {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }
  diff(vector) {
    const [x1, y1] = vector;
    this.x -= x1;
    this.y -= y1;
  }
  multiplyBy(number) {
    this.x *= number;
    this.y *= number;
  }
  toString() {
    return `x: ${this.x} y: ${this.y}`;
  }
}
