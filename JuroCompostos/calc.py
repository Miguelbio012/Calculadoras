# Solicita o valor do capital

capital = float(input("O valor do capital inserido, será de:"))

# Solicita o valor da taxa de juros
taxa = float(input("O valor da taxa será de:"))

#Tipo de taxa
taxa_tipo = input("A taxa que foi inserida está em mês ou em ano? (Digite 'm' para mensal e 'a' para anual): ").lower()

#Condições para cada tipo

if taxa_tipo == 'a':
    # Converte a taxa anual para mensal usando a fórmula correta
    taxa_anual = taxa / 100  # Converte porcentagem para decimal
    taxaJC = (1 + taxa_anual) ** (1 / 12) - 1
elif taxa_tipo == 'm':
    # Considera a taxa mensal
    taxaJC = taxa / 100
else:
    print("Entrada inválida para o tipo de taxa. Por favor, digite 'm' para mensal ou 'a' para anual.")
    exit()

# Taxa para exclusivamente Juros Compostos.
# taxaJC = taxa / 100

# Nessa primeira variável tempo, ele será indicado em ANOS.
tempoAnos = int(input("O tempo em anos será de:"))

# Transformação de anos -> meses.
tempoMes = tempoAnos * 12

# Agora será declarada a fórmula em juros compostos.

montante = capital * (1 + taxaJC) ** tempoMes

# Apresentação do resultado

print(f"O montante após {tempoMes} meses será de {montante}")
