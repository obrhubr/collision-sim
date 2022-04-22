# Imports
from tkinter import*
from tkinter.messagebox import*

# Functions
def editBorders():

    def confirm():
        global borders

        for loop in allBorderEntries:
            borders.append([loop[0].get(),loop[1].get(),loop[2].get(),loop[3].get()])

        for loop in borders:
            if "" in loop:
                showerror("Error","All fields have to be filled in.")
                borders = []
                return

        updateUI()
        fen.destroy()

    def on_closing():
        updateUI()
        fen.destroy()

    def show_line(id):
        try:
            if allLinesGUI[id] is not None:
                can.delete(allLinesGUI[id])
            allLinesGUI[id] = can.create_line(allBorderEntries[id][0].get(),allBorderEntries[id][1].get(),allBorderEntries[id][2].get(),allBorderEntries[id][3].get())
        except:
            showerror("Error","Complete all the fields before being able to show the line.")
        
    def new_fields():
        allBorderEntries.append([StringVar(),StringVar(),StringVar(),StringVar()])
        allLinesGUI.append(None)
        Entry(fen, width = 10, textvariable = allBorderEntries[len(allBorderEntries)-1][0]).grid(column = 1, row = 3+len(allBorderEntries), padx = 10, pady = 10)
        Entry(fen, width = 10, textvariable = allBorderEntries[len(allBorderEntries)-1][1]).grid(column = 2, row = 3+len(allBorderEntries), padx = 10, pady = 10)
        Entry(fen, width = 10, textvariable = allBorderEntries[len(allBorderEntries)-1][2]).grid(column = 3, row = 3+len(allBorderEntries), padx = 10, pady = 10)
        Entry(fen, width = 10, textvariable = allBorderEntries[len(allBorderEntries)-1][3]).grid(column = 4, row = 3+len(allBorderEntries), padx = 10, pady = 10)
        Button(fen, text = "Show", command = lambda x = len(allBorderEntries)-1 : show_line(x), width = 10).grid(column = 5, row = 3+len(allBorderEntries), padx = 10, pady = 10)
        
    fen = Toplevel()
    fen.state('zoomed')
    fen.title("Border settings")
    fen.protocol("WM_DELETE_WINDOW", on_closing)

    can = Canvas(fen, width = 1000, height = 1000, bg = "white")
    can.grid(column = 0, row = 0, rowspan = 50, padx = 10, pady = 10)

    Button(fen, text = "New Border", width = 60, command = new_fields).grid(column = 1, row = 0, columnspan = 5, padx = 10, pady = 10)
    Button(fen, text = "Confirm borders", width = 60, command = confirm).grid(column = 1, row = 1, columnspan = 5, padx = 10, pady = 10)

    Label(fen, text = "X1").grid(column = 1, row = 2, padx = 10, pady = 10)
    Label(fen, text = "Y1").grid(column = 2, row = 2, padx = 10, pady = 10)
    Label(fen, text = "X2").grid(column = 3, row = 2, padx = 10, pady = 10)
    Label(fen, text = "Y2").grid(column = 4, row = 2, padx = 10, pady = 10)

    fen.mainloop()

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
                float(loop.get().replace(",","."))
            except:
                allNumbers = False
        
        if not allNumbers:
            showerror("Error","All settings have to be numerical - no strings allowed.")
            return

        else:

            try:

                totalTimeValid = float(entryVariables[0].get().replace(",",".")) > float(entryVariables[1].get().replace(",","."))
                timeStepValid = float(entryVariables[1].get().replace(",",".")) <= 1 and float(entryVariables[1].get().replace(",",".")) >= 0.02

                if not totalTimeValid:
                    showerror("Error","Total simulation time has to be bigger than timestep.")
                    return
                elif not timeStepValid:
                    showerror("Error","Timestep has to be between 0.02 and 1")
                    return
                else:
                    showinfo("Sucess","All parameters valid.")


                    global_settings["totalTime"] = float(entryVariables[0].get().replace(",","."))
                    global_settings["timeStep"] = float(entryVariables[1].get().replace(",","."))

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

    Button(fen, text = "Confirm values", command = confirm, width = 35).grid(column = 0, row = 2, padx = 10, pady = 10, columnspan = 2)

    fen.mainloop()

def finish_setup():

    if not len(objects) >= 2:
        showerror("Error","You have to set at least 2 objects with valid data.")
        return

    if len(borders) == 0:
        showerror("Error","You have not defined the borders.")
        return
    
    if global_settings["totalTime"] == 0:
        showerror("Error","You have to set the global settings before being able to generate a setup file.")
        return

    with open("data.setup","w") as f:
        f.write(str(global_settings["totalTime"])+","+str(global_settings["timeStep"])+","+str(len(objects))+"\n")
        for loop in borders:
            f.write("B,"+str(loop[0])+","+str(loop[1])+","+str(loop[2])+","+str(loop[3])+"\n")
        for loop in objects:
            f.write("O,"+str(loop["m"])+","+str(loop["v"])+","+str(loop["xp"])+","+str(loop["yp"])+","+str(loop["xv"])+","+str(loop["yv"])+","+str(loop["xa"])+","+str(loop["ya"])+","+str(loop["b"])+"\n")

    showinfo("Sucess","Setup file generation sucessful.")
    # Generate .setup file


def updateUI():
    global objects, allLinesGUI, allBorderEntries, borders
    for child in mainFrame.winfo_children():
        child.destroy() 

    allLinesGUI = []
    allBorderEntries = []

    if len(objects) > 0:
        for loop in range(len(objects)):
            Button(mainFrame, text = f"Edit object {loop+1}", command = lambda x = loop: newObject(x), width = 50, height = 2, relief = FLAT).grid(column = 0, row = loop, padx = 10, pady = 10)


    Button(mainFrame, text = "New Object", command = newObject, width = 50, height = 2).grid(column = 0, row = len(objects), padx = 10, pady = 10)

    Button(mainFrame, text = "Edit time settings", command = editSettings, width = 50, height = 2).grid(column = 0, row = len(objects)+1, padx = 10, pady = 10)

    Button(mainFrame, text = "Edit border settings", command = editBorders, width = 50, height = 2).grid(column = 0, row = len(objects)+2, padx = 10, pady = 10)

    Button(mainFrame, text = "Generate setting file", command = finish_setup, width = 50, height = 2).grid(column = 0, row = len(objects)+3, padx = 10, pady = 10)

# Global variables
objects = []
global_settings = {"totalTime":0, "timeStep":0}
borders = []
allBorderEntries = []
allLinesGUI = []

# GUI / Tkinter part
window = Tk()
window.title("Setup")

mainFrame = Frame(window)
mainFrame.grid()

updateUI()

# GUI mainloop
window.mainloop()