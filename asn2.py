import math
import sys

x = str(input("Welcome to the EOQ Calculator prepared by Jack Hotaling\nEnter q to quit or the name of the coffee\n"))
totalQ = 0

while x != 'q':
  d = float(input("Please enter the demand\n"))
  c = float(input("Please enter the unit cost\n"))
  k = float(input("Please enter the order cost\n"))
  h = float(input("Please enter the holding cost\n"))

  q = math.sqrt((2*d*k)/h)
  tac = ((q/2)*h)+((d*k)/q)+(d*c)
  t = (q/d)*12
  totalQ += q


  print("Given D={0:.2f}, C={1:.2f}, K={2:.2f}, h={3:.2f}\nYou should order {4:.2f}lbs. of {5:s} every {6:.2f} months for a total of ${7:.2f}" .format(d, c, k, h, q, x, t, tac)) 

  x = str(input("Enter q to quit or the name of the coffee\n"))

else:
  print("If you purchase all of the coffee you will need space to hold {0:.2f} lbs. of coffee.\nPress any key to exit ...\n" .format(totalQ))

  if input(): exit()