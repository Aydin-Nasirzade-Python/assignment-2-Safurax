#import libraries here

def main():
  x=int(input('Enter the year [ex. 2021]: '))
  if x>=0:
    if x%12==8:
        print(f'{x} is the year of the Dragon')
    elif x%12==9:
        print(f'{x} is the year of the Snake')
    elif x%12==10:
        print(f'{x} is the year of the Horse')
    elif x%12==11:
        print(f'{x} is the year of the Sheep')
    elif x%12==7:
        print(f'{x} is the year of the Hare')
    elif x%12==1:
        print(f'{x} is the year of the Rooster')
    elif x%12==2:
        print(f'{x} is the year of the Dog')
    elif x%12==3:
        print(f'{x} is the year of the Pig')
    elif x%12==4:
        print(f'{x} is the year of the Rat')
    elif x%12==5:
        print(f'{x} is the year of the Ox')
    elif x%12==6:
        print(f'{x} is the year of the Tiger')
    else:
        print(f'{x} is the year of the Monkey')
  else:
    print('Invalid year!')
  pass

if __name__ == "__main__":
  main()
