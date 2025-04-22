#Σημείωμα για εσάς, αγνοήστε τα comments σαν αυτό. 


#Title here.
print("Alpha 0.1.4")
print("---------------------")
def Lysi():
    AT = 100
    AT_number = input("Αρχική τιμή: ")
    E = None
    TT = input("Τελική τιμή: ")
    #==================================#
    #This the logic on  how to do said operation.
    def Lysi_logic():
        LYSI = AT_number - TT
        LYSI = LYSI * AT
        LYSI = float(LYSI / AT_number)
        print("Τελική έκπτοση είναι", LYSI)
    Lysi_logic()
Lysi()
