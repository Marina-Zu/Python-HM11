#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = 2 * x ** 3 + 2 * x ** 2 - 18 * x - 18
f


# In[2]:


solveset (f, x, Reals).evalf(2)


# In[3]:


lst = [-oo, oo]
lst[1:1] = solveset(diff(f), x, Reals).evalf(2)
lst


# In[4]:


# Промежутки возрастания и убывания
inc = []
red = []
for i in range(1, len(lst)):
    temp = is_increasing(f, Interval.open(lst[i-1], lst[i]))
    if temp:
        inc.append(f"{lst[i-1]},{lst[i]}")
    else:
        red.append(f"{lst[i-1]},{lst[i]}")
print("Возрастает на интервале: ", *inc, sep = "\n")
print("Убывает на интервале: ", *red, sep = "\n")


# In[5]:


# Нарисовать график
plot(f, (x, -4, 4), legend = True)


# In[6]:


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


# In[7]:


# Промежутки знакопостоянства функции

print("Меньше нуля на интервале: ", sep = "\n")
solveset(f < 0, x, Reals).evalf(2)


# In[8]:


print("Больше нуля на интервале: ", end = '')
solveset(f > 0, x, Reals).evalf(2)


# In[ ]:




