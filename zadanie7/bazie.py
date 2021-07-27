import matplotlib.pyplot as plt
import numpy as np

def krzywa_Bezier(points,width):
    npoints = len(points);    
    xpoints = np.array([p[0] for p in (npoints)]);
    ypoints = np.array([p[0] for p in (npoints)]);
    
    x=0;
    y=1;
    plt.plot(x, y, 'o')

    plt.legend(['wezly', 'najblizszy'], loc='best')
    plt.show()
    return True;


nPoints = 3
points = np.random.rand(nPoints,2)*200
krzywa_Bezier(points, 3);