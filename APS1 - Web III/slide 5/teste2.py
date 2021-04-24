from tatu2 import Cliente
from tatu2 import Conta

joao = Cliente('João Silva', '777-1234')
maria = Cliente('Maria Oliveira', '555-4321')

conta_joao = Conta('1245', [joao], 500)
conta_maria = Conta('5421', [maria], 1000)
conta_conjunta = Conta('1899', [joao, maria], 50000)

conta_joao.depositar(5000)
conta_maria.sacar(100)
conta_maria.depositar(4000)

conta_conjunta.depositar(1500)
conta_conjunta.sacar(100)
conta_conjunta.sacar(250)

conta_conjunta.resumir_informacoes()
conta_conjunta.exibir_extrato()

conta_maria.resumir_informacoes()
conta_maria.exibir_extrato()
