import numpy as np
cimport numpy as cnp
cimport cython

def ccmp(int f, int s, int direct):
    if direct :
        return f >= s
    else:
        return f <= s

def cfind_extreme(cnp.ndarray arr, int arrlen , int exnum, int direct):
    cdef cnp.ndarray[cnp.int32_t, ndim=1] pos = np.zeros(20, dtype=np.intc)
    cdef int posi = 0
    cdef int skipi = -1
    for i in range(arrlen):
        if i <= skipi: continue
        if ccmp(arr[i],exnum,direct):
            pos[posi] = i
            posi +=1
            skipi = i
            while skipi < arrlen-1:
                if not ccmp(arr[skipi+1],exnum,direct):
                    pos[posi] = skipi
                    posi += 1
                    break;
                if skipi+1 == arrlen-1 and ccmp(arr[skipi+1],exnum,direct):
                    pos[posi] = skipi+1
                skipi += 1
    return pos

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

def cmp(f,s,direct):
    if direct == "large":
        return f >= s
    if direct == "small":
        return f <= s
def find_extreme(arr,exnum,direct):
    pos=[]
    skipi = -1
    for i,v in enumerate(arr):
        if i <= skipi: continue
        if cmp(v,exnum,direct):
            pos.append(i)
            skipi = i
            while skipi < arr.size-1:
                if not cmp(arr[skipi+1],exnum,direct):
                    pos.append(skipi)
                    break;
                if skipi+1 == arr.size-1 and cmp(arr[skipi+1],exnum,direct):
                    pos.append(skipi+1)
                skipi += 1
                
    return pos