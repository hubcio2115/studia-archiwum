// It may not be the best solution but it is 100% mine.
/**
 * Function  takes a matrix of numbers and returns sum of each diagonal going up
 * from the primary diagonal and then from the left down corner to the primary diagonal.
 * @param matrix number[][]
 * @returns number[]
 */
const sumOfDiagonals = (matrix) => {
  return [
    // This part creates sums of the primary diagonal and up
    ...matrix.reduce(
      (acc, _, index) => {
        matrix.reduce(
          (helper) => {
            if (!(helper[1] > matrix.length - 1)) {
              if (acc[index] === undefined) acc[index] = 0;
              acc[index] += matrix[helper[0]][helper[1]];
            }

            return [helper[0] + 1, helper[1] + 1];
          },
          [0, index]
        );
        return acc;
      },
      [0]
    ),
    // This part creates sums of the left down corner to the primary diagonal
    ...matrix
      .reduce(
        (acc, _, index) => {
          matrix.reduce(
            (helper) => {
              if (!(helper[0] > matrix.length - 1)) {
                if (acc[index] === undefined) acc[index] = 0;
                acc[index] += matrix[helper[0]][helper[1]];
              }

              return [helper[0] + 1, helper[1] + 1];
            },
            [index + 1, 0]
          );

          return acc;
        },
        [0]
      )
      .map((_, index, arr) => {
        return arr[arr.length - index - 1];
      }),
  ];
};

const matrix = [
  [1, 2, 3, 5],
  [4, 5, 6, 6],
  [7, 8, 9, 6],
  [7, 8, 9, 6],
];

console.log(sumOfDiagonals(matrix));
