#import libraries here

def main():
  x=int(input('Enter the wavelength in nm: '))
  if x>=380 and x<450:
    print('The relevant color is Violet')
  elif x>=450 and x<495:
    print('The relevant color is Blue')
  elif x>=495 and x<570:
    print('The relevant color is Green')
  elif x>=570 and x<590:
    print('The relevant color is Yellow')
  elif x>=590 and x<620:
    print('The relevant color is Orange')
  elif x>=620 and x<750:
    print('The relevant color is Red')
  else:
    print('Invalid input!')
  pass

if __name__ == "__main__":
  main()
