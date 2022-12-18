def point_move(point, vector):
    c= [x + y for x, y in zip(point, vector)]
    return c
    
def obj_move(object_in,vector):
    vertices_out=[]
    for vertex in object_in.vertices:
        vertices_out.append(point_move(vertex, vector))
    object_out=object_in
    object_out.vertices=vertices_out
    return object_out
    
class Plane:
    def __init__ (self, length, width, height):
        self.vertices=[
            [0,0,0],
            [length,0,0],
            [length,width,0],
            [0,width,0]]
        
        self.edges=[
            [0,1],
            [1,2],
            [2,3],
            [3,0]]
        
        self.faces=[
            [0,1,2,3]]

class Box:
    def __init__ (self, length, width, height):
        self.vertices=[
            [0,0,0],
            [length,0,0],
            [length,width,0],
            [0,width,0],
            [0,0,height],
            [length,0,height],
            [length,width,height],
            [0,width,height]]
        
        self.edges=[
            [0,1],
            [1,2],
            [2,3],
            [3,0],
            [4,5],
            [5,6],
            [6,7],
            [7,4],
            [0,4],
            [1,5],
            [2,6],
            [3,7]]
        
        self.faces=[
            [0,1,2,3],
            [4,5,6,7],
            [0,1,5,4],
            [1,2,6,5],
            [2,3,7,6],
            [3,0,4,7]]