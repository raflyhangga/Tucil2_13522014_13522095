import matplotlib.pyplot as plt

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