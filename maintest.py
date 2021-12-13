from math import pi, sin
from sys import stdin

config = list()

for line in stdin:
    config.append(line)
#print (type(config))
#print (config)

def sepstrno(list,a,b):
    return (list[a].split('=')[b].strip())


list_var=list()
list_Variable=list()

for i in range(len(config)):
 list_var[i]= str (sepstrno(config,i,0)).lower()

for i in range(len(config)):
 if ( sepstrno(config,i,0).lower()== list_var[i] ):
  list_Variable[i]=int(list_var[i])

else:
  print ('Expected : {}. Recieved : {}'.format(sepstrno(config,i,0)),format(sepstrno(config,i,0)))