#!/usr/bin/env python
# coding: utf-8


#importar o sqlite3 - criação da tabela funcionários - definir as colunas 

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


# criação da tabela departamentos - definir as colunas


rh.execute("""CREATE TABLE Departamentos(
codigo INTEGER PRIMARY KEY NOT NULL,
nome VARCHAR NOT NULL,
Localizaçao TEXT NOT NULL,
Cod_Func_Ger INTEGER NOT NULL);""")
rh.commit()

#criar o cursor para execução de comandos


cursor = rh.cursor()


#Criar a aopção de deletar as tabelas para correções


#para ter como opção #Funcionários
sql = """
DROP TABLE Departamentos  
"""
rh.execute(sql)
rh.commit()
print("tabela deletada")


# Visualizar as tabela funcionarios


for row in cursor.execute("SELECT * FROM Funcionarios"):  
    print(row)


# Visualizar as tabela departamentos


for row in cursor.execute("SELECT * FROM Departamentos"):
    print(row)


#filtros


cursor.execute("""SELECT primeiro_nome, ultimo_nome 
FROM Funcionarios 
ORDER BY ultimo_nome""")
print(cursor.fetchall())


#filtros


cursor.execute("""SELECT * FROM Funcionarios 
ORDER BY cidade""")
print(cursor.fetchall())


#filtros


#mudança de 1000 para 4000 mil para facilitar a leitura
cursor.execute("""SELECT * FROM Funcionarios
WHERE salario > 4000
ORDER BY primeiro_nome, segundo_nome, ultimo_nome""")
print(cursor.fetchall())


#filtros


cursor.execute("""SELECT data_nasci, primeiro_nome
FROM Funcionarios 
ORDER BY data_nasci DESC""")
print(cursor.fetchall())


#filtros


cursor.execute("""SELECT SUM(salario) 
FROM Funcionarios""")
print(cursor.fetchall())


#filtros


cursor.execute("""SELECT Funcionarios.primeiro_nome, Departamentos.nome, 
Funcionarios.funcao
FROM Funcionarios JOIN Departamentos
ON Funcionarios.cod_dep = Departamentos.codigo
ORDER BY Funcionarios.primeiro_nome""")
print(cursor.fetchall())


#filtros


cursor.execute("""SELECT COUNT(*)
FROM Funcionarios""")
print(cursor.fetchall())


#filtros

cursor.execute("""SELECT Departamentos.nome, Funcionarios.primeiro_nome
FROM Departamentos JOIN 
Funcionarios ON Departamentos.codigo = 
Funcionarios.cod_dep
ORDER BY Departamentos.nome, Funcionarios.primeiro_nome""")
print(cursor.fetchall())







