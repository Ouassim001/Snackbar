def much():
    amountfries = int(input("how many french fries?\n"))
    amountfrikad1 = int(input("how many normal frikadel?\n"))
    amountfrikad2 = int(input("how many veggie frikadel?\n"))
    amountfrikad3 = int(input("how many XXL frikadel?\n"))
    amountqroq = int(input("how many qroquette?\n"))
    for i in range(amountfries):
        fritesauce = input("what sauce for the fries?\n")
    
    # for f in range(amountfrikad1):
    #     ofkind = input("what kind of frikadel?\n")

    # for f in range(amountfrikad2):
    #     ofkind = input("what kind of frikadel?\n")

    # for f in range(amountfrikad3):
    #     ofkind = input("what kind of frikadel?\n")

    for k in range(amountqroq):
        bread = input("with or without bread?\n")

    fritesauce = 0.20 * amountfries
    print(fritesauce)

    amountfrikad1 = 0.50 * amountfrikad1
    print(amountfrikad1)

    amountfrikad2 = 0.55 * amountfrikad2
    print(amountfrikad2)

    amountfrikad3 = 5.67 * amountfrikad3
    print(amountfrikad3)

    amountqroq = 0.75 * amountqroq
    print(amountqroq)










much()