def calcula_aporte_por_ano(anoinicial, quantidadedeanos, aporteinicial, aportecascata):
    for ano in range(quantidadedeanos):
        anoatual = anoinicial + ano
        aporteatual = aporteinicial + (ano * aportecascata)
        print(f"No ano {anoatual} seu aporte mensal será de {aporteatual}")

def calcula_cdb(rendimento_do_cdi, cdi, montante_atual, aporte_mensal, meses):
    rendimento_do_cdi_real = rendimento_do_cdi/100
    cdi_real = (cdi/100)/12
    taxa = rendimento_do_cdi_real * cdi_real
    montante_inicial = montante_atual
    for mes in range(meses):
        if (mes + 1) <= 6:
            imposto_de_renda = 22.5/100
        elif (mes + 1) <= 12:
            imposto_de_renda = 20/100
        elif (mes + 1) <= 24:
            imposto_de_renda = 17.5/100
        else:
            imposto_de_renda = 15/100 
        rendimento_bruto = montante_atual * taxa
        rendimento_liquido = rendimento_bruto - rendimento_bruto * imposto_de_renda
        montante_atual = montante_atual + rendimento_liquido + aporte_mensal

    rendimento_total = montante_atual - montante_inicial - aporte_mensal * meses
    return montante_atual, rendimento_total

valores = calcula_cdb(000, 00.00, 0000, 000, 00)
print(f"Montante: {valores[0]:.2f}")
print(f"Investido: {(valores[0]-valores[1]):.2f}")
print(f"Rendido: {valores[1]:.2f}")



