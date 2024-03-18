import matplotlib.pyplot as plt
from typing import List
from dataclasses import dataclass
import math
import time
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Bezier:
    def __init__(self,iterasi = 3, ctr_pts = list()) -> None:
        self.bezier_points:list[tuple[float,float]] = []
        self.ctrl_points:list[tuple[float,float]] = ctr_pts
        self.max_iteration = iterasi

    # Get the middle point between (x1,y1) and (x2,y2)
    def midPoints(self,ctrl1: tuple[float,float],ctrl2: tuple[float,float]):
        return ((ctrl1[0] + ctrl2[0]) / 2,(ctrl1[1] + ctrl2[1]) / 2)

    # Populating the points recursively with amount of n iterations
    def populate(
                    self,
                    ctrl1: tuple[float,float],
                    ctrl2: tuple[float,float],
                    ctrl3:tuple[float,float],
                    iterasi: int,
                    result:list[tuple[float,float]]
                ) -> None:
        if (iterasi <= self.max_iteration):
            midpoint1 = self.midPoints(ctrl1,ctrl2)
            midpoint2 = self.midPoints(ctrl2,ctrl3)
            midpoint3 = self.midPoints(midpoint1,midpoint2)
            iterasi = iterasi + 1
            self.populate(ctrl1,midpoint1,midpoint3,iterasi,result)
            result.append(midpoint3)
            self.populate(midpoint3,midpoint2,ctrl3,iterasi,result)

    # Create Canvas
    def createBezier(self) -> None:
        result:list[tuple[float,float]] = []
        c1,c2,c3 = self.ctrl_points
        self.populate(c1,c2,c3,0,result)
        self.bezier_points = result
    
    # Plotting the points
    def draw(self) -> None:
        x_coords, y_coords = zip(*self.bezier_points)
        plt.plot(x_coords, y_coords, label="Bézier Curve")
        plt.scatter(*zip(*self.ctrl_points), color="red", label="Control Points")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Bézier Curve")
        plt.legend()
        plt.grid(True)
        plt.show()

class BezierCurve:
    def __init__(self, control_points: List[Point], iteration : int): 
        self.control_points = control_points
        self.iteration = iteration
        self.result_points_dnc = []
        self.iter_res = []
        self.result_points_brutal = []
        self.dnc_execution_time = 0
        self.brutal_execution_time = 0

    def create_bezier_brutal(self):
        ## kalkulasi secara brute force hanya bekerja dengan tiga titik kontrol
        

        start_time = time.time()
        self.result_points_brutal.append(self.control_points[0])
        jml_titik = 2**self.iteration + 1
        beda = 1/(jml_titik-1) 
        count_ctrl = len(self.control_points)
        for i in range(jml_titik - 2):
            t = (i+1) * beda

            x = 0
            y = 0
            for j in range(count_ctrl):
                x += (math.comb(count_ctrl-1,j))*((1-t)**(count_ctrl-j-1))*(t**j)*self.control_points[j].x
                y += (math.comb(count_ctrl-1,j))*((1-t)**(count_ctrl-j-1))*(t**j)*self.control_points[j].y
            # x = ((1-t)**2)*self.control_points[0].x + 2*(1-t)*t*self.control_points[1].x + (t**2)*self.control_points[2].x
            # y = ((1-t)**2)*self.control_points[0].y + 2*(1-t)*t*self.control_points[1].y + (t**2)*self.control_points[2].y
            point = Point(x,y)
            self.result_points_brutal.append(point)
            
        
        self.result_points_brutal.append(self.control_points[-1])
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        self.brutal_execution_time = int(execution_time)


    def create_bezier_dnc(self):

        start_time = time.time()

        self.result_points_dnc.append(self.control_points[0])
        self.calculate_new_point(self.control_points,0)
        self.result_points_dnc.append(self.control_points[-1])
        
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000
        self.dnc_execution_time = int(execution_time)

    def calculate_new_point(self,ctrl_points : List[Point],current_iteration : int):
        if current_iteration < self.iteration:
            temp = ctrl_points
            res = []
            while len(temp) > 0:
                res.append(temp)
                temp2 = []
                for i in range(len(temp)-1):
                    mid = self.get_mid_point(temp[i],temp[i+1])
                    temp2.append(mid)
                temp = temp2

            param1 = []
            param2 = []
            for i in range(len(res)):
                param1.append(res[i][0])
                param2.append(res[len(res)-1-i][-1])

            current_iteration += 1
            self.calculate_new_point(param1,current_iteration)
            self.result_points_dnc.append(res[-1][0])
            self.calculate_new_point(param2,current_iteration)
 

    def get_mid_point(self, point1 : Point , point2 : Point) -> Point :
        return Point((point1.x + point2.x) / 2, (point1.y + point2.y) / 2)
    
    def print_points(self, list : List[Point]):
        for point in list:
            print(point.x,point.y)
    
    def print_dnc_points(self):
        self.print_points(self.result_points_dnc)

    def print_brutal_points(self):
        self.print_points(self.result_points_brutal)

    def print_iter_res(self):
        for points in self.iter_res:
            self.print_points(points)

    def get_result_points_dnc(self) -> list[Point]:
        return self.result_points_dnc
    
    def get_result_points_brutal(self) -> list[Point]:
        return self.result_points_brutal
    
    def get_control_points(self):
        return self.control_points
    
    def get_iter_res(self):
        return self.iter_res

    def get_jumlah_control_points(self):
        return len(self.control_points)
    
    def get_time_dnc(self):
        return self.dnc_execution_time
    
    def get_time_brutal(self):
        return self.brutal_execution_time

    def calculate_iter_res(self):
        for i in range(self.iteration):
            temp = []
            to_append = 2**(i+1) -1
            step = len(self.result_points_dnc) / (to_append+1)
            for j in range(0,len(self.result_points_dnc),math.floor(step)):
                temp.append(self.result_points_dnc[j])
            self.iter_res.append(temp)