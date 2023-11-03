from BibliotecaCB import Banco

conta1 = Banco( 136864, 0, 'Juliana Ferreira', 'corrente', True, 0)
conta1.depositar(valor=8500)
conta1.sacar(valor=500)
print(conta1.verificarsaldo())




