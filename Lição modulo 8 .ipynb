{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ac8998a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "rh = sqlite3.connect('lição.db')\n",
    "rh.execute(\"\"\"CREATE TABLE Funcionarios (\n",
    "cod_func INTEGER PRIMARY KEY NOT NULL,\n",
    "primeiro_nome VARCHAR NOT NULL,\n",
    "segundo_nome VARCHAR,\n",
    "ultimo_nome VARCHAR,\n",
    "data_nasci TEXT NOT NULL,\n",
    "cpf INTEGER NOT NULL,\n",
    "rg INTEGER NOT NULL,\n",
    "endereço VARCHAR NOT NULL,\n",
    "cep INTEGER NOT NULL,\n",
    "Cidade VARCHAR NOT NULL,\n",
    "fone INTEGER NOT NULL,\n",
    "cod_dep INTEGER NOT NULL,\n",
    "funcao INTEGER NOT NULL,\n",
    "salario INTEGER NOT NULL);\"\"\")\n",
    "rh.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "049f12be",
   "metadata": {},
   "outputs": [],
   "source": [
    "rh.execute(\"\"\"CREATE TABLE Departamentos(\n",
    "codigo INTEGER PRIMARY KEY NOT NULL,\n",
    "nome VARCHAR NOT NULL,\n",
    "Localizaçao TEXT NOT NULL,\n",
    "Cod_Func_Ger INTEGER NOT NULL);\"\"\")\n",
    "rh.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "e7d92e2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "cursor = rh.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "9063a25b",
   "metadata": {},
   "outputs": [
    {
     "ename": "OperationalError",
     "evalue": "database is locked",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mOperationalError\u001b[0m                          Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[22], line 4\u001b[0m\n\u001b[0;32m      1\u001b[0m sql \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;124mDROP TABLE Departamentos\u001b[39m\n\u001b[0;32m      3\u001b[0m \u001b[38;5;124m\"\"\"\u001b[39m\n\u001b[1;32m----> 4\u001b[0m rh\u001b[38;5;241m.\u001b[39mexecute(sql)\n\u001b[0;32m      5\u001b[0m rh\u001b[38;5;241m.\u001b[39mcommit()\n\u001b[0;32m      6\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtabela deletada\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "\u001b[1;31mOperationalError\u001b[0m: database is locked"
     ]
    }
   ],
   "source": [
    "#para ter como opção\n",
    "sql = \"\"\"\n",
    "DROP TABLE Departamentos\n",
    "\"\"\"\n",
    "rh.execute(sql)\n",
    "rh.commit()\n",
    "print(\"tabela deletada\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "f6eea822",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(65, 'Sofia', 'Mendes', 'Santos', '15/04/1992', 48372619504, 426831579, 'Rua das Rosas', '12345-678', 'Montanha Alta', '(11) 98765-4321', 3, 1, 4500)\n",
      "(80, 'Lucas', None, 'Silva', '03/09/1985', 91753068420, 975028413, 'Rua dos Cedros', '98765-432', 'Rio Brilhante', '(21) 98765-4321', 2, 3, 2800.5)\n",
      "(88, 'Isabela', 'Pereira', 'Oliveira', '22/07/2000', 65289143760, 203714856, 'Rua das Violetas', '56789-012', 'Vale Sereno', '(31) 98765-4321', 3, 4, 6200.75)\n",
      "(91, 'Gabriel', None, 'Pereira', '11/11/1978', 30857291683, 687395124, 'Rua dos Lírios', '23456-789', 'Campo Alegre', '(41) 98765-4321', 3, 4, 3700.25)\n",
      "(128, 'Laura', 'Santos', 'Costa', '29/06/1996', 72614908357, 140296837, 'Rua das Acácias', '87654-321', 'Cidade do Mar', '(51) 98765-4321', 3, 5, 5200.8)\n",
      "(141, 'Matheus', 'Rodrigues', 'Rodrigues', '07/02/1983', 41592783602, 359482701, 'Rua dos Ipês', '34567-890', 'Nova Esperança', '(61) 98765-4321', 3, 4, 3100.6)\n",
      "(145, 'Ana', None, 'Almeida', '18/10/1990', 83960527148, 802167394, 'Rua das Margaridas', '65432-109', 'Flores do Sul', '(71) 98765-4321', 3, 3, 5800.9)\n",
      "(152, 'Pedro', None, 'Fernandes', '25/12/2005', 12670439581, 514739260, 'Rua dos Jasmim', '98765-432', 'Porto Verde', '(81) 98765-4321', 1, 1, 4200.4)\n",
      "(154, 'Maria', 'Silva', 'Carvalho', '14/08/1974', 57083629418, 648503912, 'Rua das Orquídeas', '45678-901', 'Serra Dourada', '(91) 98765-4321', 1, 2, 6700.7)\n",
      "(166, 'João', 'Carvalho', 'Mendes', '30/01/1999', 29481570362, 321670589, 'Rua dos Girassóis', '78901-234', 'Praia Serena', '(12) 98765-4321', 3, 2, 3900.2)\n"
     ]
    }
   ],
   "source": [
    "for row in cursor.execute(\"SELECT * FROM Funcionarios\"):\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "f7d2f35c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(1, 'Produção', 'Pavilhão', 154)\n",
      "(2, 'Adm.', 'Central 1', 88)\n",
      "(3, 'RH', 'Central 2', 80)\n"
     ]
    }
   ],
   "source": [
    "for row in cursor.execute(\"SELECT * FROM Departamentos\"):\n",
    "    print(row)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "377669ac",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Ana', 'Almeida'), ('Maria', 'Carvalho'), ('Laura', 'Costa'), ('Pedro', 'Fernandes'), ('João', 'Mendes'), ('Isabela', 'Oliveira'), ('Gabriel', 'Pereira'), ('Matheus', 'Rodrigues'), ('Sofia', 'Santos'), ('Lucas', 'Silva')]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT primeiro_nome, ultimo_nome \n",
    "FROM Funcionarios \n",
    "ORDER BY ultimo_nome\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "2c749dc3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(91, 'Gabriel', None, 'Pereira', '11/11/1978', 30857291683, 687395124, 'Rua dos Lírios', '23456-789', 'Campo Alegre', '(41) 98765-4321', 3, 4, 3700.25), (128, 'Laura', 'Santos', 'Costa', '29/06/1996', 72614908357, 140296837, 'Rua das Acácias', '87654-321', 'Cidade do Mar', '(51) 98765-4321', 3, 5, 5200.8), (145, 'Ana', None, 'Almeida', '18/10/1990', 83960527148, 802167394, 'Rua das Margaridas', '65432-109', 'Flores do Sul', '(71) 98765-4321', 3, 3, 5800.9), (65, 'Sofia', 'Mendes', 'Santos', '15/04/1992', 48372619504, 426831579, 'Rua das Rosas', '12345-678', 'Montanha Alta', '(11) 98765-4321', 3, 1, 4500), (141, 'Matheus', 'Rodrigues', 'Rodrigues', '07/02/1983', 41592783602, 359482701, 'Rua dos Ipês', '34567-890', 'Nova Esperança', '(61) 98765-4321', 3, 4, 3100.6), (152, 'Pedro', None, 'Fernandes', '25/12/2005', 12670439581, 514739260, 'Rua dos Jasmim', '98765-432', 'Porto Verde', '(81) 98765-4321', 1, 1, 4200.4), (166, 'João', 'Carvalho', 'Mendes', '30/01/1999', 29481570362, 321670589, 'Rua dos Girassóis', '78901-234', 'Praia Serena', '(12) 98765-4321', 3, 2, 3900.2), (80, 'Lucas', None, 'Silva', '03/09/1985', 91753068420, 975028413, 'Rua dos Cedros', '98765-432', 'Rio Brilhante', '(21) 98765-4321', 2, 3, 2800.5), (154, 'Maria', 'Silva', 'Carvalho', '14/08/1974', 57083629418, 648503912, 'Rua das Orquídeas', '45678-901', 'Serra Dourada', '(91) 98765-4321', 1, 2, 6700.7), (88, 'Isabela', 'Pereira', 'Oliveira', '22/07/2000', 65289143760, 203714856, 'Rua das Violetas', '56789-012', 'Vale Sereno', '(31) 98765-4321', 3, 4, 6200.75)]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT * FROM Funcionarios \n",
    "ORDER BY cidade\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "e54330cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(145, 'Ana', None, 'Almeida', '18/10/1990', 83960527148, 802167394, 'Rua das Margaridas', '65432-109', 'Flores do Sul', '(71) 98765-4321', 3, 3, 5800.9), (88, 'Isabela', 'Pereira', 'Oliveira', '22/07/2000', 65289143760, 203714856, 'Rua das Violetas', '56789-012', 'Vale Sereno', '(31) 98765-4321', 3, 4, 6200.75), (128, 'Laura', 'Santos', 'Costa', '29/06/1996', 72614908357, 140296837, 'Rua das Acácias', '87654-321', 'Cidade do Mar', '(51) 98765-4321', 3, 5, 5200.8), (154, 'Maria', 'Silva', 'Carvalho', '14/08/1974', 57083629418, 648503912, 'Rua das Orquídeas', '45678-901', 'Serra Dourada', '(91) 98765-4321', 1, 2, 6700.7), (152, 'Pedro', None, 'Fernandes', '25/12/2005', 12670439581, 514739260, 'Rua dos Jasmim', '98765-432', 'Porto Verde', '(81) 98765-4321', 1, 1, 4200.4), (65, 'Sofia', 'Mendes', 'Santos', '15/04/1992', 48372619504, 426831579, 'Rua das Rosas', '12345-678', 'Montanha Alta', '(11) 98765-4321', 3, 1, 4500)]\n"
     ]
    }
   ],
   "source": [
    "#mudança de 1000 para 4000 mil para facilitar a leitura\n",
    "cursor.execute(\"\"\"SELECT * FROM Funcionarios\n",
    "WHERE salario > 4000\n",
    "ORDER BY primeiro_nome, segundo_nome, ultimo_nome\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "bd6f07ca",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('30/01/1999', 'João'), ('29/06/1996', 'Laura'), ('25/12/2005', 'Pedro'), ('22/07/2000', 'Isabela'), ('18/10/1990', 'Ana'), ('15/04/1992', 'Sofia'), ('14/08/1974', 'Maria'), ('11/11/1978', 'Gabriel'), ('07/02/1983', 'Matheus'), ('03/09/1985', 'Lucas')]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT data_nasci, primeiro_nome\n",
    "FROM Funcionarios \n",
    "ORDER BY data_nasci DESC\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "2c070757",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(46105.09999999999,)]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT SUM(salario) \n",
    "FROM Funcionarios\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "fa24922e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Ana', 'RH', 3), ('Gabriel', 'RH', 4), ('Isabela', 'RH', 4), ('João', 'RH', 2), ('Laura', 'RH', 5), ('Lucas', 'Adm.', 3), ('Maria', 'Produção', 2), ('Matheus', 'RH', 4), ('Pedro', 'Produção', 1), ('Sofia', 'RH', 1)]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT Funcionarios.primeiro_nome, Departamentos.nome, \n",
    "Funcionarios.funcao\n",
    "FROM Funcionarios JOIN Departamentos\n",
    "ON Funcionarios.cod_dep = Departamentos.codigo\n",
    "ORDER BY Funcionarios.primeiro_nome\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "4ca2e67b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[(10,)]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT COUNT(*)\n",
    "FROM Funcionarios\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "317518cc",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[('Adm.', 'Lucas'), ('Produção', 'Maria'), ('Produção', 'Pedro'), ('RH', 'Ana'), ('RH', 'Gabriel'), ('RH', 'Isabela'), ('RH', 'João'), ('RH', 'Laura'), ('RH', 'Matheus'), ('RH', 'Sofia')]\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"\"\"SELECT Departamentos.nome, Funcionarios.primeiro_nome\n",
    "FROM Departamentos JOIN \n",
    "Funcionarios ON Departamentos.codigo = \n",
    "Funcionarios.cod_dep\n",
    "ORDER BY Departamentos.nome, Funcionarios.primeiro_nome\"\"\")\n",
    "print(cursor.fetchall())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00eae822",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
