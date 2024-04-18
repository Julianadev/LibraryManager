import pandas as pd
import tkinter as tk
import pytest

class Livro:
    """
    Construtor do livro
    """
    def __init__(self, id, titulo, autor):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.left = None
        self.right = None

class Biblioteca:
    """
    Construtor da biblioteca
    """
    def __init__(self):
        self.root = None

    def insert(self, livro):
        """
        Insere um livro na árvore binária.
        :param livro:
        """
        if self.root is None:
            self.root = livro
        else:
            self._insert_rec(self.root, livro)

    def _insert_rec(self, livro_atual, livro):
        """
        Insere um livro na árvore binária de forma recursiva.
        :param livro_atual:
        :param livro:
        """
        if livro.id < livro_atual.id:
            if livro_atual.left is None:
                livro_atual.left = livro
            else:
                self._insert_rec(livro_atual.left, livro)
        else:
            if livro_atual.right is None:
                livro_atual.right = livro
            else:
                self._insert_rec(livro_atual.right, livro)

    def buscar(self, id):
        return self._buscar_rec(self.root, id)

    def _buscar_rec(self, livro_atual, id):
        """
        Busca um livro na árvore binária de forma recursiva.
        :param livro_atual:
        :param id:
        :return: O livro encontrado ou None se o livro não for encontrado
        """
        if livro_atual is None or livro_atual.id == id:
            return livro_atual
        if id < livro_atual.id:
            return self._buscar_rec(livro_atual.left, id)
        return self._buscar_rec(livro_atual.right, id)

    def buscar_e_mostrar(self, id_entry, resultado_label):
        """
        Busca um livro na árvore binária e atualiza o rótulo com o resultado.
        :param id_entry:
        :param resultado_label:
        """
        id_isbn = int(id_entry.get())
        buscar_livro = self.buscar(id_isbn)
        if buscar_livro is not None:
            resultado_label['text'] = f'O livro {buscar_livro.id} é {buscar_livro.titulo} de {buscar_livro.autor}'
        else:
            resultado_label['text'] = 'O livro não foi encontrado!'

    def read_livros(self):
        """
        Lê os livros de um arquivo CSV, limpa e gera um novo arquivo, e retorna uma lista de objetos Livro.
        contendo somente as colunas selecionadas
        :return: Uma lista de objetos Livro lidos do arquivo CSV.
        """
        df = pd.read_csv('dados.csv')
        df_novo = df[['ISBN_13', 'titulo', 'autor']]
        df_novo.to_csv('livros.csv', index=False)

        livros = []
        for index, row in df_novo.iterrows():
            livros.append(Livro(row['ISBN_13'], row['titulo'], row['autor']))
        return livros


if __name__ == "__main__":

    biblioteca = Biblioteca()

    livros = biblioteca.read_livros()

    for livro in livros:
        biblioteca.insert(livro)

    # Criar a janela da aplicação
    janela = tk.Tk()
    janela.title('Buscador de livros - Código ')

    # Criar um campo de entrada para o usuário digitar o ID do livro
    id_entry = tk.Entry(janela)
    id_entry.pack(pady=20, padx=20, fill=tk.X)

    # Criar um rótulo para mostrar o resultado da busca
    resultado_label = tk.Label(janela, text="")
    resultado_label.pack(pady=20, padx=20, fill=tk.X)

    # Criar um botão que busca o livro quando clicado
    buscar_botao = tk.Button(janela, text="Buscar Livro",
                             command=lambda: biblioteca.buscar_e_mostrar(id_entry, resultado_label))
    buscar_botao.pack(pady=20, padx=20)

    # Iniciar o loop principal da aplicação
    janela.mainloop()





