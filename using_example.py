import numpy as np

from DecisionHelper import DecisionHelper

if __name__ == '__main__':
    m = np.array([[0.9, 0.93, 0.91, 0.88, 0.51, 0.72, 0.88],
                  [0.5, 0.79, 0.67, 0.68, 0.9, 0.87, 0.82],
                  [0.3, 0.86, 0.81, 0.73, 0.82, 0.7, 0.76],
                  [1.0, 0.6, 0.7, 0.65, 0.72, 0.65, 0.51],
                  [1.0, 0.55, 0.69, 0.65, 0.68, 0.69, 0.55]])
    wei = [0.1, 0.1, 0.1, 0.2, 0.3, 0.1, 0.1]

    dh = DecisionHelper(m, wei)
    print(dh.saw())
    print(dh.topsis())
    print(dh.electre())
