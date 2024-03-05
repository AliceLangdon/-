#бля тут короче мы файлы со всей хуйни импортируем
from tkinter import *
from datetime import datetime
#код для увеличения секнд/минут/ и хотелось бы конечно еще часов
#деф тик означает что на каждом шаге должен выполняться определенный код
temp = 0
after1 = " "
last_mouse_pos = None
last_check_time = None

def tick():
    global temp, after1
    after1 = root.after(1000, tick)
    f_temp = datetime.fromtimestamp(temp).strftime("%M:%S")
    Label1.configure(text=str(f_temp) )
    temp +=1

def start_tick():
    btnStart.pack_forget()
    btnStop.pack()
    tick()

def stop_tick():
    btnStop.pack_forget()
    btnContinue.pack()
    btnReset.pack()
    root.after_cancel(after1)

def continue_tick():
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStop.pack()
    tick()

def reset_tick():
    global temp
    btnContinue.pack_forget()
    btnReset.pack_forget()
    btnStart.pack()
    temp=0
    Label1.configure(text="00:00")
    Label1.pack()


#вот тут мы создаем с помощью "корня" саму панель, ее название и размер
root = Tk()
root.title("Секундомер ещкере")
root.resizable(width=False, height=False)
root.geometry("400x300")

#тут мы просто задаем текст
Label1 = Label(root, width=20, font=("Comic Sans MC", 40), text = "00:00:00")
Label1.pack()

#тут мы делаем кнопки, там шрифт пишем, ширину кнопки и собственно привязываем к корню
btnStart = Button(root, text = "Начать", font=("Comic Sans MC", 20), width = 15, command=start_tick)
btnStop = Button(root, text = "Стоп", font=("Comic Sans MC", 20), width = 15, command=stop_tick)
btnContinue = Button(root, text = "Продолжить", font=("Comic Sans MC", 20), width = 15, command=continue_tick)
btnReset = Button(root, text = "Cброс", font=("Comic Sans MC", 20), width = 15, command=reset_tick)
btnStart.pack()


#это хуйня для того чтобы комп считывал что мы делаем мышкой или клавой
root.mainloop()