#import libraries here

def main():
  x=input('Enter name of the month [ex. June]: ')
  y=int(input('Enter the day [ex. 5]: '))
  if x=='January' or x=='February' or (x=='March' and y<20 and y>=1) or (x=='December' and y>=21 and y<=31):
    print(f'{x} {y} is in Winter')
  elif x=='April' or x=='May' or (x=='March' and y>=20 and y<=31) or (x=='June' and y<21 and y>=1):
    print(f'{x} {y} is in Spring')
  elif x=='July' or x=='August' or (x=='June' and y>=21 and y<=30) or (x=='September' and y<22 and y>=1):
    print(f'{x} {y} is in Summer')
  elif x=='October' or x=='November' or (x=='September' and y>=22 and y<=30) or (x=='December' and y>=1 and y<=20):
    print(f'{x} {y} is in Fall')
  else:
    print('Error')
  pass

if __name__ == "__main__":
  main()
