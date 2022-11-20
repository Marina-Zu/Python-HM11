#!/usr/bin/env python
# coding: utf-8

# In[3]:


from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = (x ** 2 + 3) / (3 * (x + 1))
f


# In[4]:


solveset (f, x, Reals).evalf(2)


# In[7]:


lst = [-oo, oo]
lst[1:1] = solveset(diff(f), x, Reals).evalf(2)
lst


# In[8]:


inc = []
red = []
for i in range(1, len(lst)):
    temp = is_increasing(f, Interval.open(lst[i-1], lst[i]))
    if temp:
        inc.append(f"{lst[i-1]},{lst[i]}")
    else:
        red.append(f"{lst[i-1]},{lst[i]}")
print("Возрастает на интервалах: ", *inc)
print("Убывает на интервалах: ", *red)


# In[12]:


# Нарисовать график
#plot(f, (x, -4, 3), ylim = (-5, 5), legend = True)

# Склеить график
f_1 = plot(f, (x, -5, -1.1), show = False)
f_2 = plot(f, (x, -0.9, 5), show = False)
f_1.append(f_2[0])
f_1.show()


# In[13]:


#Вычислить вершины (экстремумы функции)

from random import uniform
f_diff = sorted(solveset(diff(f), x, Reals).evalf(2))
f_diff.insert(0, f_diff[0] - 1)
f_1 = diff(f)
ext_list = []

for i, val in enumerate(f_diff):
    ext_list.append(f_1.subs(x, uniform(val, f_diff[i] + 1)))
    if i != 0:
        if ext_list[i-1] < 0 < ext_list[i]:
            print(f"Точка минимума: {val}, {f.subs(x, val).evalf(2)}")
        elif ext_list[i-1] > 0 > ext_list[i]:
            print(f"Точка максимума: {val}, {f.subs(x, val).evalf(2)}")


# In[14]:


# Промежутки знакопостоянства функции

print("Меньше нуля на интервале: ", sep = "\n")
solveset(f < 0, x, Reals).evalf(2)


# In[15]:


print("Больше нуля на интервале: ", end = '')
solveset(f > 0, x, Reals).evalf(2)


# In[ ]:




