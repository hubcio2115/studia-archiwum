const isPalindrome = (arr) => {
  const temp = arr.join("");
  return temp === temp.split("").reverse().join("");
};

console.log(isPalindrome([1, 1]));
