
# coding: utf-8

# In[30]:

filename = "mods.txt"

with open(filename, 'r') as infile:
    for line in infile:
        if line.startswith('------'):
            line = line.strip('-').strip().rstrip('-').rstrip()
            #print (line)
            module_type = line.rsplit('/',1)[1]
            
            #print (module_type)
        else:
            line = line.split()
            for count in range (0, len(line)):
                module = line[count].split('/')         
                module.insert (0, module_type)
                    
                print (module)
            
            


# In[32]:

filename = "mods.txt"

with open(filename, 'r') as infile:
    for line in infile:
        if line.startswith('------'):
            line = line.strip('-').strip().rstrip('-').rstrip()
            #print (line)
            module_type = line.rsplit('/',1)[1]
            
            #print (module_type)
        elif module_type != 'privatemodules':
            line = line.split()
            for count in range (0, len(line)):
                module = line[count].split('/')         
                module.insert (0, module_type)
                    
                print (module)
            
            


# In[ ]:



