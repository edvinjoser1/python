# Variabler för att komma ihåg namn och ålder

# Läsa in namn

#Läsa in ålder

#Skriva ut hej namn och du är x gammal

Namn = input("Vad heter du? ")
age = int(input("Hur gammal är du? "))
nineteen = int(19)
print("hej " + Namn + ". Du är " + str(age) + " år gammal")

if age < nineteen:
    print("Du är inte 19 år xd")
elif age > 19:
    print("Du är över 19 år xd")
else:
    print("GRATTIS 19 ÅRING XD")

