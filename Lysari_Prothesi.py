#Σημείωμα για εσάς, αγνοήστε τα comments σαν αυτό. 


#Title here.
print("Alpha 0.1.4")
print("---------------------")
def Lysi():
    #variables for the problem are here.
    AT = 100
    AT_number = int(input("Αρχική τιμή: "))
    P = int(input("Πρόσθεση: "))
    TT = None
    #==================================#
    #This the logic on  how to do said operation.
    def Lysi_logic():
        LYSI = AT + P
        TT = LYSI
        TT = TT * AT_number
        TT = int(TT / AT)
        print("Τελική τιμή είναι", TT)
    Lysi_logic()
Lysi()
