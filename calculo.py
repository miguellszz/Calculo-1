import sympy as sp
import math as m
from sympy import sin,cos, tan,Expr,ln,log,abc

#Simbolos Utilizados:
x,t,n,e = sp.symbols("x,t,n,e")

letras = ("ABCDEFGHI")


print("Olá Seja bem Vindo ao Calculapy")
print("----Escolha uma das 3 opções abaixo:----")
print("1 - Derivadas; 2 - Limites; 3 - Integrais")

opcao = int(input("Digite o numero correspondente a questão desejada: "))
while opcao != 1 and opcao != 2 and opcao != 3: #Verificando a resposta do usuario
    print(f"Numero Invalido!")
    opcao = int(input("Digite um numero valido!"))
match opcao: #Validação da resposta
    case 1:
        print("\nVocê escolheu a questão 1. Informe qual letra gostaria de obter o resultado (A até I):\n")
        opcao_c = input("Digite a letra correspondente: ").upper()  # Upper para transformar em maiúscula

        while opcao_c < "A" or opcao_c > "I" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()

match opcao_c: #Letras
    case "A":
        print(f"\nEm Analise de Desempenho, o custo total acumulado Ctotal de um processo de parsing (análise sintática) durante um periodo de 10 segundos pode ser determinado integrando.\nse a função de custo instantâneo. Suponha que a taxa de custo instantâneo por segundo, C(t), seja dada por uma combinação de custos fixos e variáveis: C'(t)= 4t3 _ \n6t2 + 2,onde té o tempo em segundos.\nQuestão: Calcule a integral indefinida do custo instantâneo,f C(t)dt, para obter a função de custo total C(t). Use a Propriedade da Integral da Soma (Linearidade).\n")

        funcao_po = 3*n**5 + 7*n**2 + 10
        derivada_po = sp.diff(funcao_po,n)
        resultado_po = derivada_po.subs(n, 100)
        print(f"O valor da operaçao C{funcao_po} é: {resultado_po}")
    case "C":
        print(f"\nUm especialista em redes de computadores está modelando a latência média (L(r)) de um pacote de dados em uma fila de roteador, onde aé a taxa de chegada de pacotes. \nA função que modela essa latênciaé L(π),onde 0≤π< 100.\nQuestão: Determine a taxa de variaçao instantanea da latencia em relaçäo à taxa de chegada de pacotes, calculando a derivada dLdX. Qual o valor dessa taxa quando a taxa de chegada depacotes é π =50?\n")

        funcao_q = 5*x / (100-x)
        derivada_q = sp.diff(funcao_q, x)
        resultado_q = derivada_q.subs(x, 50)

        print(f"O Resultado da operaçao {funcao_q} é: {resultado_q}")
    case "D":
        print(f"\n No desenvolvimento de gráficos de computador (computer graphics), a posição de um objeto em movimento periódico, como uma câmera oscilante, pode ser\n descrita por funçõestrigonométricas. Suponha que a coordenada vertical y da\n câmera seja dada por y(t)=4 cos(t)- 3sen(t),onde té o tempo. Questão: Calcule a função que descreve a velocidade vertical instantânea da camera, v(t)-\n")
        funcao_t = 4 * cos(t) - 3 * sin(t)
        derivada_t = sp.diff(funcao_t, t)
        resultado_t = derivada_t

        print(f"O resultado da Operação {funcao_t} é {resultado_t}")

"""#Trigonometria D
funcao_t = 4 * cos(t) - 3 * sin(t)
derivada_t = sp.diff(funcao_t, t)
resultado_t = derivada_t

print(f"O resultado da Operação {funcao_t} é {resultado_t}")

#exponecial simples E:
funcao_es = sp.exp (-x)
derivada_es = sp.diff (funcao_es, x)
resultado_es = derivada_es
print(f"O resultado da operaçao {funcao_es} é: {resultado_es}")


#Logaritimica F: 
funcao_log = 10* sp.ln (t)
derivada_log = sp.ln(funcao_log, t)
resultado_log = derivada_log
print(f"O resultado da Operaçao {funcao_log} é: {resultado_log}")

#Regra da Cadeia exponecial H: 
funcao_ce = 5**(2*t**2 - 1)
dAdT_ce = sp.diff(funcao_ce, t)
resultado_ce = dAdT_ce
print(f"O Resultado da operação {funcao_ce} é: {resultado_ce}")

#Regra da Cadeia Logaritmica I:

funcao_cl = sp.ln(n**3 + 5*n)
dTdN_cl = sp.diff(funcao_cl,n)
resultado_cl = dTdN_cl
print(f"O Resultado da operação {funcao_cl} é {resultado_cl}")"""