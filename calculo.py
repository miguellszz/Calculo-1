import sympy as sp
import math as m
from sympy import sin,cos, tan,Expr,ln,log,abc
#Simbolos Utilizados:
x,t,n,e = sp.symbols("x,t,n,e")

#REGRA DA POTENCIA A
funcao_po = 3*n**5 + 7*n**2 + 10
derivada_po = sp.diff(funcao_po,n)
resultado_po = derivada_po.subs(n, 100)
print(f"O valor da operaçao C{funcao_po} é: {resultado_po}")

#regra do quociente C: diff(x**2 / sin(x), x) 
funcao_q = 5*x / (100-x)
derivada_q = sp.diff(funcao_q, x)
resultado_po = derivada_q.subs(x, 50)

print(f"O Resultado da operaçao {funcao_q} é: {resultado_po}")

#Trigonometria D
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
print(f"O Resultado da operação {funcao_cl} é {resultado_cl}")