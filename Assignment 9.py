#!/usr/bin/env python
# coding: utf-8

# In[11]:


#string function diff noteboook
a="cat is"
b=" wet"
m=a+b
m


# In[37]:


#Capitilize
a="cat is"
b=" wet"
m=a.capitalize()
m


# In[43]:


#casefold
a="Cat Is"
b=" wet"
m=a.casefold()
m


# In[57]:


#center(width)
a="Cat Is"
b=" wet"
m=a.center(150)
m


# In[73]:


#count(sub)
a="Cat is IS is"
b=" wet"
m=a.count("is")
m


# In[79]:


#encode()
a="Cat Is"
b=" wet"
m=a.encode()
m


# In[81]:


type(m)


# In[83]:


#endswith(suffix)
a="Cat Is"
b=" wet"
m=a.endswith("s")
m


# In[85]:


#endswith(suffix)
a="Cat Is"
b=" wet"
m=a.endswith("m")
m


# In[95]:


#expandtabs(tabsize)
a="Cat Is"
b=" wet"
m=a.expandtabs()
m


# In[107]:


#find(sub)
a="Cat Is"
b=" wet"
m=a.find("S")
m


# In[111]:


#find(sub)
a="Cat Is"
b=" wet"
m=a.find("t")
m


# In[113]:


#index(sub)
a="Cat Is"
b=" wet"
m=a.index("s")
m


# In[123]:


#isalnum()
a="Cat1"
b=" wet"
m=a.isalnum()
m


# In[125]:


#isalnum()
a="Cat1 is1"
b=" wet"
m=a.isalnum()
m


# In[127]:


#isalpha()
a="Cat1 is1"
b=" wet"
m=a.isalnum()
m


# In[131]:


#isalpha()
a="Cat1 is"
b="wet"
m=b.isalnum()
m


# In[135]:


#isascii()
a="Cat1 is"
b="wet"
m=a.isascii()
m


# In[145]:


#isdecimal()
#It’s a string method that checks if all the characters in a string are decimal numbers — basically 0 to 9
a="Cat is"
b="wet"
c="123"
m=c.isdecimal()
m


# In[147]:


#isdecimal()
#It’s a string method that checks if all the characters in a string are decimal numbers — basically 0 to 9
a="Cat is"
b="wet"
c="123"
m=a.isdecimal()
m


# In[151]:


#isdigit()
a="Cat1 is"
b="wet"
m=a.isdigit()
m


# In[153]:


#isdigit()
a="12"
b="wet"
m=a.isdigit()
m


# In[155]:


#isnumeric()
a="Cat1 is"
b="wet"
m=a.isnumeric()
m


# In[159]:


#isnumeric()
a="1.2"
b="wet"
m=a.isnumeric()
m


# In[161]:


#isnumeric()
a="1"
b="wet"
m=a.isnumeric()
m


# In[163]:


#isidentifier()
a="1"
b="wet"
m=a.isidentifier()
m


# In[165]:


#isidentifier()
a="cat"
b="wet"
m=a.isidentifier()
m


# In[167]:


#isidentifier()
a="cat1"
b="wet"
m=a.isidentifier()
m


# In[169]:


#islower()
a="CAT1"
b="wet"
m=a.islower()
m


# In[173]:


#islower()
a="CAT1"
b="wet"
m=b.islower()
m


# In[175]:


#isprintable()
a="CAT1"
b="wet"
m=b.isprintable()
m


# In[177]:


#isprintable()
a="CAT122"
b="wet1123   "
m=b.isprintable()
m


# In[181]:


#isprintable()
a="CAT122"
b="\n\t"
m=b.isprintable()
m


# In[187]:


#isspace()
a="CAT122"
b="wet"
m=b.isspace()
m


# In[185]:


#isspace()
a="CAT122"
b="zet met"
m=b.isspace()
m


# In[189]:


#isspace()
a="CAT122"
b=" "
m=b.isspace()
m


# In[193]:


#istitle()
a="CAT122"
b=" "
m=b.istitle()
m


# In[195]:


#istitle()
a="CAT122"
b=" "
m=a.istitle()
m


# In[199]:


#istitle() Checks for titlecase (first letter capital)
a="Cat"
b=" "
m=a.istitle()
m


# In[201]:


#isupper()
a="Cat"
b=" "
m=a.isupper()
m


# In[203]:


#isupper()
a="CAT"
b=" "
m=a.isupper()
m


# In[209]:


#join(iterable)
a="CAT"
b="WHAT"
m=a.join(b)
m


# In[215]:


#join(iterable)
a="CAT"
b=["hi","bye","hello"," "]
m=a.join(b)
m


# In[217]:


#join(iterable)
a="CAT"
b=["hi","bye","hello"]
m=a.join(b)
m


# In[223]:


#ljust(width)
a="CAT"
b=" "
m=a.ljust(10)
m


# In[ ]:


#ljust(width)
a="CAT"
b=" "
m=a.ljust(10)
m


# In[21]:


def quiz(questions):
    score=0
    for i in questions:
        print(i["PROMPT"])
        for option in i["options"]:
            print(option)
        answer=input("enter your answer(A,B,C,D)").upper()
        if (answer==i["answer"]):
                print("correct \n")
                score=score+1
        else:
                print("wrong")
questions=[{"PROMPT":"National Bird of India","options":["A.Parrot" , "B.kingfisher" , "C.Peacock" ,"D.Sparrow" ],"answer":"C"},
           {"PROMPT":"National Flower of India","options":["A.Rose","B.Lotus","C.Lily","D.Marigold"],"answer":"B"}]
quiz(questions)


# In[ ]:




