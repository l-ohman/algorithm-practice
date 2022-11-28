// class photos
// difficulty: easy | type: greedy

// constraint: colors must be all on same row; person in front must be shorter than the person behind
// input: two arrays - one has height of all students with red shirts, other has blue shirts
// output: boolean of whether or not picture can be taken
// can assume each class has >=2 students

// works, but seems like a lot of unnecessary code...
function classPhotosFirstAttempt(redShirts, blueShirts) {
  let frontRow = redShirts.sort((a, b) => a - b);
  let backRow = blueShirts.sort((a, b) => a - b);

  if (redShirts[0] > blueShirts[0]) {
    frontRow = blueShirts;
    backRow = redShirts;
  } else if (redShirts[0] === blueShirts[0]) {
    return false;
  }

  for (let i = 0; i < frontRow.length; i++) {
    if (frontRow[i] >= backRow[i]) {
      return false;
    }
  }
  return true;
}

function classPhotos(redShirts, blueShirts) {
  redShirts.sort((a, b) => a - b);
  blueShirts.sort((a, b) => a - b);

  const isFrontRowRed = redShirts[0] < blueShirts[0];
  for (let i = 0; i < redShirts.length; i++) {
    if (redShirts[i] === blueShirts[i]) return false;

    if (isFrontRowRed) {
      if (redShirts[i] > blueShirts[i]) return false;
    } else {
      if (redShirts[i] < blueShirts[i]) return false;
    }
  }
  return true;
}

module.exports = classPhotos;
