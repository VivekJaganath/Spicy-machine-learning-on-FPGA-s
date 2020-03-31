import time
import numpy as np
from typing import Dict
import code


# Function to be translated (function under test)
def mmult(a: np.ndarray((32, 32), 'int32'),
          b: np.ndarray((32, 32), 'int32'),
          c: np.ndarray((32, 32), 'int32'),
          #declaration
          d: Dict['float', 'float']):
    # Function interface pragmas
    '''
    #pragma SDS data access_pattern(a:SEQUENTIAL, b:SEQUENTIAL, c:SEQUENTIAL)
    #pragma SDS data mem_attribute(a:PHYSICAL_CONTIGUOUS, b:PHYSICAL_CONTIGUOUS, c:PHYSICAL_CONTIGUOUS)
    #pragma SDS data data_mover(a:AXIDMA_SIMPLE, b:AXIDMA_SIMPLE, c:AXIDMA_SIMPLE)
    '''
    # internal partitioned arrays
    A_tmp = np.ndarray((32, 32), 'int32')
    B_tmp = np.ndarray((32, 32), 'int32')
    c_tmp = Dict['str', 'str']
    v_tmp = Dict ['float', 'float']
    v_tmp = {1:1, 3:5, 4:7}
    '''
    #pragma HLS array_partition variable=A_tmp cyclic factor=16 dim=1
    #pragma HLS array_partition variable=B_tmp block factor=16 dim=1
    '''
    # Copy loops
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            '''
            #pragma HLS PIPELINE
            '''
            A_tmp[i][j] = a[i][j]
            B_tmp[i][j] = b[i][j]
            #value assignment
            c_tmp = d
    # Compute loops
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            '''
            #pragma HLS PIPELINE
            '''
            result: 'int32' = 0
            for k in range(b.shape[0]):
                result += A_tmp[i][k] * B_tmp[k][j]
            c[i][j] = result


if __name__ == "__main__":
    # allocate arrays
    a = np.ndarray((32, 32), dtype='int32', buffer=np.linspace(1, 1024, 1024, dtype='int32').reshape(32, 32))
    b = np.ndarray((32, 32), dtype='int32', buffer=np.linspace(1, 1024, 1024, dtype='int32').reshape(32, 32))
    c = np.ndarray((32, 32), dtype='int32', buffer=np.zeros((32, 32), dtype='int32'))

    # execute function under test and time it
    t1 = time.time()
    mmult(a, b, c)
    t2 = time.time()
    elapsed = str((t2 - t1) * 1000000)
    # display elapsed time
    print("@time: " + elapsed + " us")

    # display results
    print('a = %s\n' % a)
    print('b = %s\n' % b)
    print('c = %s\n' % c)