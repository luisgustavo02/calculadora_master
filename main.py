import matplotlib.pyplot as plt
import numpy as np
import os
import sympy as sp

from time import sleep

# Classe para expressões matemáticas
class Calculus:
    def __init__(self, expression : str, variable : str = 'x'):
        self.expression = self.__treat__(expression)
        self.var = sp.symbols(variable)
        self.equation = self.__toEq__()
    
    # Trata a expressão para facilitar o processamento
    def __treat__(self, expression : str):
        # Adiciona '*' onde necessário
        for ii in range(len(expression)-1):
            if expression[ii].isdigit() and expression[ii+1] == 'x':
                expression = expression[:ii+1] + '*' + expression[ii+1:]
            elif expression[ii] == 'x' and expression[ii+1].isdigit():
                expression = expression[:ii+1] + '*' + expression[ii+1:]
            elif expression[ii] == ')' and expression[ii+1] == '(':
                expression = expression[:ii+1] + '*' + expression[ii+1:]
            elif expression[ii] == ')' and expression[ii+1] == 'x':
                expression = expression[:ii+1] + '*' + expression[ii+1:]
            elif expression[ii] == 'x' and expression[ii+1] == '(':
                expression = expression[:ii+1] + '*' + expression[ii+1:]
        
        expression = expression.replace('log2(x)', 'log(x)/log(2)')
        expression = expression.replace('log10(x)', 'log(x)/log(10)')
        
        return expression.replace('^', '**').replace(',', '.').replace('sen', 'sin')
    
    # Transforma a string em uma expressão simbólica
    def __toEq__(self):
        eq = self.expression.split('=')
        
        for ii in range(len(eq)):
            eq[ii] = sp.sympify(eq[ii])
        
        print("Equação convertida com sucesso.")
        print(f"Equação: {eq[0]} = {eq[1]}")
        print()

        return sp.Eq(eq[0], eq[1])

    # Resolve a equação
    def __solve__(self):
        print(self.equation)
        print(type(self.equation))
        print(self.var)
        print(type(self.var))
        self.solve = sp.solve(self.equation, self.var)

        if self.solve == [] or self.solve is None:
            print("A equação não possui soluções.")
        else:
            for ii in range(len(self.solve)):
                print(f"Solução {ii+1}: {self.solve[ii]}")

    # Simplifica a expressão
    def __simplify__(self):
        pass

    # Expande a expressão
    def __expand__(self):
        pass

    # Representação em LaTeX
    def __LaTeX__(self):
        pass

    # Imprime a expressão
    def __print__(self):
        pass

    # Imprime a expressão em LaTeX
    def __printLaTeX__(self):
        print(sp.latex(self.equation))

    # Derivada da expressão
    def diff(self, var):
        pass

    # Integral da expressão
    def integrate(self, var, lim_inf=None, lim_sup=None):
        pass

class Function:
    def __init__(self, function : str, variable : str = 'x'):
        pass

    # Plota a expressão
    def plot(self, x_lim : tuple | list = None, y_lim : tuple | list = None, num_points : int = 1000):
        pass

def main():
    # Instalando as bibliotecas necessárias
    try:
        os.system('pip install requirements.txt')
    except Exception as e:
        print(f"Erro ao instalar as bibliotecas necessárias: {e}")
        sleep(5)
        return
    
    # Limpa a tela
    os.system('cls' if os.name == 'nt' else 'clear')

    while True:
        print("Seleciona a opção desejada:")
        print("[1] Cálculo de expressões matemáticas")
        print("[2] Funções")
        choice = input("Opção: ")

        os.system('cls' if os.name == 'nt' else 'clear')

        if choice == '1':
            c = Calculus(input("Digite a expressão matemática: "), input("Digite a variável (padrão 'x'): ") or 'x')
            os.system('cls' if os.name == 'nt' else 'clear')

            c.__printLaTeX__()
            print()
            c.__solve__()
            print()

        elif choice == '2':
            print("Funções ainda não implementadas.")
            sleep(5)

        else:
            print("Opção inválida. Tente novamente.")
            sleep(5)

if __name__ == "__main__":
    main()
