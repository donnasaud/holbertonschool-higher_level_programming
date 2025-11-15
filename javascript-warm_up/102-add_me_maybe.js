#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  const newValue = number + 1;
  theFunction(newValue);
};
