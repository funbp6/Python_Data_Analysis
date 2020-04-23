#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import argparse

start_time = time.time()

p = argparse.ArgumentParser()
p.add_argument('paf_file', help='paf file')
p.add_argument('-o', '--out', help='output file name')
args = p.parse_args()
input_paf = args.paf_file
output_file = args.out

print("start parsing")
ltotal=[]
fhit_hash={}
with open(input_paf,'r') as f:
    for line in f:
        llist=line.split()
        if  llist[0] not in fhit_hash:
            fhit_hash[llist[0]]=1
            split1=llist[5].split("-", 1)
            kindom=split1[0]
            split2=split1[1].split("_", 2)
            genus=split2[0]
            speices=split2[1]
            #print(type(llist[10]))
            ident=int(llist[10])/int(llist[1])
            read_cover=int(llist[9])/int(llist[10])
            tmpl=[llist[0], kindom, genus, speices, llist[10], round(read_cover,4), round(ident,4)]
            ltotal.append(tmpl)


with open(output_file,'w') as of:
    for item in ltotal:
        for i in item:
            of.write('%s ' % i)
        of.write('\n')




# AWK method

# awk -v pick_num=3 -v seed=$RANDOM 'BEGIN{newl=0;srand(seed);}
# !($1 in a){split($6,a,"-");split(a[2],b,"_");c[++newl]=$1" "b[1]" "$11/$2" "$10/$11;a[$1]}
# END{for(i=1;i<=pick_num;i++){ri=int(1+rand()*(newl));
#     if(ri in p){i--;continue;}p[ri];printf ri" "}print "";
#     for(i in p)print i,c[i]}' file_name


print("parsing done")
print("--- %s seconds ---" % (time.time() - start_time))


# In[ ]:




