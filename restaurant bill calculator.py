#!/usr/bin/env python
# coding: utf-8

# In[7]:


t = input("How much was the total bill?")
t = int(t)
p = input("How much of a tip do you want to give as a decimal?")
p = float(p)
n = input("How many people are there to split the bill and tip?")
n = int(n)
def calculator(t, p, n):
    tip = t * p 
    ti = round(tip, 2)
    am = ti + t
    a = round(am, 2)
    tpp = ti / n
    tp = round(tpp, 2)
    app = a / n
    ap = round(app, 2)
    z = ("The total tip is ${}.")
    print(z.format(ti))
    y = ("The total amount is ${}.")
    print(y.format(a))
    x = ("The tip amount per person is ${}.")
    print(x.format(tp))
    w = ("The total amount per person is ${}.")
    print(w.format(ap))
calculator (t, p, n)

