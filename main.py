from tkinter import *
import random
import time
import datetime
import tkinter.messagebox

root = Tk()
root.geometry("1350x750+0+0")
root.title("Restaurant Management System")
root.configure(background = 'Cadet Blue')

Tops = Frame(root, bg="Cadet Blue", bd=20, pady=5, relief=RIDGE)
Tops.pack(side=TOP)

lblTitle = Label(Tops, font=('arial', 60, 'bold'), text="Restaurant Management System", bd=21, bg='Cadet Blue', fg='Cornsilk', justify=CENTER)
lblTitle.grid(row=0, column=0)


ReceiptCal_F = Frame(root, bg="Powder Blue", bd=10, relief=RIDGE)
ReceiptCal_F.pack(side=RIGHT)

Buttons_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=3, relief=RIDGE)
Buttons_F.pack(side=BOTTOM)
Cal_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=6, relief=RIDGE)
Cal_F.pack(side=TOP)
Receipt_F = Frame(ReceiptCal_F, bg="Powder Blue", bd=4, relief=RIDGE)
Receipt_F.pack(side=BOTTOM)


MenuFrame = Frame(root, bg="Cadet Blue", bd=10, relief=RIDGE)
MenuFrame.pack(side=LEFT)

Cost_F = Frame(MenuFrame, bg="Cadet Blue", bd=4)
Cost_F.pack(side=BOTTOM)

Drinks_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
Drinks_F.pack(side=LEFT)
Cake_F = Frame(MenuFrame, bg="Powder Blue", bd=10, relief=RIDGE)
Cake_F.pack(side=RIGHT)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()


#===============================Cakes============================================================================================================================================================

West_African_Cake = Checkbutton(Cake_F, text="West African Cake", variable = var9, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 0, sticky = W)

Tarte = Checkbutton(Cake_F, text="Tarte", variable = var10, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 1, sticky = W)

Lagos_Chocolate_Cake = Checkbutton(Cake_F, text="Lagos Chocolate Cake", variable = var11, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 2, sticky = W)

Kilburn_Chocolate_Cake = Checkbutton(Cake_F, text="Kilburn Chocolate Cake", variable = var12, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 3, sticky = W)

Carlton_Hill_Cake = Checkbutton(Cake_F, text="Carlton Hill Cake", variable = var13, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 4, sticky = W)

Queen_Park_Cake = Checkbutton(Cake_F, text="Queen Park Cake", variable = var14, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 5, sticky = W)

Jonathan_YO_Cake = Checkbutton(Cake_F, text="Jonathan YO Cake", variable = var15, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 6, sticky = W)

School_Cake = Checkbutton(Cake_F, text="School Cake", variable = var16, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 7, sticky = W)

#===============================Entry box for cakes================================================================================================================================================

txt_West_African_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_West_African_Cake.grid(row = 0, column = 1)

txt_Tarte = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Tarte.grid(row = 1, column = 1)

txt_Lagos_Chocolate_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Lagos_Chocolate_Cake.grid(row = 2, column = 1)

txt_Kilburn_Chocolate_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Kilburn_Chocolate_Cake.grid(row = 3, column = 1)

txt_Carlton_Hill_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Carlton_Hill_Cake.grid(row = 4, column = 1)

txt_Queen_Park_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Queen_Park_Cake.grid(row = 5, column = 1)

txt_Jonathan_YO_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Jonathan_YO_Cake.grid(row = 6, column = 1)

txt_School_Cake = Entry(Cake_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_School_Cake.grid(row = 7, column = 1)

#====================================================================================================================================================================================================


#================================Drinks==============================================================================================================================================================

Latta = Checkbutton(Drinks_F, text="Latta", variable = var1, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = 'Powder Blue').grid(row = 0, sticky = W)

Espresso = Checkbutton(Drinks_F, text="Espresso", variable = var2, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 1, sticky = W)

Iced_Latta = Checkbutton(Drinks_F, text="Iced Latta", variable = var3, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 2, sticky = W)

Vale_Coffee = Checkbutton(Drinks_F, text="Vale Coffee", variable = var4, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 3, sticky = W)

Cappuccino = Checkbutton(Drinks_F, text="Cappuccino", variable = var5, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 4, sticky = W)

African_Coffee = Checkbutton(Drinks_F, text="African Coffee", variable = var6, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 5, sticky = W)

American_Coffee = Checkbutton(Drinks_F, text="American Coffee", variable = var7, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 6, sticky = W)

Iced_Cappuccino = Checkbutton(Drinks_F, text="Iced Cappuccino", variable = var8, onvalue = 1, offvalue = 0, font=('arial', 18, 'bold'), bg = "Powder Blue").grid(row = 7, sticky = W)

#================================Entry box for drinks================================================================================================================================================

txt_Latta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Latta.grid(row = 0, column = 1)

txt_Espresso = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Espresso.grid(row = 1, column = 1)

txt_Iced_Latta = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Iced_Latta.grid(row = 2, column = 1)

txt_Vale_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Vale_Coffee.grid(row = 3, column = 1)

txt_Cappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Cappuccino.grid(row = 4, column = 1)

txt_African_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_African_Coffee.grid(row = 5, column = 1)

txt_American_Coffee = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_American_Coffee.grid(row = 6, column = 1)

txt_Iced_Cappuccino = Entry(Drinks_F, font=('arial', 16, 'bold'), bd = 3, width = 6, justify = LEFT, state = DISABLED)
txt_Iced_Cappuccino.grid(row = 7, column = 1)

#=====================================================================================================================================================================================================

txt_Receipt = Text(Receipt_F, width = 46, height = 12, bg = 'white', bd = 4, font=('arial', 12, 'bold'))
txt_Receipt.grid(row=0, column=0)

btn_Total = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Total", bg = "Powder Blue").grid(row=0, column=0)
btn_Receipt = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Receipt", bg = "Powder Blue").grid(row=0, column=1)
btn_Reset = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Reset", bg = "Powder Blue").grid(row=0, column=2)
btn_Exit = Button(Buttons_F, padx=16, pady = 1, bd = 7, fg = 'Black', font=('arial', 16, 'bold'), width = 4, text = "Exit", bg = "Powder Blue").grid(row=0, column=3)

#=====================================================================================================================================================================================================
root.mainloop()

