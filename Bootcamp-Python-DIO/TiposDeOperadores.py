#------------------------------------------------------------------------------------------------#
# Operadores Aritméticos em Python

saldo = 1000
saque = 200 
print(saldo + saque)  # Soma
print(saldo - saque)  # Subtração   
print(saldo * saque)  # Multiplicação
print(saldo / saque)  # Divisão
print(saldo // saque)  # Divisão inteira
print(saldo % saque)  # Módulo (resto da divisão)
print(saldo ** saque)  # Exponenciação
print(saldo + 100)  # Soma com um valor fixo
print(saque - 50)  # Subtração com um valor fixo    
print(saldo * 2)  # Multiplicação por um valor fixo
print(saque / 2)  # Divisão por um valor fixo   



#------------------------------------------------------------------------------------------------#
# Operadores de Comparação em Python

saldo = 200
saque = 200

print(saldo == saque)  # Verifica se o saldo é igual ao saque
print(saldo != saque)  # Verifica se o saldo é diferente do saque
print(saldo > saque)   # Verifica se o saldo é maior que o saque
print(saldo < saque)   # Verifica se o saldo é menor que o saque
print(saldo >= saque)  # Verifica se o saldo é maior ou igual ao saque
print(saldo <= saque)  # Verifica se o saldo é menor ou igual ao saque
print(saldo is saque)   # Verifica se o saldo é o mesmo objeto que o saque
print(saldo is not saque)  # Verifica se o saldo não é o mesmo objeto que o saque
print(saldo in [100, 200, 300])  # Verifica se o saldo está na lista
print(saque not in [100, 200, 300])  # Verifica se o saque não está na lista
print(saldo is None)  # Verifica se o saldo é None      
print(saque is not None)  # Verifica se o saque não é None
print(saldo == 200)  # Verifica se o saldo é igual a 200    
print(saque != 100)  # Verifica se o saque é diferente de 100
print(saldo > 150)   # Verifica se o saldo é maior que 150  

#------------------------------------------------------------------------------------------------#
# Operadores de Atribuição em Python

saldo = 1000
saque = 200 

saldo += saque  # Adiciona o saque ao saldo
print(saldo)  # Exibe o novo saldo

saldo -= saque  # Subtrai o saque do saldo
print(saldo)  # Exibe o saldo após a subtração

saldo *= 2  # Multiplica o saldo por 2
print(saldo)  # Exibe o saldo após a multiplicação  

saldo /= 2  # Divide o saldo por 2
print(saldo)  # Exibe o saldo após a divisão

saldo //= 2  # Divide o saldo por 2 e arredonda para baixo
print(saldo)  # Exibe o saldo após a divisão inteira    

saldo %= 300  # Calcula o resto da divisão do saldo por 300
print(saldo)  # Exibe o saldo após o cálculo do módulo

saldo **= 2  # Eleva o saldo ao quadrado
print(saldo)  # Exibe o saldo após a exponenciação

#------------------------------------------------------------------------------------------------#
# Operadores Lógicos em Python
saldo = 1000
saque = 200

print(saldo > 500 and saque < 300)  # Verifica se o saldo é maior que 500 e o saque é menor que 300
print(saldo < 500 or saque > 300)   # Verifica se o saldo# é menor que 500 ou o saque é maior que 300
print(not saldo > 500)  # Verifica se o saldo não é maior que 500
print(saldo > 500 and not saque < 300)  # Verifica se o saldo é maior que 500 e o saque não é menor que 300
print(saldo < 500 or not saque > 300)   # Verifica se o saldo é menor que 500 ou o saque não é maior que 300
print(saldo > 500 and saque < 300 or saldo < 1000)  # Verifica se o saldo é maior que 500 e o saque é menor que 300 ou se o saldo é menor que 1000
print(saldo > 500 and (saque < 300 or saldo < 1000))  # Verifica se o saldo é maior que 500 e (o saque é menor que 300 ou o saldo é menor que 1000)
print((saldo > 500 and saque < 300) or (saldo < 1000 and saque > 100))  # Verifica se (o saldo é maior que 500 e o saque é menor que 300) ou (o saldo é menor que 1000 e o saque é maior que 100)
print(saldo > 500 and saque < 300 and not (saldo < 1000))  # Verifica se o saldo é maior que 500, o saque é menor que 300 e o saldo não é menor que 1000
print(saldo < 500 or saque > 300 or not (saldo > 1000))  # Verifica se o saldo é menor que 500, o saque é maior que 300 ou o saldo não é maior que 1000         

#operador de negação
print(not (saldo > 500))  # Verifica se o saldo não é maior que 500
print(not (saque < 300))  # Verifica se o saque não é menor que 300
print(not (saldo < 1000))  # Verifica se o saldo não é menor que 1000
print(not (saque > 200))  # Verifica se o saque não é maior que 200
print(not (saldo == 1000))  # Verifica se o saldo não é igual a 1000
print(not (saque != 200))  # Verifica se o saque não é diferente de 200
print(not (saldo >= 500))  # Verifica se o saldo não é maior ou igual a 500
print(not (saque <= 200))  # Verifica se o saque não é menor ou igual a 200    

#Parenteses para agrupar expressões
print((saldo > 500 and saque < 300) or (saldo < 1000 and saque > 100))  # Verifica se (o saldo é maior que 500 e o saque é menor que 300) ou (o saldo é menor que 1000 e o saque é maior que 100)
print((saldo > 500 or saque < 300) and (saldo < 1000 or saque > 100))  # Verifica se (o saldo é maior que 500 ou o saque é menor que 300) e (o saldo é menor que 1000 ou o saque é maior que 100)
print((saldo > 500 and saque < 300) and not (saldo < 1000))  # Verifica se o saldo é maior que 500, o saque é menor que 300 e o saldo não é menor que 1000
print((saldo < 500 or saque > 300) or not (saldo > 1000))  # Verifica se o saldo é menor que 500, o saque é maior que 300 ou o saldo não é maior que 1000      

saldo = 1000
saque = 200 
limite = 500
conta_especial = True   
print(saldo > saque and saldo < limite)  # Verifica se o saldo é maior que o saque e menor que o limite
print(saldo > saque or conta_especial)  # Verifica se o saldo é maior que o saque ou se a conta é especial
print(not (saldo < saque))  # Verifica se o saldo não é menor que o saque
print(saldo > saque and not conta_especial)  # Verifica se o saldo é maior que o saque e a conta não é especial
print(saldo < saque or not conta_especial)  # Verifica se o saldo é menor que o saque ou a conta não é especial
print(saldo > saque and (saldo < limite or conta_especial))  # Verifica se o saldo é maior que o saque e (o saldo é menor que o limite ou a conta é especial)
print((saldo > saque and saldo < limite) or (conta_especial and saldo > saque))  # Verifica se (o saldo é maior que o saque e menor que o limite) ou (a conta é especial e o saldo é maior que o saque)
print(saldo > saque and conta_especial or saldo < limite)  # Verifica se o saldo é maior que o saque e a conta é especial ou se o saldo é menor que o limite
print(saldo > saque and conta_especial and not (saldo < limite))  # Verifica se o saldo é maior que o saque, a conta é especial e o saldo não é menor que o limite
print(saldo < saque or conta_especial or not (saldo > limite))  # Verifica se o saldo é menor que o saque, a conta é especial ou o saldo não é maior que o limite   

#------------------------------------------------------------------------------------------------#

# Operadores de Identidade em Python
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 1000, 1000

print(curso is nome_curso)  # Verifica se curso e nome_curso são o mesmo objeto
print(curso is not nome_curso)  # Verifica se curso e nome_curso não são o mesmo objeto
print(saldo is limite)  # Verifica se saldo e limite são o mesmo objeto
print(saldo is not limite)  # Verifica se saldo e limite não são o mesmo objeto
print(curso is None)  # Verifica se curso é None    
print(nome_curso is not None)  # Verifica se nome_curso não é None
print(saldo is None)  # Verifica se saldo é None    
print(limite is not None)  # Verifica se limite não é None
print(curso is "Curso de Python")  # Verifica se curso é o mesmo objeto "Curso de Python"
print(nome_curso is not "Curso de Python")  # Verifica se nome_curso não é o mesmo objeto "Curso de Python"
print(saldo is 1000)  # Verifica se saldo é o mesmo objeto 1000
print(limite is not 1000)  # Verifica se limite não é o mesmo objeto 1000


curso = "Curso de Python"
frutas = ["maçã", "banana", "laranja"]
saques = [100, 200]
print(curso is "Curso de Python")  # Verifica se curso é o mesmo objeto "Curso de Python"
print(curso is not "Curso de Java")  # Verifica se curso não é o mesmo objeto "Curso de Java"
print(frutas is ["maçã", "banana", "laranja"])  # Verifica se frutas é o mesmo objeto ["maçã", "banana", "laranja"]
print(frutas is not ["maçã", "banana", "uva"])  # Verifica se frutas não é o mesmo objeto ["maçã", "banana", "uva"]
print(saques is [100, 200])  # Verifica se saques é o mesmo objeto [100, 200]
print(saques is not [100, 300])  # Verifica se saques não é o mesmo objeto [100, 300]
print(curso is None)  # Verifica se curso é None  
print(frutas is not None)  # Verifica se frutas não é None
print(saques is None)  # Verifica se saques é None  
print(curso is not None)  # Verifica se curso não é None
print(frutas is not None)  # Verifica se frutas não é None
print(saques is not None)  # Verifica se saques não é None
print(curso is "Curso de Python")  # Verifica se curso é o mesmo objeto "Curso de Python"
print(frutas is ["maçã", "banana", "laranja"])  # Verifica se frutas é o mesmo objeto ["maçã", "banana", "laranja"]
print(saques is [100, 200])  # Verifica se saques é o mesmo objeto [100, 200]
print(curso is not "Curso de Java")  # Verifica se curso não é o mesmo objeto "Curso de Java"
print(frutas is not ["maçã", "banana", "uva"])  # Verifica se frutas não é o mesmo objeto ["maçã", "banana", "uva"]
print(saques is not [100, 300])  # Verifica se saques não é o mesmo objeto [100, 300]  
#------------------------------------------------------------------------------------------------#

# Operadores de Membro em Python
lista = [1, 2, 3, 4, 5] 
print(1 in lista)  # Verifica se 1 está na lista
print(6 not in lista)  # Verifica se 6 não está na lista    
print(2 in lista)  # Verifica se 2 está na lista
print(7 not in lista)  # Verifica se 7 não está na lista    
print("Python" in "Curso de Python")  # Verifica se "Python" está na string "Curso de Python"
print("Java" not in "Curso de Python")  # Verifica se "Java" não está na string "Curso de Python"
print("Curso" in "Curso de Python")  # Verifica se "Curso" está na string "Curso de Python"
print("JavaScript" not in "Curso de Python")  # Verifica se "JavaScript" não está na string "Curso de Python"
print(3 in [1, 2, 3, 4, 5]) # Verifica se 3 está na lista [1, 2, 3, 4, 5]       
print(8 not in [1, 2, 3, 4, 5])  # Verifica se 8 não está na lista [1, 2, 3, 4, 5]
print("Python" in "Curso de Python")  # Verifica se "Python" está na string "Curso de Python"
print("Java" not in "Curso de Python")  # Verifica se "Java" não está na string "Curso de Python"
print("Curso" in "Curso de Python")  # Verifica se "Curso" está na string "Curso de Python"

#------------------------------------------------------------------------------------------------#

# Operadores Bitwise em Python
a = 10  # 1010 em binário       
b = 4   # 0100 em binário
print(a & b)  # AND bit a bit (resultado: 0)
print(a | b)  # OR bit a bit (resultado: 14)    
print(a ^ b)  # XOR bit a bit (resultado: 14)
print(~a)  # NOT bit a bit (resultado: -11) 
print(a << 1)  # Deslocamento à esquerda (resultado: 20)
print(a >> 1)  # Deslocamento à direita (resultado: 5)
print(a & 5)  # AND bit a bit com 5 (resultado: 0)
print(a | 5)  # OR bit a bit com 5 (resultado: 15)
print(a ^ 5)  # XOR bit a bit com 5 (resultado: 15)
print(~5)  # NOT bit a bit com 5 (resultado: -6)    
print(a << 2)  # Deslocamento à esquerda por 2 (resultado: 40)
print(a >> 2)  # Deslocamento à direita por 2 (resultado: 2)    

#------------------------------------------------------------------------------------------------#

# Operadores de associação em Python
a = 10  
b = 20
c = 30
print(a is b)  # Verifica se a e b são o mesmo objeto (resultado: False)
print(a is not b)  # Verifica se a e b não são o mesmo objeto (resultado: True)
print(b is c)  # Verifica se b e c são o mesmo objeto (resultado: False)
print(b is not c)  # Verifica se b e c não são o mesmo objeto   
print(a is None)  # Verifica se a é None (resultado: False)
print(b is not None)  # Verifica se b não é None (resultado: True)
print(c is None)  # Verifica se c é None (resultado: False) 
print(a is not None)  # Verifica se a não é None (resultado: True)
print(b is not None)  # Verifica se b não é None (resultado: True)
print(c is not None)  # Verifica se c não é None (resultado: True)
print(a is 10)  # Verifica se a é o mesmo objeto 10 (resultado: True)
print(b is not 20)  # Verifica se b não é o mesmo objeto 20 (resultado: False)
print(c is 30)  # Verifica se c é o mesmo objeto 30 (resultado: True)
print(a is not 10)  # Verifica se a não é o mesmo objeto 10 (resultado: False)
print(b is not 20)  # Verifica se b não é o mesmo objeto 20 (resultado: False)
print(c is not 30)  # Verifica se c não é o mesmo objeto 30 (resultado: False)

#------------------------------------------------------------------------------------------------#


