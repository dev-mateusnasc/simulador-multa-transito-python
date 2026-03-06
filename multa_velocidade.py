def calcular_multa(velocidade, limite):
    if velocidade <= limite:
        return "✅ Dentro do limite de velocidade."
    excesso = velocidade - limite
    valor_multa = excesso * 7
    return f"""
    🚨 Multa por excesso de velocidade!
    Velocidade permitida: {limite} km/h
    Velocidade do veículo: {velocidade} km/h
    Excesso: {excesso} km/h
    Valor da multa: R$ {valor_multa:.2f}"""
def main():
    print("🚓 Simulador de multa de Trânsito")
    limite = float(input("Digite o limite da via (km/h): "))
    velocidade = float(input("Digite a velocidade do veículo (km/h):"))
    resultado = calcular_multa(velocidade, limite)
    print(resultado)
main()
