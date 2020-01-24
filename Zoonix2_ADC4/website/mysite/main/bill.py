def bill():
    import purchase #imports purchase module
    import datetime #imports datetime
    import read #imports read module
    item=[]
    price=[]
    pri=[]
    products=[]
    no_of_item=0
    d=0
    stock=(read.access()) #Gets the stock through access() function of read module
    name=purchase.name() #Stores name of customer through purchase module
    item=purchase.item(products,stock) #Stores name of products bought through purchase module
    price=purchase.price(item,stock,pri) #Stores price of products through purchase module
    stotal=purchase.stotal(price) #Stores subtotal through purchase module
    dis=purchase.discount(stotal) #Stores discount through purchase module
    total=purchase.total(stotal,dis) #Stores total through purchase module
    noi=purchase.noi(no_of_item,item) #Stores no. of items purchased through purchase module
    dt= str(datetime.datetime.now())# Stores datetime 
    file=open(name+" "+dt.split(".")[0].replace(":","-")+".txt",'w+')#Makes a new file in write mode
    
    #Inovice of the purchase
    print("---------------------------------------------")
    print("\n*******************Inovice*******************")
    file.write(("\n*******************Inovice*******************\n"))
    print("Name of customer:",name)
    file.write("Name of customer:"+str(name)+"\n")
    print("Date/Time:",dt)
    file.write("Date/Time:"+str(dt)+"\n")
    print("---------------------------------------------")
    file.write("---------------------------------------------\n")
    print('%10s'%"S/N",'%10s'%"Paricular",'%10s'%"Price")
    file.write('%10s'%"S/N"+'%10s'%"Paricular"+'%10s'%"Price"+"\n")
    for i in range(0, noi):
        print('%10d'%(i+1),'%10s'%(item[i]),'%10s'%(price[i]))
        file.write('%10s'%str((i+1))+'%10s'%str((item[i]))+'%10s'%str(price[i])+"\n")
    print ("\n"'%28s'%"SubTotal:",stotal)
    file.write("\n"'%28s'%"SubTotal:"+str(stotal)+"\n")
    print ("\n"'%27s'%"Discount:",dis)
    file.write ("\n"'%28s'%"Discount:"+str(dis)+"\n")
    print ("\n"'%28s'%"Total:",total)
    file.write("\n"'%28s'%"Total:"+str(total)+"\n")
    file.close() #Closes the file
    
    purchase.update_stock(stock,item) #Updates the stock in the existing file
