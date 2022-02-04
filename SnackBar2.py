frites = "French Fries?\n"
frikad1 = "Normal Frikadel?\n"
frikad2 = "veggie Frikadel?\n"
frikadel3 = "XXL Frikadel?\n"
qroqBread = "Qroquette With Bread?\n"
QroqNoBread = "Qroquette without bread?\n"



def much():
    amountfries = int(input("how many " + frites))
    amountfrikad1 = int(input("how many " + frikad1))
    amountfrikad2 = int(input("how many " + frikad2))
    amountfrikad3 = int(input("how many " + frikadel3))
    amountqroq1 = int(input("how many " + qroqBread))
    amountqroq2 = int(input("how many " + QroqNoBread))
    for i in range(amountfries):
        fritesauce = input("what sauce for the fries?\n")
    
    # for f in range(amountfrikad1):
    #     ofkind = input("what kind of frikadel?\n")

    # for f in range(amountfrikad2):
    #     ofkind = input("what kind of frikadel?\n")

    # for f in range(amountfrikad3):
    #     ofkind = input("what kind of frikadel?\n")

    # for k in range(amountqroq):
    #     bread = input("with or without bread?\n")

    fritesauce = 0.20 * amountfries
    print(fritesauce)

    amountfrikad1 = 0.50 * amountfrikad1
    print(amountfrikad1)

    amountfrikad2 = 0.55 * amountfrikad2
    print(amountfrikad2)

    amountfrikad3 = 5.67 * amountfrikad3
    print(amountfrikad3)

    amountqroq1 = 0.75 * amountqroq1
    print(amountqroq1)

    amountqroq2 = 0.75 * amountqroq2
    print(amountqroq2)

    float(print(frites + "---" + fritesauce))

    















much()