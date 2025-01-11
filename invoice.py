import datetime as dt
name=input("Enter customer name\n")
items_total=int(input("Enter total no. of items\n"))
item_dic={}
for i in range(items_total):
    item_name=input("Enter Item Name: ")
    qty=int(input(f"Enter qty for {item_name}: "))
    price=int(input(f"Enter price for {item_name}"))
    amount=qty*price
    ls=[qty,price,amount]
    item_dic[item_name]=ls
print(item_dic)

print(f'''     Diamond Grocery Store
        ===========================
GSTIN: DLNP101KZV                       Cust Name: {name}
                                Time: {dt.datetime.now()}
===================================================
Item Name     Qty       Price     Amount
===================================================''')
total=0
for i in item_dic:
    total+=item_dic[i][2]
    print(f'''{i}           \t\t{item_dic[i][0]}\t{item_dic[i][1]}\t{item_dic[i][2]}''')
print('''===================================================''')
print(f'''Total\t\t\t\t{total}''')
