math, physics = map(int, input().split())
case = int(input())

if math <= 80 and physics <= 80:
	print('Tidak Layak')
else:
	data_math = []
	data_physics = []
	for i in range(case):
		x, y = map(int, input().split())
		data_math.append(x)
		data_physics.append(y)
		
	average_math = sum(data_math) / len(data_math)
	average_physics = sum(data_physics) / len(data_physics)
	if math <= average_math and physics <= average_physics:
		print('Layak')
	else:
		print('Tidak Layak')