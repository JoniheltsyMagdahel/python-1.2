import tkinter as tk
from PIL import imagem
#Criando  a janela
#dando o nome para  a janela
#espessura  e altura da janela
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry("500x500")

#criando a barra de texto
#local onde a barra de texto ficara
entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.pack(pady=5)

#criando a lista
#espessura da lista
listbox = tk.Listbox(janela)
listbox.pack(pady=10)

# adiciona esse texto em uma lista (como uma Listbox), 
# e depois limpa o campo de entrada para que o usuário 
# possa adicionar uma nova tarefa, se desejar.
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        listbox.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)

#exclusão  de tarefa
def excluir_tarefa():
    listbox.delete(tk.ANCHOR)

#Se houver seleção
#Deleta o item selecionado
def concluir():
    if listbox.curselection():
        listbox.delete(listbox.curselection())
    else:
        print("Selecione uma tarefa para concluir")
    


botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_adicionar.pack(pady=5)

botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa)
botao_excluir.pack(pady=5)

botao_concluir =  tk.Button(janela, text="Concluir", command=concluir)
botao_concluir.pack(pady=5)


janela.mainloop()
