# import colorgram
#
# colors = colorgram.extract('Dhakua.png', 30)
#
# rgb_colors = []
#
# for color in colors:
#     rgb = color.rgb
#     r = rgb[0]
#     g = rgb[1]
#     b = rgb[2]
#     img_colors = (r, g, b)
#     rgb_colors.append(img_colors)
#
# print(rgb_colors)

# first_color = colors[0]
# rgb = first_color.rgb
# red = rgb[0]
# green = rgb[1]
# blue = rgb[2]
# print(red, green, blue)
# print(rgb)
# # # print(first_color)
# print(colors)
#

color_list = [(252, 251, 251), (57, 89, 122), (207, 227, 236), (46, 62, 96), (41, 170, 121), (133, 102, 88), (196, 171, 139), (119, 166, 200), (47, 46, 46), (222, 244, 242), (125, 74, 117), (108, 47, 47), (82, 122, 185), (133, 175, 156), (47, 53, 64), (168, 193, 216), (197, 133, 45), (169, 105, 134), (223, 194, 137), (55, 146, 196), (185, 143, 159), (214, 200, 204), (164, 208, 182), (58, 51, 57), (150, 205, 218), (123, 40, 76), (79, 97, 95), (54, 61, 57), (185, 104, 103), (239, 173, 160)]
my_colors = ["red", "green", "blue", "yellow", "black", "orange", "purple"]

import random
#from turtle import Turtle, Screen
import turtle

turtle.colormode(255)

tim = turtle.Turtle()

tim.speed("fastest")


x = -200
y = -200

tim.penup()
tim.goto(x, y)
#colormode(255)
for i in range(10):
    for j in range(10):
        tim.pendown()
        tim.color(random.choice(color_list))
        tim.begin_fill()
        tim.circle(10)
        tim.end_fill()
        tim.penup()
        tim.forward(50)
    y += 50
    tim.goto(x, y)

tim.hideturtle()

# print(tim.position())
# tim.penup()
# tim.goto(-200, -140)




















screen = turtle.Screen()
screen.exitonclick()