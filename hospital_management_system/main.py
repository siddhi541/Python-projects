from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0") #(width, height, x&y axis)
       
        # var declaration 
        self.NameofTablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.NumberofTablets = StringVar()
        self.Lot = StringVar()
        self.Issuedate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEfect = StringVar()
        self.FurtherInformation = StringVar()
        self.StorageAdvice = StringVar()
        self.BloodPressure = StringVar() #driving using machine
        self.Medication = StringVar()
        self.patientId = StringVar()
        self.nhsNumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        
        lbltitle= Label(self.root, bd= 20, relief= RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="teal", bg="white", font=("times new roman",50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ======================= data frame ==========================================
        Dataframe = Frame(self.root, bd = 20, relief=RIDGE)
        Dataframe.place(x=0, y= 130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe,bd=10, relief=RIDGE, padx=10,font=("times new roman", 12, "bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990,y=5, width=460, height=350)

        # ======================buttons frame ========================================

        Buttonframe  = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0,y=530, width=1530, height=70)

        # =======================details frame ========================================

        Detailsframe = Frame(self.root, bd= 20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=180)

        # ==================== dataframe left ======================================

        lblNameTablet = Label(DataframeLeft, text= "Name of tablets :", font=("arial", 12, "bold"),padx=2, pady=6)
        # to place it in column
        lblNameTablet.grid(row=0, column=0)
        # comboobx for tablet name
        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.NameofTablets,state="readonly", font=("arial", 12, "bold"), width=33)
        comNametablet["values"] = ("Nice", "SumoCold", "Paracetamol", "DOLO650", "Acetaminophen", "Ativan", "Sinarest", "Levocet")
        comNametablet.current(0)
        comNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, font=("arial", 12, "bold"), text="Referance No :", padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.ref,width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Dose :", padx=2, pady= 4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Dose,width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of tablets:", padx=2, pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.NumberofTablets ,width=35)
        txtNoOftablets.grid(row=3, column=1)

        lblLot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot :", padx=2, pady=6)
        lblLot.grid(row=4, column=0, sticky=W)
        txtLot = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Lot,width=35)
        txtLot.grid(row=4, column=1)

        lblIssueDate = Label(DataframeLeft, font=("arial", 12, "bold"), text= "Issue date :", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.Issuedate,width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, font=("arial", 12, "bold"), text= "Exp date :", padx= 2, pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily dose :", padx=2, pady= 4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("arial", 12,"bold"), textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side effects : ", padx= 2, pady= 6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.sideEfect,width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherinfo = Label(DataframeLeft, font=("arial", 12, "bold"), text="Further information :", padx=2)
        lblFurtherinfo.grid(row=0, column=2, sticky=W)
        txtFurtherinfo = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.FurtherInformation,width=35)
        txtFurtherinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft, font=("arial", 12, "bold"), text="Blood pressure :", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.BloodPressure, width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage advice :", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft, font=("arial", 12, "bold"), textvariable=self.StorageAdvice, width=35)
        txtStorage.grid(row=2, column=3)

        lblMedication = Label(DataframeLeft,font=("arial", 12, "bold"), text="Medication :", padx=2, pady=6)
        lblMedication.grid(row=3, column=2, sticky=W)
        txtMedication = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.Medication, width=35)
        txtMedication.grid(row=3,column=3)

        lblPatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Id :", padx=2, pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.patientId, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft,font=("arial", 12, "bold"), text="NHS Number :", padx=2, pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.nhsNumber, width=35)
        txtNhsNumber.grid(row=5,column=3)

        lblPatientName = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient name :", padx=2, pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of birth :", padx=2, pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.DateOfBirth, width=35)
        txtDOB.grid(row=7, column=3)

        lblPatientAdd = Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient address :", padx=2, pady=6)
        lblPatientAdd.grid(row=8, column=2, sticky=W)
        txtPatientAdd = Entry(DataframeLeft, font=("arial", 12, "bold"),textvariable=self.PatientAddress, width=35)
        txtPatientAdd.grid(row=8, column=3)

        # ============================dataframe right =========================================================
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=45, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ==============================buttons ======================================================
        btnPrescription = Button(Buttonframe, font=("arial", 12, "bold"), text="Prescription", cursor="hand2",command=self.iPrescription,width=23,padx=2, pady=6, bg= "teal", fg="black")
        btnPrescription.grid(row=0, column=0)

        btnInsertData = Button(Buttonframe, font=("arial", 12, "bold"),text= "Insert Data", cursor="hand2",command=self.insertData,width= 23, padx=2, pady=6, bg= "teal", fg= "black")
        btnInsertData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, font=("arial", 12, "bold"), text="Update", cursor="hand2",command=self.update,width=23, padx=2, pady=6, bg="teal", fg="black")
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, font=("arial", 12, "bold"), text="Delete",cursor="hand2", command=self.iDelete,width=23, padx=2, pady=6, bg="teal", fg="black")
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, font=("arial", 12, "bold"), text="Clear", cursor="hand2",command=self.iClear,width=23, padx=2, pady=6, bg="teal", fg="black")
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, font=("arial", 12, "bold"), text="Exit", cursor="hand2",command=self.iExit,width=23, padx= 2, pady= 6, bg = "teal", fg = "black")
        btnExit.grid(row=0, column=5)

        # ======================================TABLE===================================================
        # ===================================== 1. Scroll bar =========================================

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Detailsframe, column= ("nameoftable", "ref", "dose", "nooftablets", "lot", "issuedate", "expdate", "dailydose",
                                                                "sideEfect","FurtherInformation","storage", "bloodPressure","Medication","patientId","NHSNumber", "Patientname", "DOB", "Patientaddress"))
        


        scroll_x.pack(side=BOTTOM, fill= X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x = ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y = ttk.Scrollbar(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftable", text= "Name of Table")
        self.hospital_table.heading("ref", text="Referance No. ")
        self.hospital_table.heading("dose", text= "Dose")
        self.hospital_table.heading("nooftablets", text="No of tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily dose")
        self.hospital_table.heading("sideEfect", text= "side effect")
        self.hospital_table.heading("FurtherInformation", text="Further Information")
        self.hospital_table.heading("storage", text="Storage advice")
        self.hospital_table.heading("bloodPressure", text="blood pressure")
        self.hospital_table.heading("Medication", text="Medication")
        self.hospital_table.heading("patientId", text="patient Id")
        self.hospital_table.heading("NHSNumber", text="NHS Number")
        self.hospital_table.heading("Patientname", text="Patient Name")
        self.hospital_table.heading("DOB", text="Date of birth")
        self.hospital_table.heading("Patientaddress", text="Patient address")

        self.hospital_table["show"]="headings"
        
        self.hospital_table.column("nameoftable", width=80)
        self.hospital_table.column("ref", width=80)
        self.hospital_table.column("dose", width=80)
        self.hospital_table.column("nooftablets", width=80)
        self.hospital_table.column("lot",width=80)
        self.hospital_table.column("issuedate", width=80)
        self.hospital_table.column("expdate", width=80)
        self.hospital_table.column("dailydose", width=80)
        self.hospital_table.column("sideEfect", width=80)
        self.hospital_table.column("FurtherInformation", width=80)
        self.hospital_table.column("storage", width= 80)
        self.hospital_table.column("bloodPressure", width=80)
        self.hospital_table.column("Medication", width=80)
        self.hospital_table.column("patientId", width=80)
        self.hospital_table.column("NHSNumber", width= 80)
        self.hospital_table.column("Patientname", width=80)
        self.hospital_table.column("DOB", width=80)
        self.hospital_table.column("Patientaddress", width=80)
        
        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetchData()
    # ========================== functionality declaration ==================================
        
    def insertData(self):
        if self.NameofTablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            # database connectivity
            conn = mysql.connector.connect(host="localhost", username="root", password="mysql123", database="new_schema")
            my_cursor = conn.cursor()
           
            try:
                my_cursor.execute("insert into hospital (NameofTablets, ref, Dose, NumberofTablets, Lot, Issuedate, ExpDate, DailyDose, sideEfect, FurtherInformation, StorageAdvice, BloodPressure, Medication, patientId, nhsNumber, PatientName, DateOfBirth, PatientAddress) values (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.NameofTablets.get(),
                        self.ref.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.Lot.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.sideEfect.get(),
                        self.FurtherInformation.get(),
                        self.StorageAdvice.get(),
                        self.BloodPressure.get(),
                        self.Medication.get(),
                        self.patientId.get(),
                        self.nhsNumber.get(),
                        self.PatientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get()
                    ))
                conn.commit()
                self.fetchData()
                messagebox.showinfo("Success", "Record has been inserted")
            except Exception as e:
                messagebox.showerror("Error", "Error inserting record: {str(e)}")
            conn.close()
    
    # ================================== fetching data ==============================================
    
    def fetchData(self):
        conn = mysql.connector.connect(host="localhost", username="root",password="mysql123",database="new_schema")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        # values to be displayed when user clicks on it 
        cur_rows = self.hospital_table.focus()
        content = self.hospital_table.item(cur_rows)
        row = content["values"]
        self.NameofTablets.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.NumberofTablets.set(row[3])
        self.Lot.set(row[4])
        self.Issuedate.set(row[5])
        self.ExpDate.set(row[6])
        self.DailyDose.set(row[7])
        self.sideEfect.set(row[8])
        self.FurtherInformation.set(row[9])
        self.StorageAdvice.set(row[10])
        self.BloodPressure.set(row[11])
        self.Medication.set(row[12])
        self.patientId.set(row[13])
        self.nhsNumber.set(row[14])
        self.PatientName.set(row[15])
        self.DateOfBirth.set(row[16])
        self.PatientAddress.set(row[17])


    def update(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="mysql123", database="new_schema")
        my_cursor = conn.cursor()

        update_query = """
        UPDATE hospital SET 
        NameofTablets=%s, Dose=%s, NumberofTablets=%s, Lot=%s, Issuedate=%s, ExpDate=%s, DailyDose=%s,
        sideEfect=%s, FurtherInformation=%s, StorageAdvice=%s, BloodPressure=%s, Medication=%s, patientId=%s,
        nhsNumber=%s, PatientName=%s, DateOfBirth=%s, PatientAddress=%s 
        WHERE ref=%s
        """

        values = (
            self.NameofTablets.get(),
            self.Dose.get(),
            self.NumberofTablets.get(),
            self.Lot.get(),
            self.Issuedate.get(),
            self.ExpDate.get(),
            self.DailyDose.get(),
            self.sideEfect.get(),
            self.FurtherInformation.get(),
            self.StorageAdvice.get(),
            self.BloodPressure.get(),
            self.Medication.get(),
            self.patientId.get(),
            self.nhsNumber.get(),
            self.PatientName.get(),
            self.DateOfBirth.get(),
            self.PatientAddress.get(),
            self.ref.get(),
        )

        my_cursor.execute(update_query, values)
        
        conn.commit()
        self.fetchData()
        messagebox.showinfo("Success", "Record has been updated")
        conn.close()

    def iPrescription(self):
        self.txtPrescription.insert(END, "Name of tablets : \t\t"+ self.NameofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Ref. No. : \t\t"+ self.ref.get() + "\n")
        self.txtPrescription.insert(END, "Dose : \t\t" + self.Dose.get() + "\n")
        self.txtPrescription.insert(END, "Number of tablets : \t\t" + self.NumberofTablets.get() + "\n")
        self.txtPrescription.insert(END, "Lot : \t\t" + self.Lot.get() + "\n")
        self.txtPrescription.insert(END, "Issue date : \t\t" + self.Issuedate.get() + "\n")
        self.txtPrescription.insert(END, "Exp. date : \t\t" + self.ExpDate.get() + "\n")
        self.txtPrescription.insert(END, "Daily dose : \t\t" + self.DailyDose.get() + "\n")
        self.txtPrescription.insert(END, "Side Effect : \t\t" + self.sideEfect.get() + "\n")
        self.txtPrescription.insert(END, "Further Information : \t\t" + self.FurtherInformation.get() + "\n")
        self.txtPrescription.insert(END, "Storage Advice : \t\t" + self.StorageAdvice.get() + "\n")
        self.txtPrescription.insert(END, "Blood Pressure : \t\t" + self.BloodPressure.get() + "\n")
        self.txtPrescription.insert(END, "Medication : \t\t" + self.Medication.get() + "\n")
        self.txtPrescription.insert(END, "patientId : \t\t" + self.patientId.get() + "\n")
        self.txtPrescription.insert(END, "NHS Number : \t\t" + self.nhsNumber.get() + "\n")
        self.txtPrescription.insert(END, "Patient Name : \t\t" + self.PatientName.get() + "\n")
        self.txtPrescription.insert(END, "Date of birth : \t\t" + self.DateOfBirth.get() + "\n")
        self.txtPrescription.insert(END, "Patient Address : \t\t" + self.PatientAddress.get() + "\n")

    def iDelete(self):
        conn = mysql.connector.connect(host="localhost", user="root",password="mysql123", database="new_schema")
        my_cursor = conn.cursor()
        cur_rows = self.hospital_table.focus()
        content = self.hospital_table.item(cur_rows)
        row = content["values"]
        if(len(row) == 0):
            messagebox.showerror("Error", "No record to delete")
        else:
            delete_query = "delete from hospital where ref=%s"
            value = (self.ref.get(),)
            my_cursor.execute(delete_query, value)
            conn.commit()
            self.fetchData()
            messagebox.showinfo("Deleted", "Record has been deleted successfully")
        conn.close()
    
    def iClear(self):
        self.NameofTablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.NumberofTablets.set("")
        self.Lot.set("")
        self.Issuedate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEfect.set("")
        self.FurtherInformation.set("")
        self.StorageAdvice.set("")
        self.BloodPressure.set("")
        self.Medication.set("")
        self.patientId.set("")
        self.nhsNumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0" ,END)

    def iExit(self):

        ex = messagebox.askyesno("Exit","Confirm if you want to exit")
        if ex > 0 :
            root.destroy()  
            return









root = Tk()
ob = Hospital(root)
root.mainloop()
