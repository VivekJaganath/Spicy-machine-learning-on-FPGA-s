import numpy as np
import time
from typing import Dict

# Function to be translated (function under test)
def mmult(a:np.ndarray((2,2),'int32'),
          b:np.ndarray((2,2),'int32'),
          c:np.ndarray((2,2),'int32'),
          x: 'Dict[str, str]',
          size:'int32'):

    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            for k in range(b.shape[0]):
               c[i][j] += a[i][k] * b[k][j]


if __name__ == "__main__":
    #allocate arrays
    a = np.ndarray((2,2),'int32',np.array([[1,2],[3,4]],'int32'))
    b = np.ndarray((2,2),'int32',np.array([[5,6],[7,8]],'int32'))
    c = np.zeros((2,2),'int32')
    d = "abc"
    #execute function under test and time it
    t0 = time.time()
    mmult(a,b,c,d,2)
    t1 = time.time()
    #display elapsed time
    print('Elapsed time: %.2fus' % ((t1-t0)*1000000))

    #display results
    print('a =\n %s\n' % a)
    print('b =\n %s\n' % b)
    print('c =\n %s\n' % c)

