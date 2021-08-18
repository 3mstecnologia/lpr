import cv2
from tkinter import *
#------------------- PRE CONFIG ----------------------


#------------------- END LAYOUT, START FUNCTIONS ----------------------------------

    
#---------- MAIN FRAME ----------
root = Tk()
root.geometry('600x600+200+200')
root.wm_title("Alpr")

#---------- DETECTS FRAME ----------
detectsFrame = LabelFrame(root, text="Detecções")
detectsFrame.place(relwidth=1, relheight=0.5)

plateFrame = LabelFrame(detectsFrame, text="Placa")
plateFrame.place(relwidth=0.5, relheight=0.5)

plateLabel = Label(plateFrame, text="Imagem Placa")
plateLabel.place(relx=0.5, rely=0.5, anchor="center")

thresFrame = LabelFrame(detectsFrame, text="Threshold")
thresFrame.place(relx=0.5, relwidth=0.5, relheight=0.5)

thresLabel = Label(thresFrame, text="Image Threshold")
thresLabel.place(relx=0.5, rely=0.5, anchor="center")

plateTxtFrame = LabelFrame(detectsFrame, text="Placa detectada")
plateTxtFrame.place(rely=0.5, relwidth=0.5, relheight=0.5)

plateTxtLabel = Label(plateTxtFrame, text="AAA0000", font=("Helvetica", 14))
plateTxtLabel.place(relx=0.5, rely=0.5, anchor="center")

lastFrame = LabelFrame(detectsFrame, text="Ultima detecção")
lastFrame.place(rely=0.5, relx=0.5, relwidth=0.5, relheight=0.5)

lastLabel = Label(lastFrame, text="Imagem Final")
lastLabel.place(relx=0.5, rely=0.5, anchor="center")

#---------- CONFIGS FRAME ----------
configsFrame = LabelFrame(root, text="Configurações")
configsFrame.place(rely=0.5, relwidth=0.5, relheight=0.5)

streamFrame = LabelFrame(configsFrame, text="Stream")
streamFrame.place(relwidth=1, relheight=0.2)

streamSrc = Entry(streamFrame)
streamSrc.place(relwidth=0.75, relheight=0.6, relx=0.025, rely=0.15)

streamStartBnt = Button(streamFrame, text="Start")
streamStartBnt.place(relwidth=0.25, relheight=0.6, relx=0.75, rely=0.15)

mysqlFrame = LabelFrame(configsFrame, text="Conexão MySQL")
mysqlFrame.place(relwidth=1, relheight=0.8, rely=0.2)

mysqlHostTxt = Label(mysqlFrame, text="Host:", font=("Helvetica", 14))
mysqlHostTxt.place(relwidth=0.3, relheight=0.15)

mysqlHostEntry = Entry(mysqlFrame)
mysqlHostEntry.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.025)

mysqlPortTxt = Label(mysqlFrame, text="Port:", font=("Helvetica", 14))
mysqlPortTxt.place(rely=0.15, relwidth=0.3, relheight=0.15)

mysqlPortEntry = Entry(mysqlFrame)
mysqlPortEntry.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.175)

mysqlUserTxt = Label(mysqlFrame, text="User:", font=("Helvetica", 14))
mysqlUserTxt.place(rely=0.3, relwidth=0.3, relheight=0.15)

mysqlUserEntry = Entry(mysqlFrame)
mysqlUserEntry.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.325)

mysqlPassTxt = Label(mysqlFrame, text="Pass:", font=("Helvetica", 14))
mysqlPassTxt.place(rely=0.45, relwidth=0.3, relheight=0.15)

mysqlPassEntry = Entry(mysqlFrame)
mysqlPassEntry.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.475)


mysqlDbTxt = Label(mysqlFrame, text="DB:", font=("Helvetica", 14))
mysqlDbTxt.place(rely=0.6, relwidth=0.3, relheight=0.15)

mysqlDbEntry = Entry(mysqlFrame)
mysqlDbEntry.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.625)

mysqlConnectBtn = Button(mysqlFrame, text="Conectar")
mysqlConnectBtn.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.9)

mysqlCheckBox = Checkbutton(mysqlFrame, text="Save Plates")
mysqlCheckBox.place(relx=0.25, relwidth=0.65, relheight=0.1, rely=0.7)

#---------- TERMINAL FRAME ----------
terminalFrame = LabelFrame(root, text="Terminal")
terminalFrame.place(rely=0.5, relx=0.5, relwidth=0.5, relheight=0.5)

terminalLabel = Label(terminalFrame, text="Terminal")
terminalLabel.pack(fill="both", expand=1)

terminalList = Listbox(terminalLabel)
terminalList.pack(fill="both", expand=1)

#---------- START APP ----------
root.mainloop()