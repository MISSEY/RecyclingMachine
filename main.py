#Please Use Python 2.7 , for Python 3 input function and Dictionary should be change.

#Entry Point of the Program. Main driver function for implementing RecyclingMachine.

#importing 2 classes that is RecyclingMachine and Recyclable....
#Recyclable only define properties and desired attributes for the methods of RecylingMachine, just like ADO.

from RecyclingMachine import  RecyclingMachine as recyclemachine;
from RecyclableItem import Recyclable as recyclable;

#Initiating the object of Recylable to access the recyclable properties
ritem=recyclable();

#Intial value for the machine is True i.e N for welcoming new customer
status="N";

# Loop till the Machine accepts new customer
while(status=="N" or status=="n"):
    print(" -----New Customer-----");
    # Initially item is null and when user enter the item it gets the value from 3 products.
    item="";

    #Initialising new object for the RecyclingMachine for implementing functions required for Recyclying Machine.
    recycleobj=recyclemachine();

    #Loop till user stops entering the products into the Machine.
    while(item!="Stop"):

        #Printing the Balance after every single transaction.
        print("\n Balance : " +str(recycleobj.showbalance)+ "$ ");
        #promt to select products.
        itemnumber=int(input(" Please select a product (1.Can 2.Bottle 3.Paper 4.Stop) Please Enter Numeric Value "));
        #defining the item on the basis of user inputs.
        if(itemnumber==1):
            item="Can";
        elif(itemnumber==2):
            item="Bottle";
        elif(itemnumber==3):
            item="Paper";
        else:
            item="Stop";

        #checking whether user ended the transaction.
        if(item!="Stop"):
            #prompt for input of number of items to inserted in the machine.
            numberofitem=int(input(" How many "+ str(item)+" do you have?:"))
            # placing items one by one.
            print(" Please place "+str(numberofitem)+" "+str(item)+" into machine")
            i=0;
            while(i<numberofitem):
                #here every product checked whether it can be accepted or not, if yes then selection and then payout.
                recycleobj.select_product(itemnumber);
                i=i+1;
            #after every transaction updation log printed.
            print("\n You added "+str(numberofitem)+" "+ str(item)+" for $"+str(ritem.prices.get(item))+" each. You now have $"+str(recycleobj.showbalance)+".")

        #if user stopped transaction then Final Receipt Printed
        else:

            print("\n ----- Final Receipt -----\n")
            #Print function of Machince called for printing final result of all the transaction.
            recycleobj.print_receipt();

            print("\n Thank you for recycling at FedUni!");
    #prompt for asking customer for new transaction.
    status=raw_input(" (N)ext customer, or (Q)uit? ");






