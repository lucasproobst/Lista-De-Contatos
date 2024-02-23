"""
SISTEMA SIMPLES PARA ARMAZENAR CONTATOS
"""

import os
import time
import conexaoDB

def Limpar():
    time.sleep(1)
    os.system('clear')

def adicionar_contato():
        nome = input('Nome: ')
        telefone = int(input('Telefone: '))
        email = input('Email: ')
        endereco = input('Endereco: ')
        
        verificar_nome = conexaoDB.cursor.execute('SELECT * FROM Contatos WHERE nome = ?', (nome,)).fetchone()
        
        if nome not in verificar_nome:
            conexaoDB.cursor.execute("INSERT INTO Contatos (nome, telefone, email, endereco) VALUES (?, ?, ?, ?)", (nome, telefone, email, endereco))
            conexaoDB.banco.commit()
            print(f'[SISTEMA] - {nome} foi adicionado a lista.')
            Limpar()
        else:
            print(f'[SISTEMA] - {nome} já está na lista.')
            Limpar()
            Menu()

def remover_contato():
    nome = input('Nome do contato a ser removido: ')
    
    conexaoDB.cursor.execute("SELECT * FROM Contatos WHERE nome = ?", (nome,))
    
    contato = conexaoDB.cursor.fetchone()
    
    if contato:
        confirmacao = input(f'Deseja realmente remover o contato "{nome}"? [s]im [n]ao: ')
        if confirmacao.lower().startswith('s'):
            conexaoDB.cursor.execute("DELETE FROM Contatos WHERE nome = ?", (nome,))
            conexaoDB.banco.commit()
            print('Contato removido com sucesso.')
    else:
        print(f'O contato "{nome}" não foi encontrado.')

def formatar_telefone(numero):
    if len(numero) == 11:
        return f"({numero[:2]}){numero[2:7]}-{numero[7:]}"
    else:
        pass

def listar_contatos():
    conexaoDB.cursor.execute('SELECT * FROM Contatos')
    
    listar = conexaoDB.cursor.fetchall()
    
    Limpar()
    
    for resultado in listar:
        print('*****************************\n')
        print(f'ID: {resultado[0]}')
        print(f'Nome: {resultado[1]}')
        print(f'Telefone:{formatar_telefone(resultado[2])}')
        print(f'Email: {resultado[3]}')
        print(f'Endereço: {resultado[4]}\n')

def alterar_contato():
    listar_contatos()
    
    escolha = input('Nome que deseja alterar: ')
    
    verificar_nome = conexaoDB.cursor.execute('SELECT * FROM Contatos WHERE nome = ?', (escolha,)).fetchone()

    Limpar()
    
    if verificar_nome:
        novo_nome = input('Insira o novo nome: ')
        novo_telefone = int(input('Insira o novo telefone: '))
        novo_email = input('Insira o novo email: ')
        novo_endereco = input('Insira o novo endereço: ')

        conexaoDB.cursor.execute("UPDATE Contatos SET nome = ?, telefone = ?, email = ?, endereco = ? WHERE nome = ?", \
            (novo_nome, novo_telefone, novo_email, novo_endereco, escolha))
        conexaoDB.banco.commit()
        
        print('[SISTEMA] - Nome alterar com sucesso!')
        Limpar()
    else:
        print('[SISTEMA] - Nome nao esta na lista.')
        Limpar()

def procurarNome():
    nome = input('Nome: ')
    
    procurar = conexaoDB.cursor.execute('SELECT * FROM Contatos WHERE nome = ?', (nome,)).fetchone()
    
    if nome not in procurar:
        print(f'[SISTEMA] - {nome} não foi encontrado.')
        Limpar()
        Menu()
    else:
        listar = conexaoDB.cursor.fetchall()
    
        Limpar()
    
        for resultado in listar:
            print('*****************************\n')
            print(f'ID: {resultado[0]}')
            print(f'Nome: {resultado[1]}')
            print(f'Telefone:{formatar_telefone(resultado[2])}')
            print(f'Email: {resultado[3]}')
            print(f'Endereço: {resultado[4]}\n')

def Menu():
    while True:
        print("""
          [SISTEMA]
          [1] - Adicionar
          [2] - Remover
          [3] - Alterar
          [4] - Listar
          [5] - Procurar
          
          [0] - Sair 
          """)
        
        opcao = int(input('Opcao: '))
        
        if opcao == 1:
            adicionar_contato()
        if opcao == 2:
            remover_contato()
        if opcao == 3:
            alterar_contato()
        if opcao == 4:
            listar_contatos()
        if opcao == 5:
            procurarNome()
        if opcao == 0:
            print('saindo')
            break

Menu()