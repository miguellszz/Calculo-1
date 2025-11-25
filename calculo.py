import sympy as sp
import math as m
from sympy import sin,cos, tan,Expr,ln,log,abc,tan

#Simbolos Utilizados:
#RQ = RAIZ QUADRADA
x,t,n,e,r,T,P,u,tg = sp.symbols("x,t,n,e,r,T,P,u,tg")
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
        while opcao_c < "A" or opcao_c > "P" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()

        match opcao_c: #Letras
                    case "A": #Derivação Direta pela Regra da Potencia(Derivada de x^n)
                        print(f"\nEm Analise de Desempenho, o custo total acumulado Ctotal de um processo de parsing (análise sintática) durante um periodo de 10 segundos pode ser determinado integrando.\nse a função de custo instantâneo. Suponha que a taxa de custo instantâneo por segundo, C(t), seja dada por uma combinação de custos fixos e variáveis: C'(t)= 4t3 _ \n6t2 + 2,onde té o tempo em segundos.\nQuestão: Calcule a integral indefinida do custo instantâneo,f C(t)dt, para obter a função de custo total C(t). Use a Propriedade da Integral da Soma (Linearidade).\n")

                        funcao_po = 3*n**5 + 7*n**2 + 10
                        derivada_po = sp.diff(funcao_po,n)
                        resultado_po = derivada_po.subs(n, 100)
                        print(f"O Resultado da Operação é: {resultado_po}")

                    case "B":#Derivação Direta Pela Regra do Produto(Derivada de U * V)
                        print(f'\nEm processamento de sinais ou otimizaçao, é comum que a taxa de transferencia de dados (T(t)) de um sistema seja modelada como o produto de duas funçoes: a eficiencia do protcolo(E(t)) e\na largura de banda disponivel (B(t)).\nSuponha que, em um intervalo de tempo t, E(t) = (t^2+1) e B(t) = sen(t)\nQuestão: Calcule a derivada da funçao de transferencia T(t) = (t^2+1) * sen(t) ')

                        funcao_DDRP = (t**2 + 1) * sin(t)
                        derivada_DDRP = sp.diff(funcao_DDRP, t)
                        resultado_DDRP = derivada_DDRP.subs(t, pi)
                        print(f"O Resultado da Operação é: {resultado_DDRP}")

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

                        print(f"O Resultado da Operação é {resultado_t}")

                    case "E": #Exponecial Simples(Machine Learning)
                        print(f"\n Em aprendizado de máquina (Machine Learning), a função sigmoide,f(x)1/1+e^-x,é crucial para introduzir não-linearidade em redes neurais.\nA derivada dessa função é essencial para o algoritmo de backpropagation.Considere o componente e-. \nQuestão: Calcule a derivada da função g(ar)= e-t.\n")

                        funcao_es = sp.exp (-x)
                        derivada_es = sp.diff (funcao_es, x)
                        resultado_es = derivada_es
                        print(f"O Resultado da operaçao é: {resultado_es}")

                    case "F": #Logaritimica(Teoria da Informação)
                        print(f"\n Em teoria da informação, a quantidade de informação ou entropia muitas vezes envolve logaritmos naturais. Suponha que o desperdicio de memória em um algoritmo de compressão seja modelado pela funçao M(t)= 10ln(t),onde t é a compelixidade de tempo de compressão. \nQuestão: Calcule a taxa de variação instantânea do desperdicio de memoria em relação à   \ncomplexidade de tempo,dM/dT.\n")

                        funcao_log = 10* sp.ln (t)
                        derivada_log = sp.ln(funcao_log, t)
                        resultado_log = derivada_log

                        print(f"O Resultado da Operaçao é: {resultado_log}")

                    case "G":#Derivação Direta pela Fórmula da Tabela, Numero 7 (Regra da Cadeia Composta Simples)
                        print(f"\nUm pesquisador em criptografia está nalisando a segurança de um novo protocolo onde a probabilidade de falha é uma funçao composta.\nA probabilidade,P, Depende da taxa de erro r, e a taxca de erro depende da temperatura T do processador, tal que P(r) = r^3 e r(T) = sen(T)\nQuestão: Calcule a dferivada da probabilidade de falha em relação á temperatura, dP/dT, usando a regra da cadeia")

                        funcao_CCS = sin(T)**3
                        dPdT= sp.diff(funcao_CCS, T)
                        resultado_CCS = dPdT

                        print(f"O Resultado da Operação é: {resultado_CCS}")

                    case "H": #Regra da Cadeia Exponecial
                        print(f"\nEm modelagem de crescimento de virus (em software ou biologico) ou em modelagem de falha de hardware, o tempo medio entre falhas (MTBF)pode ter um\ncomportamente exponecial. \nConsidere a função A(t) = 5^2t^2-1, que modela a area de influencia de um malware apos o tempo t\nQuestão: determine a taxa de crescimento instantanea da area de influencia do malware, dA/dt")

                        funcao_ce = 5**(2*t**2 - 1)
                        dAdT_ce = sp.diff(funcao_ce, t)
                        resultado_ce = dAdT_ce

                        print(f"O Resultado da Operação é: {resultado_ce}")

                    case "I": #Regra da Cadeia Logaritimica
                        print(f"\nNa otimização de consultas em banco de dados, o tempo de busca em uma \nestrutura de dados balanceada (como uma árvore B)é proporcional ao logaritmo do\n número de registros. A complexidade de tempo de uma nova operaçãoé modelada por T(n)=ln(n3+5n). \nQuestão: Calcule a taxa de variação da complexidade de tempo em relação ao número de registros n,%. \n")

                        funcao_cl = sp.ln(n**3 + 5*n)
                        dTdN_cl = sp.diff(funcao_cl,n)
                        resultado_cl = dTdN_cl

                        print(f"O Resultado da Operação é {resultado_cl}")

                    case "J":
                        print(f"Em teoria da computação, um algoritmo de força bruta possui um tempo de execução que dobra a cada novo elemento inserido. A função de tempo é dada por:T(n)=2nT(n) = 2^nT(n)=2n\nQuestão: Determine a taxa de crescimento instantânea T(n).")
                        derivada_IMP = sp.Function('theta')(x)

                        equacao = sp.tan(derivada_IMP) - x**2

                        dT_dx = sp.diff(equacao, x)
                        resultado_IMP = sp.solve(dT_dx, sp.diff(derivada_IMP, x))[0]

                        print(f"O Resultado da Operação é: {resultado_IMP}")

                    case "K":
                        print(f"\nPara converter coordenadas de um mundo 3D para um ângulo de visão, utiliza-se frequentemente a função arco-tangente. Considere a função:y(x)=arctan(x)y(x) = arctan(x)y(x)=arctan(x) \nQuestão: Encontre a derivada y(x).")
                        funcao_PA = sp.atan(x)
                        derivada_PA = sp.diff(funcao_PA,x)
                        resultado_PA = derivada_PA

                        print(f"O Resultado da Operação é {resultado_PA}")

                    case "L":
                        print(f"Uma rede neural simples utiliza uma função baseada na exponencial negativa para ativação.Seja a função: f(x)=e-2xf(x) = e^-2xf(x)=e-2x \nQuestão: Calcule f(x)f'(x)f(x) utilizando a regra da cadeia.")
                        funcao_FA = sp.exp(-2*x)
                        derivada_FA = sp.diff(funcao_FA,x)
                        resultado_FA = derivada_FA

                        print(f"O Resultado da Operação é {resultado_FA}")
                    case "M":
                        print(f"\nVocê está modelando a eficiência de um processador móvel. A eficiência E(t)E(t)E(t) (performance por watt) ao longo do tempo ttt é dada por uma função que envolve um decaimento logarítmico normalizado pelo tempo de uso:E(t) = ln(t^2 + 1) / t \nQuestão: Calcule E(t) para descobrir o momento em que a eficiência começa a cair (onde a derivada seria zero). Aplique a regra do quociente, lembrando que o numerador exige a regra dacadeia.")
                        funcao_M = sp.ln(t**2+1) / t
                        derivada_M = sp.diff(funcao_M,t)
                        resultado_M = derivada_M

                        print(f"O Resultado da Operação é {resultado_M}")
                        
                    case "N":
                        print(f"\nTaxa de Transmissão de Dados (Throughput) Em redes de computadores, a quantidade total de dados transmitidos depende da largura de banda disponível e de um fator de compressão que varia com o tempo. Seja D(t) a função de dados dada por: D(t) = t^2 * e^3t  Determine a velocidade instantânea de transmissão D(t)D(t)D(t). Use a regra do produto, notando que o termo e^3t exige a regra da cadeia.")
                        funcao_N = t**2 * sp.exp(3*t)
                        derivada_N = sp.diff(funcao_N, t)
                        resultado_N = derivada_N
                        print(f"O Resultado da Operação é {resultado_N}")
                    case "O":
                        print(f"A posição de um braço robotico é dada por uma função oscilatoria amortecida: 0(t) = sin(2t)/t^2 + 1.\nQuestão: Calcule a velocidade angular 0(t) usando a regra do quociente trigonometrico")
                        funcao_O = sp.sin(2*t) / t**2 + 1
                        derivada_O = sp.diff(funcao_O, t)
                        resultado_O = derivada_O
                        print(f"O Resultado da Operação é :{resultado_O}")
                    case "P":
                        print(f"Um sinal de audio digital tem sua amplitude modulada pela função: S(t) = 3t * cos(t^2).\nQuestão: Determine S(t) usando a regra do produto trigonometrico")
                        funcao_P1 = 3*t
                        funcao_P2 = sp.cos(t**2)
                        derivada_P1 = sp.diff(funcao_P1,t)
                        derivada_P2= sp.diff(funcao_P2,t)
                        resultado_P = derivada_P1 * derivada_P2

                        print(f"O Resultado da Operação é: {resultado_P}")

#Limites:
match opcao:
    case 2:
        print("\nVocê escolheu a questão 2. Informe qual letra gostaria de obter o resultado (A até O):\n")
        opcao_c = input("Digite a letra correspondente: ").upper()  # Upper para transformar em maiúscula
        while opcao_c < "A" or opcao_c > "O" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()
        match opcao_c:
            case "A":
                print("Em um sistema de moivmentação de robos, a posicao é s(x) = x^2-25 (x --> 5)")
                funcao_A = (x**2 - 25) / (x-5)
                limite_A = sp.limit(funcao_A,x, 5)
                resultado_A = limite_A
                print(f"O Resultado da sua expressão é:{resultado_A}")

            case "B":
                print(f"Um sensor optico mede a intensidade I(x) = RQ(x+4). Calcular limite (x-->0) (RQ(x+4)-2)/x ")
                funcao_B = (sp.sqrt(x + 4) - 2) / x
                limite_B = sp.limit(funcao_B,x,0)
                resultado_B = limite_B
                print(f"O Resultado da Operação é:{resultado_B}")

            case "C":
                print("Um sinal eletrico é modelado por f(x) = sin(4x). Calcular limite (x-->0) (sin(4x))/x")
                funcao_C = sp.sin(4*x) / x
                limite_C = sp.limit(funcao_C,x,0)
                resultado_C = limite_C
                print(f"O Resultado da Operação é:{resultado_C}")

            case "D":
                print("Analisar o crescimento inicial da funçãoT(x)= e^x-1. Calcular limite (x-->0) (e^x-1)/x")
                funcao_D = (sp.exp(x) - 1) / x 
                limite_D = sp.limit(funcao_D,x,0)
                resultado_D = limite_D
                print(f"O Resultado da Operação é:{resultado_D}")

            case "E":
                print("Comparar o crescimento de RQx em relação a x. Calcular limite (x-->oo) (RQx)/x")
                funcao_E = sp.sqrt(x) / x
                limite_E = sp.limit(funcao_E,x,sp.oo)
                resultado_E = limite_E
                print(f"O Resultado da Operação é:{resultado_E}")

            case "F":
                print("Analisar o decaimento do sinal I(x) = e^x. Calcular limite (x-->oo) e^x")
                funcao_F = sp.exp(-x)
                limite_F = sp.limit(funcao_F,x,sp.oo)
                resultado_F = limite_F
                print(f"O Resultado da Operação é:{resultado_F}")

            case "G":
                print("Força F(x) = 1/3 em colisoes. Calcular limite (x --> oo) 1/x")
                funcao_G = 1 / x
                limite_G = sp.limit(funcao_G,x,sp.oo)
                resultado_G = limite_G
                print(f"O Resultado da Operação é:Diverge(não existe limite finito)")

            case "H":    
                print("Analisar ln(x) para pacotes pequenos. Calcular limite (x-->0+) ln(x)")
                funcao_H = sp.ln(x)
                limite_H = sp.limit(funcao_H,x,0,dir="+")
                resultado_H = limite_H
                print(f"O Resultado da Operação é:{resultado_H}")

            case "I":
                print("Osilação s(x) = sin(x). Calcular limite (x-->oo) sin(x)/x")
                funcao_I = sp.sin(x) / x
                limite_I = sp.limit(funcao_I,x,sp.oo)
                resultado_I = limite_I
                print(f"O Resultado da Operação é:{resultado_I}")

            case "J":
                print("Comparar custos C_A = x^3+3x e C_B = 2x^3 - 5. Calcular limite (x-->oo) (x^3+3x)/(2x^3-5)")
                funcao_J = (x**3 + 3*x) / (2*x**3 - 5)
                limite_J = sp.limit(funcao_J,x,sp.oo)
                resultado_J = limite_J
                print(f"O Resultado da Operação é:{resultado_J}")
            case "K":
                print("Entropia de eventos raros: x ln(x). Calcular limite (x-->oo) x ln(x)")
                funcao_K = x * sp.ln(x)
                limite_K = sp.limit(funcao_K,x,0,dir="+")
                resultado_K = limite_K
                print(f"O Resultado da Operação é:{resultado_K}")

            case "L":
                print("Distancia entre curvas: RQ(x^2+x) - x. Calcular limite (x-->0) RQ(x^2+x) - /x")
                funcao_L = sp.sqrt(x**2 + x) - x
                limite_L = sp.limit(funcao_L,x,sp.oo)
                resultado_L = limite_L
                print(f"O Resultado da Operação é:{resultado_L}")

            case "M":
                print("Juros compostos: (1+1/x)^x. Calcular limite (x-->oo) (1+1/n)^x")
                funcao_M = (1 + 1/x)**x
                limite_M = sp.limit(funcao_M,x,sp.oo)
                resultado_M = limite_M
                print(f"O Resultado da Operação é:{resultado_M}")

            case "N":
                print("Probabilidades raras: x^x. Calcular limite (x-->0+) x^x")
                funcao_N = x**x
                limite_N = sp.limit(funcao_N,x,0,dir="+")
                resultado_N = limite_N
                print(f"O Resultado da Operação é:{resultado_N}")

            case "O": 
                print("Crescimento desacelerado: x^(1/x). Calcular limite (x-->oo) x^(1/x)")
                funcao_O = x**(1/x)
                limite_O = sp.limit(funcao_O,x,sp.oo)
                resultado_O = limite_O
                print(f"O Resultado da Operação é:{resultado_O}")

#Integrais:
match opcao:
    case 3:
        print("\nVocê escolheu a questão 3. Informe qual letra gostaria de obter o resultado (A,B ou C):\n")
        opcao_c = input("Digite a letra correspondente: ").upper()  # Upper para transformar em maiúscula
        while opcao_c < "A" or opcao_c > "C" or len(opcao_c) != 1: #Validaçao das letras
            print("Letra inválida!")
            opcao_c = input("Digite a letra válida: ").upper()

        match opcao_c:
                case "A":
                    print(f"\nEm Análise de Desempenho, o custo total acumulado de um processo de parsing (análise sintática) durante um período de 10 segundos pode ser determinado integrando-se a função de custo instantâneo. Suponha que a taxa de custo instantâneo por segundo, C(t)C'(t)C(t), seja dada por uma combinação de custos fixos e variáveis.\nQuestão: Calcule a integral indefinida do custo instantâneo,para obter a função de custo total C(t)C(t)C(t). Use a Propriedade da Integral da Soma (Linearidade).Calcule a integral indefinida de f(t)=2t⋅et^2 usando o método de Integral por Substituição.")
                    integral_Ind = 4*t**3 - 6*t**2 + 2
                    integral_S = sp.integrate(integral_Ind,(t))
                    resultado_Ind = integral_S

                    print(f"O Resultado da operação{resultado_Ind}")

                case "B":
                    print(f"\nEm Teoria de Probabilidade e Estatística Aplicada, é comum encontrar Funções Densidade de Probabilidade (PDF) para modelar o tempo de vida útil de um componente de hardware. Suponha que a taxa de falha de um servidor ao longo do tempo ttt seja modelada pela função. Para encontrar a função de probabilidade acumulada (CDF), é necessário integrar essa função.\n")
                    integral_prob = 2*t * e*t**2
                    substi_Int = {u: t**2}
                    du = sp.diff(t**2,t)
                    Int_u = sp.integrate(sp.exp (u), u)
                    resultado_prob = Int_u.subs(u, t**2)
                    print(f"o Resultado da Operação é {resultado_prob}")

                case "C":
                    print(f"Um engenheiro está modelando o sinal acumulado de ruído N(t)N(t)N(t) em um sistema de comunicação ao longo do tempo. A taxa de geração de ruído N(t)N(t)N(t) é dada pela função que representa a variação do ruído ao longo do tempo pelo fator de interferência. Para otimizar o sistema, ele precisa encontrar a função do ruído total acumulado.\n Questão: Calcule a integral indefinida usando o método de Integral por Partes.")
                    u = t
                    du = sp.diff(u, t)
                    dv = sp.sin(t)
                    v = sp.integrate(dv, t)
                    I_manual = u*v - sp.integrate(v*du, t)

                    print(f"O Resultado da Operação é{I_manual}")


