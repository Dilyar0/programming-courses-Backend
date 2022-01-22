# from turtle import *
# color('red', 'yellow')
# begin_fill()
# while True:
#     forward(200)
#     left(170)
#     if abs(pos()) < 1:
#         break
# end_fill()
# done()


from turtle import *
speed(8)
color("yellow")
bgcolor("black")
i = 200
while i>0:
    left(i)
    forward(i*3)
    i = i - i