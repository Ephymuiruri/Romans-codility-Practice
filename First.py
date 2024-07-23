def BankBalance(R,v):
    bank1= 0
    bank2 = 0
    lowestA = 0
    lowestB = 0
    for i in range(0,len(v)):
        transferAmount = v[i]
        recipient = R[i]
        print(transferAmount,recipient)
        if recipient == "A":
            bank1 = bank1 + transferAmount
            bank2 = bank2 - transferAmount
            print(recipient,bank1,bank2)
        else:
            bank1 = bank1 - transferAmount
            bank2 = bank2 + transferAmount
            print(bank1,bank2)
        if bank1 == lowestA or bank1 < lowestA:
            lowestA = bank1
        elif bank2 == lowestB or bank2 < lowestB:
            lowestB = bank2
    print(lowestA,lowestB)
    return [abs(lowestA),abs(lowestB)]

string ="ABAB"
values = [10, 5, 10, 15]   

print(BankBalance(string,values))
