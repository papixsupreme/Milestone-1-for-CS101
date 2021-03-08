#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hamming_dist(dna1, dna2):
    count = 0 
    i = 0
    while(i < len(dna1)):
        if dna1[i] != dna2[i]:
            count += 1
        i += 1
    return count
a = 'GAGCCTACTAACGGGAT'
b = 'CATCGTAATGACGGCCT'        
print(hamming_dist(a,b))


# In[ ]:




