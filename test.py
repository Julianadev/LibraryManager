
from main import Biblioteca
from tkinter import Tk, Entry, Label


def test_buscar_e_mostrar():
    biblioteca = Biblioteca()

    # Criando uma instância de Tk para simular a janela da aplicação
    janela = Tk()

    # Criando um campo de entrada (Entry) e um rótulo (Label) para simular os elementos da interface
    id_entry = Entry(janela)
    resultado_label = Label(janela, text="")

    # Definindo um valor para o campo de entrada (simulando o texto digitado pelo usuário)
    id_entry.insert(0, "9788551005736")

    # Testando a função buscar_e_mostrar
    biblioteca.buscar_e_mostrar(id_entry, resultado_label)

    # Verificando se o rótulo foi atualizado corretamente
    assert resultado_label["text"] == "O livro não foi encontrado!"
