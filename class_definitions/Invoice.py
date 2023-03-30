"""
Write an Invoice class with the following data members, which are identified as required or optional in the constructor.
invoice_id - required
customer_id - required
last_name - required
first_name - required
phone_number - required
address - required
items_with_price - dictionary, optional
Methods:
constructor that sets all required items as listed above and uses appropriate default values for optional
built-ins (str() and repr())
add_item() that adds an item to items_with_price dictionary (Recall: what is the dictionary function to add?)
create_invoice() that prints each item and price, then a total with tax calculated
Driver:
# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802' ,'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
Output:
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
"""

class Invoice:
    '''Invoice Class '''
    # Constructor
    def __init__(self,invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price=dict()):
        self.inv_id = invoice_id
        self.cust_id = customer_id
        self.l_name = last_name
        self.f_name = first_name
        self.p_number = phone_number
        self.addy = address
        self.items_and_price = items_with_price

    # Defining how string of object appears
    def __str__(self):
         return str(self.inv_id)+" " + str(self.cust_id)

    # Defining representation of object
    def __repr__(self):
         return "Invoice(\""+str(self.inv_id)+"\",\""+str(self.cust_id)+"\",\""+self.l_name+"\",\""+self.f_name+"\",\""+self.p_number+"\",\""+self.addy+"\")"

    def add_item(self,input_item_and_price): #Method to add items and prices as dictionary to object
        self.items_and_price.update(input_item_and_price)

    def create_invoice(self):
        for j in self.items_and_price: #Loop to print out item and price in formatted string
            print(j+".....$"+str(self.items_and_price[j]))
        subtotal=sum(self.items_and_price.values()) #Summing subtotal
        TAX_RATE=.06 #Constant for tax rate
        tax=subtotal*TAX_RATE #Tax calculation using subtotal
        print(f'Tax........${tax:.2f}') #Formatted print line for Tax
        total=subtotal+tax
        print(f'Total.......${total:.2f}') #Formatted print line for Total

    #step 1, get your innit working
        #hint: look at previous assignments to see how to make an empty dictionary
    #step 2, add_item method which adds in dictionary to empty dictionary
    #step 3, start working through create_invoice() assignment
        #work thorugh pseudocode - need to loop through dictionary to get key, price, and make a subtotal to find tax, then sum all to get a total

# Driver code (shouldn't have to touch this)
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

print(str(invoice))                     # str displays the defined string of object
print(repr(invoice))                    # repr displays representation of object
del invoice

#Output should look like this; TAX is 6% or 0.06
"""
iPad.....$799.99
Surface.....$999.99
Tax......... $108.00
Total.......$1907.98
"""