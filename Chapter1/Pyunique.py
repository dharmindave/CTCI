#!/usr/bin/env python
# coding: utf-8

# In[2]:


def unique(str):
    if len(str)>256:
        return False
    else :
        dict={}
        for s in str:
            if (s in dict.keys())== False: 
                dict[s]="right value "
            else :
                return False 
    return True
str= input("enter the string ")
print(unique(str))
    


# In[ ]:




