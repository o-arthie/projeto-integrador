def main():
    print("=== SISTEMA DE DIVISÃO DE DESPESAS DE VIAGEM ===")
    print("------------------------------------------------")

    #definição do titular (quem vai ser o titular do cartão usado)
    titular = input("Digite o nome de QUEM vai passar o cartão: ").strip().title()

    #cadastro de usuários (Quem vai pagar o consumo depois)
    participantes = []
    print("\n--- Cadastro de Participantes ---")
    print(f"(Não precisa digitar o nome de {titular}, ele(a) já está incluído)")

    while True:
        nome = input("Nome do participante (ou [Enter] para parar): ").strip().title()
        if not nome:
            break
        participantes.append(nome)

    #grupo total inclui o titular + os participantes cadastrados
    total_pessoas = len(participantes) + 1

    #lançar as despesas
    print("\n--- Lançamento de Compras/Despesas ---")
    compras = []
    valor_total_viagem = 0.0

    while True:
        descricao = input("Descrição da compra (ou [Enter] para encerrar): ").strip()
        if not descricao:
            break

        try:
            #substitui vírgula por ponto para aceitar vírgulas ou pontos (ex: 10,50)
            valor_input = input(f"Valor de '{descricao}': R$ ").replace(',', '.')
            valor = float(valor_input)

            compras.append({"item": descricao, "valor": valor})
            valor_total_viagem += valor
        except ValueError:
            print("Erro: Por favor, digite um valor numérico válido.")

    #calculos e relatorio
    if valor_total_viagem == 0:
        print("\nNenhuma despesa foi registrada. Encerrando.")
        return

    valor_por_pessoa = valor_total_viagem / total_pessoas

    print("\n" + "="*40)
    print("RELATÓRIO FINAL DA VIAGEM".center(40))
    print("="*40)

    print(f"Total de Pessoas: {total_pessoas} (Incluindo {titular})")
    print(f"Custo TOTAL da viagem: R$ {valor_total_viagem:.2f}")
    print(f"Custo por pessoa (Rateio): R$ {valor_por_pessoa:.2f}")

    print("-" * 40)
    print("DETALHAMENTO DOS REPASSES:")
    print("-" * 40)

    #mostrar quanto cada um deve transferir
    for pessoa in participantes:
        print(f"- {pessoa} deve pagar R$ {valor_por_pessoa:.2f} para {titular}")

    print("-" * 40)
    #mostra a parte que o titular "absorveu" (gastou com ele mesmo)
    print(f"Nota: {titular} gastou R$ {valor_por_pessoa:.2f} consigo mesmo(a)")
    print(f"e receberá R$ {valor_por_pessoa * len(participantes):.2f} dos amigos.")
    print("="*40)

if __name__ == "__main__":
    main()
