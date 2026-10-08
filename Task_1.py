year=int(input("Dogum ilinizi daxil edin:"))
remainder=year%12
if remainder==0:
    zodiac="Monkey"
elif remainder==1:
    zodiac="Rooster"
elif remainder==2:
    zodiac="Dog"
elif remainder==3:
    zodiac="Pig"
elif remainder==4:
    zodiac="Rat"
elif remainder==5:
    zodiac="Ox"
elif remainder==6:
    zodiac="Tiger"
elif remainder==7:
    zodiac="Rabbit"
elif remainder==8:
    zodiac="Dragon"
elif remainder==9:
    zodiac="Snake"
elif remainder==10:
    zodiac="Horse"
else:
    zodiac="Sheep"
print("Your Chinese Zodiac Sign is:",zodiac)

