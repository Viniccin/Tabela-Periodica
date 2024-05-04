import tkinter as tk
from tkinter import messagebox

# Dicionário com informações sobre os elementos da tabela periódica
elementos = {
    'H': 'O hidrogênio é o elemento químico de número atômico 1, e sua forma mais comum é o isótopo protium.',
    'He': 'O hélio é o elemento químico de número atômico 2, e é o segundo elemento mais leve e abundante no universo.',
    # Adicione informações para outros elementos da tabela periódica conforme necessário
}

def mostrar_info(elemento):
    info = elementos.get(elemento, 'Informação não disponível.')
    messagebox.showinfo('Informações sobre {}'.format(elemento), info)

def criar_interface():
    root = tk.Tk()
    root.title('Tabela Periódica')

    # Adicione botões para cada elemento da tabela periódica
    for elemento in elementos.keys():
        btn = tk.Button(root, text=elemento, command=lambda el=elemento: mostrar_info(el))
        btn.pack(padx=10, pady=5)

    root.mainloop()

if __name__ == "__main__":
    criar_interface()
