import datetime
def menu(stock):
    print ('%-10s'%"Product Name",'%10s'%"Price",'%10s'%"Quantity")
    for i in range(len(stock)):
        print ('%-10s'%stock[i][0],'%10d'%stock[i][1],'%10d'%stock[i][2])
    
def name():
    name=input("\nEnter name of customer:")
    return name

def item(products,stock):
    ask="y"
    while ask=="y":
        count=0
        buy=input("\nEnter name of product:")
        for i in range(len(stock)):
            if buy==stock[i][0]:
                if stock[i][2]>0:
                    products.append(buy)
                else:
                    print("\nOut of Stock")
            else:
                count=count+1
            if count ==len(stock):
                print("Item not found, please enter product again")
        ask=input("\nAny more product?(y/n)")
    return products

def price(item,stock,pri):
    for product in item:
        for items in stock:
            i = stock.index(items)
            if product==stock[i][0]:
                pri.append(stock[i][1])
    return pri

def noi(no_of_item,products):
    for item in products:
        no_of_item += 1
    return no_of_item

def stotal(price):
    st=0
    for i in range(len(price)):
        st=st+(price[i])
    return st

def discount(stotal):
    try:
        d=int(input("\nEnter discout percent"))
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        d=int(input("\nEnter discout percent"))
    discount=(d/100)*(stotal)
    return discount

def total(stotal,dis):
    total=0
    total=(stotal)-(dis)
    return total

def update_stock(stock,item):
    for j in range(len(item)):
        for i in range(len(stock)):
            if item[j]==stock[i][0]:
                x=int(stock[i][2])
                stock[i][2]=x-1
                break
    f = open("stock.txt", "w")
    for x in range(len(stock)):
        a=""
        for y in range(len(stock[0])):
            a=str(a+","+str(stock[x][y]))
        f.write(a.replace(',','',1)+"\n")
    f.close  
