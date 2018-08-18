
# coding: utf-8

# In[1]:


def zero_exception():
    try:
        x=5
        y=0
        print(x/y)
    except ZeroDivisionError:
        print("Error: Dividing by Zero!")
zero_exception()


# In[4]:


subjects = ['Americans','Indians']
verbs = ['play','watch']
objects = ['Baseball','Cricket']
a = [' '.join([i,j,k]) for i in subjects for j in verbs for k in objects]
for l in a:
    print(l)

