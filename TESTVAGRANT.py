print("NAME : DHANANJAY KUMAR"\nEmail : dhananjaykumar137c@gmail.com\nUSN : 1BI20AI009)



class shopKeeper:
    def __init__(self,name,uprice,gst,quantity):
        self.n = name
        self.p = uprice
        self.g = gst
        self.q = quantity
        self.gst = 0
        self.price = 0
        self.gprice = 0
        self.finalprice = 0
        
    def calc_dis_price(self):
        if self.p > 500:
            self.price = self.p + self.p * 1/20
        else:
            self.price = self.p    
    
    def calc_gst_price(self):
        self.gprice =self.price + self.price*(self.g/100)
    
    def quan_price(self):
        if self.gprice == 0:
            self.finalprice = self.q * self.price
        else:
            self.finalprice = self.q * self.gprice    
        
    def calc_gst(self):
        self.gst = self.price*(self.g/100)        
        
    def print_prod(self):
        print("Name of the product: ",self.n)
        print("Unit price of the product: ",self.p)
        print("GST applied on the product: ",self.g)
        print("Qunatity of the product: ",self.q)
        print("Price of the product after calculating discount: ",self.price)
        print("price of the product after applying gst: ",self.gprice)
        print("Final price of the product after applying gst and discount: ",self.finalprice)
        print("-------------------------------------\n\n")
        
        
        
product1 = shopKeeper("Leather wallet",1100,18,1)
product2 = shopKeeper("Umbrella",900,12,4)
product3 = shopKeeper("Cigarette",200,28,3)
product4 = shopKeeper("Honey",100,0,2)

prod = [product1,product2,product3,product4]

for product in prod:
    product.calc_dis_price()
    product.calc_gst_price()
    product.quan_price()
    product.calc_gst()
    product.print_prod()
    
print("Q1. Identify the product for which we pay maximun GST?\n")
print("Lets calculate the GSTs of all products")

max_gst = 0
obj = ""
j=1
for product in prod:
    print(f"Product{j} :",product.gst)
    if product.gst>max_gst:
        obj = product.n
        max_gst = product.gst
        j+=1
        
print("The maximum gst among the product is: ",max_gst)
print("The product for which we pay max GST amount is", obj)
total_amount = 0

print("Q2. Calculate the total amount to be paid to the shopkeeper?\n")
     
for product in prod:
    total_amount = total_amount + product.finalprice
                
print("The total amount to be paid to the shopkeeper is : ",total_amount)
            
