cena = 2.35
daudzums = int(input("Ievadi daudzumu: "))
maksa = cena*daudzums
if daudzums>2:
  maksa=maksa*0.90
print(maksa)
print("--------------------")

pirmais = int(input("Ievadi 1. spelētāja punktus: "))
otrais = int(input("Ievadi 2. spelētāja punktus: "))
if pirmais>otrais:
  print("Uzvar pirmais!")
if pirmais<otrais:
  print("Uzvar otrais!")
if pirmais==otrais:
  print("Neizšķirts!")
print("--------------------")

sk1 = int(input("Ievadi 1. skaitli: "))
sk2 = int(input("Ievadi 2. skaitli: "))
sk3 = int(input("Ievadi 3. skaitli: "))
print(min(sk1,sk2,sk3))
print("--------------------")

svars = float(input("Ievadi svaru kg: "))
garums =  float(input("Ievadi garumu m: ")) 
optim = garums*100-svars
if -7<=svars-optim<=7:
  print("Normāls svars!")
elif svars-optim>7:
  print("Pārāk liels svars!")
else:
  print("Pārāk mazs svars!")
print("--------------------")