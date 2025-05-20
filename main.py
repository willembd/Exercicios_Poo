from biblioteca import Animal, Cachorro, Gato, Funcionario, Gerente, Veiculo, Carro, Moto, Pessoa, Cliente, Empregado

"""cachorro1 = Cachorro("toby", 10)
cachorro1.nome_idade()
cachorro1.fazer_som()

gato1= Gato("Ray", 5)
gato1.nome_idade()
gato1.fazer_som()"""


"""funcionario1 = Funcionario("Ana", 1.450 )
funcionario1.exibir_dados()

gerente1 = Gerente("Barbara", 2.400, "Gerente")
gerente1.exibir_dados()"""


"""veiculo1 = Veiculo("Nissan", "abc", 2015)
veiculo2 = Veiculo("Nissan", "aftgkh", 2019)
moto1 = Moto("honda", "titan", 2022, 400)

veiculos = []
veiculos_modernos = []

veiculos.append(veiculo1)
veiculos.append(veiculo2)
veiculos.append(moto1)

for v in veiculos:
    v.exibir_Dados()
    if v.e_moderno():
        veiculos_modernos.append(v)

for x in veiculos_modernos:
    x.exibir_Dados()"""


empresa= []

cliente1 = Cliente("Maria", 32, 456123, 6000)
cliente2 = Cliente("João", 45, 987321, 1500)
funcionario1 = Empregado("Bia", 28, "gerente", 2200)
funcionario2 = Empregado("Paulo", 22, "analista", 1800)

empresa.append(cliente1)
empresa.append(cliente2)
empresa.append(funcionario1)
empresa.append(funcionario2)

for x in empresa:
    x.exibir_dados()

print()

cliente1.sacar(200)
cliente2.depositar(150)

print()

funcionario1.aumentar_salario()
