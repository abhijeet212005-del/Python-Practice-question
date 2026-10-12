def generate_bill(item, price, quantity=1, discount=0, tax_rate=0.05):
    subtotal = price * quantity
    disamt = subtotal * (discount / 100)
    discounted_amt = subtotal - disamt  
    
    taxamt = discounted_amt * tax_rate  
    totalbill = discounted_amt + taxamt
    
    print("----SUMMARY----")
    print(f"Name of item: {item}")
    print(f"Quantity: {quantity}")
    print(f"Price of item: {price}")
    print(f"Discount on item: {discount}%")
    print(f"Tax: {taxamt}") 
    print(f"Total Amount: {totalbill}") 
generate_bill("Laptop",50000)
generate_bill("Mouse",10.00,quantity=3) 
generate_bill("keyboard",500,discount=10,tax_rate=0.10)
generate_bill("Monitor",7000,quantity=2,discount=5,tax_rate=0.1)