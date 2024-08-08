import numpy as np
import numpy.linalg as nl
import math

class Spector:

    def __init__(self, intensities):

        self.intensities = intensities

    def getNorm(self):

        return nl.norm(self.intensities)
    
    def dotProduct(self, spector: Spector):

        return np.dot(self.intensities, spector.intensities)

    def normalized(self):

        return Spector(self.intensities/self.getNorm())
