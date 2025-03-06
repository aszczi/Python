i = float(input ("podaj cene: "))


if i<300:
  print (f"cena po rabacie: {i*0.9} wartosc rabatu {i*0.1}")
else:
  print("cena po rabacie: {} wartosc rabatu {}".format(i*0.8, i*0.2))



