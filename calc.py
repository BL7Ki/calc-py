import tkinter as tk # Importa a biblioteca tkinter para criar interfaces gráficas
from tkinter import * # Importa todos os elementos de tkinter para facilitar o uso

# Variáveis para armazenar números e o estado das operações
numero1 = '' # Primeiro número inserido
numero2 = '' # Segundo número inserido
adicao = FALSE # Flag para operação de adição
subtracao = FALSE # Flag para operação de subtração
multiplicacao = FALSE # Flag para operação de multiplicação
divisao = FALSE # Flag para operação de divisão

# Configuração da interface gráfica principal
root = Tk() # Cria a janela principal da interface gráfica
root.title('Sua calculadora') # Define o título da janela
root.geometry("408x355") # Define o tamanho da janela
root.maxsize(408, 355) # Define o tamanho máximo da janela
root.minsize(408, 355) # Define o tamanho mínimo da janela

root.configure(background='#282828') # Configura a cor de fundo da janela

# Cria um campo de entrada (Entry) para mostrar números e resultados
e = Entry(root, width=15, borderwidth=4, relief=FLAT, fg='#FFFFFF',
          bg='#a7a28f', font=('futura', 25, 'bold'), justify=CENTER)
e.grid(
    row=0, # Posição na linha 0
    column=0, # Posição na coluna 0
    columnspan=4, # Ocupa 4 colunas
    pady=2 # Espaço ao redor do campo de entrada
)

# Função chamada quando um botão numérico é clicado
def botao_click(num):
    e.insert(END, num) # Insere o número no final do campo de entrada

# Função chamada quando o botão de adição é clicado
def botao_adiciona():
    global numero1
    global adicao
    adicao = TRUE # Define a flag de adição como verdadeira
    numero1 = e.get() # Obtém o número atual do campo de entrada
    e.delete(0, END) # Limpa o campo de entrada

# Função chamada quando o botão de subtração é clicado
def botao_subrai():
    global numero1
    global subtracao
    subtracao = TRUE # Define a flag de subtração como verdadeira
    numero1 = e.get() # Obtém o número atual do campo de entrada
    e.delete(0, END) # Limpa o campo de entrada

# Função chamada quando o botão de multiplicação é clicado
def botao_multiplica():
    global numero1
    global multiplicacao
    multiplicacao = TRUE # Define a flag de multiplicação como verdadeira
    numero1 = e.get() # Obtém o número atual do campo de entrada
    e.delete(0, END) # Limpa o campo de entrada

# Função chamada quando o botão de divisão é clicado
def botao_divide():
    global numero1
    global divisao
    divisao = TRUE # Define a flag de divisão como verdadeira
    numero1 = e.get() # Obtém o número atual do campo de entrada
    e.delete(0, END) # Limpa o campo de entrada

# Função chamada quando o botão de igual é clicado
def botao_igual():
    global subtracao
    global divisao
    global multiplicacao
    global adicao
    numero2 = e.get() # Obtém o segundo número do campo de entrada
    e.delete(0, END) # Limpa o campo de entrada
    # Executa a operação de acordo com a flag definida e exibe o resultado
    if adicao == TRUE:
        e.insert(0, int(numero1) + int(numero2))
        adicao = FALSE # Reseta a flag de adição
    if multiplicacao == TRUE:
        e.insert(0, int(numero1) * int(numero2))
        multiplicacao = FALSE # Reseta a flag de multiplicação
    if subtracao == TRUE:
        e.insert(0, int(numero1) - int(numero2))
        subtracao = FALSE # Reseta a flag de subtração
    if divisao == TRUE:
        e.insert(0, int(numero1) // int(numero2)) # Usa divisão inteira
        divisao = FALSE # Reseta a flag de divisão

# Função chamada quando o botão de limpar é clicado
def botao_limpa():
    e.delete(0, END) # Limpa o campo de entrada

# Função para criar botões numéricos
def botao_num(num, row, column):
    botao = Button(root,
                   text=num,
                   padx=40, # Espaço horizontal dentro do botão
                   pady=20, # Espaço vertical dentro do botão
                   command=lambda: botao_click(num),
                   fg='#FFFFFF', # Cor do texto
                   activebackground='#ecb653', # Cor de fundo quando o botão é pressionado
                   activeforeground='#FFFFFF', # Cor do texto quando o botão é pressionado
                   bg='#282828', # Cor de fundo do botão
                   relief=FLAT, # Estilo do botão
                   font=('futura', 12, 'bold')) # Fonte do texto
    botao.grid(row=row, column=column) # Posiciona o botão na grid

# Função para criar botões de operadores
def botao_operador(op, command, row, column):
    operador = Button(root,
                      text=op,
                      padx=40,
                      pady=20,
                      command=command,
                      fg='#FFFFFF',
                      activebackground='#ecb653',
                      activeforeground='#FFFFFF',
                      bg='#c8c8c8',
                      relief=FLAT,
                      font=('futura', 12, 'bold'))
    operador.grid(row=row, column=column)

# Criação dos botões de operadores e números na interface
botao_operador('÷', botao_divide, 0, 4) # Botão de divisão
# Primeira fileira
botao_num(1, 1, 1) # Botão 1
botao_num(2, 1, 2) # Botão 2
botao_num(3, 1, 3) # Botão 3
botao_operador('×', botao_multiplica, 1, 4) # Botão de multiplicação
# Segunda fileira
botao_num(4, 2, 1) # Botão 4
botao_num(5, 2, 2) # Botão 5
botao_num(6, 2, 3) # Botão 6
botao_operador(' -', botao_subrai, 2, 4) # Botão de subtração
# Terceira fileira
botao_num(7, 3, 1) # Botão 7
botao_num(8, 3, 2) # Botão 8
botao_num(9, 3, 3) # Botão 9
botao_operador('+', botao_adiciona, 3, 4) # Botão de adição
# Quarta fileira
zero = Button(root,
              text='0',
              padx=91, # Espaço horizontal maior para o botão 0
              pady=20,
              command=lambda: botao_click(0),
              fg='#FFFFFF',
              activebackground='#ecb653',
              activeforeground='#FFFFFF',
              bg='#282828',
              relief=FLAT,
              font=('futura', 12, 'bold'))
zero.grid(row=4, column=1, columnspan=2) # Botão 0 ocupa duas colunas
botao_operador('C', botao_limpa, 4, 4) # Botão de limpar
botao_operador('=', botao_igual, 4, 3) # Botão de igual

root.mainloop() # Inicia o loop principal da interface gráfica
