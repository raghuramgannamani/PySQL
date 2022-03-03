def main():
    CustomerName = input("Enter the Customer's Name: ")
    NumOfKM = float(input("Enter the distance in kilometers for delivery (KM):"))
    CostOfRecord = float(input("Enter the cost of records purchased:$"))

    SalesTax = 1.14

    print("Purchase Summary For:" +CustomerName)
    DeliveryCost = NumOfKM * 15
    PurchaseCost = CostOfRecord * SalesTax
    TotalCost = DeliveryCost + PurchaseCost
    print ("Delivery Cost :${0:.2f}".format(DeliveryCost))
    print ("Purchase Cost: ${0:.2f}".format(PurchaseCost))
    print("Total Cost: ${0:.2f}".format(TotalCost))
main()
