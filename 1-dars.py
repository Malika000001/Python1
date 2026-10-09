name=input ("name: ")
surname_name=input ("surname: ")

type=input ("meal name: ")
price=int(input("price: "))
quantity=int(input("quantity: "))
karta=input("karta (yes/no): ")
subtotal=price*quantity
print("subtotal: ", subtotal)

if subtotal>=100:
    discount=subtotal*0.1
    total=subtotal-discount
    print("discount: ", discount)
    print("total: ", total)


if karta=="yes":
    total=total*0.9
    print("total with karta: ", total)  

tax_rate=0.12
tax=total*tax_rate
print("tax: ", tax)

if subtotal>=500000:
    subtotal=shipping
    print("shipping: ", shipping)
    
else:
    shipping=subtotal+25000
print("shipping: ", shipping)