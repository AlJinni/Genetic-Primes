exports.method(currentRound, opHistory, myHistory) {
  if (currentRound/2 != Math.round(currentRound/2)) {
    return false;
  } else if (currentRound > 2) {
    return opHistory[opHistory.length-2];
  } else {
    return true;
  }
}
