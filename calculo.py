import sympy as sp
import math as m
from sympy import sin,cos, tan,Expr,ln,log,abc

#Simbolos Utilizados:
x,t,n,e,r,T,P = sp.symbols("x,t,n,e,r,T,P")
pi = sp.pi
letras = ("ABCDEFGHIJKLMNOP")


print("Olá Seja bem Vindo ao Calculapy")
print("----Escolha uma das 3 opções abaixo:----")
print("1 - Derivadas; 2 - Limites; 3 - Integrais")

opcao = int(input("Digite o numero correspondente a questão desejada: "))
while opcao != 1 and opcao != 2 and opcao != 3: #Verificando a resposta do usuario
    print(f"Numero Invalido!")
    opcao = int(input("Digite um numero valido!"))
match opcao: #Validação da resposta
#DERIVADAS:
    case 1:
        print("\nVocê escolheu a questão 1. Informe qual letra gostaria de obter o resultado (A até I):\n")
        opcao_c = input("Digite a letra correspondente: ").upper()  # Upper para transformar em maiúscula

        while opcao_c < "A" or opcao_c > "I" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()

match opcao_c: #Letras
    case "A": #Derivação Direta pela Regra da Potencia(Derivada de x^n)
        print(f"\nEm Analise de Desempenho, o custo total acumulado Ctotal de um processo de parsing (análise sintática) durante um periodo de 10 segundos pode ser determinado integrando.\nse a função de custo instantâneo. Suponha que a taxa de custo instantâneo por segundo, C(t), seja dada por uma combinação de custos fixos e variáveis: C'(t)= 4t3 _ \n6t2 + 2,onde té o tempo em segundos.\nQuestão: Calcule a integral indefinida do custo instantâneo,f C(t)dt, para obter a função de custo total C(t). Use a Propriedade da Integral da Soma (Linearidade).\n")

        funcao_po = 3*n**5 + 7*n**2 + 10
        derivada_po = sp.diff(funcao_po,n)
        resultado_po = derivada_po.subs(n, 100)
        print(f"O valor da operaçao C{funcao_po} é: {resultado_po}")

    case "B":#Derivação Direta Pela Regra do Produto(Derivada de U * V)
        print(f'\nEm processamento de sinais ou otimizaçao, é comum que a taxa de transferencia de dados (T(t)) de um sistema seja modelada como o produto de duas funçoes: a eficiencia do protcolo(E(t)) e\na largura de banda disponivel (B(t)).\nSuponha que, em um intervalo de tempo t, E(t) = (t^2+1) e B(t) = sen(t)\nQuestão: Calcule a derivada da funçao de transferencia T(t) = (t^2+1) * sen(t) ')

        funcao_DDRP = (t**2 + 1) * sin(t)
        derivada_DDRP = sp.diff(funcao_DDRP, t)
        resultado_DDRP = derivada_DDRP.subs(t, pi)
        print(f"O valor da operação é T{funcao_DDRP} é: {resultado_DDRP}")

    case "C": #Derivação Direita pela Regra do Quociente (Derivada de U/V)
        print(f"\nUm especialista em redes de computadores está modelando a latência média (L(r)) de um pacote de dados em uma fila de roteador, onde aé a taxa de chegada de pacotes. \nA função que modela essa latênciaé L(π),onde 0≤π< 100.\nQuestão: Determine a taxa de variaçao instantanea da latencia em relaçäo à taxa de chegada de pacotes, calculando a derivada dL/dX. Qual o valor dessa taxa quando a taxa de chegada depacotes é π =50?\n")

        funcao_q = 5*x / (100-x)
        derivada_q = sp.diff(funcao_q, x)
        resultado_q = derivada_q.subs(x, 50)

        print(f"O Resultado da operaçao {funcao_q} é: {resultado_q}")

    case "D": #Derivação Direta pela Fórmula da Tabela, numero4 (Derivada de sen(x) ou cos(x))
        print(f"\n No desenvolvimento de gráficos de computador (computer graphics), a posição de um objeto em movimento periódico, como uma câmera oscilante, pode ser\n descrita por funçõestrigonométricas. Suponha que a coordenada vertical y da\n câmera seja dada por y(t)=4 cos(t)- 3sen(t),onde té o tempo. \nQuestão: Calcule a função que descreve a velocidade vertical instantânea da camera, v(t)-dY/dT\n")

        funcao_t = 4 * cos(t) - 3 * sin(t)
        derivada_t = sp.diff(funcao_t, t)
        resultado_t = derivada_t

        print(f"O resultado da Operação {funcao_t} é {resultado_t}")

    case "E": #Exponecial Simples(Machine Learning)
        print(f"\n Em aprendizado de máquina (Machine Learning), a função sigmoide,f(x)1/1+e^-x,é crucial para introduzir não-linearidade em redes neurais.\nA derivada dessa função é essencial para o algoritmo de backpropagation.Considere o componente e-. \nQuestão: Calcule a derivada da função g(ar)= e-t.\n")

        funcao_es = sp.exp (-x)
        derivada_es = sp.diff (funcao_es, x)
        resultado_es = derivada_es

        print(f"O resultado da operaçao {funcao_es} é: {resultado_es}")

    case "F": #Logaritimica(Teoria da Informação)
        print(f"\n Em teoria da informação, a quantidade de informação ou entropia muitas vezes envolve logaritmos naturais. Suponha que o desperdicio de memória em um algoritmo de compressão seja modelado pela funçao M(t)= 10ln(t),onde t é a compelixidade de tempo de compressão. \nQuestão: Calcule a taxa de variação instantânea do desperdicio de memoria em relação à   \ncomplexidade de tempo,dM/dT.\n")

        funcao_log = 10* sp.ln (t)
        derivada_log = sp.ln(funcao_log, t)
        resultado_log = derivada_log

        print(f"O resultado da Operaçao {funcao_log} é: {resultado_log}")

    case "G":#Derivação Direta pela Fórmula da Tabela, Numero 7 (Regra da Cadeia Composta Simples)
        print(f"\nUm pesquisador em criptografia está nalisando a segurança de um novo protocolo onde a probabilidade de falha é uma funçao composta.\nA probabilidade,P, Depende da taxa de erro r, e a taxca de erro depende da temperatura T do processador, tal que P(r) = r^3 e r(T) = sen(T)\nQuestão: Calcule a dferivada da probabilidade de falha em relação á temperatura, dP/dT, usando a regra da cadeia")

        funcao_CCS = sin(T)**3
        dPdT= sp.diff(funcao_CCS, T)
        resultado_CCS = dPdT
        print(f"O Resultado da operação {funcao_CCS} é: {resultado_CCS}")

    case "H": #Regra da Cadeia Exponecial
        print(f"\nEm modelagem de crescimento de virus (em software ou biologico) ou em modelagem de falha de hardware, o tempo medio entre falhas (MTBF)pode ter um\ncomportamente exponecial. \nConsidere a função A(t) = 5^2t^2-1, que modela a area de influencia de um malware apos o tempo t\nQuestão: determine a taxa de crescimento instantanea da area de influencia do malware, dA/dt")

        funcao_ce = 5**(2*t**2 - 1)
        dAdT_ce = sp.diff(funcao_ce, t)
        resultado_ce = dAdT_ce

        print(f"O Resultado da operação {funcao_ce} é: {resultado_ce}")

    case "I": #Regra da Cadeia Logaritimica
        print(f"\nNa otimização de consultas em banco de dados, o tempo de busca em uma \nestrutura de dados balanceada (como uma árvore B)é proporcional ao logaritmo do\n número de registros. A complexidade de tempo de uma nova operaçãoé modelada por T(n)=ln(n3+5n). \nQuestão: Calcule a taxa de variação da complexidade de tempo em relação ao número de registros n,%. \n")

        funcao_cl = sp.ln(n**3 + 5*n)
        dTdN_cl = sp.diff(funcao_cl,n)
        resultado_cl = dTdN_cl

        print(f"O Resultado da operação {funcao_cl} é {resultado_cl}")

#Limites:
match opcao:
    case 2:
        print("\nVocê escolheu a questão 2. Informe qual letra gostaria de obter o resultado (A até O):\n")
        opcao_c = input("Digite a letra correspondente: ").upper()  # Upper para transformar em maiúscula
while opcao_c < "A" or opcao_c > "I" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()
