# Import libraries
import numpy as np
import matplotlib.pyplot as plt
 
# return the minimum of two opposing forces
def literature_def(Fa,Fb,Fg):
    if np.sign(Fa) != np.sign(Fb):
        Fi = min(abs(Fa),abs(Fb))
    else:
        Fi = 0
    return Fi
################# Calculate all situations around a circle by moving the frame of reference #################
# In this case I will rotate the frame of reference by rotating both vectors together
# Function to rotate a point (x, y) by angle theta

def rotate_point(x, y, theta):
    cos_theta = np.cos(theta)
    sin_theta = np.sin(theta)
    new_x = x * cos_theta - y * sin_theta
    new_y = x * sin_theta + y * cos_theta
    return new_x, new_y

v1 = [0,0,np.sqrt(.5),np.sqrt(.5)]
x_pos_v1 =    v1[0]
y_pos_v1 =    v1[1]
x_direct_v1 = v1[2]
y_direct_v1 = v1[3]

v2 = [0,0,1,0]
x_pos_v2 =    v2[0]
y_pos_v2 =    v2[1]
x_direct_v2 = v2[2]
y_direct_v2 = v2[3]

Fi_y = [0,0,0,0]
Fi_x = [0,0,0,0]
Fi_mag = 0
fi_x_array = []
fi_y_array = []
fi_mag_array = []
v1_x_array = []
v1_y_array = []
v2_x_array = []
v2_y_array = []

# Generate points on a circle
resolution = 1000 # Resolution of the circle
theta = np.linspace(0, 2*np.pi, resolution, endpoint=False)  # Angle values

# loop over points on the circle
for i in range(resolution):
    x1, y1 = rotate_point(v1[2],v1[3],theta[i])
    x2, y2 = rotate_point(v2[2],v2[3],theta[i])
    fi_x = literature_def(x1, x2 ,0)
    fi_y = literature_def(y1, y2 ,0)
    Fi_mag = np.sqrt(fi_x**2 + fi_y**2) 
    # store components an array for plotting later
    v1_x_array.append(x1)
    v1_y_array.append(y1)
    v2_x_array.append(x2)
    v2_y_array.append(y2)
    fi_x_array.append(fi_x)
    fi_y_array.append(fi_y)
    fi_mag_array.append(Fi_mag)
        
# # plot the points of fi_x_array, fi_y_array, and fi_mag_array by index
plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_mag_array), color = 'black')
plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_x_array), color = 'r')
plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_y_array), color = 'g')
plt.legend(['Fi_mag', 'Fi_x', 'Fi_y'])
plt.show

# # # Circle plot
fig, ax = plt.subplots(figsize = (7, 7))
ax.quiver(np.zeros(len(v1_x_array)), np.zeros(len(v1_y_array)), v1_x_array, v1_y_array, scale = 3)
ax.quiver(np.zeros(len(v2_x_array)), np.zeros(len(v2_y_array)), v2_x_array, v2_y_array, scale = 3)
ax.quiver(x_pos_v1, y_pos_v1, x_direct_v1, y_direct_v1, scale = 3, color = 'b')
ax.quiver(x_pos_v1, y_pos_v2, x_direct_v2, y_direct_v2, scale = 3, color = 'b')
ax.axis([-1.5, 1.5, -1.5, 1.5])
# ax.quiver(x_pos_fiy, y_pos_fiy, x_direct_fiy, y_direct_fiy, scale = 5, color = 'g')
plt.show




################## Calculate all situations around a circle by moving the follower force #################

# v1 = [0,0,np.sqrt(.5),np.sqrt(.5)]
# x_pos_v1 =    v1[0]
# y_pos_v1 =    v1[1]
# x_direct_v1 = v1[2]
# y_direct_v1 = v1[3]

# v2 = [0,0,0,0]
# Fi_y = [0,0,0,0]
# Fi_x = [0,0,0,0]
# Fi_mag = 0
# fi_x_array = []
# fi_y_array = []
# fi_mag_array = []
# x_array = []
# y_array = []

# # Generate points on a circle
# resolution = 100  # Resolution of the circle
# theta = np.linspace(0, 2*np.pi, resolution)  # Angle values
# radius = 1.0  # Radius of the circle

# # loop over points on the circle
# for i in range(resolution):
#     v2_x = radius * np.cos(theta[i])
#     v2_y = radius * np.sin(theta[i])
#     fi_x = literature_def(v1[2],v2_x,0)
#     fi_y = literature_def(v1[3],v2_y,0)
#     Fi_mag = np.sqrt(fi_x**2 + fi_y**2) 
#     # store components an array for plotting later
#     x_array.append(v2_x)
#     y_array.append(v2_y)
#     fi_x_array.append(fi_x)
#     fi_y_array.append(fi_y)
#     fi_mag_array.append(Fi_mag)
        
# # plot the points of fi_x_array, fi_y_array, and fi_mag_array by index
# plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_mag_array), color = 'black')
# plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_x_array), color = 'r')
# plt.scatter(np.array(np.rad2deg(theta)), np.array(fi_y_array), color = 'g')
# plt.legend(['Fi_mag', 'Fi_x', 'Fi_y'])
# plt.show

# # # Circle plot
# fig, ax = plt.subplots(figsize = (7, 7))
# ax.quiver(np.zeros(len(x_array)), np.zeros(len(y_array)), x_array, y_array, scale = 3)
# ax.quiver(x_pos_v1, y_pos_v1, x_direct_v1, y_direct_v1, scale = 3, color = 'b')
# ax.axis([-1.5, 1.5, -1.5, 1.5])

################# calculate one off situations ################# 

# v1 = [0,0,1,1]
# v2 = [0,0,-1.3,-.7]
# Fi_y = [0,0,0,0]
# Fi_x = [0,0,0,0]
# Fi_mag = 0

# # calculate the three componets of interaction force 
# Fi_x[2] = literature_def(v1[2],v2[2],0)
# Fi_y[3] = literature_def(v1[3],v2[3],0)
# Fi_mag = np.sqrt(Fi_x[2]**2 + Fi_y[3]**2) 

# # seperate vectors into four arrays where each array coresponds to the index of the vector
# x_pos =     [v1[0],v2[0]]
# y_pos =     [v1[1],v2[1]]
# x_direct =  [v1[2],v2[2]]
# y_direct =  [v1[3],v2[3]]

# x_pos_fix =     [Fi_x[0]]
# y_pos_fix =     [Fi_x[1]]
# x_direct_fix =  [Fi_x[2]]
# y_direct_fix =  [Fi_x[3]]

# x_pos_fiy =     [Fi_y[0]]
# y_pos_fiy =     [Fi_y[1]]
# x_direct_fiy =  [Fi_y[2]]
# y_direct_fiy =  [Fi_y[3]]
    
 

 
# # Creating plot
# fig, ax = plt.subplots(figsize = (12, 12))
# ax.quiver(x_pos_fix, y_pos_fix, x_direct_fix, y_direct_fix, scale = 5, color = 'r')
# ax.quiver(x_pos_fiy, y_pos_fiy, x_direct_fiy, y_direct_fiy, scale = 5, color = 'g')
# ax.quiver(x_pos, y_pos, x_direct, y_direct, scale = 5)
 
# ax.axis([-1.5, 1.5, -1.5, 1.5])
 
# # show plot
# plt.show()