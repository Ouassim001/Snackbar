import time
print("|------welcome at Snackbar PO!------|")

def want():
    want = input("do you want to order.  Y/N\n").lower()
    if want == "Y" or want == "y":
        print("good")
    else:
        print("OK Goodbye")
    

def order():
        print("what do you want?")
        time.sleep(1)
        menu = input("""MENU
        $1,50 - French Fries -------  |Type -a- for French Fries
        $0,50 - Frikandel Sausage  -  |Type -b- for Frikandel Sausage 
        $0,75 - Croquette ----------  |Type -c- for Croquette\n""")

        if menu == "a" or menu == "A":
            more = input("anything else?  Y/N \n")
            if more  == "Y" or more == "y":
                menu = input("""MENU
        $1,50 - French Fries -------  |Type -a- for French Fries
        $0,50 - Frikandel Sausage  -  |Type -b- for Frikandel Sausage 
        $0,75 - Croquette ----------  |Type -c- for Croquette\n""")

            elif more == "N" or more == "n":
                print("ok")
        if menu == "b" or menu == "B":
            more = input("anything else?  Y/N \n")
            if more  == "Y" or more == "y":
                menu = input("""MENU
        $1,50 - French Fries -------  |Type -a- for French Fries
        $0,50 - Frikandel Sausage  -  |Type -b- for Frikandel Sausage 
        $0,75 - Croquette ----------  |Type -c- for Croquette\n""")
            elif more == "N" or more == "n":
                print("ok")
        
        if menu == "c" or menu == "C":
            more = input("anything else?  Y/N \n")
            if more  == "Y" or more == "y":
                menu = input("""MENU
        $1,50 - French Fries -------  |Type -a- for French Fries
        $0,50 - Frikandel Sausage  -  |Type -b- for Frikandel Sausage 
        $0,75 - Croquette ----------  |Type -c- for Croquette\n""")
            elif more == "N" or more == "n":
                print("ok")

def much(order):
    a = int(input("how much do you want from -a- \n"))
    adda = 0
    if a < 40 and a > 0:
        adda = 1.50 * a
    
          

    b = int(input("how much do you want from -b- \n"))
    addb = 0
    if b < 40 and b > 0:
        addb = 1.50 * b
        
        
    
    c = int(input("how much do you want from -c- \n"))
    addc = 0
    if c < 40 and c > 0:
        addc = 1.50 * c
        
    

        


    if adda > 0:
        print("|---French Fries--------|${0}".format(adda))
    else:
        print("")
    
    if addb > 0:
        print("|---Frikandel Sausage---|${0}".format(addb))
    else:
        print("")

    if addc > 0:
        print("|--- Qroquette----------|${0}".format(addc))
    else:
        print("")




want()
order()
much(order)

