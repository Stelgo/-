#Σημείωμα για εσάς, αγνοήστε τα comments σαν αυτό. 


#Title here.
print("Alpha 0.2.0")
print("---------------------")
def Lysi():
    AT = 100
    AT_number = int(input("Αρχική τιμή: "))
    P = None
    TT = int(input("Τελική τιμή: "))
    #==================================#
    #This the logic on  how to do said operation.
    def Lysi_logic():
        LYSI = AT_number - TT
        LYSI_2 = AT_number / AT
        LYSI = LYSI / LYSI_2
        LYSI = int(LYSI)
        print("Τελική πρόσθεση είναι", LYSI)
    Lysi_logic()
Lysi()
