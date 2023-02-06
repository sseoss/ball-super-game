from tkinter import*
import random
import time
screen = Tk()
screen.title('Игра')
screen.resizable(0, 0)
screen.wm_attributes('-topmost',1)
canvas = Canvas(screen, width=500 , height = 400,bd =0 , highlightthickness=0 )
canvas.pack()
class Paddle:
    def __init__(self, canvas , color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0, 100, 10 , fill = color)
        self.canvas.move(self.id,200,300)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0

    def draw(self):
        self.canvas.move(self.id, self.x , 0)
        position = self.canvas.coords(self.id)
        if position[2] >= self.canvas_width:
            self.x = 0
        elif position[0] <= 0:
            self.x= 0


    def turn_left(self, evt):

        self.x = -2



    def turn_right(self, evt):
        self.x = 2
class Ball:
    def __init__(self, canvas ,color ):
        self.paddle = paddle
        self.canvas = canvas
        self.schet = schet
        self.id = canvas.create_oval(10, 10 , 25 , 25, fill = color)
        self.canvas.move(self.id,245,100)
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = 2
        self.canvas_height = self.canvas.winfo_height ()
        self.canvas_width = self.canvas.winfo_width ()
        self.hit_bottom = False




    def hit_paddl(self, position):
        paddle_position = self.canvas.coords(self.paddle.id)
        if position[2] >= paddle_position[0] and position[0] <= paddle_position[2]:
            if paddle_position[1] <= position[3] <= paddle_position[3]:
                self.schet.hit()
                return True


        return False



    def draw(self):
        self.canvas.move(self.id, self.x , self.y)
        position = self.canvas.coords(self.id)
        if position[3] >= self.canvas_height:
            self.hit_bottom = True
            canvas.create_text(200, 200 , text="ВЫ ПРОИГРАЛИ", fill='red', font=('Arial', 32))
        if position[1] <= 0:
            self.y = 3
        if position[2]>= self.canvas_width:
            self.x = -3
        if position[0] <= 0:
            self.x = 3
        if self.hit_paddl(position):
            self.y = -3

class Schet:
    def __init__(self, canvas, color):
        self.schet = 0
        self.canvas = canvas
        self.id = canvas.create_text(430, 70 , text=self.schet, fill=color, font=('Arial', 15))
    def hit(self):
        self.schet += 1
        self.canvas.itemconfig(self.id,text = self.schet)




screen.update()
schet = Schet(canvas, 'black')
paddle = Paddle(canvas,'blue')

ball = Ball(canvas,'red')
while 1:
    if ball.hit_bottom == False:
        paddle.draw()
        ball.draw()


    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)