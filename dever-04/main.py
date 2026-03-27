def f(n):
   
    if n == 1:
        return 2
    
    else:
        return 2 * f(n - 1) + n**2


try:
    valor_n = int(input("Digite o valor de n: "))

    if valor_n < 1:
        print("Por favor, insira um número inteiro maior ou igual a 1.")
    else:
        resultado = f(valor_n)
        print(f"O resultado de F({valor_n}) é: {resultado}")

except ValueError:
    print("Entrada inválida. Digite um número inteiro.")
