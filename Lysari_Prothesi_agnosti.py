#Σημείωμα για εσάς, αγνοήστε τα comments σαν αυτό. 


#Title here.
print("Alpha 0.1.4")
print("---------------------")
def Lysi():
    AT = 100
    AT_number = int(input("Αρχική τιμή: "))
    E = None
    TT = int(input("Τελική τιμή: "))
    #==================================#
    #This the logic on  how to do said operation.
    def Lysi_logic():
        LYSI = AT_number - TT
        LYSI = LYSI * AT
        LYSI = LYSI / AT_number
        print(LYSI)
    Lysi_logic()
Lysi()