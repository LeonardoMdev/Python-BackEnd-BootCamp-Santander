#------------------------------------------------------------------------------------------------#
# Identação de Blocos de Código
def sacar(self, valor: float) -> None: #Inicio do bloco do método sacar
    if valor > 0: # Verifica se o valor do saque é positivo
        # Bloco de código para realizar o saque
        if self.saldo >= valor: # Verifica se o valor do saque é positivo e se há saldo suficiente
            self.saldo -= valor # Atualiza o saldo subtraindo o valor do saque
            print(f'Saque de R$ {valor:.2f} realizado com sucesso!') 
        else:
            print('Saldo insuficiente para realizar o saque.')
    else:
        print('Valor de saque deve ser positivo.') 
# Fim do bloco do método sacar (IF)



#------------------------------------------------------------------------------------------------#
# Estruturas Condicionais e de Repetição






