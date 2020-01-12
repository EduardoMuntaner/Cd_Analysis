#python script for calculating drag coeff of a rocket with aspect ratio L/D
#, at height h and Mach number M. Zero-lift is assumed

#speed of sound
global v_s = 343.0
global l = 1 # length (of the body(?))
global d = 1 # reference diameter
global A_r = l/d
rho = 1 #figure out a better way than to just add a bunch of functions 

# Because of complicated aerodynamics, the calculation must be split by
# body sections; nose, body and base. Three functions are needed, one 
# for each part.

# the major contributor of drag on the nose and base is due to wave shock/
# major pressure differences caused by Mach speeds

def Cd_nose(A_r, M):
    return 3.6/((A_r)*(M-1) +3)
    

def Cd_base(coast, M):
    if coast:
        return 0.25/M
    else:
        return 0.25/(M*(1- A_e/S_r)
    return
    

# the drag from the body is mostly due to friction, not wave shock
# (it is still a weak function in M)
def Cd_body(A_r, M, l, h):
    return 0.053*(A_r)*((M/(q*l))**(0.2)


# dynamic pressure as a function of height h and Mach number M
def q(h, M):
    return rho*M*v_s**2/2






