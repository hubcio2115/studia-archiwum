import { games } from "./games";

const links = games.reduce((acc, game) => {
  return acc.length < 4 ? [...acc, game.imageUrl] : acc;
}, []);

console.log(links);
