class Pessoa:
    def __init__(self, nome: str, idade: int, genero: str):
        self.nome = nome
        self.idade = idade
        self.genero = genero

    def exibir_informacoes(self) -> None:
        print(f"Nome: {self.nome}, Idade: {self.idade}, Gênero: {self.genero}")


pessoa1 = Pessoa("João", 30, "Masculino")
pessoa2 = Pessoa("Maria", 25, "Feminino")
pessoa3 = Pessoa("Eduardo", 23, "Masculino")
pessoa4 = Pessoa("Thiago", 35, "Masculino")
pessoa5 = Pessoa("Carl", 34, "Masculino")
pessoa6 = Pessoa("Cherry", 41, "Feminino")
pessoa7 = Pessoa("Camila", 17, "Feminino")
pessoa8 = Pessoa("Paulo", 30, "Masculino")

pessoas = [pessoa1, pessoa2, pessoa3, pessoa4, pessoa5, pessoa6, pessoa7, pessoa8]

for pessoa in pessoas:
    pessoa.exibir_informacoes()
