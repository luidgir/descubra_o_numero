import random

# Gerando um número aleatório entre 1 e 100
numero_aleatorio = random.randint(1, 100)
i=1     # Intervalo inicial
f=100   # Intervado final
t=0     # Número de tentativas

print("Um número aleatório foi criado!")

n=int(input("Digite um número inteiro entre 1 e 100 \n"))
t=t+1

while n!=numero_aleatorio:
  if n>numero_aleatorio:
    f=n
  else:
    i=n
  n=int(input(f"Errou!! Digite um número inteiro entre {i} e {f}\n"))
  t=t+1

print("==========================================================")  
print("Você acertou em ",t," tentativas! O número escolhido é: ",n)
print("==========================================================")  
