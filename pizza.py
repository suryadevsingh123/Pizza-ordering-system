from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
import time
import datetime

root =Tk()
root.geometry("1350x650+0+0")
root.title("PIZZA ORDERING SYSTEM")
root.configure(background='black')

def exit():
    qExit = messagebox.askyesno("PIZZA ORDERING SYSTEM " ,"DO YOU WANT TO EXIT THE SYSTEM ")
    if qExit>0:
        root.destroy()
        return
def Reset():
    CustomerRef.set("")
    Tax.set("")
    SubTotal.set("")
    TotalCost.set("")
    DeliveryCost.set("")
    CustomerName.set("")
    CustomerPhone.set("")
    CustomerEmail.set("")
    OrderTime.set("")
    OrderDate.set("")
    

def Submit1():
     submit2 =messagebox.askyesno("YOUR Order is Submitted " ,"DO YOU WANT TO EXIT THE SYSTEM ")
     if submit2>0:
            root.destroy()
            return
def OrderRef():
    RefPay=random.randint(20000,709467)
    RefPaid= ("PH" + str(RefPay))
    CustomerRef.set(RefPaid)

def Costoforder():
    Qty1=float(QtyofGoldenCorn.get())
    Qty2=float(QtyofFarmHouse.get())
    Qty3=float(QtyofDeluxeVeggie.get())
    Qty4=float(QtyofPeppyPanner.get())
    Qty5=float(QtyofVeggieParadise.get())
    
    UnitPrice1=float(UnitPriceofGoldenCorn.get())
    UnitPrice2=float(UnitPriceofFarmHouse.get())
    UnitPrice3=float(UnitPriceofDeluxeVeggie.get())
    UnitPrice4=float(UnitPriceofPeppyPanner.get())
    UnitPrice5=float(UnitPriceofVeggieParadise.get())
    
    CostofPizza1= str(Qty1 * UnitPrice1)
    CostofPizza2= str(Qty2 * UnitPrice2)
    CostofPizza3= str(Qty3 * UnitPrice3)
    CostofPizza4= str(Qty4 * UnitPrice4)
    CostofPizza5= str(Qty5 * UnitPrice5)
    
    CostofGoldenCorn.set(CostofPizza1)
    CostofFarmHouse.set(CostofPizza2)
    CostofDeluxeVeggie.set(CostofPizza3)
    CostofPeppyPanner.set(CostofPizza4)
    CostofVeggieParadise.set(CostofPizza5)
    
    CostofPizza1= (Qty1 * UnitPrice1)
    CostofPizza2= (Qty2 * UnitPrice2)
    CostofPizza3= (Qty3 * UnitPrice3)
    CostofPizza4= (Qty4 * UnitPrice4)
    CostofPizza5= (Qty5 * UnitPrice5)
    
    AllCost=( (Qty1 * UnitPrice1) + (Qty2 * UnitPrice2) + (Qty3 * UnitPrice3) + (Qty4 * UnitPrice4) + (Qty5 * UnitPrice5))
    TaxAll="Rs" ,str('%.2f'%((AllCost) * 0.2))
    Tax.set(TaxAll)
    
    Subtotalp="Rs" ,str('%.2f'%(AllCost))
    SubTotal.set(Subtotalp)
    
    Totalcostp="Rs" ,str('%.2f'%(AllCost+((AllCost) * 0.2)))
    TotalCost.set(Totalcostp)
    
#================================
    
CustomerRef=StringVar()
Tax=StringVar()
SubTotal=StringVar()
TotalCost=StringVar()
GoldenCorn_Pizza=StringVar()
FarmHouse_Pizza=StringVar()
DeluxeVeggie_Pizza=StringVar()
PeppyPanner_Pizza=StringVar()
VeggieParadise_Pizza=StringVar()
DeliveryCost=StringVar()
CustomerName=StringVar()
CustomerPhone=StringVar()
CustomerEmail=StringVar()
OrderTime=StringVar()
OrderDate=StringVar()
Discount=StringVar()
CostofGoldenCorn=StringVar()
CostofFarmHouse=StringVar()
CostofDeluxeVeggie=StringVar()
CostofPeppyPanner=StringVar()
CostofVeggieParadise=StringVar()
UnitPriceofGoldenCorn=StringVar()
UnitPriceofFarmHouse=StringVar()
UnitPriceofDeluxeVeggie=StringVar()
UnitPriceofPeppyPanner=StringVar()
UnitPriceofVeggieParadise=StringVar()
QtyofGoldenCorn=StringVar()
QtyofFarmHouse=StringVar()
QtyofDeluxeVeggie=StringVar()
QtyofPeppyPanner=StringVar()
QtyofVeggieParadise=StringVar()

CostofGoldenCorn.set(0)
CostofFarmHouse.set(0)
CostofDeluxeVeggie.set(0)
CostofPeppyPanner.set(0)
CostofVeggieParadise.set(0)
UnitPriceofGoldenCorn.set(0)
UnitPriceofFarmHouse.set(0)
UnitPriceofDeluxeVeggie.set(0)
UnitPriceofPeppyPanner.set(0)
UnitPriceofVeggieParadise.set(0)
QtyofGoldenCorn.set(0)
QtyofFarmHouse.set(0)
QtyofDeluxeVeggie.set(0)
QtyofPeppyPanner.set(0)
QtyofVeggieParadise.set(0)
Discount.set(0)
OrderTime.set(time.strftime("%H:%M:%S"))
OrderDate.set(time.strftime("%d/%m/%y"))




Tops = Frame(root, width=1350, height =50 ,bd=16, relief='raise')
Tops.pack(side=TOP)
LF = Frame(root, width=700, height =650 ,bd=16, relief='raise')
LF.pack(side=LEFT)
RF = Frame(root, width=600, height =650 ,bd=16, relief='raise')
RF.pack(side=RIGHT)

Tops.configure(background='black')
LF.configure(background='black')
RF.configure(background='black')

LeftInsideLF = Frame(LF, width=700, height =100 ,bd=8, relief='raise')
LeftInsideLF.pack(side=TOP)
LeftInsideLFLF = Frame(LF, width=700, height =400 ,bd=8, relief='raise')
LeftInsideLFLF.pack(side=LEFT)

RightInsideLF= Frame(RF, width=604, height =200 ,bd=8, relief='raise')
RightInsideLF.pack(side=TOP)
RightInsideLFLF = Frame(RF, width=306, height =400 ,bd=8, relief='raise')
RightInsideLFLF.pack(side=LEFT)
RightInsideRFRF = Frame(RF, width=300, height =400 ,bd=8, relief='raise')
RightInsideRFRF.pack(side=RIGHT)

lb1Info = Label(Tops, font=('arial', 50, 'bold'), text="       PIZZA ORDERING SYSTEM       ", bd=10, anchor='w')
lb1Info.grid(row=0,column=0)

#===================================Top Left Frame===========================================
lb1CustomerName=Label(LeftInsideLF, font=('arial',14 , 'bold'), text="Customer Name", fg="black", bd=10, anchor='w')
lb1CustomerName.grid(row=0,column=0)

txtCustomerName= Entry(LeftInsideLF, font=('arial',14 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=CustomerName)
txtCustomerName.grid(row=0,column=1)

lb1CustomerPhone=Label(LeftInsideLF, font=('arial',14 , 'bold'), text="Customer Phone", fg="black", bd=10, anchor='w')
lb1CustomerPhone.grid(row=1,column=0)

txtCustomerPhone= Entry(LeftInsideLF, font=('arial',14 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=CustomerPhone)
txtCustomerPhone.grid(row=1,column=1)

lb1CustomerEmail=Label(LeftInsideLF, font=('arial',14 , 'bold'), text="Customer Email", fg="black", bd=10, anchor='w')
lb1CustomerEmail.grid(row=2,column=0)

txtCustomerEmail= Entry(LeftInsideLF, font=('arial',14 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=CustomerEmail)
txtCustomerEmail.grid(row=2,column=1)

#===================================Top Right Frame===========================================
lb1DateOfOrder=Label(RightInsideLF, font=('arial',12 , 'bold'), text="Order Date", fg="black", bd=10, anchor='w')
lb1DateOfOrder.grid(row=0,column=0)

txtDateOfOrder= Entry(RightInsideLF, font=('arial',12 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=OrderDate)
txtDateOfOrder.grid(row=0,column=1)

lb1TimeOfOrder=Label(RightInsideLF, font=('arial',12 , 'bold'), text="Order Time", fg="black", bd=10, anchor='w')
lb1TimeOfOrder.grid(row=1,column=0)

txtTimeOfOrder= Entry(RightInsideLF, font=('arial',12 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=OrderTime)
txtTimeOfOrder.grid(row=1,column=1)

lb1CustomerRef=Label(RightInsideLF, font=('arial',12 , 'bold'), text="Customer Ref", fg="black", bd=10, anchor='w')
lb1CustomerRef.grid(row=2,column=0)

txtCustomerRef= Entry(RightInsideLF, font=('arial',12 , 'bold'), bd=20, width=43, bg=
                   "white", justify='left', textvariable=CustomerRef)
txtCustomerRef.grid(row=2,column=1)


#===================================Right Frame===========================================
lb1MethodOfPayment=Label(RightInsideLFLF, font=('arial',12 , 'bold'), text="MethodOfPayment", fg="black", bd=16, anchor='w')
lb1MethodOfPayment.grid(row=0,column=0)

cmdMethodOfPayment=ttk.Combobox(RightInsideLFLF, font=('arial',12 , 'bold'))
cmdMethodOfPayment['value']=(' ','Cash','Debit Card','Credit Card','UPI')
cmdMethodOfPayment.grid(row=0,column=1)

lb1Discount=Label(RightInsideLFLF, font=('arial',12 , 'bold'), text="Discount", fg="black", bd=16, anchor='w')
lb1Discount.grid(row=1,column=0)

txtDiscount= Entry(RightInsideLFLF, font=('arial',12 , 'bold'), bd=16, width=18, bg=
                   "white", justify='left', textvariable=Discount)
txtDiscount.grid(row=1,column=1)

lb1Tax=Label(RightInsideLFLF, font=('arial',12 , 'bold'), text="Tax", fg="black", bd=16, anchor='w')
lb1Tax.grid(row=2,column=0)

txtTax= Entry(RightInsideLFLF, font=('arial',12 , 'bold'), bd=16, width=18, bg=
                   "white", justify='left', textvariable=Tax)
txtTax.grid(row=2,column=1)

lb1SubTotal=Label(RightInsideLFLF, font=('arial',12 , 'bold'), text="Sub Total", fg="black", bd=16, anchor='w')
lb1SubTotal.grid(row=3,column=0)

txtSubTotal= Entry(RightInsideLFLF, font=('arial',12 , 'bold'), bd=16, width=18, bg=
                   "white", justify='left', textvariable=SubTotal)
txtSubTotal.grid(row=3,column=1)

lb1TotalCost=Label(RightInsideLFLF, font=('arial',12 , 'bold'), text="Total Cost", fg="black", bd=16, anchor='w')
lb1TotalCost.grid(row=4,column=0)

txtTotalCost= Entry(RightInsideLFLF, font=('arial',12 , 'bold'), bd=16, width=18, bg=
                   "white", justify='left', textvariable=TotalCost)
txtTotalCost.grid(row=4,column=1)

#===================================Bottom Left Frames===========================================
lb1ItemOrder=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Item Order", fg="black", bd=20)
lb1ItemOrder.grid(row=0,column=0)
lb1Qty=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Qty", fg="black", bd=10)
lb1Qty.grid(row=0,column=1)
lb1UnitPrice=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Unit Price", fg="black", bd=20)
lb1UnitPrice.grid(row=0,column=2)
lb1CostOfItem=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Cost Of Item", fg="black", bd=20)
lb1CostOfItem.grid(row=0,column=3)
btnSubmit=Button(LeftInsideLFLF, pady=8, bd=8, fg="black", font=('arial',16,'bold'), width=11, text
                   ="Submit", bg="white",command=Submit1)
btnSubmit.grid(row=0,column=4)

#======================
lb1GoldenCorn=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Golden Corn", fg="black", bd=8)
lb1GoldenCorn.grid(row=1,column=0)
lb1FarmHouse=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="FarmHouse", fg="black", bd=8)
lb1FarmHouse.grid(row=2,column=0)
lb1DeluxeVeggie=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Deluxe Veggie", fg="black", bd=8)
lb1DeluxeVeggie.grid(row=3,column=0)
lb1PeppyPanner=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Peppy Panner", fg="black", bd=8)
lb1PeppyPanner.grid(row=4,column=0)
lb1VeggieParadise=Label(LeftInsideLFLF, font=('arial',14 , 'bold'), text="Veggie Paradise", fg="black", bd=8)
lb1VeggieParadise.grid(row=5,column=0)

#========================
txtQtyGoldenCorn= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=QtyofGoldenCorn)
txtQtyGoldenCorn.grid(row=1,column=1)
txtQtyFarmHouse= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=QtyofFarmHouse)
txtQtyFarmHouse.grid(row=2,column=1)
txtQtyDeluxeVeggie= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=QtyofDeluxeVeggie)
txtQtyDeluxeVeggie.grid(row=3,column=1)
txtQtyPeppyPanner= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=QtyofPeppyPanner)
txtQtyPeppyPanner.grid(row=4,column=1)
txtQtyVeggieParadise= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=QtyofVeggieParadise)
txtQtyVeggieParadise.grid(row=5,column=1)

#===================================
txtUnitPriceGoldenCorn= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=UnitPriceofGoldenCorn)
txtUnitPriceGoldenCorn.grid(row=1,column=2)
txtUnitPriceFarmHouse= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=UnitPriceofFarmHouse)
txtUnitPriceFarmHouse.grid(row=2,column=2)
txtUnitPriceDeluxeVeggie= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=UnitPriceofDeluxeVeggie)
txtUnitPriceDeluxeVeggie.grid(row=3,column=2)
txtUnitPricePeppyPanner= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=UnitPriceofPeppyPanner)
txtUnitPricePeppyPanner.grid(row=4,column=2)
txtUnitPriceVeggieParadise= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=UnitPriceofVeggieParadise)
txtUnitPriceVeggieParadise.grid(row=5,column=2)
#================================
txtCostofGoldenCorn= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=CostofGoldenCorn)
txtCostofGoldenCorn.grid(row=1,column=3)
txtCostofFarmHouse= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=CostofFarmHouse)
txtCostofFarmHouse.grid(row=2,column=3)
txtCostofDeluxeVeggie= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=CostofDeluxeVeggie)
txtCostofDeluxeVeggie.grid(row=3,column=3)
txtCostofPeppyPanner= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=CostofPeppyPanner)
txtCostofPeppyPanner.grid(row=4,column=3)
txtCostofVeggieParadise= Entry(LeftInsideLFLF, font=('arial',10 , 'bold'), bd=8, width=8, bg=
                   "white", justify='left', textvariable=CostofVeggieParadise)
txtCostofVeggieParadise.grid(row=5,column=3)



#===================================Bottom Right Frames===========================================
btnTotalCost=Button(RightInsideRFRF, pady=8, bd=8, fg="black", font=('arial',16,'bold'), width=11, text
                   ="Total Cost", bg="white",command=Costoforder).grid(row=0,column=0)
btnReset=Button(RightInsideRFRF, pady=8, bd=8, fg="black", font=('arial',16,'bold'), width=11, text
                   ="Reset", bg="white",command=Reset).grid(row=1,column=0)
btnOrderRef=Button(RightInsideRFRF, pady=8, bd=8, fg="black", font=('arial',16,'bold'), width=11, text
                   ="Order Ref", bg="white",command=OrderRef).grid(row=2,column=0)
btnExit=Button(RightInsideRFRF, pady=8, bd=8, fg="black", font=('arial',16,'bold'), width=11, text
                   ="Exit", bg="white",command=exit).grid(row=3,column=0)



root.mainloop()