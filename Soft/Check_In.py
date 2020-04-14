import math

# visualisation
import matplotlib.pyplot as plt
import matplotlib.lines as lines

# visualisation

def Sum_points(P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    return x1+x2, y1+y2

def Multiply_point(multiplier, P):
    x, y = P
    return float(x)*float(multiplier), float(y)*float(multiplier)

def Check_if_object_is_polygon(Cartesian_coords_list):
    if Cartesian_coords_list[0] == Cartesian_coords_list[len(Cartesian_coords_list)-1]:
        return True
    else:
        return False
#chaikin corner cutting
class Algo():
    def __init__(self, Cartesian_coords_list):
        self.Cartesian_coords_list = Cartesian_coords_list

    def Find_Q_point_position(self, P1, P2):
        Summand1 = Multiply_point(float(3)/float(4), P1)
        Summand2 = Multiply_point(float(1)/float(4), P2)
        Q = Sum_points(Summand1, Summand2)
        return Q

    def Find_R_point_position(self, P1, P2):
        Summand1 = Multiply_point(float(1)/float(4), P1)
        Summand2 = Multiply_point(float(3)/float(4), P2)
        R = Sum_points(Summand1, Summand2)
        return R

    def Smooth_by_Chaikin(self, number_of_refinements):
        refinement = 1
        copy_first_coord = Check_if_object_is_polygon(self.Cartesian_coords_list)
        while refinement <= number_of_refinements:
            self.New_cartesian_coords_list = []

            for num, tuple in enumerate(self.Cartesian_coords_list):
                if num+1 == len(self.Cartesian_coords_list):
                    pass
                else:
                    P1, P2 = (tuple, self.Cartesian_coords_list[num+1])
                    Q = obj.Find_Q_point_position(P1, P2)
                    R = obj.Find_R_point_position(P1, P2)
                    self.New_cartesian_coords_list.append(Q)
                    self.New_cartesian_coords_list.append(R)
            if copy_first_coord:
                self.New_cartesian_coords_list.append(self.New_cartesian_coords_list[0])



            self.Cartesian_coords_list = self.New_cartesian_coords_list
            refinement += 1
        return self.Cartesian_coords_list
def chkin(Mtmatrix):

    Cartesian_coords_list =  Mtmatrix

    global obj
    obj = Algo(Cartesian_coords_list)
    Smoothed_obj = obj.Smooth_by_Chaikin(number_of_refinements = 2)
    return Smoothed_obj
    # visualisation
    #x1 = [i for i,j in Smoothed_obj]
    #y1 = [j for i,j in Smoothed_obj]
    #x2 = [i for i,j in Cartesian_coords_list]
    #y2 = [j for i,j in Cartesian_coords_list]
    #plt.plot(range(7),range(7),'w', alpha=0.7)
    #myline = lines.Line2D(x1,y1,color='r')
    #mynewline = lines.Line2D(x2,y2,color='b')
    #plt.gca().add_artist(myline)
    #plt.gca().add_artist(mynewline)
    #plt.show()
