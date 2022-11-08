import math

#### PROJECTILE CALCULATOR ####

print("""
        This is a projectile calculator written by Ben Grant

        Things to take note before using:
            - Air resistance is considered to be negligible so in reality,
              the calculations done by this calculator are slightly exaggerated
""")

def quadraticMinus(a, b, c):
    # finds the root but with - in the place of the +/- in the formula
    return (-b - math.sqrt(b**2 - (4*a*c)))/(2*a)

def quadraticPlus(a, b, c):
    # finds the root but with + in the place of the +/- in the formula
    return (-b + math.sqrt(b**2 - (4*a*c)))/(2*a)



GRAVITY = -9.81 #accelaration

u = float(input("enter the initial velocity of the projectile as it is shot (m/s)"))
theta = float(input("enter the angle from the horizontal at which the projectile is shot (degrees)"))
height = float(input("enter the height from the landing plane (ground) that the projectile is shot from (m)"))


u_horizontal_vel = u*math.cos(math.radians(theta))
u_vertical_vel = u*math.sin(math.radians(theta))

def findTime():
    if (quadraticMinus(GRAVITY, (2*u_vertical_vel), (height*2)) <= quadraticPlus(GRAVITY, (2*u_vertical_vel), (height*2))):
        return quadraticPlus(GRAVITY, (2*u_vertical_vel), (height*2))
    
    elif (quadraticMinus(GRAVITY, (2*u_vertical_vel), (height*2)) >= quadraticPlus(GRAVITY, (2*u_vertical_vel), (height*2))):
        return quadraticMinus(GRAVITY, (2*u_vertical_vel), (height*2))

v_horizontal_vel = u_horizontal_vel
v_vertical_vel = u_vertical_vel + (GRAVITY * findTime())

def getDistanceH():
    return u_horizontal_vel * findTime()

def getDistanceTotal():
    return math.sqrt(height**2 + getDistanceH()**2)

def getFinalVelocity():    
    return math.sqrt(v_horizontal_vel**2 + v_vertical_vel**2)

def findAngleItHitsGround():
    return abs(math.degrees(math.atan(v_vertical_vel/v_horizontal_vel)))

print("\ntime in the air:", findTime(), "seconds\n")
print("resultant velocity as it hits the ground:", getFinalVelocity(), "m/s\n")
print("angle it hits the ground:", findAngleItHitsGround(), "degrees\n")
print("horizontal distance travelled:", getDistanceH(), "m\n")
print("total displacement from start point:", getDistanceTotal(), "m\n")
