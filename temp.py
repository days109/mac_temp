#temp
print('c or f')
temp = input('請輸入單位')
if temp == 'c':
	c = float(input('請輸入攝氏溫度：'))
	f = c * 9 / 5 + 32
	print('華氏溫度為', f)
elif temp == 'f':
	f = float(input('請輸入華氏溫度：'))
	c = (f - 32) * 5 / 9
	print('攝氏溫度為', c)
else:
	print('輸入錯誤')
	




