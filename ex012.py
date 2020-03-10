precoproduto = float(input('Qual é o preço do produto? R$'))
descontoavista = precoproduto - (precoproduto * 0.15)
descontoaprazo = precoproduto - (precoproduto * 0.05)
parcela = precoproduto / 3
print('O preço final do produto à vista com desconto de 15% é R${:.2f}. Parcelado até 3x com desconto de 5% é R${:.2f} (3x R${:.2f}), acima disso não há desconto.'.format(descontoavista, descontoaprazo, parcela))