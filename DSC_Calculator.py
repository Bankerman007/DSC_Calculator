# cashflow.py
# A program to determine company & global cash flow
# by: Scott Wright

from tkinter import*
root= Tk()
root.title("Debt Service Calculator")


# creates label widget
e= Entry(root, width=50)
e.grid(row=10, column= 20)
e.insert(0, "Enter Net Income")


e1= Entry(root, width=50) 
e1.grid(row=12,column=20)
e1.insert(0, "Enter interest expense")


e2= Entry(root, width=50) 
e2.grid(row=14,column=20)
e2.insert(0, "Enter 50 percent of year 1 depreciation")


e3= Entry(root, width=50)
e3.grid(row= 16, column=20)
e3.insert(0, "input 50 percent of year 1 section 179 expense")


e4= Entry(root, width=50)
e4.grid(row= 18, column=20)
e4.insert(0, "input year 1 distributions")


e5= Entry(root, width=50)
e5.grid(row= 20, column=20)
e5.insert(0, "input total applical rental income")


e6= Entry(root, width=50)
e6.grid(row= 22, column=20)
e6.insert(0, "input other business income net of debt payments")


e7= Entry(root, width=50)
e7.grid(row= 24, column=20)
e7.insert(0, "input total personal wages & distributions from all PG's")


e8= Entry(root, width=50)
e8.grid(row= 26, column=20)
e8.insert(0, "yearly personal loan payments for all PG's")


e9= Entry(root, width=50)
e9.grid(row= 28, column=20)
e9.insert(0, "input existing yearly business debt payments")


e10= Entry(root, width=50)
e10.grid(row= 30, column=20)
e10.insert(0, "input new business loan amount")


e11= Entry(root, width=50)
e11.grid(row= 32, column=20)
e11.insert(0,  "input new business debt rate")


e12= Entry(root, width=50)
e12.grid(row= 34, column=20)
e12.insert(0, "new business loan term in months")

#create output lines and calculation
def my_click(): 
    net_Income = e.get()
    interest = e1.get()
    depr = e2.get()
    sec_179Depr = e3.get()
    distributions = e4.get()
    rental_Income = e5.get()
    other_Business_Income = e6.get()
    total_wages = e7.get()
    personal_Debt = e8.get()
    existing_Business_Debt_Pmts = e9.get()
    new_Business_Debt_Amount = e10.get()
    new_Business_Debt_Rate = e11.get()
    new_Business_Debt_Term = e12.get()
    new_Business_Loan_Debt_Service = int(new_Business_Debt_Term)*12/int(new_Business_Debt_Rate)
    business_Debt = int(existing_Business_Debt_Pmts) + int(new_Business_Loan_Debt_Service)
    business_Debt_Service = int(net_Income) + int(interest) + int(depr) + int(sec_179Depr) + int(rental_Income) - int(distributions)/int(business_Debt)
    global_Debt_Service = int(net_Income) + int(interest) + int(depr) + int(sec_179Depr) + int(rental_Income) + int(other_Business_Income) - int(distributions) + int(total_wages)/ int(new_Business_Loan_Debt_Service) + int(existing_Business_Debt_Pmts) + int(personal_Debt)
    e13 = Label(root, text= "Business Debt Service is " + str(business_Debt_Service))
    e13.grid(row= 100, column=20)
    e14 = Label(root, text= "Global Debt Service is " + str(global_Debt_Service))
    e14.grid(row=105, column=20)
    

# create calculate button
calculate_DSC_button = Button(root, text="Calculate DSC", padx=1,pady=2, bg="gray", command=my_click)
calculate_DSC_button.grid(row=80, column=20)


# create loop in gui
root.mainloop()


    

