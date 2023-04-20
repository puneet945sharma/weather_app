from tkinter import*
from tkinter import  ttk
import requests 

def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=71a158087eab457ae25b14a88bae316f").json()
    w1_label.config(text=data["weather"][0]["main"])
    wb1_label.config(text=data["weather"][0]["description"])
    temp1_label.config(text=str(int(data["main"]["temp"]-273.15)))
    per1_label.config(text=data["main"]["pressure"])


win=Tk()
win.title(" i love python")
win.config(bg= "blue")
win.geometry("500x570")

name_label= Label(win,text=" weather app",
                  font=("Time New Roman", 30, "bold"))

name_label.place(x=25,y= 50, height=50,width=450)

city_name= StringVar()
list_name= ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com= ttk.Combobox(win,text=" weather app", values= list_name,
                  font=("Time New Roman", 20, "bold"), textvariable=city_name)
com.place(x=25,y= 120, height=50,width=450)




w_label= Label(win,text=" weather climate",
                  font=("Time New Roman", 20))
w_label.place(x=25,y= 260, height=50,width=210)

w1_label= Label(win,text=" ",
                  font=("Time New Roman", 20))
w1_label.place(x=250,y= 260, height=50,width=210)

wb_label= Label(win,text=" weather Description ",
                  font=("Time New Roman", 17))
wb_label.place(x=25,y=330, height=50,width=210)

wb1_label= Label(win,text="  ",
                  font=("Time New Roman", 17))
wb1_label.place(x=250,y=330, height=50,width=210)

temp_label= Label(win,text=" Temperature",
                  font=("Time New Roman", 20))
temp_label.place(x=25,y=400, height=50,width=210)

temp1_label= Label(win,text=" ",
                  font=("Time New Roman", 20))
temp1_label.place(x=250,y=400, height=50,width=210)

per_label= Label(win,text=" Pressure ",
                  font=("Time New Roman", 20))
per_label.place(x=25,y=470, height=50,width=210)

per1_label= Label(win,text="  ",
                  font=("Time New Roman", 20))
per1_label.place(x=250,y=470, height=50,width=210)

done_button= Button(win, text="Done", 
                  font=("Time New Roman", 20, "bold"), command=data_get)

done_button.place(x=200, y=190,height=50,width=100)




win.mainloop() #keep the window open 
               # window continue run    