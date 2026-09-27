# ==============================================================================
# PACOTE DE EXERCÍCIOS: 30 FUNÇÕES EM PYTHON PARA TREINAMENTO
# ==============================================================================
# Este arquivo contém 30 funções simples divididas em categorias:
# - Matemática e Lógica Básica
# - Manipulação de Listas e Laços de Repetição (For/While)
# - Gamificação e RPG (Para aplicar a lógica em mecânicas de jogos)
#
# Cada função possui comentários explicando o que ela faz, os parâmetros que
# recebe e o que retorna. É um excelente material para os alunos importarem
# em seus próprios projetos e testarem os resultados!
# ==============================================================================

import random

# ------------------------------------------------------------------------------
# CATEGORIA 1: MATEMÁTICA E LÓGICA BÁSICA
# ------------------------------------------------------------------------------


def eh_par(numero):
    '''
    Verifica se um número é par.
    Parâmetros:
      numero (int): O número a ser verificado.
    Retorno:
      bool: True se for par, False caso contrário.
    '''
    return numero % 2 == 0


def eh_impar(numero):
    '''
    Verifica se um número é ímpar.
    Parâmetros:
      numero (int): O número a ser verificado.
    Retorno:
      bool: True se for ímpar, False caso contrário.
    '''
    return numero % 2 != 0


def eh_positivo(numero):
    '''
    Verifica se o número é estritamente positivo (maior que zero).
    Parâmetros:
      numero (float/int): O valor a ser avaliado.
    Retorno:
      bool: True se positivo, False se zero ou negativo.
    '''
    return numero > 0


def eh_negativo(numero):
    '''
    Verifica se o número é negativo (menor que zero).
    Parâmetros:
      numero (float/int): O valor a ser avaliado.
    Retorno:
      bool: True se negativo, False se zero ou positivo.
    '''
    return numero < 0


def eh_primo(numero):
    '''
    Verifica se um número inteiro é primo.
    Parâmetros:
      numero (int): O número a ser testado.
    Retorno:
      bool: True se for primo, False caso contrário.
    '''
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True


def calcula_dobro(numero):
    '''
    Calcula o dobro de um valor.
    Parâmetros:
      numero (float/int): O número base.
    Retorno:
      float/int: O dobro do número.
    '''
    return numero * 2


def maior_de_dois(a, b):
    '''
    Compara dois números e retorna o maior deles.
    Parâmetros:
      a, b (float/int): Os números a serem comparados.
    Retorno:
      float/int: O maior número.
    '''
    if a > b:
        return a
    return b


def menor_de_dois(a, b):
    '''
    Compara dois números e retorna o menor deles.
    Parâmetros:
      a, b (float/int): Os números a serem comparados.
    Retorno:
      float/int: O menor número.
    '''
    if a < b:
        return a
    return b


def calcula_media(nota1, nota2, nota3):
    '''
    Calcula a média aritmética de 3 notas.
    Parâmetros:
      nota1, nota2, nota3 (float): As notas do aluno.
    Retorno:
      float: O valor da média.
    '''
    return (nota1 + nota2 + nota3) / 3


def celsius_para_fahrenheit(celsius):
    '''
    Converte uma temperatura de Celsius para Fahrenheit.
    Parâmetros:
      celsius (float): Temperatura em graus Celsius.
    Retorno:
      float: Temperatura equivalente em Fahrenheit.
    '''
    return (celsius * 9/5) + 32


def calcular_area_triangulo(base, altura):
    '''
    Calcula a área de um triângulo usando a fórmula clássica: A = (base * altura) / 2.
    Parâmetros:
      base (float): A medida da base do triângulo.
      altura (float): A medida da altura.
    Retorno:
      float: O valor da área calculada.
    '''
    area = (base * altura) / 2
    return area


def converter_temperatura(celsius):
    '''
    Converte uma temperatura de graus Celsius para Fahrenheit.
    Fórmula: F = (C * 9/5) + 32
    Parâmetros:
      celsius (float): A temperatura em Celsius.
    Retorno:
      float: A temperatura equivalente em Fahrenheit.
    '''
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def calcular_salario(horas_trabalhadas, valor_por_hora):
    '''
    Calcula o salário mensal de um trabalhador.
    Parâmetros:
      horas_trabalhadas (float): Total de horas trabalhadas no mês.
      valor_por_hora (float): Quanto o trabalhador recebe por hora de serviço.
    Retorno:
      float: O salário total a receber.
    '''
    salario = horas_trabalhadas * valor_por_hora
    return salario


def classificar_idade(idade):
    '''
    Classifica um indivíduo em faixas etárias baseadas em sua idade.
    Parâmetros:
      idade (int): A idade da pessoa em anos.
    Retorno:
      str: A categoria correspondente (Infantil, Jovem, Adulto ou Idoso).
    '''
    if idade < 12:
        return "Infantil"
    elif 12 <= idade < 18:
        return "Jovem"
    elif 18 <= idade < 60:
        return "Adulto"
    else:
        return "Idoso"


def classificar_categoria_imc(imc):
    '''
    Recebe o valor numérico do IMC e o classifica nas faixas de saúde.
    Parâmetros:
      imc (float): O valor do Índice de Massa Corporal.
    Retorno:
      str: A classificação oficial de saúde.
    '''
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"


def verificar_aprovacao(nota1, nota2, nota3):
    '''
    Calcula a média de 3 notas e verifica a aprovação (Média >= 7.0).
    Pode ser usado para automatizar as médias da EEB Prof. Ângelo Cascaes Tancredo.
    Parâmetros:
      nota1, nota2, nota3 (float): As três avaliações do trimestre.
    Retorno:
      str: "Aprovado" se a média for maior ou igual a 7, senão "Reprovado".
    '''
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7.0:
        return f"Aprovado (Média: {media:.2f})"
    return f"Reprovado (Média: {media:.2f})"


# ------------------------------------------------------------------------------
# CATEGORIA 2: LISTAS E LAÇOS DE REPETIÇÃO (FOR / WHILE)
# ------------------------------------------------------------------------------

def encontrar_maior_numero(lista_numeros):
    '''
    Percorre uma lista de tamanho N e retorna o maior valor encontrado.
    Parâmetros:
      lista_numeros (list): Uma lista contendo números inteiros ou decimais.
    Retorno:
      float/int: O maior número da lista. Retorna None se a lista estiver vazia.
    '''
    if not lista_numeros:
        return None
    maior = lista_numeros[0]
    for num in lista_numeros:
        if num > maior:
            maior = num
    return maior


def soma_elementos_lista(lista_numeros):
    '''
    Soma todos os valores numéricos presentes em uma lista usando um laço for.
    Parâmetros:
      lista_numeros (list): Uma lista contendo números.
    Retorno:
      float/int: A soma total.
    '''
    soma = 0
    for num in lista_numeros:
        soma += num
    return soma


def encontra_maior_na_lista(lista_numeros):
    '''
    Percorre a lista e encontra o maior valor armazenado.
    Parâmetros:
      lista_numeros (list): Uma lista de números (não deve ser vazia).
    Retorno:
      float/int: O maior valor encontrado.
    '''
    if not lista_numeros:
        return None
    maior = lista_numeros[0]
    for num in lista_numeros:
        if num > maior:
            maior = num
    return maior


def conta_numeros_pares(lista_numeros):
    '''
    Conta quantos números pares existem dentro da lista.
    Parâmetros:
      lista_numeros (list): Lista de números inteiros.
    Retorno:
      int: A quantidade de números pares.
    '''
    contador = 0
    for num in lista_numeros:
        if num % 2 == 0:
            contador += 1
    return contador


def filtra_numeros_positivos(lista_numeros):
    '''
    Cria uma nova lista contendo apenas os números maiores que zero.
    Parâmetros:
      lista_numeros (list): Lista mista de números.
    Retorno:
      list: Uma nova lista apenas com os positivos.
    '''
    positivos = []
    for num in lista_numeros:
        if num > 0:
            positivos.append(num)
    return positivos


def multiplica_lista(lista_numeros, multiplicador):
    '''
    Multiplica todos os elementos da lista por um valor específico.
    Parâmetros:
      lista_numeros (list): Lista de números.
      multiplicador (int/float): O valor pelo qual multiplicar.
    Retorno:
      list: Uma nova lista com os valores multiplicados.
    '''
    resultado = []
    for num in lista_numeros:
        resultado.append(num * multiplicador)
    return resultado


def inverte_lista(lista):
    '''
    Recebe uma lista e retorna os elementos de trás para frente usando while.
    Parâmetros:
      lista (list): Uma lista qualquer.
    Retorno:
      list: A lista em ordem invertida.
    '''
    lista_invertida = []
    indice = len(lista) - 1
    while indice >= 0:
        lista_invertida.append(lista[indice])
        indice -= 1
    return lista_invertida


def verifica_elemento_presente(lista, elemento_procurado):
    '''
    Verifica se um determinado elemento existe na lista.
    Parâmetros:
      lista (list): A lista onde será feita a busca.
      elemento_procurado (any): O valor a ser buscado.
    Retorno:
      bool: True se encontrar, False caso contrário.
    '''
    for item in lista:
        if item == elemento_procurado:
            return True
    return False


def tabuada_completa(numero):
    '''
    Gera uma lista com os resultados da tabuada de 1 a 10 de um número.
    Parâmetros:
      numero (int): O número base da tabuada.
    Retorno:
      list: Uma lista contendo os 10 resultados.
    '''
    resultados = []
    for i in range(1, 11):
        resultados.append(numero * i)
    return resultados


def conta_vogais(texto):
    '''
    Percorre uma string (texto) e conta quantas vogais ela possui.
    Parâmetros:
      texto (str): O texto a ser analisado.
    Retorno:
      int: O número de vogais encontradas.
    '''
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


def remove_duplicatas(lista):
    '''
    Gera uma nova lista removendo os itens que estão repetidos.
    Parâmetros:
      lista (list): Uma lista com possíveis elementos repetidos.
    Retorno:
      list: Uma nova lista apenas com itens únicos.
    '''
    lista_unica = []
    for item in lista:
        if item not in lista_unica:
            lista_unica.append(item)
    return lista_unica


def encontrar_letra(lista_letras, letra_procurada):
    '''
    Percorre uma lista de caracteres para encontrar uma letra específica.
    Parâmetros:
      lista_letras (list): Lista contendo as letras (ex: ['a', 'b', 'c']).
      letra_procurada (str): A letra que o aluno deseja encontrar.
    Retorno:
      bool: True se a letra estiver na lista, False caso contrário.
    '''
    for letra in lista_letras:
        if letra.lower() == letra_procurada.lower():
            return True
    return False


def encontrar_elemento(lista, elemento_procurado):
    '''
    Verifica se um elemento (número, string, etc.) existe dentro da lista e 
    retorna sua posição.
    Parâmetros:
      lista (list): A lista genérica de itens.
      elemento_procurado (any): O item a ser buscado.
    Retorno:
      int: O índice (posição) do elemento na lista, ou -1 se não for encontrado.
    '''
    for i in range(len(lista)):
        if lista[i] == elemento_procurado:
            return i
    return -1


def fatiar_lista(lista, inicio, fim):
    '''
    Fatia (slice) uma lista para pegar apenas um pedaço específico dela.
    Parâmetros:
      lista (list): A lista original.
      inicio (int): O índice onde o corte começa.
      fim (int): O índice onde o corte termina (exclusivo).
    Retorno:
      list: Uma nova lista contendo apenas os elementos do intervalo.
    '''
    return lista[inicio:fim]


def construir_lista(quantidade):
    '''
    Constrói uma lista pedindo ao usuário que digite os dados dinamicamente no terminal.
    Parâmetros:
      quantidade (int): Quantos itens a lista deve ter.
    Retorno:
      list: A lista final preenchida pelo usuário.
    '''
    nova_lista = []
    for i in range(quantidade):
        item = input(f"Digite o valor do {i+1}º elemento: ")
        nova_lista.append(item)
    return nova_lista


def organizar_placar(lista_pontuacoes, ordem_decrescente=False):
    '''
    Organiza a lista de pontuações em ordem crescente ou decrescente[cite: 1].
    Parâmetros:
      lista_pontuacoes (list): Lista contendo os valores numéricos.
      ordem_decrescente (bool): Se True, ordena do maior para o menor.
    Retorno:
      list: Uma nova lista devidamente ordenada.
    '''
    # Clonamos primeiro para não bagunçar a lista original do sistema
    lista_ordenada = lista_pontuacoes.copy()
    lista_ordenada.sort(reverse=ordem_decrescente)
    return lista_ordenada


def extrair_top_jogadores(lista_completa, inicio, fim):
    '''
    Fatia (slice) uma lista para pegar apenas um pedaço específico dela, 
    como o Top 3 jogadores de um ranking[cite: 1].
    Parâmetros:
      lista_completa (list): A lista original.
      inicio (int): O índice onde o corte começa.
      fim (int): O índice onde o corte termina (exclusivo)[cite: 1].
    Retorno:
      list: Uma nova lista contendo apenas os elementos do intervalo.
    '''
    return lista_completa[inicio:fim]


def contar_moedas_inventario(inventario, item_procurado):
    '''
    Conta exatamente quantas vezes um item específico aparece dentro da lista[cite: 1].
    Parâmetros:
      inventario (list): A lista representando os itens caídos/guardados.
      item_procurado (str/any): O nome exato do item a ser contado.
    Retorno:
      int: A quantidade total de vezes que o item foi encontrado.
    '''
    quantidade = inventario.count(item_procurado)
    return quantidade


def criar_backup_inventario(lista_original):
    '''
    Cria uma cópia real e independente na memória, evitando o problema 
    de "espelhamento" (referência) gerado ao usar apenas o sinal de igual.
    Parâmetros:
  lista_original (list): A lista base a ser clonada.
    Retorno:
      list: Uma nova caixa na memória com os dados idênticos, garantindo 
            que alterações no clone não afetem o original
    '''
    clone_perfeito = lista_original.copy()
    return clone_perfeito


# ------------------------------------------------------------------------------
# CATEGORIA 3: ESTÉTICA E IMPRESSÕES NO CONSOLE
# ------------------------------------------------------------------------------

def imprimir_menu_personalizado(itens, valores):
    '''
    Imprime um menu formatado como nota fiscal para exibição no console.
    Parâmetros:
      itens (list): Lista com os nomes dos produtos.
      valores (list): Lista com os preços correspondentes.
    Retorno:
      Nenhum. Apenas exibe no terminal a arte formatada.
    '''
    print("=" * 50)
    print(f"{'CANTINA DA EEB PROF. ÂNGELO CASCAES TANCREDO':^50}")
    print("=" * 50)
    print(f"{'PRODUTO':<35} | {'VALOR':>10}")
    print("-" * 50)

    total = 0
    for i in range(len(itens)):
        print(f"{itens[i]:<35} | R$ {valores[i]:>7.2f}")
        total += valores[i]

    print("-" * 50)
    print(f"{'TOTAL A PAGAR:':<35} | R$ {total:>7.2f}")
    print("=" * 50)


# ------------------------------------------------------------------------------
# CATEGORIA 4: GAMIFICAÇÃO E RPG (Aplicando Lógica)
# ------------------------------------------------------------------------------

def calcula_dano_ataque(poder_ataque, armadura_inimigo):
    '''
    Calcula o dano causado em um monstro, garantindo que não seja negativo.
    Parâmetros:
      poder_ataque (int): O ataque base do herói.
      armadura_inimigo (int): A defesa do monstro.
    Retorno:
      int: O dano final causado (mínimo de 0).
    '''
    dano = poder_ataque - armadura_inimigo
    if dano < 0:
        return 0
    return dano


def calcula_dano_critico(dano_base, eh_critico):
    '''
    Dobra o dano caso o ataque seja considerado um acerto crítico.
    Parâmetros:
      dano_base (int): O dano normal já calculado.
      eh_critico (bool): True se for golpe crítico, False se normal.
    Retorno:
      int: O dano com ou sem o multiplicador crítico.
    '''
    if eh_critico:
        return dano_base * 2
    return dano_base


def pode_equipar_item(nivel_personagem, nivel_minimo_item):
    '''
    Verifica se o personagem tem nível suficiente para equipar uma arma.
    Parâmetros:
      nivel_personagem (int): Nível atual do herói.
      nivel_minimo_item (int): Nível exigido pelo equipamento.
    Retorno:
      bool: True se puder equipar, False caso contrário.
    '''
    return nivel_personagem >= nivel_minimo_item


def filtra_bestiario_perigoso(lista_monstros, nivel_ameaca_minimo):
    '''
    Filtra um bestiário para retornar apenas os monstros mais fortes.
    Parâmetros:
      lista_monstros (list): Lista de listas (ex: [['Goblin', 2], ['Dragão', 50]])
      nivel_ameaca_minimo (int): Nível mínimo para ser considerado perigoso.
    Retorno:
      list: Uma nova lista apenas com o nome dos monstros perigosos.
    '''
    perigosos = []
    for monstro in lista_monstros:
        nome = monstro[0]
        nivel = monstro[1]
        if nivel >= nivel_ameaca_minimo:
            perigosos.append(nome)
    return perigosos


def aplica_pocao_cura(vida_atual, vida_maxima, valor_cura):
    '''
    Aplica cura ao personagem sem deixar ultrapassar a vida máxima.
    Parâmetros:
      vida_atual (int): HP atual do personagem.
      vida_maxima (int): Limite máximo de HP do personagem.
      valor_cura (int): Quanto a poção recupera.
    Retorno:
      int: A nova vida do personagem após o uso da poção.
    '''
    nova_vida = vida_atual + valor_cura
    if nova_vida > vida_maxima:
        return vida_maxima
    return nova_vida


def conta_itens_mochila(mochila, nome_item):
    '''
    Conta quantas unidades de um item específico o herói tem na mochila.
    Parâmetros:
      mochila (list): Lista com os nomes dos itens guardados.
      nome_item (str): O item que estamos procurando (ex: "Poção de Vida").
    Retorno:
      int: A quantidade desse item na mochila.
    '''
    quantidade = 0
    for item in mochila:
        if item == nome_item:
            quantidade += 1
    return quantidade


def calcula_xp_batalha(lista_inimigos_derrotados, xp_por_inimigo):
    '''
    Calcula a experiência total ganha ao fim de um combate.
    Parâmetros:
      lista_inimigos_derrotados (list): Lista com os inimigos vencidos.
      xp_por_inimigo (int): Quanto de XP cada monstro concede.
    Retorno:
      int: O total de experiência acumulada.
    '''
    total_inimigos = len(lista_inimigos_derrotados)
    return total_inimigos * xp_por_inimigo


def verifica_subida_de_nivel(xp_atual, xp_necessaria):
    '''
    Checa se o personagem acumulou experiência suficiente para subir de nível.
    Parâmetros:
      xp_atual (int): A experiência total do personagem.
      xp_necessaria (int): O limiar para alcançar o próximo nível.
    Retorno:
      bool: True se subiu de nível, False se ainda falta XP.
    '''
    return xp_atual >= xp_necessaria


def rola_dado(faces):
    '''
    Simula a rolagem de um dado de RPG (D4, D6, D20, etc).
    Parâmetros:
      faces (int): O número de lados do dado (ex: 20 para um D20).
    Retorno:
      int: Um número sorteado entre 1 e o número de faces.
    '''
    return random.randint(1, faces)


def sorteia_loot(tabela_loot):
    '''
    Sorteia um item aleatório deixado por um inimigo derrotado.
    Parâmetros:
      tabela_loot (list): Uma lista contendo os itens possíveis de cair.
    Retorno:
      str: O nome do item sorteado (ou None se a lista for vazia).
    '''
    if not tabela_loot:
        return None
    indice_sorteado = random.randint(0, len(tabela_loot) - 1)
    return tabela_loot[indice_sorteado]


# ------------------------------------------------------------------------------
# CATEGORIA 5: FÓRMULAS DE FÍSICA E SAÚDE
# ------------------------------------------------------------------------------

def calcular_velocidade_media(distancia, tempo):
    '''
    Calcula a velocidade média de um corpo em movimento (v = d / t).
    Parâmetros:
      distancia (float): O espaço percorrido (em metros ou km).
      tempo (float): O tempo gasto para percorrer o espaço (em segundos ou horas).
    Retorno:
      float: A velocidade média. Retorna 0 se o tempo for zero (evitando erro de sistema).
    '''
    if tempo <= 0:
        return 0
    velocidade = distancia / tempo
    return velocidade


def calcular_imc(peso, altura):
    '''
    Calcula o Índice de Massa Corporal (IMC) básico.
    Fórmula: IMC = peso / altura²
    Parâmetros:
      peso (float): O peso em quilogramas (kg).
      altura (float): A altura em metros (m).
    Retorno:
      float: O valor exato do IMC arredondado para duas casas decimais.
    '''
    imc = peso / (altura ** 2)
    return round(imc, 2)


# ------------------------------------------------------------------------------
# CATEGORIA 6: LAÇOS DE REPETIÇÃO E MATEMÁTICA AVANÇADA
# ------------------------------------------------------------------------------

def separar_pares_impares(lista_numeros):
    '''
    Analisa uma lista mista e separa os números em duas categorias.
    Parâmetros:
      lista_numeros (list): Uma lista de números inteiros.
    Retorno:
      tuple: Duas listas separadas (lista_pares, lista_impares).
    '''
    pares = []
    impares = []
    for num in lista_numeros:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares


def gerar_tabuada(numero):
    '''
    Gera a tabuada completa (de 1 a 10) de um número escolhido.
    Parâmetros:
      numero (int): O número base para a tabuada.
    Retorno:
      list: Uma lista contendo os 10 resultados formatados como strings.
    '''
    resultados = []
    for i in range(1, 11):
        resultados.append(f"{numero} x {i} = {numero * i}")
    return resultados


def somar_ate_n(n):
    '''
    Soma todos os números inteiros de 1 até N usando um laço for.
    Útil para calcular a curva de progressão de experiência no Imperiall World.
    Parâmetros:
      n (int): O limite final da contagem.
    Retorno:
      int: O valor total acumulado.
    '''
    soma_total = 0
    for i in range(1, n + 1):
        soma_total += i
    return soma_total


def contar_pares_ate_cem():
    '''
    Conta exatamente quantos números pares existem no intervalo de 1 a 100.
    Parâmetros:
      Nenhum.
    Retorno:
      int: A quantidade total de números pares encontrados.
    '''
    contador = 0
    for i in range(1, 101):
        if i % 2 == 0:
            contador += 1
    return contador


def calcular_fatorial(n):
    '''
    Calcula o fatorial de um número (n!). Ex: 5! = 5 * 4 * 3 * 2 * 1.
    Parâmetros:
      n (int): O número inteiro positivo a ser calculado.
    Retorno:
        int: O resultado do fatorial. Retorna 1 se N for 0.
    '''
    if n == 0 or n == 1:
        return 1
    fatorial = 1
    for i in range(2, n + 1):
        fatorial *= i
    return fatorial


def gerar_fibonacci(quantidade_termos):
    '''
    Gera os primeiros N termos da famosa Sequência de Fibonacci.
    Parâmetros:
      quantidade_termos (int): Quantos números da sequência gerar.
    Retorno:
      list: Lista contendo a sequência gerada.
    '''
    if quantidade_termos <= 0:
        return []
    elif quantidade_termos == 1:
        return [0]

    sequencia = [0, 1]
    while len(sequencia) < quantidade_termos:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia


# ------------------------------------------------------------------------------
# CATEGORIA 7: MATEMÁTICA AVANÇADA E GEOMETRIA
# ------------------------------------------------------------------------------

def calcular_potencia_manual(base, expoente):
    '''
    Calcula a potência (base^expoente) usando um laço for, sem usar o operador **.
    Parâmetros:
      base (int/float): O número que será multiplicado.
      expoente (int): Quantas vezes a base será multiplicada por ela mesma.
    Retorno:
      float/int: O resultado da potência.
    '''
    if expoente == 0:
        return 1

    resultado = 1
    for _ in range(abs(expoente)):
        resultado *= base

    if expoente < 0:
        return 1 / resultado
    return resultado


def calcular_bhaskara(a, b, c):
    '''
    Calcula as raízes de uma equação do 2º grau usando a fórmula de Bhaskara.
    Parâmetros:
      a, b, c (float): Os coeficientes da equação ax² + bx + c = 0.
    Retorno:
      tuple/str: As duas raízes (x1, x2) ou uma mensagem informando que não há raízes reais.
    '''
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        return "A equação não possui raízes reais (Delta negativo)."

    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)
    return round(x1, 2), round(x2, 2)


def calcular_distancia_pontos(x1, y1, x2, y2):
    '''
    Calcula a distância entre dois pontos (x1,y1) e (x2,y2) no plano cartesiano.
    Parâmetros:
      x1, y1 (float): Coordenadas do primeiro ponto.
      x2, y2 (float): Coordenadas do segundo ponto.
    Retorno:
      float: A distância exata entre eles.
    '''
    distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return round(distancia, 2)


def calcular_termo_pa(a1, n, r):
    '''
    Encontra o enésimo termo de uma Progressão Aritmética (P.A.).
    Fórmula: an = a1 + (n - 1) * r
    Parâmetros:
      a1 (float): O primeiro termo da P.A.
      n (int): A posição do termo que queremos descobrir.
      r (float): A razão (de quanto em quanto a P.A. cresce).
    Retorno:
      float: O valor do termo na posição N.
    '''
    an = a1 + (n - 1) * r
    return an


def calcular_termo_pg(a1, n, r):
    '''
    Encontra o enésimo termo de uma Progressão Geométrica (P.G.).
    Fórmula: an = a1 * (r ** (n - 1))
    Parâmetros:
      a1 (float): O primeiro termo da P.G.
      n (int): A posição do termo que queremos descobrir.
      r (float): A razão multiplicativa.
    Retorno:
      float: O valor do termo na posição N.
    '''
    an = a1 * (r ** (n - 1))
    return an


def calcular_bhaskara(a, b, c):
    '''
    Calcula as raízes de uma equação do 2º grau usando a fórmula de Bhaskara.
    Parâmetros:
      a, b, c (float): Coeficientes da equação ax² + bx + c = 0.
    Retorno:
      tuple/str: As raízes da equação ou uma mensagem de aviso se delta < 0.
    '''
    delta = (b ** 2) - (4 * a * c)

    if delta < 0:
        return "A equação não possui raízes reais (Delta negativo)."

    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)

    return round(x1, 2), round(x2, 2)


def teorema_pitagoras(cateto_a, cateto_b):
    '''
    Calcula o valor da hipotenusa em um triângulo retângulo.
    Fórmula: c² = a² + b²
    Parâmetros:
      cateto_a, cateto_b (float): Os dois lados menores do triângulo.
    Retorno:
      float: O comprimento da hipotenusa.
    '''
    hipotenusa = ((cateto_a ** 2) + (cateto_b ** 2)) ** 0.5
    return round(hipotenusa, 2)


def juros_compostos(capital, taxa_mensal, meses):
    '''
    Calcula o montante final de um investimento com juros sobre juros.
    Fórmula: M = C * (1 + i)^t
    Parâmetros:
      capital (float): O valor inicial investido.
      taxa_mensal (float): A taxa de juros em porcentagem (ex: 5 para 5%).
      meses (int): Tempo da aplicação.
    Retorno:
      float: O valor total acumulado.
    '''
    taxa_decimal = taxa_mensal / 100
    montante = capital * ((1 + taxa_decimal) ** meses)
    return round(montante, 2)


def calcular_ponto_medio(x1, y1, x2, y2):
    '''
    Encontra as coordenadas exatas do ponto médio de um segmento de reta.
    Fórmula: M = ((x1 + x2) / 2, (y1 + y2) / 2)
    Parâmetros:
      x1, y1 (float): Coordenadas do ponto A no plano cartesiano.
      x2, y2 (float): Coordenadas do ponto B.
    Retorno:
      tuple: As coordenadas (x, y) do ponto central.
    '''
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return round(mx, 2), round(my, 2)


def calcular_volume_cilindro(raio, altura):
    '''
    Calcula o espaço interno (volume) de um cilindro.
    Fórmula: V = π * r² * h
    Parâmetros:
      raio (float): A medida do raio da base circular.
      altura (float): A altura do cilindro.
    Retorno:
      float: O volume calculado em unidades cúbicas.
    '''
    pi = 3.14159
    volume = pi * (raio ** 2) * altura
    return round(volume, 2)


def calcular_distancia_origem(x, y, z):
    '''
    Calcula a distância de um ponto no espaço 3D até a origem (0,0,0).
    Fórmula: d = √(x² + y² + z²)
    Parâmetros:
      x, y, z (float): Coordenadas espaciais do ponto.
    Retorno:
      float: A distância linear absoluta.
    '''
    distancia = (x**2 + y**2 + z**2) ** 0.5
    return round(distancia, 2)

# ------------------------------------------------------------------------------
# CATEGORIA 8: FÍSICA APLICADA
# ------------------------------------------------------------------------------


def converter_kmh_para_ms(velocidade_kmh):
    '''
    Converte uma velocidade de Quilômetros por hora (km/h) para Metros por segundo (m/s).
    Parâmetros:
      velocidade_kmh (float): Velocidade em km/h.
    Retorno:
      float: Velocidade equivalente em m/s.
    '''
    velocidade_ms = velocidade_kmh / 3.6
    return round(velocidade_ms, 2)


def calcular_posicao_mru(posicao_inicial, velocidade, tempo):
    '''
    Calcula a posição final de um objeto em Movimento Retilíneo Uniforme (MRU).
    Fórmula: S = S0 + v * t
    Parâmetros:
      posicao_inicial (float): Posição inicial (S0).
      velocidade (float): Velocidade constante (v).
      tempo (float): Tempo de percurso (t).
    Retorno:
      float: A posição final (S).
    '''
    posicao_final = posicao_inicial + (velocidade * tempo)
    return posicao_final


def calcular_energia_cinetica(massa, velocidade):
    '''
    Calcula a energia de movimento de um corpo.
    Fórmula: Ec = (m * v²) / 2
    Parâmetros:
      massa (float): A massa do corpo em kg.
      velocidade (float): A velocidade em m/s.
    Retorno:
      float: A energia cinética em Joules (J).
    '''
    energia = (massa * (velocidade ** 2)) / 2
    return round(energia, 2)


def calcular_forca_resultante(massa, aceleracao):
    '''
    Calcula a força aplicada sobre um corpo, usando a 2ª Lei de Newton.
    Fórmula: F = m * a
    Parâmetros:
      massa (float): Massa em kg.
      aceleracao (float): Aceleração em m/s².
    Retorno:
      float: A força resultante em Newtons (N).
    '''
    forca = massa * aceleracao
    return round(forca, 2)


def calcular_lei_ohm(resistencia, corrente):
    '''
    Calcula a tensão elétrica em um circuito resistivo usando a 1ª Lei de Ohm.
    Fórmula: V = R * I
    Parâmetros:
      resistencia (float): Resistência em Ohms (Ω).
      corrente (float): Corrente elétrica em Amperes (A).
    Retorno:
      float: A tensão elétrica em Volts (V).
    '''
    tensao = resistencia * corrente
    return round(tensao, 2)


# ==============================================================================
# CATEGORIA 9: MANIPULAÇÃO DE STRINGS E LINGUAGEM
# ==============================================================================

def analisar_morfologia_didatica(frase):
    '''
    Simula uma inteligência artificial básica verificando palavras em 
    uma mini base de dados (listas) embutida no código.
    Parâmetros:
      frase (str): O texto digitado pelo usuário.
    Retorno:
      dict: Um dicionário com a contagem de verbos e adjetivos encontrados.
    '''
    # Nossa "Base de Dados" simulada para a aula na EEB Prof. Ângelo Cascaes Tancredo
    banco_verbos = ['correr', 'estudar', 'programar', 'fazer', 'ler', 'comer']
    banco_adjetivos = ['rápido', 'inteligente',
                       'difícil', 'fácil', 'bom', 'legal']

    # Limpeza e separação da string
    palavras = frase.lower().replace('.', '').replace(',', '').split()

    contagem = {
        "verbos_encontrados": 0,
        "adjetivos_encontrados": 0,
        "palavras_desconhecidas": 0
    }

    for palavra in palavras:
        if palavra in banco_verbos:
            contagem["verbos_encontrados"] += 1
        elif palavra in banco_adjetivos:
            contagem["adjetivos_encontrados"] += 1
        else:
            contagem["palavras_desconhecidas"] += 1

    return contagem


def contar_consoantes(texto):
    '''
    Conta quantas consoantes existem em uma string, ignorando espaços e pontuações.
    Parâmetros:
      texto (str): A frase a ser analisada.
    Retorno:
      int: Quantidade total de consoantes.
    '''
    vogais_e_simbolos = 'aeiouáéíóúãõâêîôû.,!? -_'
    contador = 0

    for caractere in texto.lower():
        # Se for uma letra (isalpha) e NÃO estiver na lista de vogais
        if caractere.isalpha() and caractere not in vogais_e_simbolos:
            contador += 1

    return contador


# ==============================================================================
# CATEGORIA 10: CÁLCULOS PERCENTUAIS E ESTATÍSTICA
# ==============================================================================

def descobrir_porcentagem(parte, total):
    '''
    Descobre quantos por cento (%) um valor menor representa do valor total.
    Fórmula: (parte / total) * 100
    Parâmetros:
      parte (float): O valor ou quantidade parcial.
      total (float): O valor total que representa os 100%.
    Retorno:
      float: O valor em porcentagem. Retorna 0 se o total for nulo.
    '''
    if total <= 0:
        return 0

    porcentagem = (parte / total) * 100
    return round(porcentagem, 2)


def calcular_acrescimo_percentual(valor_base, percentual):
    '''
    Aplica um aumento percentual sobre um valor (ex: juros ou buff de ataque).
    Parâmetros:
      valor_base (float): O número original.
      percentual (float): A taxa de aumento (ex: 15 para 15%).
    Retorno:
      float: O novo valor acrescido.
    '''
    aumento = valor_base * (percentual / 100)
    return round(valor_base + aumento, 2)


def exibe_relatorio_aproveitamento(nome_aluno, acertos, total_questoes):
    '''
    Imprime um relatório formatado usando o cálculo percentual para exibir
    o desempenho acadêmico.
    '''
    taxa = descobrir_porcentagem(acertos, total_questoes)

    print("=" * 45)
    print(f"{'EEB PROF. ÂNGELO CASCAES TANCREDO':^45}")
    print("=" * 45)
    print(f"Aluno(a): {nome_aluno:<25}")
    print(f"Desempenho: {acertos} corretas de {total_questoes} totais")
    print(f"Taxa de Aproveitamento: {taxa}%")

    if taxa >= 70:
        print("Status do Sistema: [ APROVADO ]")
    else:
        print("Status do Sistema: [ REVISÃO NECESSÁRIA ]")
    print("-" * 45)


# ==============================================================================
# MÓDULO DE INTELIGÊNCIA: CRIPTOGRAFIA E DESCRIPTOGRAFIA
# ==============================================================================

def criptografar_mensagem(texto, chave_deslocamento):
    '''
    Criptografa uma string deslocando seus caracteres na tabela ASCII.
    Parâmetros:
      texto (str): A mensagem original.
      chave_deslocamento (int): O número de "casas" para pular no alfabeto.
    Retorno:
      str: A mensagem criptografada.
    '''
    texto_criptografado = ""

    for letra in texto:
        # Verifica se o caractere é uma letra do alfabeto (ignora espaços e pontuações)
        if letra.isalpha():
            # Descobre o código numérico da letra na tabela ASCII
            codigo_ascii = ord(letra)
            # Aplica o deslocamento matemático
            novo_codigo = codigo_ascii + chave_deslocamento
            # Converte o número de volta para caractere e guarda no acumulador
            texto_criptografado += chr(novo_codigo)
        else:
            # Mantém espaços e símbolos inalterados
            texto_criptografado += letra

    return texto_criptografado


def descriptografar_mensagem(texto_secreto, chave_deslocamento):
    '''
    Reverte a criptografia subtraindo a chave de deslocamento.
    '''
    texto_descriptografado = ""

    for letra in texto_secreto:
        if letra.isalpha():
            codigo_ascii = ord(letra)
            # Operador de subtração para desfazer a conversão
            novo_codigo = codigo_ascii - chave_deslocamento
            texto_descriptografado += chr(novo_codigo)
        else:
            texto_descriptografado += letra

    return texto_descriptografado


def sominha(num1, num2):
    soma = num1 + num2
    print(f"A soma é {soma}")
    return soma


def perimetro(lado1, lado2, lado3):
    perim = lado1 + lado2 + lado3
    print(f"O perímetro é {perim}")
    return perim


def minha_nota():
    print("=" * 50)
    print(f"{'CUPOM FISCAL':^50}")
    print(f"{'PRODUTO':<35} | {'VALOR':>10}")
    for i in range(1, 5):
        print(f"{'PRODUTO':<35} | {'VALOR':>10}")
        print(f"{'PRODUTO':<35} | {'VALOR':>10}")
        print(f"{'PRODUTO':<35} | {'VALOR':>10}")


def saldinho(valor_usuario):
    notebook = 3000
    saldo = valor_usuario - notebook
    if saldo >= 0:
        print("Você conseguiu, mandou bem!")
    else:
        print("Saldo insuficiente.")


def impressão_personal_qtd_caract(qtd):
    print("-" * qtd)
    print(f"{'CASA DO CÓDIGO':^qtd}")
    print("-" * qtd)
    print(f"{'EDUARDO KAZENSKI':^qtd}")
    print("-" * qtd)
