def calcula_aporte_por_ano(anoinicial, quantidadedeanos, aporteinicial, aportecascata):
    for ano in range(quantidadedeanos):
        anoatual = anoinicial + ano
        aporteatual = aporteinicial + (ano * aportecascata)
        print(f"No ano {anoatual} seu aporte mensal será de {aporteatual}")

def calcula_cdb(rendimento_do_cdi, cdi, montante_atual, aportes_mensais, meses):
    rendimento_do_cdi_real = rendimento_do_cdi / 100
    cdi_real = (cdi / 100) / 12
    taxa = rendimento_do_cdi_real * cdi_real
    montante_inicial = montante_atual
    
    for mes in range(meses):
        if mes < len(aportes_mensais):
            aporte_mensal = aportes_mensais[mes]
        else:
            aporte_mensal = 0 

        if (mes + 1) <= 6:
            imposto_de_renda = 22.5 / 100
        elif (mes + 1) <= 12:
            imposto_de_renda = 20 / 100
        elif (mes + 1) <= 24:
            imposto_de_renda = 17.5 / 100
        else:
            imposto_de_renda = 15 / 100 
        
        rendimento_bruto = montante_atual * taxa
        rendimento_liquido = rendimento_bruto - rendimento_bruto * imposto_de_renda
        montante_atual = montante_atual + rendimento_liquido + aporte_mensal
        
        print(f"O montante no mês {mes + 1} é de {montante_atual:.2f}")
    
    rendimento_total = montante_atual - montante_inicial - sum(aportes_mensais[:meses])
    return montante_atual, rendimento_total

# Exemplo de uso
aportes = [2600, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800, 2800]
valores = calcula_cdb(100, 12.15, 1936, aportes, 13)

print(f"Montante: {valores[0]:.2f}")
print(f"Investido: {(valores[0] - valores[1]):.2f}")
print(f"Rendido: {valores[1]:.2f}")



