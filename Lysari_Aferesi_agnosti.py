#Σημείωμα για εσάς, αγνοήστε τα comments σαν αυτό. 


#Title here.
print("Alpha 0.1.4")
print("---------------------")
def Lysi():
    AT = 100
    AT_number = int(input("Αρχική τιμή: "))
    P = None
    TT = int(input("Τελική τιμή: "))
    #==================================#
    #This the logic on  how to do said operation.
    def Lysi_logic():
        LYSI = TT - AT_number
        LYSI_2 = AT_number / AT
        LYSI = LYSI / LYSI_2
        LYSI = int(LYSI)
        print(LYSI)
    Lysi_logic()
Lysi()