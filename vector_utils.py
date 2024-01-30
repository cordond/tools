import numpy as np
import matplotlib.pyplot as plt

def cartesian_to_polar(x, y):
    r = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return np.array([r, phi])

def polar_to_cartesian(r, phi):
    x = r * np.cos(phi)
    y = r * np.sin(phi)
    return np.array([x, y])

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    norm = np.linalg.norm(vector)
    if norm == 0:
        return vector
    else:
        return vector / norm

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::
            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))

def plot_vectors(vectors, colors):
    origin = np.array([[np.zeros(len(vectors[:,0]))],[np.zeros(len(vectors[:,0]))]]) # origin point
    plt.quiver(*origin, vectors[:,0], vectors[:,1], color=colors, angles = 'xy', scale_units = 'xy', scale = 1)
    # Set plot limits
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.show()

def get_magnitude(vector, fast=False):
    '''
    Calculate the magnitude of a vector
    '''
    if fast:
        magnitude = np.sqrt(vector.dot(vector))
    else:
        magnitude = np.linalg.norm(vector)
    return magnitude

def get_parallel_component(vector_A, vector_B):
    '''
    Calculate the parallel component of vector_A onto vector_B
    '''
    parallel_component = np.dot(vector_A, vector_B) / np.linalg.norm(vector_B)**2 * vector_B
    return parallel_component

def get_perpendicular_component(vector_A, vector_B):
    '''
    Calculate the perpendicular component of vector_A onto vector_B
    '''
    parallel_component = get_parallel_component(vector_A, vector_B)
    perpendicular_component = vector_A - parallel_component
    return perpendicular_component

def get_bisector(vector_A, vector_B):
    '''
    Calculate the bisector of two vectors
    https://proofwiki.org/wiki/Angle_Bisector_Vector
    '''
    bisector = get_magnitude(vector_A)*vector_B + get_magnitude(vector_B)*vector_A
    return bisector

def is_vector_endpoint_above_vector_slope(vectorA, vectorB):
    '''
    Check if the endpoint of vectorA is above the slope of vectorB
    '''
    Ax = vectorA[0]
    Ay = vectorA[1]
    Bx = vectorB[0]
    By = vectorB[1]

    B_slope = By / Bx

    # calculate the y value of vectorB at the x value of vectorA
    By_at_Ax = B_slope * Ax
    
    # if the y value of vectorA is above the y value of vectorB at the x value of vectorA, then vectorA is above vectorB
    if Ay > By_at_Ax:
        return True
    else:
        return False


