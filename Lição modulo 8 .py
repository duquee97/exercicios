#!/usr/bin/env python
# coding: utf-8

# In[18]:


import sqlite3
rh = sqlite3.connect('lição.db')
rh.execute("""CREATE TABLE Funcionarios (
cod_func INTEGER PRIMARY KEY NOT NULL,
primeiro_nome VARCHAR NOT NULL,
segundo_nome VARCHAR,
ultimo_nome VARCHAR,
data_nasci TEXT NOT NULL,
cpf INTEGER NOT NULL,
rg INTEGER NOT NULL,
endereço VARCHAR NOT NULL,
cep INTEGER NOT NULL,
Cidade VARCHAR NOT NULL,
fone INTEGER NOT NULL,
cod_dep INTEGER NOT NULL,
funcao INTEGER NOT NULL,
salario INTEGER NOT NULL);""")
rh.commit()


# In[19]:


rh.execute("""CREATE TABLE Departamentos(
codigo INTEGER PRIMARY KEY NOT NULL,
nome VARCHAR NOT NULL,
Localizaçao TEXT NOT NULL,
Cod_Func_Ger INTEGER NOT NULL);""")
rh.commit()


# In[26]:


cursor = rh.cursor()


# In[22]:


#para ter como opção
sql = """
DROP TABLE Departamentos
"""
rh.execute(sql)
rh.commit()
print("tabela deletada")


# In[33]:


for row in cursor.execute("SELECT * FROM Funcionarios"):
    print(row)


# In[31]:


for row in cursor.execute("SELECT * FROM Departamentos"):
    print(row)


# In[34]:


cursor.execute("""SELECT primeiro_nome, ultimo_nome 
FROM Funcionarios 
ORDER BY ultimo_nome""")
print(cursor.fetchall())


# In[36]:


cursor.execute("""SELECT * FROM Funcionarios 
ORDER BY cidade""")
print(cursor.fetchall())


# In[38]:


#mudança de 1000 para 4000 mil para facilitar a leitura
cursor.execute("""SELECT * FROM Funcionarios
WHERE salario > 4000
ORDER BY primeiro_nome, segundo_nome, ultimo_nome""")
print(cursor.fetchall())


# In[39]:


cursor.execute("""SELECT data_nasci, primeiro_nome
FROM Funcionarios 
ORDER BY data_nasci DESC""")
print(cursor.fetchall())


# In[40]:


cursor.execute("""SELECT SUM(salario) 
FROM Funcionarios""")
print(cursor.fetchall())


# In[41]:


cursor.execute("""SELECT Funcionarios.primeiro_nome, Departamentos.nome, 
Funcionarios.funcao
FROM Funcionarios JOIN Departamentos
ON Funcionarios.cod_dep = Departamentos.codigo
ORDER BY Funcionarios.primeiro_nome""")
print(cursor.fetchall())


# In[42]:


cursor.execute("""SELECT COUNT(*)
FROM Funcionarios""")
print(cursor.fetchall())


# In[43]:


cursor.execute("""SELECT Departamentos.nome, Funcionarios.primeiro_nome
FROM Departamentos JOIN 
Funcionarios ON Departamentos.codigo = 
Funcionarios.cod_dep
ORDER BY Departamentos.nome, Funcionarios.primeiro_nome""")
print(cursor.fetchall())


# In[ ]:




