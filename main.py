# Imports
from tkinter import*
from tkinter.messagebox import*

# Functions
def newObject():
    
    fen = Toplevel()
    fen.title("New object")
    fen.mainloop()

def editSettings():

    def confirm():
        
        allNumbers = True
        for loop in entryVariables:
            try:
                print(float(loop.get().replace(",",".")))
            except:
                allNumbers = False
        
        if not allNumbers:
            showerror("Error","All settings have to be numerical - no strings allowed.")
            return

        else:

            try:
                xIsInt = float(entryVariables[0].get())==int(entryVariables[0].get())
                yIsInt = float(entryVariables[1].get())==int(entryVariables[1].get())
                totalTimeValid = float(entryVariables[2].get().replace(",",".")) > float(entryVariables[3].get().replace(",","."))
                timeStepValid = float(entryVariables[3].get().replace(",",".")) <= 1 and float(entryVariables[3].get().replace(",",".")) >= 0.02

                if not (xIsInt and yIsInt):
                    showerror("Error","Size of box (x and y) have to be integers.")
                    return
                elif not totalTimeValid:
                    showerror("Error","Total simulation time has to be bigger than timestep.")
                    return
                elif not timeStepValid:
                    showerror("Error","Timestep has to be between 0.02 and 1")
                    return
                else:
                    showinfo("Sucess","All parameters valid.")

                    settings["x_size"] = int(entryVariables[0].get())
                    settings["y_size"] = int(entryVariables[1].get())
                    settings["totalTime"] = float(entryVariables[2].get().replace(",","."))
                    settings["timeStep"] = float(entryVariables[3].get().replace(",","."))
                    
            except:
                showerror("Error","Size of box (x and y) have to be integers.")
                return


    fen = Toplevel()
    fen.title("Edit settings")

    entryVariables = [StringVar(), StringVar(), StringVar(), StringVar()]

    Label(fen, text = "X size of box: ").grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[0], width = 20).grid(column = 1, row = 0, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Y size of box: ").grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[1], width = 20).grid(column = 1, row = 1, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Total duration: ").grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[2], width = 20).grid(column = 1, row = 2, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Timestep: ").grid(column = 0, row = 3, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[3], width = 20).grid(column = 1, row = 3, padx = 10, pady = 10, sticky = NW)

    Button(fen, text = "Confirm values", command = confirm, width = 35).grid(column = 0, row = 4, padx = 10, pady = 10, columnspan = 2)

    fen.mainloop()

def updateUI():
    global objects
    for child in mainFrame.winfo_children():
        child.destroy() 

    if len(objects) > 0:
        pass

    Button(mainFrame, text = "New Object", command = newObject, width = 50, height = 2).grid(column = 0, row = len(objects), padx = 10, pady = 10)
    Button(mainFrame, text = "Edit global settings", command = editSettings, width = 50, height = 2).grid(column = 0, row = len(objects)+1, padx = 10, pady = 10)

# Global variables
objects = []
settings = {"x_size":0, "y_size":0, "totalTime":0, "timeStep":0}

# GUI / Tkinter part
window = Tk()
window.title("Setup")

mainFrame = Frame(window)
mainFrame.grid()

updateUI()

# GUI mainloop
window.mainloop()

print(settings)


    

    





