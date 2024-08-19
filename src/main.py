
from database.db3 import criar_tabela
from src.database.db3 import consultar_ficha, inserir_ficha

if __name__ == "__main__":
    criar_tabela()

    inserir_ficha("Odontologia Pediatrica", "Dentista")
    inserir_ficha("Engenharia de Software", "Desenvolvedor Senior")
    inserir_ficha("Desing de Sistemas", "Chefe de Setor de Desing")

    ficha = consultar_ficha()
    for item in ficha:
        print(item)




