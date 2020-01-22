#! /usr/bin/env python3

# Muhammad Luqman
# calculate the square root of a number.

def sqrt(x):
  """
  calculate the square root of argument x.
  """
  # check that x is positive
  if x < 0:
    print("ErrorL negative value supplied")
    return -1
  else:
    print("Here we go..")

  # initial guess for the square root.
  z = x / 2.0

  #continuously improve the guess
  # adapted from https://tour.golang.org/flowcontrol/8
  while abs(x - (z*z)) > 0.000001 :
    z = z - (((z * z) - x) / (2 * z))

  return z

myval = 63.0
print("The square root of",myval,"is",sqrt(myval))

