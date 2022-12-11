// on a tandem bicycle, each cyclist has a top speed; the bicycle will travel at
// the higher speed of the two. each bicycle has a redShirt cyclist and a blueShirt cyclist

// input: two arrays of speeds of bicyclists, and a boolean representing whether
// the goal is to get the highest possible max speed or highest possible minimum speed
// output: if 'fastest' is true, return max possible total speed;
// else, return minimum total speed;
// "total speed" defined as the sum of the speeds of all tandem bicycles

// to MINIMIZE loss, pair the fastest and slowest together
// to MAXIMIZE loss, minimizing the average speed differential for each pair
function tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest) {
  redShirtSpeeds.sort((a, b) => a - b);
  // would have been better to use a ternary when sorting 2nd array
  // ex: (fastest ? a-b : b-a)
  blueShirtSpeeds.sort((a, b) => a - b);

  let speed = 0;
  if (fastest) {
    for (let i = 0; i < redShirtSpeeds.length; i++) {
      // iterates through redshirts forwards, but blueshirts backwards (max differential)
      speed += Math.max(
        redShirtSpeeds[i],
        blueShirtSpeeds[blueShirtSpeeds.length - (i + 1)]
      );
    }
  } else {
    for (let i = 0; i < redShirtSpeeds.length; i++) {
      // iterates through both arrays the same (min differential)
      speed += Math.max(redShirtSpeeds[i], blueShirtSpeeds[i]);
    }
  }
  return speed;
}

module.exports = tandemBicycle;
