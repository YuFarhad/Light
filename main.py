import tkinter as tk
    
roomsList = [
    "Кухня",
    "Гостинная",
    "Прихожая",
    "Спальня",
    "Ванная",
    "Детская"
]

buttonList = []

scaleList = []

checkInRoomslists = []

lampStatusLists = []

def switchLamps():
    print("Переключение...")


lampsAmount = 2
f = tk.Tk()
f.geometry("380x650")
it = 0
k = 0
while it < len(roomsList):
    buttonList.insert(it, tk.Button(text=roomsList[it], command=switchLamps))
    buttonList[it].grid(row=it*(lampsAmount+1), column=0)
    k = 0
    cbList = []
    stateList = []
    while k < lampsAmount:
        stateList.insert(k, tk.IntVar())
        k += 1
    lampStatusLists.insert(it, stateList)
    k = 0
    while k < lampsAmount:
        cbList.insert(k, tk.Checkbutton(text=k + 1, variable=lampStatusLists[it][k], onvalue=1, offvalue=0))
        cbList[k].grid(row=it * (lampsAmount + 1) + k + 1, column=0)
        k += 1
    checkInRoomslists.insert(it, cbList)
    scaleList.insert(it, tk.Scale(label="Яркость ламп", from_=1, to=100, orient=tk.HORIZONTAL, length=300, width=10))
    scaleList[it].grid(row=it*(lampsAmount+1), column=1)
    it += 1



f.mainloop()

#check

for i in range(len(lampStatusLists)):
    for k in range(len(lampStatusLists[i])):
        print(lampStatusLists[i][k])
    print()
