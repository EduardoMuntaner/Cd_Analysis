#python script for calculating drag coeff of a rocket, at height h and Mach 
# number M. Zero-lift is assumed. atmospheric pkg used is only correct to 
# 86 km, approximate thereafter.

import numpy as np
import matplotlib.pyplot as plt
import 

# Rocket Measurements (length, aspect ratio, etc.)
global LBod = 1 # length of the body (m)
global LNos = 1 # length of the nose (m)
global D = 1 # reference diameter (m)
global AR_B = LBod/D # Aspect ratio of the body
global AR_N = LNos/D # Aspect ratio of the nose
global S_r = np.pi*(D/2)**2 # reference area using reference diameter (m^2)
global A_e = 0.1 # Area of exhaust


# flight parameters (height values, Mach values, etc)
global coast = false
global max_h = 100000 # max height (m)
global N = 10 # number of heights at which to calculate Cd
global height = np.linspace(0, max_h, N) # array of heights
global NM = 100 # number of points for Mach Nums
global M_min = 1 # min Mach Num
global M_max = 6 # max Mach Num
global Mach_Num = np.linspace(M_min, M_max, NM) # array of Mach Nums



# Because of complicated aerodynamics, the calculation must be split by body 
# sections; nose, body and base. Three functions are needed, one for each part.

# the major contributor of drag on the nose and base is due to wave shock/
# major pressure differences caused by Mach speeds


"""
#Cd_nose: Calculates the Cd at the nose
~~~~~~~~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~
AR_N: Aspect ratio of the nose (length/diameter)
M: Mach number
#~~~~~~~~~~~~~~~~~~~~OUTPUTS~~~~~~~~~~~~~~~~~~~~~
Cd for the nose
"""
def Cd_nose(AR_N, M):
    return 3.6/((AR_N)*(M-1) +3)
    


######################################################
#Cd_base: Calculates the Cd at the nose              #
#~~~~~~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~     #
#coast: boolean; false during thrust, true otherwise #
#M: Mach number of the rocket                        #
#~~~~~~~~~~~~~~~~~~~~OUTPUTS~~~~~~~~~~~~~~~~~~~~~    #
#Cd for the base                                     #
def Cd_base(coast, M, A_e, S_r):
    if coast:
        return 0.25/M
    else:
        return (0.25/M)*(1- A_e/S_r)
    return




# the drag from the body is mostly due to friction, not wave shock
# (it is still a weak function in M)
####################################################
#Cd_body: Calculates the Cd on the body            #
#~~~~~~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~   #
#AR_N: Aspect ratio of the body (length/diameter)  #
#M: Mach number of the rocket                      #
#~~~~~~~~~~~~~~~~~~~~OUTPUTS~~~~~~~~~~~~~~~~~~~~~  #
#Cd for the body                                   # 
def Cd_body(AR_B, M, LBod, h):
    return 0.053*(AR_B)*(M/(q(h,M)*l))**(0.2)



#################################################################
#1: Calculates the dynamic pressure on the rocket at the nose   #
#~~~~~~~~~~~~~~~~~~~~INPUTS~~~~~~~~~~~~~~~~~~~~~~               #
#h: height of the rocket in meters                              #
#M: Mach number of the rocket                                   #
#~~~~~~~~~~~~~~~~~~~~OUTPUTS~~~~~~~~~~~~~~~~~~~~~               #
#returns the dynamic pressure                                   #


# dynamic pressure as a function of height h and Mach number M
def q(h, M):
    return pkg.Environment.density(h)*M*pkg.Environment.local_speed_of_sound(h)**2/2




for h in height:
    Cd = np.zeros(NM)
    Cd = Cd_nose(AR_N, M) + Cd_body(AR_B, M, LBod, h) + Cd_base(coast, M, A_e, S_r)
    plt.plot(Cd, M)
    
    plt.savefig("$C_D$ for height %f meters" % (h))
    
    
