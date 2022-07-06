class Fraction {
  constructor(numerator, denumerator) {
    this.numerator = numerator;
    this.denumerator = denumerator;
  }
  multiplyBy(v) {
    if (v.constructor == Fraction) {
      this.numerator *= v.numerator;
      this.denumerator *= v.denumerator;
    }
    if (typeof v == "number" && v > 0) this.numerator *= v;
  }
  multiply(x, y) {
    return Fraction(x.numerator * y.numerator, x.denumerator * y.denumerator);
  }
  print() {
    console.log(`${this.numerator}/${this.denumerator}`);
  }
}

const myFraction = new Fraction(1, 2);
myFraction.multiplyBy(new Fraction(1, 2));
myFraction.multiplyBy(2);
myFraction.print();
