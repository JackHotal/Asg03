import math
import sys

def calcEOQ(d, c, k, h):
  q = math.sqrt((2*d*k)/h)
  tac = ((q/2)*h)+((d*k)/q)+(d*c)
  t = (q/d)*12
  eoq = (q, tac, t)
  return eoq

def newBrand(x):
  print("VALIDATE DATA")
  #data validation (positive + integer)
  d = float(input("How many pounds of coffee per year do you need to stock?\n"))
  c = float(input("Please enter the unit cost\n"))
  k = float(input("Please enter the order cost\n"))
  h = float(input("Please enter the holding cost\n"))

  brand = [x, d, c, k, h]
  eoq = calcEOQ(d, c, k, h)
  for i in eoq:
    brand.append(i)
  return brand

def main():
  x = str(input("Welcome to the EOQ Calculator prepared by Jack Hotaling\nEnter q to quit or the name of the coffee\n"))
  totalQ = 0

  #store brands:
  brandList = []

  while x != 'q':
    newB = newBrand(x)
    brandList.append(newB)
    print(newB[6])
    totalQ += newB[6]
    x = str(input("Enter q to quit and display the results or the name of the coffee\n"))
  else:
    print('buy this shit')
    for B in brandList:
      print("Buy {0}".format(B[0]))

    print("store:{0}".format(totalQ))
    if input(): sys.exit()

main()

if __name__ == "__main()__":
  main()