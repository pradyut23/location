import urllib.request, urllib.parse, urllib.error
import json
import ssl
from tkinter import *

class Address:
    def __init__(self,master):
        master.minsize(900,500)

        # ****Image Background****
        self.photo=PhotoImage(file='map2.png')
        self.bgLabel=Label(root,image=self.photo)
        self.bgLabel.place(x=0,y=0,relwidth=1,relheight=1)

        # ****Entry****
        frame1=Frame(master)
        frame1.pack(fill=X)
        self.label=Label(frame1,text='Enter Location')
        self.label.config(font=('Courier',16,'bold'))

        self.add=Entry(frame1,font=('Courier',16))          #Text entry bar inserted
        self.add.pack(side=LEFT,expand=True,fill=X)
        self.add.focus()            #Sets cursor on the entry field on app window initialization

        # ****Button****
        self.button1=Button(frame1,text='Find',width=10,font=('Courier',15))
        self.button1.bind('<Button-1>',self.address)
        self.button1.pack(side=LEFT,padx=7,pady=1)

        # ****Frame for outputs****
        self.frameO=Frame(master)
        self.locLabel1=Label(self.frameO)
        self.locLabel1.grid(row=0,column=0,sticky=E)
        self.latLabel1=Label(self.frameO)
        self.latLabel1.grid(row=1,column=0,sticky=E)
        self.longLabel1=Label(self.frameO)
        self.longLabel1.grid(row=2,column=0,sticky=E)

        self.locLabel=Label(self.frameO)
        self.locLabel.grid(row=0,column=1,sticky=W)
        self.latLabel=Label(self.frameO)
        self.latLabel.grid(row=1,column=1,sticky=W)
        self.longLabel=Label(self.frameO)
        self.longLabel.grid(row=2,column=1,sticky=W)

        # ****Enter and Escape Key action****
        master.bind('<Return>',self.address)
        master.bind('<Escape>',self.exit)


    # The function fetches the address from the json file using the given api(serviceurl)
    def address(self,event):
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        #address = input('Enter location: ')
        address=self.add.get()

        parms = dict()
        parms['address'] = address
        parms['key'] = 42
        url = serviceurl + urllib.parse.urlencode(parms)

        print('Retrieving', url)
        uh = urllib.request.urlopen(url,context=ctx)
        data = uh.read().decode()
        print('Retrieved', len(data), 'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('Failure To Retrieve')
            print(data)

        self.location = id = js["results"][0]["formatted_address"]
        self.lat = id = js["results"][0]["geometry"]["location"]["lat"]
        self.long = id = js["results"][0]["geometry"]["location"]["lng"]
        print("")
        print("Full Address with Latitude and Longitude:-")
        print(self.location)
        print("Latitude -",self.lat)
        print("Longitude -",self.long)
        self.print()
        self.add.delete(first=0,last=END)       #deletes input in the entry field

    # Function to exit the application
    def exit(self,event):
        root.quit()

    # Function to print the address on the application on a seperate frame
    def print(self):
        self.frameO.pack(side=BOTTOM)
        self.locLabel1.configure(text='Address:',fg='blue',)
        self.latLabel1.configure(text='Latitude:',fg='blue')
        self.longLabel1.configure(text='Longitude:',fg='blue')

        self.locLabel.configure(text=self.location,fg='blue')
        self.latLabel.configure(text=self.lat,fg='blue')
        self.longLabel.configure(text=self.long,fg='blue')

root=Tk()               #Window initialization
adder=Address(root)     #Object created for reference
root.mainloop()         #Loop to make the window appear continuously
