import { booksArray } from "./books.js";

const result = booksArray.reduce((acc, book) => {
  const { title, author } = book;

  Array.isArray(book.genre)
    ? book.genre.map((genre) => {
        acc[genre]
          ? acc[genre].push({ title, author })
          : (acc[genre] = [{ title, author }]);
      })
    : acc[book.genre]
    ? acc[book.genre].push({ title, author })
    : (acc[book.genre] = [{ title, author }]);

  return acc;
}, {});

console.log(result);
