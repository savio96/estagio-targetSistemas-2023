def dic(sigla, valor):
	return {'sigla':sigla, 'valor': valor}

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros
print('Total: ', total)
print('SP: ', round(sp/total, 2)*100,"%")
print('RJ: ', round(rj/total, 2)*100,"%")
print('MG: ', round(mg/total, 2)*100,"%")
print('ES: ', round(es/total, 2)*100,"%")
print('Outros: ', round(outros/total, 2)*100,"%")