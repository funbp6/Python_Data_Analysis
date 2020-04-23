from __future__ import print_function
import sys
import math
import argparse
import copy

def subset(rseq, sseq, rnum, snum):
    subset = []
    #build set
    for i in range(len(rseq)):
        #every point in sequence create one set
        newset = set()
        #try every possible combination
        for rcnt in range(rnum):
            for scnt in range(snum):
                 if rseq[i][rcnt] != sseq[i][scnt]:
                    #if the char is different in that point, add this to new set
                    newset.add((rcnt)*snum + scnt+1)                    
                    #print rcnt, scnt
        subset.append(newset)
        #print ("subset:",subset)       
    return subset


def set_cover(universe,subsets):
    elements = set(e for s in subsets for e in s)
    if elements != universe:
        return None
    covered = set()
    cover = []
    while covered != elements:
        subset = max(subsets, key = lambda s: len(s-covered))
        cover.append(subset)
        covered |= subset

    return cover

def print_greedy_setcover(greedy_round, universe, subsets, rtran):
    while greedy_round > 0:
        cover = set_cover(universe,subsets)
        gdict={}
        if cover != None:
            print ("FileAns:")
            for i in range(len(rtran)):
                for j in range(len(cover)):
                    if cover[j] == subsets[i]:
                        gdict[i]=len(cover[j])
                        print (' ',"position:",(i+1),"above num:",(len(cover[j])))
            print ("\n")
        else:#set cover doesn't exist
            print(cover)
        big=0
        bigv=0
        for key, value in gdict.items():
            if value>big:
                big=value
                bigv=key
        subsets[bigv]=set([])
        greedy_round -= 1


def main():
    greedy_round = args.first_n
    rn = args.resist_num
    sn = args.sensitive_num
    #print ("rn= ", rn, "sn= ",sn)
        
    rlist=[]
    slist=[]
    with open(args.file,'r') as fin:  
        for lnum,line in enumerate(fin):
            if lnum == 0:
                continue
            if lnum <= rn:
                rlist.append(line)
            if rn < lnum <= sn+rn:
                slist.append(line)

    rtran = map(list, zip(*rlist))          
    stran = map(list, zip(*slist))

    universe = set(range(1,rn*sn+1))
    subsets = subset(rtran, stran, rn, sn)
    # subsets[2966]=set([])
    # subsets[2967]=set([])
    # subsets[2968]=set([])
    # subsets[2969]=set([])
    # subsets[2970]=set([])
    # subsets[2971]=set([])
    # subsets[2972]=set([])
    print_greedy_setcover(greedy_round, universe, subsets, rtran)


if __name__ == '__main__':
    p = argparse.ArgumentParser()
    p.add_argument('-n', '--first_n', help="output first n terms", type=int, default=1)
    p.add_argument("resist_num", help="resistance bacterial number", type=int)
    p.add_argument("sensitive_num", help="sensitivity bacterial number", type=int)
    p.add_argument("file", help="file name")
    args = p.parse_args()
    print (p.parse_args())

    if not (args.resist_num and args.sensitive_num):
        print("wrong input: please input resistance and sensitivity bacterial number")
        sys.exit()
    
    main()



        


