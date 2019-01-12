#class that define only attributes or properties to be used in functions.
#setting the values and initialising each and every property as a Item attribute.
class Recyclable:

    def __init__(self,):
        #name of item or product.
        self.item = "";
        #itemnumber for fetching the item name from the product dictionary.
        self.itemnumber=0;
        #total number of item of the particular product.
        self.totalnumberitem=0;

        #product dictionary for fetching product realtime.
        self.product = {
            1: "Can",
            2: "Bottle",
            3: "Paper",
            4: "Stop"
        }
        #prices dictionary for fetching the base prices of desired inserted product in the machine.
        self.prices = {
            "Can":0.2,
            "Bottle":0.5,
            "Paper":0.1
        }
        #counter for counting the number of items that is placed in the machine, initially it is 0.
        self.count={
            "Can":0,
            "Bottle":0,
            "Paper":0
        }
        #breakdown prices for each and every product that is inserted in the machine.
        self.totalamount={
            "Can":0,
            "Bottle":0,
            "Paper":0
        }
        #balance for calcualting final balance and then transfer to showbalance of RecyclingMachine class.
        self.balance=0;

