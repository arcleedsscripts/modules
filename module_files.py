
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
            
            


# In[33]:

import sqlite3


# In[35]:

filename = 'mods.sqlite'
conn = sqlite3.connect(filename)
c = conn.cursor()


# In[40]:

c.execute("INSERT OR IGNORE INTO service(servicename) VALUES ('arc1')")


# In[41]:

conn.commit()
conn.close()


# In[57]:

filename = "mods.txt"
servicename = 'arc1'

dbfilename = 'mods.sqlite'
conn = sqlite3.connect(dbfilename)
c = conn.cursor()

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
                module.insert (0, servicename)
                    
                print (module)
                modulename = module[2]
                module_type = module[1]
                print (module_type)
                
                try:
                    moduleversion = module[3]
                except IndexError:
                    moduleversion = ''
                
                c.execute("INSERT OR IGNORE INTO service(servicename) VALUES ('" + servicename + "')")
                sql = "INSERT OR IGNORE INTO module(module,module_type) VALUES ('" + modulename + "' , '" + module_type + "')"
                print (sql)
                c.execute(sql)
                #c.execute("INSERT OR IGNORE INTO module_service(servicename, module, version)" .\
                #          "VALUES ('" + servicename + "' , '" + modulename + "' , '" + moduleversion + "')") 
                sql = "INSERT OR IGNORE INTO module_service(servicename, module, version) VALUES ('" + servicename + "' , '" + modulename + "' , '" + moduleversion + "')"
                print (sql)
                c.execute(sql)
                
                
conn.commit()
conn.close()
            


# In[ ]:

dbfilename = 'mods.sqlite'
conn = sqlite3.connect(dbfilename)
c = conn.cursor()

sql = "SELECT module.module, module_service.version FROM module, module_service WHERE module_servicename = 'arc1' AND module.module_type= 'applications'"

