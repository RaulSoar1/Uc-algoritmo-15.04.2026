def soma_segura(a, b):
    try:
        return a + b
    except TypeError:
        print("Entrada inválida")
        return 0


def divisao(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Não divida por zero!"
    
    print(soma_segura(5, 3))    
      # 8
print(soma_segura(5, "a"))
     # Entrada inválida → 0

print(divisao(10, 2))        
  # 5.0
  
print(divisao(10, 0))         
 # Não divida por zero!
