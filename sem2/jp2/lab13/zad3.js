import axios from "axios";
import { inspect } from "util"; // funkcja ta loguje w nodzie cały obiekt ze wszystkimi zagnieżdżeniami, a nie od pewnego momentu [Object]

(async () => {
  const ids = Array.from(Array(5).keys()).map((_) => {
    return Math.floor(Math.random() * 99 + 1);
  });

  try {
    const entries = [];
    for (const index of ids) {
      const post = await axios.get(
        `https://jsonplaceholder.typicode.com/posts/${index}`
      );

      const { title, body } = post.data;

      entries.push({ title, body });
    }

    const comments = [];
    for (const index of ids) {
      const resComments = await axios.get(
        `https://jsonplaceholder.typicode.com/posts/${index}/comments`
      );

      comments.push(
        resComments.data.map((comment) => {
          const { name, email, body } = comment;
          return { name, email, body };
        })
      );
    }

    const result = entries.map((entry, index) => {
      return { entry, comments: comments[index] };
    });


    console.log(
      inspect(result, { showHidden: false, depth: null, colors: true })
    )
  } catch (e) {
    console.log(e);
  }
})();
