#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("student_scores.csv")
df


# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.sample()


# In[7]:


df.describe()


# In[8]:


df.isnull().sum()


# # Drop unnamed column

# In[9]:


df = df.drop("Unnamed: 0", axis = 1)
df.head()


# # Change weekly study hours column

# In[10]:


df["WklyStudyHours"] = df["WklyStudyHours"].str.replace("05-Oct","5-10")
df.head()


# # Gender Distribution

# In[11]:


plt.figure(figsize = (4,3))
sns.countplot(data = df,x="Gender")

plt.show()


# In[12]:


plt.figure(figsize = (5,5))
ax = sns.countplot(data = df,x="Gender")
ax.bar_label(ax.containers[0])

plt.title("Gender Distribution")
plt.show()


# #from the about chart we have analysed that:
# 
# 
# #the number of females in the data is more than the number of males

# In[13]:


gb = df.groupby("ParentEduc").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
gb


# In[14]:


sns.heatmap(gb)

plt.show()


# In[15]:


plt.figure(figsize = (5,5))
sns.heatmap(gb,annot = True)


plt.title("Relationship between Parent's Education and Student's Score")
plt.show()


# #from the above chart we have concluded that the education of the parents have a good impact on their scores

# In[16]:


gb1 = df.groupby("ParentMaritalStatus").agg({"MathScore":'mean',"ReadingScore":'mean',"WritingScore":'mean'})
gb1


# In[17]:


plt.figure(figsize = (5,5))
sns.heatmap(gb1,annot = True)

plt.show()


# #from the above chart we have concluded that there is no/negligible impact on the 
# 
# #student's score due to their parent's marital status 

# In[18]:


sns.boxplot(data = df,x = "MathScore")

plt.show()


# In[19]:


sns.boxplot(data = df,x = "ReadingScore")

plt.show()


# In[20]:


sns.boxplot(data = df,x = "WritingScore")

plt.show()


# In[21]:


print(df["EthnicGroup"].unique())


# # Distribution of Ethinic Groups

# In[22]:


groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupA


# In[23]:


groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupB


# In[24]:


groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupC


# In[25]:


groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupD


# In[26]:


groupE = df.loc[(df['EthnicGroup'] == "group E")].count()
groupE


# In[27]:


#2nd Method
groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()
print(groupA["EthnicGroup"])

#mlist = [groupA["EthnicGroup"]]
#plt.pie([])

plt.show()


# In[28]:


#2nd Method
groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist)

plt.show()


# In[29]:


#2nd Method
groupA = df.loc[(df['EthnicGroup'] == "group A")].count()
groupB = df.loc[(df['EthnicGroup'] == "group B")].count()
groupC = df.loc[(df['EthnicGroup'] == "group C")].count()
groupD = df.loc[(df['EthnicGroup'] == "group D")].count()
groupE = df.loc[(df['EthnicGroup'] == "group E")].count()

l = ["group A","group B","group C","group D","groud E"]
mlist = [groupA["EthnicGroup"],groupB["EthnicGroup"],groupC["EthnicGroup"],groupD["EthnicGroup"],groupE["EthnicGroup"]]
plt.pie(mlist,labels = l, autopct = "%1.2f%%")

plt.title("Distribution of Ethnic Groups")

plt.show()


# In[30]:


ax = sns.countplot(data = df,x = "EthnicGroup")

ax.bar_label(ax.containers[0])


# In[31]:


print(mlist)


# # ThankYou!
