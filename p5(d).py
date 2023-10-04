from tkinter import *
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

root=Tk()
root.title("Salary Predictor")
root.geometry("700x500+50+50")
f=("arial",30,"bold")


lb_header=Label(root,text="Salary Predictor",font=f,background="light blue")
lb_header.pack(pady=20)

def find():
	try:
		data=pd.read_csv("esmsep23.csv")

		feature=data[["exp"]]
		target=data["sal"]

		x_train,x_test,y_train,y_test=train_test_split(feature,target)

		model=LinearRegression()
		model.fit(x_train,y_train)

		exp=float(ent_exp.get())
		sal=model.predict([[exp]])
		msg="Salary = " + str(round(sal[0],2)) + "K"	
		lb_ans.configure(text=msg)
	except ValueError:
		msg="You Should enter numbers only"
		lb_ans.configure(text=msg)
	ent_exp.delete(0,END)
	ent_exp.focus()

lb_exp=Label(root,text="Enter Experience",font=f)
lb_exp.pack(pady=20)
ent_exp=Entry(root,font=f)
ent_exp.pack(pady=20)

btn_find=Button(root,text="Find",font=f,command=find)
btn_find.pack(pady=20)

lb_ans=Label(root,font=f)
lb_ans.pack(pady=20)

root.mainloop()
