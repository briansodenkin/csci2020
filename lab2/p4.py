import math

def check_invalid(triangle):
    if triangle[0] > 0 and triangle[1] > 0 and triangle[2] > 0:
        if triangle[0]+triangle[1]> triangle[2] and triangle[1]+triangle[2]>triangle[0] and triangle[2]+triangle[0]>triangle[1]:
            return False
    return True

def is_obtuse_triangle(triangle):
    a = triangle[0]**2
    b = triangle[1]**2
    c = triangle[2]**2
    
    if (a > b+c or b > a+c or c > b+a):
        return True
    else:
        return False

def perimeter(triangle):
    return triangle[0] + triangle[1] + triangle[2]

def area(triangle):
    s = perimeter(triangle)/2
    return (math.sqrt(s * (s-triangle[0]) * (s-triangle[1]) * (s-triangle[2])))

# print(area((3,4,5)))

