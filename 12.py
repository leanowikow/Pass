#import module random
import random
#create a function pass_gen
def pass_gen(length):
  digits='1234567890'
  letter='ABCDEFGHIJKLMNOPRSTUVWXYZ'
  letter_2='abcdefghijklmnoprstuvwxyz'
  symbol='!@#$%^&*()_+'
  password=''
  var=[digits,letter,letter_2,symbol]
#password generation
  if length<12:
    return print ('Error! password shoud be more then 12 simbols')
  else:
    password+=random.choice(digits)
    password+=random.choice(letter)
    password+=random.choice(letter_2)
    password+=random.choice(symbol)
    while len(password) < length:
      password+=str(random.choice([random.randint(0,4)]))
    print(password)
pass_gen(12)
