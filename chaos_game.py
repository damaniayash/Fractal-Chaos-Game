# -*- coding: utf-8 -*-
"""
Created on Sun May 10 16:06:05 2020

@author: damaniayash
"""
#Fractal Generation using Chaos Game

import turtle
import argparse
#from turtle import Screen
import random

parser = argparse.ArgumentParser() 
parser.add_argument("-a", "--Animation", type = bool, default = False, help = "Animate or not to Animate")
args = parser.parse_args()
if args.Animation == True:
	dot_size = 3
else:
	dot_size = 2 


# Drawing polygons.
# Returns a list of co-ordinates representing vertices of the polygon.
def drawPolygon(sides:int, side_length:int, initial_coordintes:int) -> list:
	turtle.speed('fast')
	turtle.screensize(canvwidth=300, canvheight=300, bg='black')
	turtle.pen(pencolor='white', pensize=2)
	turtle.penup()
	vertex_set=[]
	turtle.setpos(initial_coordintes)
	turtle.pendown()
	for i in range(sides):
		turtle.forward(side_length)
		turtle.left(360/sides)
		vertex_set.append(turtle.pos())
		turtle.dot()
	turtle.penup()
	#turtle.done()
	return vertex_set

# Actual Chaos Game Sierpinski Triangle
def chaosGameTriangle(iterations:int, distFactor:int):
	vertex_set=drawPolygon(3,600,[-300,-265])
	# Set Random Initial Starting Point.
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	for itr in range(iterations):
		print('Iteration : ', itr)
		# Randomly select any one of the vertices.
		vertex=random.choice([0,1,2])
		curr_x,curr_y = turtle.pos()
		# New pointed created at a Fixed distance between current co-ordinate and random point.
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()

# Modified for Square fractals
def chaosGameSquare(iterations:int, distFactor:float):
	vertex_set=drawPolygon(4,530,[-265,-265])
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	prev_vertex=0
	for itr in range(iterations):
		print('Iteration : ',itr)
		#Ensure previous vertex is not repeated
		all_vertices=[0,1,2,3]
		vertex=random.choice(all_vertices)
		if prev_vertex == vertex:
			all_vertices.remove(vertex)
			vertex=random.choice(all_vertices)
		prev_vertex=vertex
		curr_x,curr_y = turtle.pos()
		# New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()

def chaosGameVicsek(iterations:int, distFactor:float):
	vertex_set=drawPolygon(4,530,[-265,-265])
	# Add center of the Square as a possible co-ordinate while jumping
	vertex_set.append([0.0,0.0])
	turtle.setpos([0.0,0.0])
	turtle.dot('white')
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	for itr in range(iterations):
		print('Iteration : ',itr)
		all_vertices=[0,1,2,3,4]
		vertex=random.choice(all_vertices)
		curr_x,curr_y = turtle.pos()
		# New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()



#Modified for Pentagon Fractal
def chaosGamePentagon(iterations:int,distFactor:float):
	vertex_set=drawPolygon(5,350,[-180,-265])
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	prev_vertex=0
	for itr in range(iterations):
		print('Iteration : ',itr)
		#Ensure previous vertex is not repeated
		all_vertices=[0,1,2,3,4]
		vertex=random.choice(all_vertices)
		if prev_vertex == vertex:
			all_vertices.remove(vertex)
			vertex=random.choice(all_vertices)
		prev_vertex=vertex
		curr_x,curr_y = turtle.pos()
        # New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()

def chaosGameSquare1(iterations:int, distFactor:float):
	vertex_set=drawPolygon(4,530,[-265,-265])
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	choice_list=[0,0]
	prev_vertex=6
	pprev_vertex=6
	for itr in range(2,iterations+2):
		print('Iteration : ',itr)
		#Ensure current node is not a neighbour of previous node if previous 2 nodes were same.
		all_vertices=[0,1,2,3]
		vertex=random.choice(all_vertices)
		choice_list.append(vertex)
		prev_vertex=choice_list[itr-1]
		pprev_vertex=choice_list[itr-2]
		if prev_vertex == pprev_vertex:
			if prev_vertex == 0:
				vertex=random.choice([0,2])
			if prev_vertex == 1:
				vertex=random.choice([1,3])
			if prev_vertex == 2:
				vertex=random.choice([0,2])
			if prev_vertex == 3:
				vertex=random.choice([1,3])
		print(prev_vertex)
		print(pprev_vertex)
		curr_x,curr_y = turtle.pos()
		# New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()

def chaosGamePentagon1(iterations:int, distFactor:float):
	vertex_set=drawPolygon(5,350,[-180,-265])
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	choice_list=[0,0]
	prev_vertex=6
	pprev_vertex=6
	for itr in range(2,iterations+2):
		print('Iteration : ',itr)
		#Ensure current node is not a neighbour of previous node if previous 2 nodes were same.
		all_vertices=[0,1,2,3,4]
		vertex=random.choice(all_vertices)
		choice_list.append(vertex)
		prev_vertex=choice_list[itr-1]
		pprev_vertex=choice_list[itr-2]
		if prev_vertex == pprev_vertex:
			if prev_vertex == 0:
				vertex=random.choice([2,3])
			if prev_vertex == 1:
				vertex=random.choice([3,4])
			if prev_vertex == 2:
				vertex=random.choice([0,4])
			if prev_vertex == 3:
				vertex=random.choice([0,1])
			if prev_vertex == 4:
				vertex=random.choice([1,2])
		print(prev_vertex)
		print(pprev_vertex)
		curr_x,curr_y = turtle.pos()
		# New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()
def chaosGameHexagon(iterations:int,distFactor:float):
	vertex_set=drawPolygon(6,300,[-155,-260])
	#Set Random Initial Starting Point
	turtle.setpos(random.uniform(-300.0,300.0),random.uniform(-300.0,300.0))
	#turtle.dot()
	turtle.speed('fastest')
	prev_vertex=0
	for itr in range(iterations):
		print('Iteration : ',itr)
		#Ensure previous vertex is not repeated
		all_vertices=[0,1,2,3,4,5]
		vertex=random.choice(all_vertices)
		if prev_vertex == vertex:
			all_vertices.remove(vertex)
			vertex=random.choice(all_vertices)
		prev_vertex=vertex
		curr_x,curr_y = turtle.pos()
        # New pointed created at a Fixed distance between current co-ordinate and random point
		new_x,new_y = ((curr_x + vertex_set[vertex][0]) * distFactor) , ((curr_y + vertex_set[vertex][1]) * distFactor)
		turtle.setpos(new_x,new_y)
		turtle.dot(dot_size,'white')
	turtle.done()
def barnsleyFern(iterations:int):
	turtle.screensize(canvwidth=300, canvheight=300, bg='black')
	x = 0
	y = 0
	for itr in range(iterations):
		print('Iteration : ',itr)
		turtle.setpos([85*x,57*y-275])   
		turtle.pendown()
		turtle.dot(dot_size,'green')
		turtle.penup()
		probablity = (100 * random.random())
		curr_x = x
		curr_y = y
		if probablity < 1:
			x = 0
			y = 0.16*curr_y
		elif probablity < 86:
			x = 0.85*curr_x + 0.04*curr_y
			y = -0.04*curr_x + 0.85*curr_y + 1.6
		elif probablity < 93:
			x = 0.20*curr_x - 0.26*curr_y
			y = 0.23*curr_x + 0.22 * curr_y + 1.6
		else:
			x = -0.15*curr_x + 0.28*curr_y
			y = 0.26*curr_x + 0.24*curr_y + 0.44
	turtle.done()


#Driver

choice = int(input('Press\n1.Sierpinski Triangle\n2.Square Fractal\n3.Pentagon Fractal\n4.Vicsek Fractal\n5.Hexagonal Fractal\n6.Another Square Fractal\n7.Barnsley Fern\n'))
iters = int(input('Enter Iterations\n'))
turtle.tracer(args.Animation)
if choice == 1:
	chaosGameTriangle(iters,0.5)
elif choice == 2:
	chaosGameSquare(iters,0.5)
elif choice == 3:
	chaosGamePentagon(iters,0.5)
elif choice == 4:
	chaosGameVicsek(iters,0.333333)
elif choice == 5:
	chaosGameHexagon(iters,0.5)
elif choice == 6:
	chaosGameSquare1(iters,0.5)
elif choice == 7:
	barnsleyFern(iters)
else:
	print('Invalid input OR window closed')




