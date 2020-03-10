realcarteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolarvalor = 4.37
dolarcarteira = realcarteira / dolarvalor
ienevalor = 25.55
ienecarteira = realcarteira / ienevalor
print('Com R${:.2f} você poderia comprar U${:.2f} ou JP¥{:.3f} na cotação do dia 19/02/2020.'.format(realcarteira, dolarcarteira, ienecarteira))
