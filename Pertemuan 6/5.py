umur =  int(input("Masukan umur anda: "))

if umur < 0:
    print("you are kids")
elif umur >= 12 and umur < 18:
    print("you are young")
elif umur >= 18 and umur < 60:
    print("you are adult")
else:
    print("you are lansia")