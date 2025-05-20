
class Animal():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def fazer_som(self):
        print("Som indefinido")

class Cachorro(Animal):
    def __init__(self,nome,idade):
        super().__init__(nome,idade)

    def nome_idade(self):
        print(f"O nome do cachorro é {self.nome}, e ele tem {self.idade} anos")

    def fazer_som(self):
        print("Latindo")

class Gato(Animal):
    def nome_idade(self):
        print(f"O nome do gato é {self.nome}, e ele tem {self.idade} anos")

    def fazer_som(self):
        print("Miando")


class Funcionario():
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_dados(self):
        print(f"O funcionario {self.nome} tem o salario de {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento


    def exibir_dados(self):
        print(f"O funcionario {self.nome} tem o salario de {self.salario}, no departamento {self.departamento}")


class Veiculo():
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo=modelo
        self.ano = ano

    def exibir_Dados(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano}")

    def e_moderno(self):
        if self.ano >= 2018:
            return True
        return False

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, quant_portas):
        super().__init__(marca, modelo, ano)
        self.quant_portas= quant_portas


    def exibir_Dados(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Portas: {self.quant_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_Dados(self):
        print(f"Marca: {self.marca} | Modelo: {self.modelo} | Ano: {self.ano} | Cilindradas: {self.cilindradas}")


class Pessoa():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade}")

class Cliente(Pessoa):
    def __init__(self,nome, idade, numero_conta, saldo):
        super().__init__(nome, idade)
        self.numero_conta = numero_conta
        self.saldo = saldo

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Conta: {self.numero_conta} | Saldo: {self.saldo}")

    def depositar(self, valor):
        self.valor = valor
        self.saldo = self.saldo + self.valor
        print(f"Depósito de {self.valor} feito para {self.nome}. Saldo atual: {self.saldo}")

    def sacar(self, valor):
        self.valor = valor
        if self.saldo > self.valor:
            self.saldo = self.saldo - self.valor
            print(f"Saque de {self.valor} feito para {self.nome}. Saldo atual: {self.saldo}")
            return
        print("Saldo insuficiente")

class Empregado(Pessoa):
    def __init__(self, nome, idade, cargo, salario):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.salario = salario

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Idade: {self.idade} | Cargo: {self.cargo} | Salario: {self.salario}")

    def aumentar_salario(self):
        if self.cargo == "gerente":
            self.salario = self.salario * 1.10
            print(f"Aumento de 10% para {self.nome}")
            print(f"Novo salário de {self.nome}: {self.salario}")
