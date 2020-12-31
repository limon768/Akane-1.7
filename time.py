import urllib.request
import re




AkanesNumber = 1
userNumber = 10

if userNumber > AkanesNumber:
    print("Your Number is too Big")
elif userNumber<AkanesNumber:
     print("Your Number is too Short")
elif userNumber == AkanesNumber:
    print("Good Game Well Played")