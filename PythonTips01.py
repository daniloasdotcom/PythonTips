from tkinter import *
from tkinter.filedialog import askopenfilename

def abrirArquivo():
    arquivo = askopenfilename()
    print(arquivo)

janela = Tk()
menu = Menu(janela)
janela.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Arquivo", menu = filemenu)
filemenu.add_command(label="Abrir arquivo", command=abrirArquivo)
filemenu.add_command(label="Novo Arquivo")
filemenu.add_separator()
filemenu.add_command(label="Fechar", command=janela.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Ajuda", menu = helpmenu)
helpmenu.add_command(label="Sobre")
helpmenu.add_command(label="Guia de usuário")

mainloop()