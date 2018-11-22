def recorrencia():
	for i in range(0, 6):
		a = [dia, mes, ano]
		for n in range(3, 13):
			a.append(funcoes(i, n, a))
		escrever(i, a)
		del a

def funcoes(nFuncao, n, a):
	if nFuncao == 0:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + n * (3 ** n)
	elif nFuncao == 1:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + n * (2 ** n)
	elif nFuncao == 2:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + (n ** 2) * (3 ** n)
	elif nFuncao == 3:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + (n ** 2) * (2 ** n)
	elif nFuncao == 4:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + ((n ** 2 + 2 * n - 1) * 3 ** n)
	elif nFuncao == 5:
		return 6 * a[n-1] - 12 * a[n-2] + 8 * a[n-3] + ((n ** 2 + 2 * n - 1) * 2 ** n)

def escrever(nFuncao, a):
	with open('recorrencias', 'a') as arquivo:
		if nFuncao == 0:
			arquivo.write('\n\n(a) an = 6an−1 − 12an−2 + 8an−3 + n3n:\n')
		elif nFuncao == 1:
			arquivo.write('\n\n(b) an = 6an−1 − 12an−2 + 8an−3 + n2n:\n')
		elif nFuncao == 2:
			arquivo.write('\n\n(c) an = 6an−1 − 12an−2 + 8an−3 + n23n:\n')
		elif nFuncao == 3:
			arquivo.write('\n\n(d) an = 6an−1 − 12an−2 + 8an−3 + n22n:\n')
		elif nFuncao == 4:
			arquivo.write('\n\n(e) an = 6an−1 −12an−2 +8an−3 +(n2 +2n−1)3n:\n')
		elif nFuncao == 5:
			arquivo.write('\n\n(f) an = 6an−1 −12an−2 +8an−3 +(n2 +2n−1)2n\n')
		for i, pos in enumerate(a):
				arquivo.write(str(i) + ' = ' + str(pos) + '\n')

dia = int(input('Qual é o dia do seu aniversário?\n'))
mes = int(input('Qual é a unidade do mês do seu aniversário\n'))
ano = int(input('Qual é o algarismo das unidades do ano do seu aniversário\n'))

with open('recorrencias', 'w') as arquivo:
	arquivo.write('Universidade Federal da Fronteira Sul\nTrabalho\nKadu Marcos Grando')

recorrencia()