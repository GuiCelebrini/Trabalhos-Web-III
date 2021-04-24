from tatu3 import Cliente
from tatu3 import Conta, ContaEspecial

joao = Cliente('João Silva', '777-1234')
maria = Cliente('Maria Oliveira', '555-4321')

conta_conjunta = ContaEspecial('1899', [joao, maria], 50000, 15000)

conta_conjunta.sacar(60000)
conta_conjunta.depositar(9000)
conta_conjunta.depositar(500)
conta_conjunta.depositar(250)

conta_conjunta.resumir_informacoes()
conta_conjunta.exibir_extrato()
