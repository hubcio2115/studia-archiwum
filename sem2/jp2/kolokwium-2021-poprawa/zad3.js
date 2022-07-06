class CoffeeShop {
  constructor(name, menu) {
    this.name = name;
    this.menu = menu;
    this.orders = [];
  }

  addOrder(name) {
    const item = this.menu.filter((item) => item.item === name)[0];

    if (item === undefined) return "This item is currently unavailable!";

    this.orders = [...this.orders, item];
    return "Order added!";
  }

  fulfillOrder() {
    if (this.orders.length === 0) return "All orders have been fulfilled!";

    const item = this.orders.shift();
    return `The ${item.item} is ready!`;
  }

  listOrder() {
    return this.orders;
  }

  dueAmount() {
    return this.orders.reduce((acc, currentItem) => {
      return acc + currentItem.price;
    }, 0);
  }

  cheapestItem() {
    return [...this.menu].sort((a, b) => a.price - b.price)[0].item;
  }

  drinksOnly() {
    return this.menu.reduce((acc, element) => {
      return element.type === "drink" ? [...acc, element.item] : acc;
    }, []);
  }

  foodOnly() {
    return this.menu.reduce((acc, element) => {
      return element.type === "food" ? [...acc, element.item] : acc;
    }, []);
  }
}

const shop = new CoffeeShop("Shop1", [
  { item: "cinnamon roll", type: "food", price: 4.99 },
  { item: "hot chocolate", type: "drink", price: 2.99 },
  { item: "lemon tea", type: "drink", price: 2.5 },
]);

console.log(shop.addOrder("espresso"));

console.log(shop.addOrder("hot chocolate"));
console.log(shop.addOrder("cinnamon roll"));

console.log(shop.listOrder());
console.log(shop.dueAmount());

console.log(shop.fulfillOrder());
console.log(shop.fulfillOrder());
console.log(shop.fulfillOrder());

console.log(shop.listOrder());
console.log(shop.dueAmount());

console.log(shop.cheapestItem());
console.log(shop.drinksOnly());
console.log(shop.foodOnly());
