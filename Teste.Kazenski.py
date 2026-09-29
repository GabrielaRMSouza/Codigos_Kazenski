# SIMULADO KAZENSKI — RODADA 1
# Imagine que você foi contratada para desenvolver um pequeno sistema para uma biblioteca escolar.
# A biblioteca quer controlar o empréstimo de livros.
# Cada aluno possui uma quantidade de livros que pode pegar emprestados de acordo com seu tipo de 
# cadastro:
# Comum: pode ter até 2 livros emprestados.
# Monitor: pode ter até 4 livros emprestados.
# Professor: pode ter até 6 livros emprestados.

# O sistema deve receber:
# O tipo de cadastro do usuário.
# A quantidade de livros que ele já possui emprestados.
# A quantidade de livros que ele deseja pegar agora.

# O sistema deve verificar se, após o novo empréstimo, o usuário continuará dentro do limite permitido.
# Por exemplo:
# Um aluno comum possui 1 livro e quer pegar mais 1.
# Ele ficará com:
# 1 + 1 = 2 livros
# Portanto, o empréstimo pode ser realizado.
# Mas se ele possuir 2 livros e quiser pegar mais 1:
# 2 + 1 = 3 livros
# Nesse caso, ultrapassaria o limite.
#---------------------------------------------------------------------------------------------------
# 1. Interpretação
# Explique com suas palavras qual é o problema que o programa precisa resolver.

# 2. Entradas
# Quais informações o programa precisa receber?

# 3. Processamento
# O que o programa precisa fazer com essas informações para descobrir se o empréstimo pode ser realizado?

# 4. Decisão
# Qual condição precisa ser verdadeira para o sistema permitir o empréstimo?

# 5. Fluxograma

# 6. Código
# Faça o código em Python que você acha que resolveria o problema.

# 7. Explicação
# Escolha uma parte do seu próprio código e explique linha por linha o que ela faz.

#------------------------------------------------------------------------------------------------------

# 1. O programa precisa controlar empréstimos de uma biblioteca e verificar a quantidade de livros
# que cada usuario tem direito de pegar emprestado, dependendo do seu tipo de cadastro
# (comum, monitor e professor)
# 
# 2. O programa precisa saber o tipo do cadastro do usuário, a quantidade de livros que ele já possui
# emprestado e a quantidade de livros que ele deseja pegar agora. (só de curiosidade, e se o usuário
# digitado não tenha sido cadastrado? O que vai acontecer? Ou se o usuário ainda não tiver
# livro algum? Como o programa vai lidar com isso? E se digitar um número negativo? KKKKKK ) 

# 3. O programa precisa somar a quantidade de livros que o usuário já possui com a quantidade de 
#livros que ele deseja pegar e verificar se o resultado dessa soma é menor ou igual do 
#limite permitido do usuário digitado.

# 4. A condição que precisa ser verdadeira para o sistema aceitar o empréstimo é que a soma da 
#quantidade de livros que o usuário já possui com a quantidade de livros que ele deseja pegar 
#seja menor ou igual ao limite do usuário selecionado.

# 5. INICIO - Pedir o tipo de cadastro do usuário - Pedir a quantidade de livros que ele já possui - 
# Pedir a quantidade de livros que ele deseja pegar agora - O resultado da soma é menor ou igual ao 
#limite do usuário selecionado? - SIM - Empréstimo realizado - NÃO - Empréstimo não realizado - FIM

# 6.
tipo_cadastro = input("Digite o tipo de cadastro do usuário (Comum, Monitor, Professor): ").lower()
quantidade_emprestada = int(input("Digite a quantidade de livros que o usuário já possui emprestados: "))
quantidade_desejada = int(input("Digite a quantidade de livros que o usuário deseja pegar agora: "))

if tipo_cadastro == "comum":
    limite = 2
elif tipo_cadastro == "monitor":
    limite = 4
elif tipo_cadastro == "professor":
    limite = 6
else:
    limite = 0
    print("Tipo de cadastro inválido.")
if limite > 0:
    if quantidade_emprestada + quantidade_desejada <= limite:
        print("Empréstimo realizado.")
    else:
        print("Empréstimo não realizado. Limite excedido.")
# 7.  Escolhi a parte do código que verifica o tipo de cadastro do usuário e define o limite de livros
# que ele pode pegar emprestado. A primeira linha verifica se o tipo de cadastro é "Comum" ou "comum",
#"Monitor" ou "monitor", e "Professor" ou "professor". Dependendo do tipo selecionado, o limite de livros
# é definido como 2, 4 ou 6. Em seguida, o programa verifica se a soma da quantidade de livros com os
#livros que o usuário deseja pegar é menor ou igual ao limite definido. Se for, o empréstimo é realizado,
# caso contrário, o empréstimo não é realizado e uma mensagem de limite exedido é exibida.