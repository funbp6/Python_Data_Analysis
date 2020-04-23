import numpy as np
cimport numpy as cnp
cimport cython

def ccmp(int f, int s, int direct):
    if direct :
        return f >= s
    else:
        return f <= s

def cpfind_extreme(cnp.ndarray arr, int arrlen , int exnum, int direct):
    pos=[]
    cdef int skipi = -1
    for i in range(arrlen):
        if i <= skipi: continue
        if ccmp(arr[i],exnum,direct):
            pos.append(i)
            skipi = i
            while skipi < arrlen-1:
                if not ccmp(arr[skipi+1],exnum,direct):
                    pos.append(skipi)
                    break;
                if skipi+1 == arrlen-1 and ccmp(arr[skipi+1],exnum,direct):
                    pos.append(skipi+1)
                skipi += 1
    return pos
