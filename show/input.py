from tkinter import*
from tkinter.filedialog import*

def draw_borders():
    for loop in borders:
        canvas.create_line(int(loop[0]),int(loop[1]),int(loop[2]),int(loop[3]))

def update_UI():
    global currentID, mouvementData, objectsUI
    

    if currentID < totalTime:
        for loop in range(objectNb):

            canvas.delete(objectsUI[loop])

            objectsUI[loop]=canvas.create_oval(
                                                int(float(mouvementData[currentID][0+2*loop]))-int(float(objectData[loop][0])),
                                                int(float(mouvementData[currentID][1+2*loop]))-int(float(objectData[loop][0])),
                                                int(float(mouvementData[currentID][0+2*loop]))+int(float(objectData[loop][0])),
                                                int(float(mouvementData[currentID][1+2*loop]))+int(float(objectData[loop][0]))
                                                )
            
        currentID += 1
        window.after(int(timeStep*1000), update_UI)

window = Tk()
window.title("Animation")
window.state('zoomed')

setup_file = askopenfilename(filetypes=[("Setup files","*.setup")])
output_file = askopenfilename(filetypes=[("Data files","*.data")])

borders = []
timeStep = 0
totalTime = 0
objectNb = 0
objectRawData = []
objectData = []
mouvementData = []

currentID = 0
objectsUI = []

# Reading all informations from data.setup file
with open(setup_file,"r") as f:
    totalTime, timeStep, objectNb = f.readline().split(",")
    totalTime, timeStep, objectNb = int(float(totalTime)), float(timeStep), int(objectNb)
    
    line = f.readline()
    while line[0] == "B":
        borders.append(line.strip().split(",")[1:])
        line = f.readline()
    
    objectRawData.append(line)

    for loop in range(objectNb-1):
        objectRawData.append(f.readline())

    for element in objectRawData:
        objectData.append(element.strip().split(",")[2:5])

# Reading all informations from output.data file
with open(output_file,"r") as f:
    for loop in range(totalTime):
        mouvementData.append(f.readline()[:-2].strip().split(","))

canvas = Canvas(window, width = 1000, height = 1000, bg = "white")
canvas.grid(column = 0, row = 0, padx = 10, pady = 10)

draw_borders()

print(objectData)
for loop in objectData:
    objectsUI.append(canvas.create_oval(int(float(loop[1]))-int(float(loop[0])),int(float(loop[2]))-int(float(loop[0])),int(float(loop[1]))+int(float(loop[0])),int(float(loop[2]))+int(float(loop[0]))))


window.after(int(timeStep*1000), update_UI)

window.mainloop()
