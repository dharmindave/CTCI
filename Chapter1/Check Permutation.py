#!/usr/bin/env python
# coding: utf-8

# In[14]:



def checkpermutation(str1,str2):
    str1=str1.replace(" ","")
    str2=str2.replace(" ","")
        
    if (len(str1)!=len(str2)):
        return False
    for i in str1:
        if i in str2:
            str2=str2.replace(i,"")
            print("succesful")
    return len(str2)==0
str1="dharmin"
str2="dharmni"
print(checkpermutation(str1,str2))


# In[ ]:





# In[ ]:




