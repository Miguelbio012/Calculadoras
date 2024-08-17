# Calculadora de arranjo e combinação
import math #Essa biblioteca ja está imbutida no python e será usada para transformar os números em fatoriais

# Escolha para saber qual método de resolução será usado
tipoQuestao = input("A questão será solucionada com o método de ARRANJO ou Combinação? (Digite 'a' para arranjo e 'c' para combinação e 'cs' para combinação simples) ").lower()

#Condição para realização das fórmulas
if tipoQuestao == 'a' :
    #Usará a fórmula de ARRANJO
    totalOP = int(input("Quais são as opções totais ? ")) #Opções totais
    restriOP = int(input("Quais são as opções restritas ? ")) #Opções restritas

    fatorialTotal = math.factorial(totalOP) #Transformando o número de opções totais em fatorial
    fatorialRestrito = math.factorial(restriOP) #Transformando o número de opções restritas em fatorial

    dividendo = totalOP - restriOP #

    fatdiv = math.factorial(dividendo) #

    Arranjo = fatorialTotal / fatdiv #

    print(f"O resultado dessa questão, usando o método de arranjo será de: {int(Arranjo)} arranjos.")

elif tipoQuestao == 'c' :
    #Userá a fórmula de COMBINAÇÃO
    OP_total = int(input("Quais são as opções totais ? ")) #Opções totais
    OP_rest = int(input("Quais são as opções restritas ? ")) #Opções restritas

    fat_total = math.factorial(OP_total)
    fat_rest = math.factorial(OP_rest)

    Combinacao = fat_total / fat_rest * ( 1 / math.factorial(OP_total - OP_rest))

    print(f"O resultado dessa questão usando o método de combinação foi de: {int(Combinacao)} combinações.")

elif tipoQuestao == 'cs' : # Para combinação simples usando apenas fatorial
    # Usará apenas a formula de fatorial comum
    quest_fat = int(input("Qual numero deseja fazer a combinação simples ?? "))
    # Agora irá transformar o número inserido em seu fatorial 
    fat_Total = math.factorial(quest_fat)

    print(f"O resultado do seu fatorial será de {int(fat_Total)}") 

else :
    print("O valor inserido não foi identificado, por favor tente novamente").exit()