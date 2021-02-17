# Imports
from tkinter import*
from tkinter.messagebox import*

# Functions
def newObject(id = None):

    def confirm():
        #TODO: Verify if values are valid
        try:
            object_settings = {
                            "m":float(entryVariables[0].get()), 
                            "v":float(entryVariables[1].get()), 
                            "xp":int(entryVariables[2].get()), 
                            "yp":int(entryVariables[3].get()), 
                            "xv":float(entryVariables[4].get()), 
                            "yv":float(entryVariables[5].get()), 
                            "xa":float(entryVariables[6].get()), 
                            "ya":float(entryVariables[7].get()), 
                            "b":scale.get()
                            }

            if id is not None:
                del objects[id]
                objects.insert(id, object_settings)

            else:
                objects.append(object_settings)

            showinfo("Sucess","New object data saved.")
            fen.destroy()
            updateUI()

        except:
            showerror("Error","Some values are not of the right type.")

    
    fen = Toplevel()
    fen.title("New object")

    entryVariables = [StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar(), StringVar()]

    Label(fen, text = "Object mass: ").grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[0], width = 20).grid(column = 1, row = 0, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Object volume: ").grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[1], width = 20).grid(column = 1, row = 1, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "X position: ").grid(column = 0, row = 2, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[2], width = 20).grid(column = 1, row = 2, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Y position: ").grid(column = 0, row = 3, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[3], width = 20).grid(column = 1, row = 3, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "X velocity: ").grid(column = 0, row = 4, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[4], width = 20).grid(column = 1, row = 4, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Y velocity: ").grid(column = 0, row = 5, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[5], width = 20).grid(column = 1, row = 5, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "X acceleration: ").grid(column = 0, row = 6, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[6], width = 20).grid(column = 1, row = 6, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Y acceleration: ").grid(column = 0, row = 7, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[7], width = 20).grid(column = 1, row = 7, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Bounciness: ").grid(column = 0, row = 8, padx = 10, pady = 20, sticky = NW)
    scale = Scale(fen, from_=0, to=1, orient=HORIZONTAL, length=120, showvalue=1, resolution=0.01)
    scale.grid(column = 1, row = 8, padx = 10, pady = 2, sticky = NW)

    Button(fen, text = "Confirm values", command = confirm, width = 35).grid(column = 0, row = 9, padx = 10, pady = 10, columnspan = 2)

    if id is not None:
        entryVariables[0].set(objects[id]["m"])
        entryVariables[1].set(objects[id]["v"])
        entryVariables[2].set(objects[id]["xp"])
        entryVariables[3].set(objects[id]["yp"])
        entryVariables[4].set(objects[id]["xv"])
        entryVariables[5].set(objects[id]["yv"])
        entryVariables[6].set(objects[id]["xa"])
        entryVariables[7].set(objects[id]["ya"])
        scale.set(objects[id]["b"])

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

                    global_settings["x_size"] = int(entryVariables[0].get())
                    global_settings["y_size"] = int(entryVariables[1].get())
                    global_settings["totalTime"] = float(entryVariables[2].get().replace(",","."))
                    global_settings["timeStep"] = float(entryVariables[3].get().replace(",","."))

                    fen.destroy()
                    
            except:
                showerror("Error","Size of box (x and y) have to be integers.")
                return


    fen = Toplevel()
    fen.title("Edit settings")

    entryVariables = [StringVar(), StringVar()]
    entryVariables[0].set(global_settings["totalTime"])
    entryVariables[1].set(global_settings["timeStep"])

    Label(fen, text = "Total duration: ").grid(column = 0, row = 0, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[0], width = 20).grid(column = 1, row = 0, padx = 10, pady = 10, sticky = NW)

    Label(fen, text = "Timestep: ").grid(column = 0, row = 1, padx = 10, pady = 10, sticky = NW)
    Entry(fen, textvariable = entryVariables[1], width = 20).grid(column = 1, row = 1, padx = 10, pady = 10, sticky = NW)

    Button(fen, text = "Edit border values", command = None, width = 35).grid(column = 0, row = 2, padx = 10, pady = 10, columnspan = 2)
    Button(fen, text = "Confirm values", command = confirm, width = 35).grid(column = 0, row = 3, padx = 10, pady = 10, columnspan = 2)

    fen.mainloop()

def finish_setup():

    if not len(objects) > 2:
        showerror("Error","You have to set at least 2 objects with valid data.")
        return
    
    if global_settings["totalTime"] == 0:
        showerror("Error","You have to set the global settings before being able to generate a setup file.")
        return

    showinfo("Sucess","Setup file generation sucessful.")
    # Generate .setup file


def updateUI():
    global objects
    for child in mainFrame.winfo_children():
        child.destroy() 

    if len(objects) > 0:
        for loop in range(len(objects)):
            Button(mainFrame, text = f"Edit object {loop+1}", command = lambda x = loop: newObject(x), width = 50, height = 2, relief = FLAT).grid(column = 0, row = loop, padx = 10, pady = 10)


    Button(mainFrame, text = "New Object", command = newObject, width = 50, height = 2).grid(column = 0, row = len(objects), padx = 10, pady = 10)

    Button(mainFrame, text = "Edit global settings", command = editSettings, width = 50, height = 2).grid(column = 0, row = len(objects)+1, padx = 10, pady = 10)

    Button(mainFrame, text = "Generate setting file", command = finish_setup, width = 50, height = 2).grid(column = 0, row = len(objects)+2, padx = 10, pady = 10)

# Global variables
objects = []
global_settings = {"totalTime":0, "timeStep":0}

# GUI / Tkinter part
window = Tk()
window.title("Setup")

mainFrame = Frame(window)
mainFrame.grid()

updateUI()

# GUI mainloop
window.mainloop()