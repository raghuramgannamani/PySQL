def main():
    #Hard-Coded bill Variable PROGRAM 1
    Bill=85
    TotalTax=0.16*Bill
    TotalTip=0.21*Bill
    print("Your Original Bill amount is:$",Bill)
    print("Yout Tax is:${0:.2f}".format(TotalTax))
    print("Your Tip is:${0:.2f}".format(TotalTip))
    print("Yout Total is:${0:.2f}".format(Bill+TotalTax+TotalTip))

    #User Input PROGRAM 2
    OriginalBill = float(input("Please Enter your Original Bill Amount:$"))
    print("Your Original Bill Amount is:$",OriginalBill)
    Tax = (1.16*OriginalBill)-OriginalBill
    Tip = (1.21*OriginalBill)-OriginalBill
    print("Your Tax is:${0:.2f}".format(Tax))
    print("Your Tip is:${0:.2f}".format(Tip))
    Total = Tax+Tip+OriginalBill
    print("Your Total is:$",Total)
main()