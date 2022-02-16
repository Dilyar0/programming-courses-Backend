from tkinter import *
import time
import random

field = Tk()
field.title("Game")
field.resizable(0, 0)
field.wm_attributes("- Topmost", 1)
canvas = Canvas(field, width=600, height=500, highlightthickness=0)
canvas.pack()
field.update()

class Ball:
    def __init__(self, canvas, paddle, score, color):
        self.canvas = canvas
        self.paddle = paddle
        self.color = color

        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)

        starts = [-2, -1, 1, 2]
        random.shuffle(starts)

        self.y = -2

        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]
                self.score_hit()
                return True
            return True
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.move(self.id)
        if pos[1] <= 0:
            self.y = 2
        if pos[3] >= self.canvas_height:
            canvas.hit_bottom = True
            canvas.create_text(250, 120, text="Вы проиграли", font=("Counter", 30), fill="red")
        if self.hit_paddle(pos) == True:
            self.y = -2
        if pos[0] <= 0:
            self.x = 2
        if pos[2] >= self.canvas_width:
            self.x = -2

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color

        self.id = canvas.create_rectangle(0, 0 , 100, 10, fill=color)
