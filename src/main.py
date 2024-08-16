from database.db import inserir_usuario, consultar_usuarios
from database.db2 import criar_tabela, inserir_genero, consultar_genero

if __name__ == "__main__":
    criar_tabela()

    inserir_usuario('João', 30)
    inserir_usuario('Carla', 47)

    usuarios = consultar_usuarios()
    for usuario in usuarios:
        print(usuario)

if __name__ == "__main__":
    criar_tabela()

    inserir_genero(1, "Masculino")
    inserir_genero(2, "Feminino")

    generos = consultar_genero()
    for genero in generos:
        print(genero)
