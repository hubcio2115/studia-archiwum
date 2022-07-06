let nums = [1, 2, 3];

if (nums.every((value) => value > 0)) {
  nums.sort();
  if (nums[0] + nums[1] > nums[2]) {
    console.log("Z tych wartości można zrobić trójkąt.");
  } else {
    console.log("Z tych wartości nie można zrobić trójkąta.");
  }
}
