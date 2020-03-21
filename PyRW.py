#!/usr/bin/env python
# coding: utf-8

# ### LABORATORIO DE COMPORTAMIENTO SOCIAL E INTELIGENCIA ARTIFICIAL
# Laurent Avila Chauvet / Marzo 2020

# #### Rescorla–Wagner model
# ΔV= αβ(λ-Vtot)   /   VTot = sum(ΣΔV)

# In[1]:


#library
import matplotlib.pyplot as plt

#Acquisition
Trials = 15
V = 0                                        #V
A = 0.5                                      #α
B = 0.5                                      #β
L = 1                                        #λ

VData = [0 for i in range(Trials)]
Data = [0 for i in range(Trials)]

for i in range(Trials):
    Data[i] = V + sum(VData)                     #VTot = sum(ΣΔV)
    VData[i] = (A*B)*(L-Data[i])          #ΔV= αβ(λ-Vtot) 
  
plt.figure()    
plt.plot(Data, 'k-o')
plt.axis([-.5, len(Data)-.5, 0, 1])


# In[2]:


#library
import matplotlib.pyplot as plt

##Extinction
Trials = 15
V = 1                                        #V
A = 0.5                                      #α
B = 0.5                                      #β
L = 0                                        #λ

VData = [0 for i in range(Trials)]
Data = [0 for i in range(Trials)]

for i in range(Trials):
    Data[i] = V + sum(VData)                     #VTot = sum(ΣΔV)
    VData[i] = (A*B)*(L-Data[i])          #ΔV= αβ(λ-Vtot) 
    
plt.figure()    
plt.plot(Data, 'k-o')
plt.axis([-.5, len(Data)-.5, 0, 1])

