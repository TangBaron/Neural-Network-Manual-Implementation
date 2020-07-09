
import numpy as np

#与门的实现
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7 #b表示的时阈值，这里我们将阈值表示成偏置
    tmp = np.sum(w*x)+b
    if tmp <=0:
        return 0
    else:
        return 1

#与非门的实现
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7 #b表示的时阈值，这里我们将阈值表示成偏置
    tmp = np.sum(w*x)+b
    if tmp <=0:
        return 0
    else:
        return 1

#或门的实现
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2 #b表示的时阈值，这里我们将阈值表示成偏置
    tmp = np.sum(w*x)+b
    if tmp <=0:
        return 0
    else:
        return 1
