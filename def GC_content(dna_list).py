#!/usr/bin/env python
# coding: utf-8

# In[9]:


def GC_content(dna_list):
    count_GC=[]
    for i in range(len(dna_list)):
        dna_str=dna_list[i]
        count_GC.append(dna_str.count('G')+dna_str.count('C'))
    maxGC_num=max(count_GC)
    maxGC_index=count_GC.index(maxGC_num)
    perc_GC=((maxGC_num)/(len(dna_list[maxGC_index])))*100
    return(maxGC_index,perc_GC)
GC_content(["CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG","CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC","CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




