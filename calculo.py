import sympy as sp
#Para calcular a derivada de uma função com SymPy, você pode usar o método diff(). Por exemplo, se 
#quiséssemos calcular a derivada da função \(f(x) = x^2\), o código seria algo como diff(x**2, x), onde x é 
#uma variável previamente definida como um símbolo do SymPy. Este método é incrivelmente flexível, permitindo 
#cálculos de derivadas de ordens superiores apenas adicionando um parâmetro adicional.
print("Olá Seja Bem Vindo ao programa de Cálculo!")
print("------ ESSE É O MENU PRINCIPAL ------")
print("ESCOLHA QUAL PERGUNTA VOCE DESEJA OBTER A RESPOSTA:\n 1 - f(x)=(3x^2+2x+1)\n 2 - \n 3 - ")

opcao = int(input("Digite o número correspondente a sua pergunta: "))
x = sp.symbols('x')
resultado_1 = sp.diff((3*x**2 + 2*x + 1), x)
resultado_2 = ""
resultado_3 = ""


while opcao != 1 and opcao != 2 and opcao != 3:
    print("Opção inválida. Por favor, escolha uma opção válida.")
    opcao = int(input("Digite o número correspondente a sua pergunta: "))

if opcao == 1:
    print("Você escolheu a opção 1")
    print(f"A resposta da questão 1 é: {resultado_1}\n")
elif opcao ==2:
    print("Você escolheu a opção 2")
    print(f"A resposta da questão 2 é: {resultado_2}\n")
elif opcao ==3:
    print("Você escolheu a opção 3")
    print(f"A resposta da questão 3 é: {resultado_3}\n")
else:
    print("Opção inválida.")

print(f"OBRIGADO POR UTILIZAR O PROGRAMA DE CÁLCULO!")