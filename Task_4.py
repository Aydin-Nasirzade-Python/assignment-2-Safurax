#import libraries here

def main():
  x=int(input('Enter the year [ex. 2021]: '))
  if x>=0:
    if x%12==8:
        print(f'{x} is the year of Dragon')
    elif x%12==9:
        print(f'{x} is the year of Snake')
    elif x%12==10:
        print(f'{x} is the year of Horse')
    elif x%12==11:
        print(f'{x} is the year of Sheep')
    elif x%12==7:
        print(f'{x} is the year of Hare')
    elif x%12==1:
        print(f'{x} is the year of Rooster')
    elif x%12==2:
        print(f'{x} is the year of Dog')
    elif x%12==3:
        print(f'{x} is the year of Pig')
    elif x%12==4:
        print(f'{x} is the year of Rat')
    elif x%12==5:
        print(f'{x} is the year of Ox')
    elif x%12==6:
        print(f'{x} is the year of Tiger')
    else:
        print(f'{x} is the year of Monkey')
  else:
    print('Invalid year!')
  pass

if __name__ == "__main__":
  main()
