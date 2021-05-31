from tkinter import *
import tkinter.ttk as exTk
from covid import Covid
import time
import pandas as pd
from PIL import Image ,ImageTk

window = Tk()
window.title("Covid-19")
window.iconbitmap("../covid.ico") 
window.geometry("500x550")
load = Image.open("../covid-19.jpeg").resize((500,550,),Image.ANTIALIAS)
render = ImageTk.PhotoImage(load) 
img = Label(window,image=render)
img.place(x=0,y=0)

covid = Covid()
covid.get_data()


def update(con):
	vn_cases = covid.get_status_by_country_name(con)

	seconds = 0
	for x in vn_cases: 
		if x == 'last_update':
			seconds = time.time()
			local_time = time.ctime(seconds)
			vn_cases[x] = local_time
	
	df = pd.DataFrame(vn_cases.items(),columns=['CATEGORY','DATA_FOR_COVID_19'])
	return df
def clear():
	text.delete(1.0,END)
	
name = Label(window ,text="*APP UPDATE COVID-19*", fg="#ffffff",bg="#005b7a")
name.pack(pady=5)
name.config(font=("Transformers Movie",30))

frame_a = Frame()
frame_a.pack(pady=10)
ac = Label(master=frame_a, text='Tổng số ca đang điều trị : ',bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
ac.grid(row=0,column=0)
active = Label(master=frame_a ,text=covid.get_total_active_cases(),bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
active.grid(row=0,column=1)

frame_b = Frame()
frame_b.pack(pady=10)
co = Label(master=frame_b, text='Tổng số ca phát hiện : ',bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
co.grid(row=0,column=0)
confirm = Label(master=frame_b,text=covid.get_total_confirmed_cases(),bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
confirm.grid(row=0,column=1)

frame_c = Frame()
frame_c.pack(pady=10)
re = Label(master=frame_c, text='Tổng số ca đã khỏi : ',bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
re.grid(row=0,column=0)
recover = Label(master=frame_c,text=covid.get_total_recovered(),bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
recover.grid(row=0,column=1)

frame_d = Frame()
frame_d.pack(pady=10)
de = Label(master=frame_d, text='Tổng số ca tử vong : ',bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
de.grid(row=0,column=0)
death = Label(master=frame_d,text=covid.get_total_deaths(),bg='#4d4d4d',fg='#66ccff',font=("Courier", 12),relief='ridge', borderwidth=5)
death.grid(row=0,column=1)

text = Text(bg='#4d4d4d',fg='#66ccff',width=40, height=10,font=("Courier", 12),relief='ridge', borderwidth=5)
text.pack()

def country():
	covid = Covid()
	covid.get_data()
	countries = covid.list_countries()
	lst = []
	for i in range(1,190):
		lst.append(countries[i]['name'])
	return tuple(lst)

cmb_2 = exTk.Combobox(window , width = 20, font=("ROBOTO", 13))
cmb_2["values"] = country()
cmb_2.current(151)
cmb_2.pack(pady=10)

def get_data():
	x = update(cmb_2.get())
	text.insert(END,x)

frame_e = Frame()
frame_e.pack()

up = Button(master=frame_e, text='Enter', command=get_data, width=25 ,borderwidth=5,bg='#99ffff',font='13')
up.grid(row=0,column=0)

clear = Button(master=frame_e, text='Clear',command=clear, width=25,borderwidth=5,bg='#ff9999',font='13')
clear.grid(row=0, column=1)


window.mainloop()



