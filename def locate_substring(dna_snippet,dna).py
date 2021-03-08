#!/usr/bin/env python
# coding: utf-8

# In[1]:


def locate_substring(dna_snippet,dna):
        indexes = [i for i in range(len(dna_snippet)) if dna_snippet.startswith(dna, i)] 
        return indexes

print(locate_substring("GATATATGCATATACTT","ATAT"))


# In[ ]:




