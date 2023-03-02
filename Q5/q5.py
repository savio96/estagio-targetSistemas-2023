def inverte(string):
	return ''.join([string[-i] for i in range(1, len(string)+1)])


palavra="target sistemas"
print(palavra,"-----", inverte(palavra))