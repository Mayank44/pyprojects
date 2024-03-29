"""dijkstra's algorithm"""
import heapq
import random
from itemclass import *

validnodes=[(1,1),(1,2),(1,3),(1,5),(1,6),(1,9),(1,10),(2,1),
            (2,2),(2,3),(2,4),(2,5),(2,6),(2,9),(2,10),(3,1),
            (3,2),(3,3),(3,4),(3,5),(3,6),(3,9),(3,10),(10,15),
            (10,16),(10,17),(10,18),(11,15),(11,16),(11,17)]

class SquareGrid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.walls = []
    
    def in_bounds(self, id):
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id):
        return id not in self.walls
    
    def neighbours(self, id):
        (x, y) = id
        results = [(x+1, y),(x, y-1),(x-1, y),(x, y+1)]
        if (x+y) % 2 == 0: results.reverse()#just for looks
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results

class GridWithWeights(SquareGrid):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.weights = {}
    
    def cost(self, from_node, to_node):
        return self.weights.get(to_node,1)

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self,item,priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
            
def from_id_width(id, width):
    return (id % width, id // width)

def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']: r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1: r = ">"
        if x2 == x1 - 1: r = "<"
        if y2 == y1 + 1: r = "v"
        if y2 == y1 - 1: r = "^"
    if 'start' in style and id == style['start']: r = "A"
    if 'goal' in style and id == style['goal']: r = "Z"
    if 'path' in style and id in style['path']: r = "@"
    if id in graph.walls: r = "#" * width
    return r
    
def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()

def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)
        
def astar_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbours(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost<cost_so_far[next]:
                cost_so_far[next]=new_cost
                priority = new_cost + heuristic(goal, next)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    return path
    
diagram4 = GridWithWeights(20, 20)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8),(0,9)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6), 
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6), 
                                       (5, 7), (5, 8), (6, 2), (6, 3), 
                                       (6, 4), (6, 5), (6, 6), (6, 7), 
                                       (7, 3), (7, 4), (7, 5)]}

#came_from, cost_so_far = dijkstra_search(diagram4,(1,4),(7,7))
#
#goal = (7,7)
#
#draw_grid(diagram4,width=3,point_to=came_from,start=(1,4),goal=(7,8))
#print()
#draw_grid(diagram4,width=3,number=cost_so_far,start=(1,4),goal=(7,8))
#print()
#draw_grid(diagram4,width=3,path=reconstruct_path(came_from,start=(1,4),goal=(7,7)))
#
#print(cost_so_far[goal])

class Vehicle:
    def __init__(self, capacity, speed, vehiclename):
        self.capacity = capacity
        self.speed = speed
        self.vehiclename = vehiclename
        
        
    def ReturnCost(self, cost_so_far):
        print(cost_so_far[goal])
        distance = cost_so_far[goal]
        deliverytime = distance/self.speed
        print(deliverytime)
        
def RandomItem(itemindex):
    randomitem = random.choice(itemindex)
    print(randomitem.itemname)
    print(randomitem.weight)
    return randomitem
    
    
Drone = Vehicle(2,10,"drone")
Robot = Vehicle(4,7,"robot")
Courier = Vehicle(7,6,"courier")
PnP = Vehicle(10,4,"van")
vehicle_list = [Drone, Robot, Courier, PnP]
compatible_list = []

def VehicleCheck(randomitem):
    print(randomitem.weight)
    for x in vehicle_list:
        if x.capacity >= randomitem.weight:
            compatible_list.append(x)
    current_vehicle = random.choice(compatible_list)        
    print(current_vehicle.vehiclename)    
    return current_vehicle


def Deliver(current_vehicle):
    randomhouse = random.choice(validnodes)
    print(randomhouse)
    print(current_vehicle.speed)
    came_from, cost_so_far= astar_search(diagram4, (0,4),(randomhouse))
    draw_grid(diagram4,width=3,path=reconstruct_path(came_from,start = (0,4),goal = randomhouse))
    print(cost_so_far[randomhouse])    
    print(cost_so_far[randomhouse]/current_vehicle.speed)
    
Deliver(VehicleCheck(RandomItem(itemindex)))
name = []
for i in compatible_list:
    name.append(i.vehiclename)
print(name)


#current_vehicle.ReturnCost()
#VehicleCheck(RandomItem(itemindex))
#name = []
#for i in compatible_list:
#    name.append(i.vehiclename)
#print(name)

















