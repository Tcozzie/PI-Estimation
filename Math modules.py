import random
import math

def estimate_pi():

    count = 0
    points = 1000

    for point in range(points):
        x = random.random()
        y = random.random()
        r_squared = x**2 + y**2
        r = math.sqrt(r_squared)
        if (r <= 1):
            count = count + 1
            
    circle_points = (count/points) * 4
    
    return circle_points
    

def main():
    result = estimate_pi()
    print(result)

main()
