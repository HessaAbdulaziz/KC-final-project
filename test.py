import customtkinter
from customtkinter import CTkToplevel
from tkinter import messagebox

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')
# main window
app=customtkinter.CTk()
app.geometry('700x350')

# welcom lable
label = customtkinter.CTkLabel(app, text="Welcom to Donation Nation", fg_color="white",font=('aerial',30), height=10, width=30,text_color=('black'))
label.pack(pady=20, padx=10)

# about label
label = customtkinter.CTkLabel(app, text="this code will help you find the charity that supports the cualities that you want faster than a lightning!", fg_color="transparent")
label.pack(pady=20, padx=10)

# entries
entry = customtkinter.CTkEntry(app, placeholder_text="inter a donation type money/not money(clothes/funiture)", width= 500)
entry.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(app, placeholder_text="disaster type: wars or natural disaster", width= 500)
entry2.pack(pady=12, padx=10)

entry3 = customtkinter.CTkEntry(app, placeholder_text="choose a country/contant(Africa/Syria/Palestine):", width= 500)
entry3.pack(pady=12, padx=10)
#choises
choise1= 'money'
choise2= 'not money'

choise1pt2='wars'
choise2pt2='natural disaster'

choise1pt3='syria'
choise2pt3='palestine'
choise3pt3='africa'
# user choise code
def choise():
    global choise1
    global choise2
    global choise1pt2
    global choise2pt2
    global choise1pt3
    global choise2pt3
    global choise3pt3

    written_entry=entry.get()
    written_entry2=entry2.get()
    written_entry3=entry3.get()
# if coundition for the choises
    if written_entry == choise1 and written_entry2== choise1pt2 or written_entry2==choise2pt2 and written_entry3==choise1pt3 or written_entry3==choise2pt3:
        newwindow = CTkToplevel(app) 
        newwindow .geometry('700x350')
#lable
        newlabel2 = customtkinter.CTkLabel(newwindow, text=f'ZakatHouse {charities[1]}', fg_color="transparent")
        newlabel2.pack(pady=20, padx=10)

        newlabel3 = customtkinter.CTkLabel(newwindow, text=f'KRCS {charities[2]}', fg_color="transparent")
        newlabel3.pack(pady=20, padx=10)
        
    elif written_entry == choise1 and written_entry2== choise1pt2 or written_entry2==choise2pt2 and written_entry3==choise3pt3:

        newwindow = CTkToplevel(app) 
        newwindow .geometry('700x350')
#lable
        newlabel = customtkinter.CTkLabel(newwindow, text=f'Direct Aid {charities[0]}', fg_color="transparent")
        newlabel.pack(pady=20, padx=10)

        newlabel2 = customtkinter.CTkLabel(newwindow, text=f'ZakatHouse {charities[1]}', fg_color="transparent")
        newlabel2.pack(pady=20, padx=10)

        newlabel3 = customtkinter.CTkLabel(newwindow, text=f'KRCS {charities[2]}', fg_color="transparent")
        newlabel3.pack(pady=20, padx=10)

    elif written_entry== choise2 and written_entry2==choise2pt2 or written_entry2==choise1pt2 and written_entry3==choise1pt3 or written_entry3==choise2pt3 or written_entry3==choise3pt3:

        newwindow = CTkToplevel(app) 
        newwindow .geometry('700x350')
# lable
        newlabel = customtkinter.CTkLabel(newwindow, text=f'alhikma {charities[4]}', fg_color="transparent")
        newlabel.pack(pady=20, padx=10)

        newlabel2 = customtkinter.CTkLabel(newwindow, text=f'kiswa Kuwait  {charities[3]}', fg_color="transparent")
        newlabel2.pack(pady=20, padx=10)

    else:
# error message
        messagebox.showerror('error','sorry not available')

# submit button
newbutton=customtkinter.CTkButton(app, text="submit",command= choise, height=60, width=140, font=('aerial', 20))
newbutton.pack(pady=12, padx=10)

#the dictionary
charities = [{
#direct aid
    'since': 1981,
    'type': 'non-governmental'
},
#ZakatHouse 
{
    'since': 1982,
    'type': 'independent government body'
},
#KRCS  
{
    'name':'Kuwait Red Crescent Society',
    'since': 1966,
    'type': 'non-governmental'
},
#kiswa
{
    'istagram': '@kiswakuait',
    'discribtion':'a recycling centre that givs clithes extra value with zero waste'
},
#alhikma
{
    'phone number': 90010402
}]

app.mainloop()