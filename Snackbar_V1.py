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
    amount = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20.21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
    a = int(input("how much do you want from -a- \n"))
    adda = 0
    if a in amount:
        adda = 1.50 * a
    
          

    b = int(input("how much do you want from -b- \n"))
    addb = 0
    if b in amount: 
        addb = 1.50 * b
        
        
    
    c = int(input("how much do you want from -c- \n"))
    addc = 0
    if c in amount:
        addc = 1.50 * c
        
    

        


    print("|---French Fries--------|${0}".format(adda))
    print("|---Frikandel Sausage---|${0}".format(addb))
    print("|--- Qroquette----------|${0}".format(addc))





        
        


want()
order()
much(order)

