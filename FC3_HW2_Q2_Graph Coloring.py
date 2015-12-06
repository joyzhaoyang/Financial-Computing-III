"""
This file: FC3HW2Prob2.py
Programmer: Joy Zhao (yangzhao@tepper.cmu.edu)
Course/Section: 46-903
Assignment: Homework2, Problem2
Description: Display a schedule of final exams
Methods: Graph Coloring
Last Modified: 04/08/15
Known Bugs:
"""

""" Build a dictionary with course as key and its neighbours as values """
coursefile = open('StudentsCourses.txt')
courses = {} # dictionary

for line in coursefile:
    word = line.rstrip().split(' ')
    num_courses = int(word[1])
    for i in range(num_courses): 
        if not courses.has_key(word[i+2]):
            courses[word[i+2]] = set() # set: unique element
        neighbour = set(word[i] for i in range(2,num_courses+2))
        neighbour.remove(word[i+2])
        courses[word[i+2]]=courses[word[i+2]].union(neighbour)
# if two courses are taken by the same person, drwa an arc between them
        
""" Build an arc list """
arc = []
for c in courses:
    for n in courses[c]:
        if not (c,n) in arc and not (n,c) in arc:
            arc.append((c,n))

""" Build nodes, edges, and labels for the graph """
import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
G.add_nodes_from(courses.keys()) # nodes
G.add_edges_from(arc) # arcs
pos=nx.spring_layout(G)
sz = 700
# label
labels = {}
for c in courses.keys():
    labels[c] = c

""" Graph coloring algorithm """
all_color =  ['red','orange','yellow','green','cyan','blue','purple','pink']
schedule = 0
num_colored = 0 # number of nodes colored

while num_colored < len(G.nodes()):
    newclr = []
    for v in G.nodes():
        if G.node[v].values() == []: # not colored
            found = False
            for w in newclr:
                if w in list(courses[v]): # an edge found
                    found = True
            if found == False:
                #color this node
                color = all_color[schedule]
                G.node[v][color] = color
                newclr.append(v)
                num_colored = num_colored+1
    #print the new node list
    nx.draw_networkx_nodes(G, pos, nodelist = newclr, node_size = sz,node_color = color)
    #print out the schedule:
    schedule = schedule+1
    print 'Final Exam Period', schedule, "=>",' '.join([c for c in newclr])      

""" Draw the graph """
nx.draw_networkx_edges(G, pos, arc)
nx.draw_networkx_labels(G,pos, labels,font_size=12)
plt.show()

""" The Fix """
raw_input("Press enter to exit")

