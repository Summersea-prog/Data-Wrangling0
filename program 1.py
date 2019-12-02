import pandas as pd
a={'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'Math' :[80,95,79]}
a1=pd.DataFrame(a,columns=['Student','Math'])
b={'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'Electronics' :[85,81,83]}
b1=pd.DataFrame(b,columns=['Student','Electronics'])
c={'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'GEAS' :[90,79,93]}
c1=pd.DataFrame(c,columns=['Student','GEAS'])
d={'Student' : ['Ice Bear' , 'Panda' , 'Grizzly'], 'ESAT' :[93,89,88]}
d1=pd.DataFrame(d,columns=['Student','ESAT'])
e=pd.merge(a1,b1, how = 'right', on ='Student')
e1=pd.merge(e,c1, how = 'right', on ='Student')
f=pd.merge(e1,d1, how = 'right', on ='Student')
boom=pd.melt(f,id_vars= 'Student', value_vars = ['Math' ,'Electronics', 'GEAS' , 'ESAT'])
boom1=boom.rename(columns = {'variable':'Subject', 'value':'Grades'})
boom2=boom1.sort_values('Student')
boom3=boom2.reset_index()
boomboom=boom3.drop(columns='index')