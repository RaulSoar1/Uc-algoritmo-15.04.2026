def calcular_media():
    """
    Solicita 3 notas ao usuário, calcula e exibe a média.
    Encerra caso haja entrada inválida.
    """
    notas = []

    try:
        for i in range(1, 4):
            entrada = input(f"Digite a {i}ª nota: ").strip()
            nota = float(entrada)
            notas.append(nota)

        media = sum(notas) / len(notas)
        print(f"\nMédia final: {media:.2f}")

    except ValueError:
        print("\nErro: as notas devem ser valores numéricos.")
        return


def calcular_total():
    """
    Solicita o preço de 2 produtos e calcula o total.
    Encerra caso haja entrada inválida.
    """
    try:
        entrada1 = input("Digite o preço do primeiro produto: ").strip()
        preco1 = float(entrada1)

        entrada2 = input("Digite o preço do segundo produto: ").strip()
        preco2 = float(entrada2)

        total = preco1 + preco2
        print(f"\nTotal da compra: R$ {total:.2f}")

    except ValueError:
        print("\nErro: os preços devem ser valores numéricos.")
        return


def menu():
    """
    Menu principal para escolher qual programa executar.
    """
    while True:
        print("\n=== MENU ===")
        print("1 - Calcular média de notas")
        print("2 - Calcular total da compra")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            calcular_media()
        elif opcao == "2":
            calcular_total()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Execução do programa
if __name__ == "__main__":
    menu()