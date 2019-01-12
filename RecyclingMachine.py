from RecyclableItem import Recyclable as recyclable

#class RecyclingMachine for implementing various functions.
class RecyclingMachine :
    #constructor for initialising recyclable object, and balanceshow object.
    def __init__(self):

        self.recyclableitem=recyclable();
        self.showbalance=0;


    #function for selecting the product and checking the validation whether machine can accept or not.
    def select_product(self,itemnumber):
        #definig itemnumber such as 1,2,3,4 so that can fetch item from the dictionary.
        self.recyclableitem.itemnumber=itemnumber;
        #fetching item name from dictionary.
        self.recyclableitem.item=self.recyclableitem.product.get(self.recyclableitem.itemnumber);
        #validation whether number of items for particular product is reached maximum or not. if yes then cannot accept more.
        if(self.recyclableitem.count.get(self.recyclableitem.item)>=50):
            print(" Cannot be Accepted, overlimit")
        #else keep adding.
        else:
            print(" "+self.recyclableitem.item + " accepted ");
            #calculating number of items inserted for particular product, it is inserted on by one by main.py
            self.recyclableitem.totalnumberitem=self.recyclableitem.totalnumberitem+1;
            #after selecting product accepting the range of products.
            self.accept_product();

    #function for the calculation of prices after accepting the product in machine.
    def payout(self):
        #fetching base prices of every product from the dictionary prices.
        total_amount=(self.recyclableitem.prices.get(self.recyclableitem.item))
        #calculation for each and every input in the machine.
        self.recyclableitem.totalamount[self.recyclableitem.item]=self.recyclableitem.totalamount.get(self.recyclableitem.item)+total_amount;
        #finally storing balance result into showbalance for showing after every transaction.
        self.showbalance=self.recyclableitem.balance=self.recyclableitem.balance+total_amount;

    def accept_product(self):
        #accepting product into the machine and counting the same range of product one by one as it is inserted.
        self.recyclableitem.count[self.recyclableitem.item]=self.recyclableitem.count.get(self.recyclableitem.item)+1;
        #for final calculation.
        self.payout()

    #function for printing the final result of on going customer.
    def print_receipt(self):
        #for loop for getting the counts of each products and simultaneously price breakdowns of each product.
        #every data is stored in key and value so iteration is according key value.
        for key,val in self.recyclableitem.count.items():

            #not showing product that is not inserted in the machine, i.e value would be 0.
            if(val!=0):
                #printing the number of items placed in the machine with prices and name.
                print(str(val)+ " "+ key + "      " + str(self.recyclableitem.totalamount.get(key)));

        #total number of items and total amount to be paid.
        print("\n Number of items	   "+ str(self.recyclableitem.totalnumberitem))
        print(" Amount Paid :    $" +str(self.recyclableitem.balance))














