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
        cbList.insert(k, tk.Checkbutton(text=k+1, variable=stateList[k]))
        if k == lampsAmount:
            checkInRoomslists.insert(it, cbList)
        cbList[k].grid(row=it*(lampsAmount+1)+k+1, column=0)
        k += 1
    scaleList.insert(it, tk.Scale(label="Яркость ламп", from_=1, to=100, orient=tk.HORIZONTAL, length=300, width=10))
    scaleList[it].grid(row=it*(lampsAmount+1), column=1)
    it += 1

f.mainloop()
