def pedir_velocidade():
    return float(input("Registre a velocidade em que você passou na via: "))
def gerar_multa():
    if velocidade > 80:
        resultado = (velocidade - 80) * 7
        return resultado
    else:
        return 0
velocidade = pedir_velocidade()
valor_multa = gerar_multa()
if valor_multa > 0:
    print(f"Você foi multado no valor de {valor_multa}")
else:
    print("Você está nos limites da via, boa viagem!")
