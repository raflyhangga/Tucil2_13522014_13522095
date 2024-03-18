from typing import List
import math
import time


class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y


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
        for i in range(len(self.iter_res)):
            print("Iterasi ke-",i+1)
            self.print_points(self.iter_res[i])

    def get_result_points_dnc(self):
        return self.result_points_dnc
    
    def get_result_points_brutal(self):
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
        
    
