#import libraries here

def main():
  x=input('Enter a month [ex. March]: ')
  y=int(input('Enter the day [ex. 12]: '))
  if  (x=='December' and y>=22 and y<=31) or (x=='January' and y>=1 and y<=19):
    print('Your zodiac sign is Capricorn')
  elif (x=='January' and y>=20 and y<=31) or (x=='February' and y>=1 and y<=18):
    print('Your zodiac sign is Aquarius')
  elif (x=='February' and y>=19 and y<=29) or (x=='March' and y>=1 and y<=20):
    print('Your zodiac sign is Pisces')
  elif (x=='March' and y>=21 and y<=31) or (x=='April' and y>=1 and y<=19):
    print('Your zodiac sign is Aries')
  elif (x=='April' and y>=20 and y<=30) or (x=='May' and y>=1 and y<=20):
    print('Your zodiac sign is Taurus')
  elif (x=='May' and y>=21 and y<=31) or (x=='June' and y>=1 and y<=20):
    print('Your zodiac sign is Gemini')
  elif (x=='June' and y>=21 and y<=30) or (x=='July' and y>=1 and y<=22):
    print('Your zodiac sign is Cancer')
  elif (x=='July' and y>=23 and y<=31) or (x=='August' and y>=1 and y<=22):
    print('Your zodiac sign is Leo')
  elif (x=='August' and y>=23 and y<=31) or (x=='September' and y>=1 and y<=22):
    print('Your zodiac sign is Virgo')
  elif (x=='September' and y>=23 and y<=30) or (x=='October' and y>=1 and y<=22):
    print('Your zodiac sign is Libra')
  elif (x=='October' and y>=23 and y<=31) or (x=='November' and y>=1 and y<=21):
    print('Your zodiac sign is Scorpion')
  elif (x=='November' and y>=22 and y<=30) or (x=='December' and y>=1 and y<=21):
    print('Your zodiac sign is Sagittarius')
  else:
    print('Either a month or a day is invalid!')
  pass

if __name__ == "__main__":
  main()
