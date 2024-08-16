from database.db import criar_tabela, inserir_usuario, consultar_usuarios

if __name__ == "__main__":
    criar_tabela()

    inserir_usuario('João', 30)

    usuarios = consultar_usuarios()
    for usuario in usuarios:
        print(usuario)