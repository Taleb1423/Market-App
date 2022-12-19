from datetime import date
from tkinter import *
import tkinter.messagebox as tkMessageBox
import mysql.connector
import tkinter as tk
import tkinter.ttk as ttk


root = Tk()
root.title("Market Inventory")
width = 1024
height = 520
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")


def database():

    global cursor

    global db

    db = mysql.connector.connect(host="localhost",
                                 user='root',
                                 password='souheil1312',
                                 db="db_pro")

    cursor = db.cursor()


# ========================================VARIABLES========================================

SEARCHPRO = StringVar()
SEARCHSHIP = StringVar()
SEARCHUNIT = StringVar()
SEARCHSUPPLIER = StringVar()
SEARCHSTAFF = StringVar()

# ======================================== inventory METHODS ==========================================
# ++++++++++++++++++++++++++++++++++++++++ UNITS ++++++++++++++++++++++++++++++++++++++++++

# ======================================== VIEW Units =====================================


def searchunit():

    if SEARCHUNIT.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `unit` WHERE `unit_product_name` LIKE %s", ('%'+str(SEARCHUNIT.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetunit():
    tree.delete(*tree.get_children())
    displayunits()
    SEARCHUNIT.set("")


#  def deletep():
#    database()
#    if not tree.selection():
#        print("ERROR")
#    else:
#        result = tkMessageBox.askquestion(
#            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
#        if result == 'yes':
#            curitem = tree.focus()
#            contents = (tree.item(curitem))
#            selecteditem = contents['values']
#            tree.delete(curitem)
#
#            cursor.execute(
#                "DELETE FROM `product` WHERE `product_name` = %s" % selecteditem[0])
#            db.commit()
#            cursor.close()
#            db.close()


def displayunits():

    database()
    cursor.execute(
        "SELECT serial_number, production_date, unit_order_id, unit_product_name, unit_shippment FROM unit")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformunit():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Units",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHUNIT,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchunit)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetunit)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deleteship)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Serial_Number", "Production_Date", "Unit_Order_Id", "Unit_Product_Name", "Unit_Shippment"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Serial_Number', text="Serial_Number", anchor=W)
    tree.heading('Production_Date', text="Production_Date", anchor=W)
    tree.heading('Unit_Order_Id', text="Unit_Oreder_Id", anchor=W)
    tree.heading('Unit_Product_Name', text="Unit_Product_Name", anchor=W)
    tree.heading('Unit_Shippment', text="Unit_Shippment", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayunits()


def showviewunit():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformunit()

# ___________________________________ DISPLAY SHIPMENTS ___________________________________________


def searchship():

    if SEARCHSHIP.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `shipment` WHERE `shipment_suplier` LIKE %s", ('%'+str(SEARCHSHIP.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor.close()
        db.close()


def resetship():
    tree.delete(*tree.get_children())
    displayshipments()
    SEARCHSHIP.set("")


def displayshipments():

    database()
    cursor.execute("SELECT shipment_id, date_ordered, username, shipment_price, shipment_suplier FROM shipment INNER JOIN staff ON shipment.staff_id = staff.staff_id")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformship():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Shipments",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCHSHIP,
                   font=('arial', 15), width=10)

    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchship)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetship)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deleteship)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Shipment_id", "Date_ordered", "Staff_User_Name", "Shipment_price", "Shipment_supplier"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Shipment_id', text="Shipment_ID", anchor=W)
    tree.heading('Date_ordered', text="Date_ordered", anchor=W)
    tree.heading('Staff_User_Name', text="Staff_User_Name", anchor=W)
    tree.heading('Shipment_price', text="Shipment_price", anchor=W)
    tree.heading('Shipment_supplier', text="Shipment_supplier", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayshipments()


def showviewshipment():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformship()

# ========================================ADD NEW SHIPMENT==================================


def addnewshipment():

    database()

    # print(user)

    date_ordered = date.today()
    sup = sup_variable.get()
    pro = pro_variable.get()
    qty = product_quantity.get()
    qty = int(qty)
    # print(qty)

    query1 = 'SELECT staff_id FROM staff WHERE username= %s'
    val1 = (user,)
    cursor.execute(query1, val1)
    staf = cursor.fetchone()
    rep1 = staf[0]
    rep1 = int(rep1)
    # print(rep1)

    query2 = 'SELECT buy_price FROM product where product_name=%s'
    val2 = (pro,)
    cursor.execute(query2, val2)
    buy_price = cursor.fetchone()
    # print(buy_price)

    rep2 = buy_price[0]
    unit_price = int(rep2)
    # print(unit_price)

    price = (qty * unit_price)
    # print(price)

    sql1 = "INSERT INTO `shipment` (date_ordered, staff_id, shipment_price, shipment_suplier) VALUES(%s, %s, %s, %s)"
    # (date_ordered, 'intel', 5*(select buy_price from product where product_name= 'test1'),1)
    val3 = (date_ordered, rep1, price, sup,)
    cursor.execute(sql1, val3)

    db.commit()

    query3 = 'SELECT MAX(shipment_id) FROM shipment'
    cursor.execute(query3)
    recent_shipment = cursor.fetchone()
    rep3 = recent_shipment[0]
    recent_shipment_id = int(rep3)
    print(recent_shipment_id)

    for x in range(qty):
        print(x)
        sql2 = "INSERT INTO `unit` (production_date, unit_product_name, unit_shippment) VALUES(%s, %s, %s)"
        val4 = (date_ordered, pro, recent_shipment_id,)
        cursor.execute(sql2, val4)

    db.commit()
    cursor.close()
    db.close()


def addnewformshipment():

    global product_quantity
    global pro_variable
    global sup_variable

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Shipment",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_product_name = Label(
        midaddnew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_product_name.grid(row=1, sticky=W)

    lbl_supplier_name = Label(
        midaddnew, text="Supplier Name:", font=('arial', 25), bd=10)
    lbl_supplier_name.grid(row=2, sticky=W)

    lbl_product_quantity = Label(
        midaddnew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_product_quantity.grid(row=3, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    database()

    cursor.execute('SELECT product_name FROM product')
    pro_result = cursor.fetchall()
    pro_options = [item[0] for item in pro_result]
    pro_variable = tk.StringVar(root)
    pro_variable.set(pro_options[0])

    pro_dropdown = tk.OptionMenu(midaddnew, pro_variable, *pro_options)
    pro_dropdown.grid(row=1, column=1)

    cursor.execute('SELECT name FROM suplier')
    sup_result = cursor.fetchall()
    sup_options = [item[0] for item in sup_result]
    sup_variable = tk.StringVar(root)
    sup_variable.set(sup_options[0])

    sup_dropdown = tk.OptionMenu(midaddnew, sup_variable, *sup_options)
    sup_dropdown.grid(row=2, column=1)

    product_quantity = Entry(midaddnew,
                             font=('arial', 25), width=15)
    product_quantity.grid(row=3, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=7, columnspan=2, pady=20)

    def save2():
        addnewshipment()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save2)
    btn_add.grid(row=6, columnspan=2, pady=20)


def showaddshipment():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Shipment")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformshipment()


# ++++++++++++++++++++++++++++++++++++++++++++++++++ PRODUCTS ++++++++++++++++++++++++++++++++++++++++++++++++


# ================================================== VIEW PRODUCTS ===========================================

def searchp():

    if SEARCHPRO.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `product` WHERE `product_name` LIKE %s", ('%'+str(SEARCHPRO.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetp():
    tree.delete(*tree.get_children())
    displayproducts()
    SEARCHPRO.set("")


#  def deletep():
#    database()
#    if not tree.selection():
#        print("ERROR")
#    else:
#        result = tkMessageBox.askquestion(
#            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
#        if result == 'yes':
#            curitem = tree.focus()
#            contents = (tree.item(curitem))
#            selecteditem = contents['values']
#            tree.delete(curitem)
#
#            cursor.execute(
#                "DELETE FROM `product` WHERE `product_name` = %s" % selecteditem[0])
#            db.commit()
#            cursor.close()
#            db.close()


def displayproducts():

    database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformp():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHPRO,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchp)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetp)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deletep)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Product Name", "Product Type", "Product Sell Price", "Product Buy Price", "Product Qty"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Product Name', text="Product Name", anchor=W)
    tree.heading('Product Type', text="Product Type", anchor=W)

    tree.heading('Product Sell Price', text="Product Sell Price", anchor=W)
    tree.heading('Product Buy Price', text="Product Buy Price", anchor=W)
    tree.heading('Product Qty', text="Product Qty", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayproducts()


def showviewproduct():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformp()

# ========================================ADD NEW PRODUCT==================================


def addnewproduct():

    database()

    name = productname.get()
    typ = producttype.get()
    sellprice = productsellprice.get()
    buyprice = productbuyprice.get()
    amount = amountinstock.get()

    sql = "INSERT INTO `product` (product_name, product_type, sell_price, buy_price, amount_in_stock) VALUES(%s, %s, %s, %s, %s)"

    val = (name, typ, sellprice,
           buyprice, amount,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformproduct():

    global productname
    global producttype
    global productsellprice
    global productbuyprice
    global amountinstock

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Product",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_productname = Label(
        midaddnew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=1, sticky=W)

    lbl_qty = Label(midaddnew, text="Product Type:",
                    font=('arial', 25), bd=10)
    lbl_qty.grid(row=2, sticky=W)

    lbl_price = Label(midaddnew, text="Product Sell Price:",
                      font=('arial', 25), bd=10)
    lbl_price.grid(row=3, sticky=W)

    lbl_buy_price = Label(midaddnew, text="Product Buy Price:",
                          font=('arial', 25), bd=10)
    lbl_buy_price.grid(row=4, sticky=W)

    lbl_price = Label(midaddnew, text="Amount in Stock:",
                      font=('arial', 25), bd=10)
    lbl_price.grid(row=5, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    productname = Entry(midaddnew,
                        font=('arial', 25), width=15)
    productname.grid(row=1, column=1)

    producttype = Entry(midaddnew,
                        font=('arial', 25), width=15)
    producttype.grid(row=2, column=1)

    productsellprice = Entry(midaddnew,
                             font=('arial', 25), width=15)
    productsellprice.grid(row=3, column=1)

    productbuyprice = Entry(midaddnew,
                            font=('arial', 25), width=15)
    productbuyprice.grid(row=4, column=1)

    amountinstock = Entry(midaddnew,
                          font=('arial', 25), width=15)
    amountinstock.grid(row=5, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=7, columnspan=2, pady=20)

    def save():
        addnewproduct()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=6, columnspan=2, pady=20)


def showaddproduct():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Products")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformproduct()


# ++++++++++++++++++++++++++++++++++++++++++++++++++ Supplier ++++++++++++++++++++++++++++++++++++++++++++++++


# ================================================== VIEW Supplier ===========================================

def searchsupplier():

    if SEARCHSUPPLIER.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `suplier` WHERE `name` LIKE %s", ('%'+str(SEARCHSUPPLIER.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetsupplier():
    tree.delete(*tree.get_children())
    displaysuppliers()
    SEARCHSUPPLIER.set("")


def displaysuppliers():

    database()
    cursor.execute("SELECT * FROM `suplier`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformsupplier():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Suppliers",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHSUPPLIER,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchsupplier)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetsupplier)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deletep)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Name", "Email", "Adress", "Phone"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Email', text="Email", anchor=W)

    tree.heading('Adress', text="Adress", anchor=W)
    tree.heading('Phone', text="Phone", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displaysuppliers()


def showviewsupplier():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformsupplier()


# ========================================ADD NEW Supplier==========================================


def addnewproduct():

    database()

    name = suppliername.get()
    email = supplieremail.get()
    adress = supplieradress.get()
    phone = supplierphone.get()

    sql = "INSERT INTO `suplier` (name, email, adress, phone) VALUES(%s, %s, %s, %s)"

    val = (name, email, adress,
           phone,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformsupplier():

    global suppliername
    global supplieremail
    global supplieradress
    global supplierphone

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Supplier",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_suppliername = Label(
        midaddnew, text="Supplier Name:", font=('arial', 25), bd=10)
    lbl_suppliername.grid(row=1, sticky=W)

    lbl_email = Label(midaddnew, text="Supplier Email:",
                      font=('arial', 25), bd=10)
    lbl_email.grid(row=2, sticky=W)

    lbl_adress = Label(midaddnew, text="Supplier Address:",
                       font=('arial', 25), bd=10)
    lbl_adress.grid(row=3, sticky=W)

    lbl_phone = Label(midaddnew, text="Supplier Phone:",
                      font=('arial', 25), bd=10)
    lbl_phone.grid(row=4, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    suppliername = Entry(midaddnew,
                         font=('arial', 25), width=15)
    suppliername.grid(row=1, column=1)

    supplieremail = Entry(midaddnew,
                          font=('arial', 25), width=15)
    supplieremail.grid(row=2, column=1)

    supplieradress = Entry(midaddnew,
                           font=('arial', 25), width=15)
    supplieradress.grid(row=3, column=1)

    supplierphone = Entry(midaddnew,
                          font=('arial', 25), width=15)
    supplierphone.grid(row=4, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=6, columnspan=2, pady=10)

    def save():
        addnewproduct()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=5, columnspan=2, pady=20)


def showaddsupplier():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Supplier")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformsupplier()


# +++++++++++++++++++++++++++++++++ HOME +++++++++++++++++++++++++++++++++++


def inventorywin():

    global Home
    Home = Tk()

    Home.title("Inventory/Home")
    Home.attributes('-fullscreen', True)
    Home.resizable(0, 0)
    Home.config(bg="#6666ff")
    root.withdraw()

    title = Frame(Home, bd=1, relief=SOLID)
    title.pack(pady=10)

    lbl_display = Label(
        title, text="Market Inventory", font=('arial', 45))
    lbl_display.pack()

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command=logout)
    filemenu.add_command(label="Exit", command=damage)

    filemenu1.add_command(label="Add new Supplier", command=showaddsupplier)
    filemenu1.add_command(label="View Supplier", command=showviewsupplier)

    filemenu2.add_command(label="Add new Product", command=showaddproduct)
    filemenu2.add_command(label="View Products", command=showviewproduct)

    filemenu3.add_command(label="Make new Shipment", command=showaddshipment)
    filemenu3.add_command(label="View Shipments", command=showviewshipment)
    filemenu3.add_command(label="View Units", command=showviewunit)

    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Supplier", menu=filemenu1)
    menubar.add_cascade(label="Product", menu=filemenu2)
    menubar.add_cascade(label="Shipment", menu=filemenu3)

    Home.config(menu=menubar)

# ======================================== hr METHODS ==========================================


def searchstaff():

    if SEARCHSTAFF.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `staff` WHERE `name` LIKE %s", ('%'+str(SEARCHSTAFF.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetstaff():
    tree.delete(*tree.get_children())
    displaystaff()
    SEARCHSTAFF.set("")


def deletestaff():
    database()
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion(
            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curitem = tree.focus()
            contents = (tree.item(curitem))
            selecteditem = contents['values']
            tree.delete(curitem)
            cursor.execute(
                "DELETE FROM `staff` WHERE `staff_id` = %s" % selecteditem[0])
            db.commit()
            cursor.close()
            db.close()


def displaystaff():

    database()
    cursor.execute("SELECT * FROM `staff`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformstaff():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHSTAFF,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchstaff)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetstaff)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=deletestaff)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Staff_id", "Name", "Username", "Password", "Email", "Phone", "Adress", "date_of_birth", "start_date", "end_date", "Role", "Salary", "number_of_orders"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Staff_id', text="Staff_id", anchor=W)
    tree.heading('Name', text="Employee Name", anchor=W)
    tree.heading('Username', text="Username", anchor=W)
    tree.heading('Password', text="Password", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Phone', text="Phone", anchor=W)
    tree.heading('Adress', text="Adress", anchor=W)
    tree.heading('date_of_birth', text="Birth", anchor=W)

    tree.heading('start_date', text="start_date", anchor=W)
    tree.heading('end_date', text="end_date", anchor=W)
    tree.heading('Role', text="Role", anchor=W)
    tree.heading('Salary', text="Salary", anchor=W)
    tree.heading('number_of_orders', text="Num_Orders", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.column('#10', stretch=NO, minwidth=0, width=100)
    tree.column('#11', stretch=NO, minwidth=0, width=100)
    tree.column('#12', stretch=NO, minwidth=0, width=100)

    tree.pack()
    displaystaff()


def showviewstaff():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformstaff()

# ======================================== ADD NEW Employee ==================================


def addnewstaff():

    database()

    staff_name = S_name.get()
    username = S_username.get()
    password = S_password.get()
    email = S_email.get()
    phone = S_phone.get()
    adress = S_adress.get()
    start = S_start_date.get()
    end = S_end_date.get()
    role = S_role.get()
    salary = S_salary.get()

    sql = "INSERT INTO `staff` (name, username, password, email, phone, adress, start_date, end_date, role, salary) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"

    val = (staff_name, username, password,
           email, phone, adress, start, end, role, salary,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformstaff():

    global S_name
    global S_username
    global S_password
    global S_email
    global S_phone
    global S_adress
    global S_start_date
    global S_end_date
    global S_role
    global S_salary

    topaddnew = Frame(addnewform, width=600, height=150, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=5)

    L2 = Label(topaddnew, text="", width=30, font=(
        'arial', 18))
    L2.pack(padx=60)

    lbl_text = Label(topaddnew, text="Add New Employee",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=1100)
    midaddnew.pack(side=TOP, pady=5)

    lbl_name = Label(
        midaddnew, text="Emloyee Name:", font=('arial', 25), bd=10)
    lbl_name.grid(row=1, sticky=W)

    lbl_username = Label(midaddnew, text="Employee UserName:",
                         font=('arial', 25), bd=10)
    lbl_username.grid(row=2, sticky=W)

    lbl_password = Label(midaddnew, text="Employee Password:",
                         font=('arial', 25), bd=10)
    lbl_password.grid(row=3, sticky=W)

    lbl_email = Label(midaddnew, text="Employee Email:",
                      font=('arial', 25), bd=10)
    lbl_email.grid(row=4, sticky=W)

    lbl_phone = Label(midaddnew, text="Employee Phone:",
                      font=('arial', 25), bd=10)
    lbl_phone.grid(row=5, sticky=W)

    lbl_adress = Label(
        midaddnew, text="Emloyee Adress:", font=('arial', 25), bd=10)
    lbl_adress.grid(row=6, sticky=W)

    lbl_start = Label(midaddnew, text="Employee Start Date:",
                      font=('arial', 25), bd=10)
    lbl_start.grid(row=7, sticky=W)

    lbl_end = Label(midaddnew, text="Employee End Date:",
                    font=('arial', 25), bd=10)
    lbl_end.grid(row=8, sticky=W)

    lbl_role_price = Label(midaddnew, text="Employee Role:",
                           font=('arial', 25), bd=10)
    lbl_role_price.grid(row=9, sticky=W)

    lbl_salary = Label(midaddnew, text="Employee Salary:",
                       font=('arial', 25), bd=10)
    lbl_salary.grid(row=10, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    S_name = Entry(midaddnew,
                   font=('arial', 25), width=15)
    S_name.grid(row=1, column=1)

    S_username = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_username.grid(row=2, column=1)

    S_password = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_password.grid(row=3, column=1)

    S_email = Entry(midaddnew,
                    font=('arial', 25), width=15)
    S_email.grid(row=4, column=1)

    S_phone = Entry(midaddnew,
                    font=('arial', 25), width=15)
    S_phone.grid(row=5, column=1)

    S_adress = Entry(midaddnew,
                     font=('arial', 25), width=15)
    S_adress.grid(row=6, column=1)

    S_start_date = Entry(midaddnew,
                         font=('arial', 25), width=15)
    S_start_date.grid(row=7, column=1)

    S_end_date = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_end_date.grid(row=8, column=1)

    S_role = Entry(midaddnew,
                   font=('arial', 25), width=15)
    S_role.grid(row=9, column=1)

    S_salary = Entry(midaddnew,
                     font=('arial', 25), width=15)
    S_salary.grid(row=10, column=1)

    def save():
        addnewstaff()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=11, columnspan=2, pady=5)


def showaddstaff():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/Drop/View Staff")
    width = 1000
    height = 750
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #  addnewform.resizable(0, 0)
    addnewformstaff()


def hrwin():

    global Home
    Home = Tk()

    Home.title("Inventory/Home")
    Home.attributes('-fullscreen', True)
    Home.resizable(0, 0)
    Home.config(bg="#6666ff")
    root.withdraw()

    title = Frame(Home, bd=1, relief=SOLID)
    title.pack(pady=10)

    lbl_display = Label(
        title, text="Market Inventory", font=('arial', 45))
    lbl_display.pack()

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu1 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command=logout)
    filemenu.add_command(label="Exit", command=damage)

    filemenu1.add_command(label="Add new Employee", command=showaddstaff)
    filemenu1.add_command(label="View staff", command=showviewstaff)

    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Employee", menu=filemenu1)

    Home.config(menu=menubar)


# ======================================== admin METHODS ==========================================


# ======================================== VIEW Staff ===================================


def searchstaff():

    if SEARCHSTAFF.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `staff` WHERE `name` LIKE %s", ('%'+str(SEARCHSTAFF.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetstaff():
    tree.delete(*tree.get_children())
    displaystaff()
    SEARCHSTAFF.set("")


def deletestaff():
    database()
    if not tree.selection():
        print("ERROR")
    else:
        result = tkMessageBox.askquestion(
            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curitem = tree.focus()
            contents = (tree.item(curitem))
            selecteditem = contents['values']
            tree.delete(curitem)
            cursor.execute(
                "DELETE FROM `staff` WHERE `staff_id` = %s" % selecteditem[0])
            db.commit()
            cursor.close()
            db.close()


def displaystaff():

    database()
    cursor.execute("SELECT * FROM `staff`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformstaff():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Employees",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHSTAFF,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchstaff)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetstaff)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_delete = Button(LeftViewForm, text="Delete", command=deletestaff)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Staff_id", "Name", "Username", "Password", "Email", "Phone", "Adress", "date_of_birth", "start_date", "end_date", "Role", "Salary", "number_of_orders"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Staff_id', text="Staff_id", anchor=W)
    tree.heading('Name', text="Employee Name", anchor=W)
    tree.heading('Username', text="Username", anchor=W)
    tree.heading('Password', text="Password", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Phone', text="Phone", anchor=W)
    tree.heading('Adress', text="Adress", anchor=W)
    tree.heading('date_of_birth', text="Birth", anchor=W)

    tree.heading('start_date', text="start_date", anchor=W)
    tree.heading('end_date', text="end_date", anchor=W)
    tree.heading('Role', text="Role", anchor=W)
    tree.heading('Salary', text="Salary", anchor=W)
    tree.heading('number_of_orders', text="Num_Orders", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=100)
    tree.column('#3', stretch=NO, minwidth=0, width=100)
    tree.column('#4', stretch=NO, minwidth=0, width=100)
    tree.column('#5', stretch=NO, minwidth=0, width=100)
    tree.column('#6', stretch=NO, minwidth=0, width=100)
    tree.column('#7', stretch=NO, minwidth=0, width=100)
    tree.column('#8', stretch=NO, minwidth=0, width=100)
    tree.column('#9', stretch=NO, minwidth=0, width=100)
    tree.column('#10', stretch=NO, minwidth=0, width=100)
    tree.column('#11', stretch=NO, minwidth=0, width=100)
    tree.column('#12', stretch=NO, minwidth=0, width=100)

    tree.pack()
    displaystaff()


def showviewstaff():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformstaff()

# ======================================== ADD NEW Employee ==================================


def addnewstaff():

    database()

    staff_name = S_name.get()
    username = S_username.get()
    password = S_password.get()
    email = S_email.get()
    phone = S_phone.get()
    adress = S_adress.get()
    start = S_start_date.get()
    end = S_end_date.get()
    role = S_role.get()
    salary = S_salary.get()

    sql = "INSERT INTO `staff` (name, username, password, email, phone, adress, start_date, end_date, role, salary) VALUES(%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"

    val = (staff_name, username, password,
           email, phone, adress, start, end, role, salary,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformstaff():

    global S_name
    global S_username
    global S_password
    global S_email
    global S_phone
    global S_adress
    global S_start_date
    global S_end_date
    global S_role
    global S_salary

    topaddnew = Frame(addnewform, width=600, height=150, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=5)

    L2 = Label(topaddnew, text="", width=30, font=(
        'arial', 18))
    L2.pack(padx=60)

    lbl_text = Label(topaddnew, text="Add New Employee",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=1100)
    midaddnew.pack(side=TOP, pady=5)

    lbl_name = Label(
        midaddnew, text="Emloyee Name:", font=('arial', 25), bd=10)
    lbl_name.grid(row=1, sticky=W)

    lbl_username = Label(midaddnew, text="Employee UserName:",
                         font=('arial', 25), bd=10)
    lbl_username.grid(row=2, sticky=W)

    lbl_password = Label(midaddnew, text="Employee Password:",
                         font=('arial', 25), bd=10)
    lbl_password.grid(row=3, sticky=W)

    lbl_email = Label(midaddnew, text="Employee Email:",
                      font=('arial', 25), bd=10)
    lbl_email.grid(row=4, sticky=W)

    lbl_phone = Label(midaddnew, text="Employee Phone:",
                      font=('arial', 25), bd=10)
    lbl_phone.grid(row=5, sticky=W)

    lbl_adress = Label(
        midaddnew, text="Emloyee Adress:", font=('arial', 25), bd=10)
    lbl_adress.grid(row=6, sticky=W)

    lbl_start = Label(midaddnew, text="Employee Start Date:",
                      font=('arial', 25), bd=10)
    lbl_start.grid(row=7, sticky=W)

    lbl_end = Label(midaddnew, text="Employee End Date:",
                    font=('arial', 25), bd=10)
    lbl_end.grid(row=8, sticky=W)

    lbl_role_price = Label(midaddnew, text="Employee Role:",
                           font=('arial', 25), bd=10)
    lbl_role_price.grid(row=9, sticky=W)

    lbl_salary = Label(midaddnew, text="Employee Salary:",
                       font=('arial', 25), bd=10)
    lbl_salary.grid(row=10, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    S_name = Entry(midaddnew,
                   font=('arial', 25), width=15)
    S_name.grid(row=1, column=1)

    S_username = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_username.grid(row=2, column=1)

    S_password = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_password.grid(row=3, column=1)

    S_email = Entry(midaddnew,
                    font=('arial', 25), width=15)
    S_email.grid(row=4, column=1)

    S_phone = Entry(midaddnew,
                    font=('arial', 25), width=15)
    S_phone.grid(row=5, column=1)

    S_adress = Entry(midaddnew,
                     font=('arial', 25), width=15)
    S_adress.grid(row=6, column=1)

    S_start_date = Entry(midaddnew,
                         font=('arial', 25), width=15)
    S_start_date.grid(row=7, column=1)

    S_end_date = Entry(midaddnew,
                       font=('arial', 25), width=15)
    S_end_date.grid(row=8, column=1)

    S_role = Entry(midaddnew,
                   font=('arial', 25), width=15)
    S_role.grid(row=9, column=1)

    S_salary = Entry(midaddnew,
                     font=('arial', 25), width=15)
    S_salary.grid(row=10, column=1)

    def save():
        addnewstaff()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=11, columnspan=2, pady=5)


def showaddstaff():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/Drop/View Staff")
    width = 1000
    height = 750
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    #  addnewform.resizable(0, 0)
    addnewformstaff()

# ++++++++++++++++++++++++++++++++++++++++ UNITS ++++++++++++++++++++++++++++++++++++++++++

# ======================================== VIEW Units =====================================


def searchunit():

    if SEARCHUNIT.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `unit` WHERE `unit_product_name` LIKE %s", ('%'+str(SEARCHUNIT.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetunit():
    tree.delete(*tree.get_children())
    displayunits()
    SEARCHUNIT.set("")


#  def deletep():
#    database()
#    if not tree.selection():
#        print("ERROR")
#    else:
#        result = tkMessageBox.askquestion(
#            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
#        if result == 'yes':
#            curitem = tree.focus()
#            contents = (tree.item(curitem))
#            selecteditem = contents['values']
#            tree.delete(curitem)
#
#            cursor.execute(
#                "DELETE FROM `product` WHERE `product_name` = %s" % selecteditem[0])
#            db.commit()
#            cursor.close()
#            db.close()


def displayunits():

    database()
    cursor.execute(
        "SELECT serial_number, production_date, unit_order_id, unit_product_name, unit_shippment FROM unit")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformunit():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Units",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHUNIT,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchunit)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetunit)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deleteship)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Serial_Number", "Production_Date", "Unit_Order_Id", "Unit_Product_Name", "Unit_Shippment"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Serial_Number', text="Serial_Number", anchor=W)
    tree.heading('Production_Date', text="Production_Date", anchor=W)
    tree.heading('Unit_Order_Id', text="Unit_Oreder_Id", anchor=W)
    tree.heading('Unit_Product_Name', text="Unit_Product_Name", anchor=W)
    tree.heading('Unit_Shippment', text="Unit_Shippment", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayunits()


def showviewunit():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformunit()

# ___________________________________ DISPLAY SHIPMENTS ___________________________________________


def searchship():

    if SEARCHSHIP.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `shipment` WHERE `shipment_suplier` LIKE %s", ('%'+str(SEARCHSHIP.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))

        cursor.close()
        db.close()


def resetship():
    tree.delete(*tree.get_children())
    displayshipments()
    SEARCHSHIP.set("")


def displayshipments():

    database()
    cursor.execute("SELECT shipment_id, date_ordered, username, shipment_price, shipment_suplier FROM shipment INNER JOIN staff ON shipment.staff_id = staff.staff_id")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformship():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Shipments",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)

    search = Entry(LeftViewForm, textvariable=SEARCHSHIP,
                   font=('arial', 15), width=10)

    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchship)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetship)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deleteship)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Shipment_id", "Date_ordered", "Staff_User_Name", "Shipment_price", "Shipment_supplier"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Shipment_id', text="Shipment_ID", anchor=W)
    tree.heading('Date_ordered', text="Date_ordered", anchor=W)
    tree.heading('Staff_User_Name', text="Staff_User_Name", anchor=W)
    tree.heading('Shipment_price', text="Shipment_price", anchor=W)
    tree.heading('Shipment_supplier', text="Shipment_supplier", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayshipments()


def showviewshipment():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformship()

# ========================================ADD NEW SHIPMENT==================================


def addnewshipment():

    database()

    # print(user)

    date_ordered = date.today()
    sup = sup_variable.get()
    pro = pro_variable.get()
    qty = product_quantity.get()
    qty = int(qty)
    # print(qty)

    query1 = 'SELECT staff_id FROM staff WHERE username= %s'
    val1 = (user,)
    cursor.execute(query1, val1)
    staf = cursor.fetchone()
    rep1 = staf[0]
    rep1 = int(rep1)
    # print(rep1)

    query2 = 'SELECT buy_price FROM product where product_name=%s'
    val2 = (pro,)
    cursor.execute(query2, val2)
    buy_price = cursor.fetchone()
    # print(buy_price)

    rep2 = buy_price[0]
    unit_price = int(rep2)
    # print(unit_price)

    price = (qty * unit_price)
    # print(price)

    sql1 = "INSERT INTO `shipment` (date_ordered, staff_id, shipment_price, shipment_suplier) VALUES(%s, %s, %s, %s)"
    # (date_ordered, 'intel', 5*(select buy_price from product where product_name= 'test1'),1)
    val3 = (date_ordered, rep1, price, sup,)
    cursor.execute(sql1, val3)

    db.commit()

    query3 = 'SELECT MAX(shipment_id) FROM shipment'
    cursor.execute(query3)
    recent_shipment = cursor.fetchone()
    rep3 = recent_shipment[0]
    recent_shipment_id = int(rep3)
    print(recent_shipment_id)

    for x in range(qty):
        print(x)
        sql2 = "INSERT INTO `unit` (production_date, unit_product_name, unit_shippment) VALUES(%s, %s, %s)"
        val4 = (date_ordered, pro, recent_shipment_id,)
        cursor.execute(sql2, val4)

    db.commit()
    cursor.close()
    db.close()


def addnewformshipment():

    global product_quantity
    global pro_variable
    global sup_variable

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Shipment",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_product_name = Label(
        midaddnew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_product_name.grid(row=1, sticky=W)

    lbl_supplier_name = Label(
        midaddnew, text="Supplier Name:", font=('arial', 25), bd=10)
    lbl_supplier_name.grid(row=2, sticky=W)

    lbl_product_quantity = Label(
        midaddnew, text="Product Quantity:", font=('arial', 25), bd=10)
    lbl_product_quantity.grid(row=3, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    database()

    cursor.execute('SELECT product_name FROM product')
    pro_result = cursor.fetchall()
    pro_options = [item[0] for item in pro_result]
    pro_variable = tk.StringVar(root)
    pro_variable.set(pro_options[0])

    pro_dropdown = tk.OptionMenu(midaddnew, pro_variable, *pro_options)
    pro_dropdown.grid(row=1, column=1)

    cursor.execute('SELECT name FROM suplier')
    sup_result = cursor.fetchall()
    sup_options = [item[0] for item in sup_result]
    sup_variable = tk.StringVar(root)
    sup_variable.set(sup_options[0])

    sup_dropdown = tk.OptionMenu(midaddnew, sup_variable, *sup_options)
    sup_dropdown.grid(row=2, column=1)

    product_quantity = Entry(midaddnew,
                             font=('arial', 25), width=15)
    product_quantity.grid(row=3, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=7, columnspan=2, pady=20)

    def save2():
        addnewshipment()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save2)
    btn_add.grid(row=6, columnspan=2, pady=20)


def showaddshipment():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Shipment")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformshipment()


# ++++++++++++++++++++++++++++++++++++++++++++++++++ PRODUCTS ++++++++++++++++++++++++++++++++++++++++++++++++


# ================================================== VIEW PRODUCTS ===========================================

def searchp():

    if SEARCHPRO.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `product` WHERE `product_name` LIKE %s", ('%'+str(SEARCHPRO.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetp():
    tree.delete(*tree.get_children())
    displayproducts()
    SEARCHPRO.set("")


#  def deletep():
#    database()
#    if not tree.selection():
#        print("ERROR")
#    else:
#        result = tkMessageBox.askquestion(
#            'Inventory', 'Are you sure you want to delete this record?', icon="warning")
#        if result == 'yes':
#            curitem = tree.focus()
#            contents = (tree.item(curitem))
#            selecteditem = contents['values']
#            tree.delete(curitem)
#
#            cursor.execute(
#                "DELETE FROM `product` WHERE `product_name` = %s" % selecteditem[0])
#            db.commit()
#            cursor.close()
#            db.close()


def displayproducts():

    database()
    cursor.execute("SELECT * FROM `product`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformp():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Products",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHPRO,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchp)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetp)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deletep)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Product Name", "Product Type", "Product Sell Price", "Product Buy Price", "Product Qty"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Product Name', text="Product Name", anchor=W)
    tree.heading('Product Type', text="Product Type", anchor=W)

    tree.heading('Product Sell Price', text="Product Sell Price", anchor=W)
    tree.heading('Product Buy Price', text="Product Buy Price", anchor=W)
    tree.heading('Product Qty', text="Product Qty", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displayproducts()


def showviewproduct():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformp()

# ========================================ADD NEW PRODUCT==================================


def addnewproduct():

    database()

    name = productname.get()
    typ = producttype.get()
    sellprice = productsellprice.get()
    buyprice = productbuyprice.get()
    amount = amountinstock.get()

    sql = "INSERT INTO `product` (product_name, product_type, sell_price, buy_price, amount_in_stock) VALUES(%s, %s, %s, %s, %s)"

    val = (name, typ, sellprice,
           buyprice, amount,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformproduct():

    global productname
    global producttype
    global productsellprice
    global productbuyprice
    global amountinstock

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Product",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_productname = Label(
        midaddnew, text="Product Name:", font=('arial', 25), bd=10)
    lbl_productname.grid(row=1, sticky=W)

    lbl_qty = Label(midaddnew, text="Product Type:",
                    font=('arial', 25), bd=10)
    lbl_qty.grid(row=2, sticky=W)

    lbl_price = Label(midaddnew, text="Product Sell Price:",
                      font=('arial', 25), bd=10)
    lbl_price.grid(row=3, sticky=W)

    lbl_buy_price = Label(midaddnew, text="Product Buy Price:",
                          font=('arial', 25), bd=10)
    lbl_buy_price.grid(row=4, sticky=W)

    lbl_price = Label(midaddnew, text="Amount in Stock:",
                      font=('arial', 25), bd=10)
    lbl_price.grid(row=5, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    productname = Entry(midaddnew,
                        font=('arial', 25), width=15)
    productname.grid(row=1, column=1)

    producttype = Entry(midaddnew,
                        font=('arial', 25), width=15)
    producttype.grid(row=2, column=1)

    productsellprice = Entry(midaddnew,
                             font=('arial', 25), width=15)
    productsellprice.grid(row=3, column=1)

    productbuyprice = Entry(midaddnew,
                            font=('arial', 25), width=15)
    productbuyprice.grid(row=4, column=1)

    amountinstock = Entry(midaddnew,
                          font=('arial', 25), width=15)
    amountinstock.grid(row=5, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=7, columnspan=2, pady=20)

    def save():
        addnewproduct()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=6, columnspan=2, pady=20)


def showaddproduct():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Products")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformproduct()


# ++++++++++++++++++++++++++++++++++++++++++++++++++ Supplier ++++++++++++++++++++++++++++++++++++++++++++++++


# ================================================== VIEW Supplier ===========================================

def searchsupplier():

    if SEARCHSUPPLIER.get() != "":
        tree.delete(*tree.get_children())
        database()
        cursor.execute(
            "SELECT * FROM `suplier` WHERE `name` LIKE %s", ('%'+str(SEARCHSUPPLIER.get())+'%',))
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        db.close()


def resetsupplier():
    tree.delete(*tree.get_children())
    displaysuppliers()
    SEARCHSUPPLIER.set("")


def displaysuppliers():

    database()
    cursor.execute("SELECT * FROM `suplier`")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    db.close()


def viewformsupplier():
    database()
    global tree
    TopViewForm = Frame(viewform, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    LeftViewForm = Frame(viewform, width=600)
    LeftViewForm.pack(side=LEFT, fill=Y)
    MidViewForm = Frame(viewform, width=600)
    MidViewForm.pack(side=RIGHT)
    lbl_text = Label(TopViewForm, text="View Suppliers",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)
    lbl_txtsearch = Label(LeftViewForm, text="Search", font=('arial', 15))
    lbl_txtsearch.pack(side=TOP, anchor=W)
    search = Entry(LeftViewForm, textvariable=SEARCHSUPPLIER,
                   font=('arial', 15), width=10)
    search.pack(side=TOP,  padx=10, fill=X)
    btn_search = Button(LeftViewForm, text="Search", command=searchsupplier)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    btn_reset = Button(LeftViewForm, text="Reset", command=resetsupplier)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
   #  btn_delete = Button(LeftViewForm, text="Delete", command=deletep)
   #  btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm, columns=("Name", "Email", "Adress", "Phone"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Email', text="Email", anchor=W)

    tree.heading('Adress', text="Adress", anchor=W)
    tree.heading('Phone', text="Phone", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=120)
    tree.column('#2', stretch=NO, minwidth=0, width=120)
    tree.column('#3', stretch=NO, minwidth=0, width=120)

    tree.pack()
    displaysuppliers()


def showviewsupplier():
    database()
    global viewform
    viewform = Toplevel()
    viewform.title("Inventory")
    width = 1100
    height = 450
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    viewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    # viewform.resizable(0, 0)
    viewformsupplier()


# ========================================ADD NEW Supplier==========================================


def addnewsupplier():

    database()

    name = suppliername.get()
    email = supplieremail.get()
    adress = supplieradress.get()
    phone = supplierphone.get()

    sql = "INSERT INTO `suplier` (name, email, adress, phone) VALUES(%s, %s, %s, %s)"

    val = (name, email, adress,
           phone,)

    cursor.execute(sql, val)

    db.commit()

    cursor.close()
    db.close()


def addnewformsupplier():

    global suppliername
    global supplieremail
    global supplieradress
    global supplierphone

    topaddnew = Frame(addnewform, width=600, height=300, bd=1, relief=SOLID)
    topaddnew.pack(side=TOP, pady=20)

    lbl_text = Label(topaddnew, text="Add New Supplier",
                     font=('arial', 18), width=600)
    lbl_text.pack(fill=X)

    midaddnew = Frame(addnewform, width=600, height=900)
    midaddnew.pack(side=TOP, pady=50)

    lbl_suppliername = Label(
        midaddnew, text="Supplier Name:", font=('arial', 25), bd=10)
    lbl_suppliername.grid(row=1, sticky=W)

    lbl_email = Label(midaddnew, text="Supplier Email:",
                      font=('arial', 25), bd=10)
    lbl_email.grid(row=2, sticky=W)

    lbl_adress = Label(midaddnew, text="Supplier Address:",
                       font=('arial', 25), bd=10)
    lbl_adress.grid(row=3, sticky=W)

    lbl_phone = Label(midaddnew, text="Supplier Phone:",
                      font=('arial', 25), bd=10)
    lbl_phone.grid(row=4, sticky=W)

    def delay2():
        L2.config(text="Record added")
        root.after(1000, message2)

    def message2():
        L2.config(text="")

# --------------------------------------------------------

    suppliername = Entry(midaddnew,
                         font=('arial', 25), width=15)
    suppliername.grid(row=1, column=1)

    supplieremail = Entry(midaddnew,
                          font=('arial', 25), width=15)
    supplieremail.grid(row=2, column=1)

    supplieradress = Entry(midaddnew,
                           font=('arial', 25), width=15)
    supplieradress.grid(row=3, column=1)

    supplierphone = Entry(midaddnew,
                          font=('arial', 25), width=15)
    supplierphone.grid(row=4, column=1)

    L2 = Label(midaddnew, text="", width=30, font=(
        'arial', 18))
    L2.grid(row=6, columnspan=2, pady=10)

    def save():
        addnewsupplier()
        delay2()

    btn_add = Button(midaddnew, text="Save", font=(
        'arial', 18), width=30, bg="#009ACD", command=save)
    btn_add.grid(row=5, columnspan=2, pady=20)


def showaddsupplier():
    database()
    global addnewform
    addnewform = Toplevel()
    addnewform.title("Add/View Supplier")
    width = 600
    height = 700
    screen_width = Home.winfo_screenwidth()
    screen_height = Home.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    addnewform.geometry("%dx%d+%d+%d" % (width, height, x, y))
    addnewform.resizable(0, 0)
    addnewformsupplier()


# +++++++++++++++++++++++++++++++++ HOME +++++++++++++++++++++++++++++++++++


def homewin():

    global Home
    Home = Tk()

    Home.title("Inventory/Home")
    Home.attributes('-fullscreen', True)
    Home.resizable(0, 0)
    Home.config(bg="#6666ff")
    root.withdraw()

    title = Frame(Home, bd=1, relief=SOLID)
    title.pack(pady=10)

    lbl_display = Label(
        title, text="Market Inventory", font=('arial', 45))
    lbl_display.pack()

    menubar = Menu(Home)
    filemenu = Menu(menubar, tearoff=0)
    filemenu1 = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command=logout)
    filemenu.add_command(label="Exit", command=damage)

    filemenu1.add_command(label="Add new Supplier", command=showaddsupplier)
    filemenu1.add_command(label="View Supplier", command=showviewsupplier)

    filemenu2.add_command(label="Add new Product", command=showaddproduct)
    filemenu2.add_command(label="View Products", command=showviewproduct)

    filemenu3.add_command(label="Make new Shipment", command=showaddshipment)
    filemenu3.add_command(label="View Shipments", command=showviewshipment)
    filemenu3.add_command(label="View Units", command=showviewunit)

    filemenu4.add_command(label="Add new Employee", command=showaddstaff)
    filemenu4.add_command(label="View staff", command=showviewstaff)

    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="Supplier", menu=filemenu1)
    menubar.add_cascade(label="Product", menu=filemenu2)
    menubar.add_cascade(label="Shipment", menu=filemenu3)
    menubar.add_cascade(label="Staff", menu=filemenu4)

    Home.config(menu=menubar)

# ========================================LOGIN==================================


def damage():
    result = tkMessageBox.askquestion(
        'Book Your Bus', 'Are you sure you want to exit?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()


def logout():
    global user
    global pas
    result = tkMessageBox.askquestion(
        'Book Your Bus', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':
        user = ""
        pas = ""
        root.deiconify()
        Home.destroy()


def login():

    database()
    global user
    global pas

    user = username.get()
    pas = password.get()
    #  print(username)
    #  print(password)

    select_query = 'SELECT role FROM `staff` WHERE `username` = %s and password = %s'
    vals = (user, pas,)
    cursor.execute(select_query, vals)
    # print(c.fetchall())
    users = cursor.fetchone()
    print(users)

    rep = users[0]
    print(rep)

    if rep == 'admin':
        homewin()

    elif rep == 'hr':
        hrwin()

    elif rep == 'inventory':
        inventorywin()
    else:
        delay1()
        user = ""
        pas = ""


#  def show():
#    p = password.get()  # get password from entry
#    print(p)
# ========================================MENUBAR WIDGETS==================================
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
# filemenu.add_command(label="Account", command=ShowLoginForm)
filemenu.add_command(label="Exit", command=damage)
menubar.add_cascade(label="File", menu=filemenu)
root.config(menu=menubar)

# ========================================FRAME============================================
Title = Frame(root, bd=1, relief=SOLID)
Title.pack(pady=10)

# ========================================LABEL WIDGET=====================================
lbl_display = Label(Title, text="Market Inventory", font=('arial', 45))
lbl_display.pack()


def message1():

    L1.config(text="")


def delay1():

    L1.config(text="Get Authorized First")
    root.after(1000, message1)


TopLoginForm = Frame(root, width=500, height=90, bd=1, relief=SOLID)
TopLoginForm.pack(side=TOP, pady=20)
lbl_text = Label(TopLoginForm, text="Administrator Login",
                 font=('arial', 18), width=600)
lbl_text.pack(fill=X)


L1 = Label(TopLoginForm, text="", font=('arial', 28), fg='red')
L1.pack()


MidLoginForm = Frame(root, width=600, height=1000)
MidLoginForm.pack(side=TOP, pady=20)
lbl_username = Label(MidLoginForm, text="Username:",
                     font=('arial', 25), bd=18)
lbl_username.grid(row=0)
lbl_password = Label(MidLoginForm, text="Password:",
                     font=('arial', 25), bd=18)
lbl_password.grid(row=1)


username = Entry(MidLoginForm,
                 font=('arial', 25), width=15)
username.grid(row=0, column=1)

password = Entry(MidLoginForm,
                 font=('arial', 25), width=15, show="*")
password.grid(row=1, column=1)

btn_login = Button(MidLoginForm, text="Login", font=(
    'arial', 18), width=30, command=login)
btn_login.grid(row=2, columnspan=2, pady=20)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()
