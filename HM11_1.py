#!/usr/bin/env python
# coding: utf-8

# In[2]:


from sympy import *
from sympy.plotting import plot

x = Symbol("x")
f = -18 * x ** 3 + 5 * x ** 2 + 10 * x - 30
f


# In[4]:


solveset (f, x, Reals).evalf(2)


# In[5]:


lst = [-oo, oo]
lst[1:1] = solveset(diff(f), x, Reals).evalf(2)
lst


# In[6]:


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


# In[8]:


# Нарисовать график
plot(f, (x, -1, 1), legend = True)


# In[17]:


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


# In[21]:


# Промежутки знакопостоянства функции

print("Меньше нуля на интервале: ", sep = "\n")
solveset(f < 0, x, Reals).evalf(2)


# In[22]:


print("Больше нуля на интервале: ", end = '')
solveset(f > 0, x, Reals).evalf(2)


# In[ ]:




