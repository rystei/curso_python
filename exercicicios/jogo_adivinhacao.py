import random

numero_aleatorio = random.randint(1, 100)
tentativa = 0
max_tentativa = 7

print("Bem-vindo ao jogo da adivinhação!")

while tentativa < max_tentativa:
    chute = int(input("Insira um número inteiro de 1 a 100: "))
    tentativa += 1

    if chute == numero_aleatorio:
        print(
            f"Parabéns! Você acertou o número aleatório {numero_aleatorio} em {tentativa} tentativas."
        )
        break
    elif chute < numero_aleatorio:
        print("O número é maior. Tente novamente.")
    else:
        print("O número é menor. Tente novamente.")

if tentativa == max_tentativa and chute != numero_aleatorio:
    print(
        f"Você atingiu o número máximo de tentativas. O número correto era {numero_aleatorio}."
    )
