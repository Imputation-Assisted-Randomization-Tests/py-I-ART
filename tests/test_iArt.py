import numpy as np
import iArt

def test_iArt():
    Z = [1, 1, 1, 1, 0, 0, 0, 0]
    X = [[5.1, 3.5], [4.9, np.nan], [4.7, 3.2], [4.5, np.nan], [7.2, 2.3], [8.6, 3.1], [6.0, 3.6], [8.4, 3.9]]
    Y = [[4.4, 0.5], [4.3, 0.7], [4.1, np.nan], [5.0, 0.4], [1.7, 0.1], [np.nan, 0.2], [1.4, np.nan], [1.7, 0.4]]
    result = iArt.test(Z=Z,X=X,Y=Y,L=1000,random_state=1)
    assert result == (True, [0.013, 0.057])

