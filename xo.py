import random
nom = 1
a = ['',' ',' ',' ']
b = ['',' ',' ',' ']
c = ['',' ',' ',' ']
win = -2
otv = 'o'
if otv == 'o' or otv == 'о':
	print('Я начинаю.')
	ost = 'x'
	while win == -2:
		if nom == 1:
			hod = random.randint(1,4)
			if hod == 1:
				a[1] = ost
			if hod == 2:
				a[3] = ost
			if hod == 3:
				c[1] = ost
			if hod == 4:
				c[3] = ost		
		if nom == 2:
			while ex != 0:
				if hodp == 'a1' or hodp == 'a3' or hodp == 'c1' or hodp == 'c3':
					if a[1] == ost:
						if c[3] == ' ':
							c[3] = ost
							ex = 0
							break
						else:
							c[1] = ost
							ex = 0
							break
					if a[3] == ost:
						if c[1] == ' ':
							c[1] = ost
							ex = 0
							break
						else:
							c[3] = ost
							ex = 0
							break
					if c[1] == ost:
						if a[3] == ' ':
							a[3] = ost
							ex = 0
							break
						else:
							a[1] = ost
							ex = 0
							break
					if c[3] == ost:
						if a[1] == ' ':
							a[1] = ost
							ex = 0
							break
						else:
							c[1] = ost
							ex = 0
							break
				elif hodp == 'a2' or hodp == 'b1' or hodp == 'b3' or hodp == 'c2':
					b[2] = ost
					ex = 0
				elif hodp == ('b2'):
					if a[1] == ost:
						c[3] = ost
						ex = 0
					if a[3] == ost:
						c[1] = ost
						ex = 0
					if c[1] == ost:
						a[3] = ost
						ex = 0
					if c[3] == ost:
						a[1] = ost
						ex = 0
				hod += 1
		if nom == 3 or nom == 4 or nom == 5:
			if a[1] == a[2] and a[3] == ' ' and a[1] != otv and a[1] != ' ':
				a[3] == ost
			elif a[1] == a[3] and a[2] == ' ' and a[3] != otv and a[3] != ' ':
				a[2] = ost                                
			elif a[3] == a[2] and a[1] == ' ' and a[3] != otv and a[3] != ' ':
				a[1] = ost                                
			elif b[1] == b[2] and b[3] == ' ' and b[1] != otv and b[1] != ' ':
				b[3] = ost                                
			elif b[1] == b[3] and b[2] == ' ' and b[3] != otv and b[3] != ' ':
				b[2] = ost                                
			elif b[3] == b[2] and b[1] == ' ' and b[3] != otv and b[3] != ' ':
				b[1] = ost                                
			elif c[1] == c[2] and c[3] == ' ' and c[1] != otv and c[1] != ' ':
				c[3] = ost                                
			elif c[1] == c[3] and c[2] == ' ' and c[3] != otv and c[3] != ' ':
				c[2] = ost                                
			elif c[3] == c[2] and c[1] == ' ' and c[3] != otv and c[3] != ' ':
				c[1] = ost                                
			elif a[1] == b[1] and c[1] == ' ' and a[1] != otv and a[1] != ' ':
				c[1] = ost                                
			elif a[1] == c[1] and b[1] == ' ' and a[1] != otv and a[1] != ' ':
				b[1] = ost                                
			elif c[1] == b[1] and a[1] == ' ' and c[1] != otv and c[1] != ' ':
				a[1] = ost                                
			elif a[2] == b[2] and c[2] == ' ' and a[2] != otv and a[2] != ' ':
				c[2] = ost                                
			elif a[2] == c[2] and b[2] == ' ' and a[2] != otv and a[2] != ' ':
				b[2] = ost                                
			elif c[2] == b[2] and a[2] == ' ' and c[2] != otv and c[2] != ' ':
				a[2] = ost                                
			elif a[3] == b[3] and c[3] == ' ' and a[3] != otv and c[2] != ' ':
				c[3] = ost                                
			elif a[3] == c[3] and b[3] == ' ' and a[3] != otv and a[3] != ' ':
				b[3] = ost                                
			elif c[3] == b[3] and a[3] == ' ' and c[3] != otv and c[3] != ' ':
				a[3] = ost                                
			elif a[1] == b[2] and c[3] == ' ' and a[1] != otv and a[1] != ' ':
				c[3] = ost                                
			elif a[1] == c[3] and b[2] == ' ' and a[1] != otv and a[1] != ' ':
				b[2] = ost                                
			elif c[3] == b[2] and a[1] == ' ' and c[3] != otv and c[3] != ' ':
				a[1] = ost                                
			elif a[3] == b[2] and c[1] == ' ' and a[3] != otv and a[3] != ' ':
				c[1] = ost                                
			elif a[3] == c[1] and b[2] == ' ' and a[3] != otv and a[3] != ' ':
				b[2] = ost                                
			elif c[1] == b[2] and a[3] == ' ' and c[1] != otv and c[1] != ' ':
				a[3] = ost
			elif a[1] == a[2] and a[3] == ' ' and a[1] == otv:
				a[3] == ost
			elif a[1] == a[3] and a[2] == ' ' and a[3] == otv:
				a[2] = ost                              
			elif a[3] == a[2] and a[1] == ' ' and a[3] == otv:
				a[1] = ost                               
			elif b[1] == b[2] and b[3] == ' ' and b[1] == otv:
				b[3] = ost                               
			elif b[1] == b[3] and b[2] == ' ' and b[3] == otv:
				b[2] = ost                               
			elif b[3] == b[2] and b[1] == ' ' and b[3] == otv:
				b[1] = ost                               
			elif c[1] == c[2] and c[3] == ' ' and c[1] == otv:
				c[3] = ost                               
			elif c[1] == c[3] and c[2] == ' ' and c[3] == otv:
				c[2] = ost                               
			elif c[3] == c[2] and c[1] == ' ' and c[3] == otv:
				c[1] = ost                              
			elif a[1] == b[1] and c[1] == ' ' and a[1] == otv:
				c[1] = ost                               
			elif a[1] == c[1] and b[1] == ' ' and a[1] == otv:
				b[1] = ost                              
			elif c[1] == b[1] and a[1] == ' ' and c[1] == otv:
				a[1] = ost                              
			elif a[2] == b[2] and c[2] == ' ' and a[2] == otv:
				c[2] = ost                              
			elif a[2] == c[2] and b[2] == ' ' and a[2] == otv:
				b[2] = ost                              
			elif c[2] == b[2] and a[2] == ' ' and c[2] == otv:
				a[2] = ost        
			elif a[3] == b[3] and c[3] == ' ' and a[3] == otv:
				c[3] = ost          
			elif a[3] == c[3] and b[3] == ' ' and a[3] == otv:
				b[3] = ost      
			elif c[3] == b[3] and a[3] == ' ' and c[3] == otv:
				a[3] = ost     
			elif a[1] == b[2] and c[3] == ' ' and a[1] == otv:
				c[3] = ost            
			elif a[1] == c[3] and b[2] == ' ' and a[1] == otv:
				b[2] = ost                   
			elif c[3] == b[2] and a[1] == ' ' and c[3] == otv:
				a[1] = ost     
			elif a[3] == b[2] and c[1] == ' ' and a[3] == otv:
				c[1] = ost
			elif a[3] == c[1] and b[2] == ' ' and a[3] == otv:
				b[2] = ost         
			elif c[1] == b[2] and a[3] == ' ' and c[1] == otv:
				a[3] = ost
			else:
				b[2] = ost
			if nom == 5:
				for i in range (3):
					if a[i] == ' ':
						a[i] = ost
					if b[i] == ' ':
						b[i] = ost
					if c[i] == ' ':
						c[i] = ost
			
		print(' |1|2|3')
		print('-+-+-+-')
		print('a|' + a[1] + '|' + a[2] + '|' + a[3])
		print('-+-+-+-')
		print('b|' + b[1] + '|' + b[2] + '|' + b[3])
		print('-+-+-+-')
		print('c|' + c[1] + '|' + c[2] + '|' + c[3])
		if nom >= 3:		
			if (a[1] == a[2] and a[2] == a[3] and a[1] == ost) or (b[1] == b[2] and b[2] == b[3] and b[1] == ost) or (c[1] == c[2] and c[2] == c[3] and c[1] == ost) or (a[1] == c[1] and c[1] == b[1] and a[1] == ost) or (a[2] == c[2] and c[2] == b[2] and a[2] == ost) or (a[3] == c[3] and c[3] == b[3] and a[3] == ost) or (a[1] == b[2] and b[2] == c[3] and a[1] == ost) or (a[3] == b[2] and b[2] == c[1] and a[3] == ost):
				print('Я победил!!!')
				
				win = 0
			if (a[1] == a[2] and a[2] == a[3] and a[1] == otv) or (b[1] == b[2] and b[2] == b[3] and b[1] == otv) or (c[1] == c[2] and c[2] == c[3] and c[1] == otv) or (a[1] == c[1] and c[1] == b[1] and a[1] == otv) or (a[2] == c[2] and c[2] == b[2] and a[2] == otv) or (a[3] == c[3] and c[3] == b[3] and a[3] == otv) or (a[1] == b[2] and b[2] == c[3] and a[1] == otv) or (a[3] == b[2] and b[2] == c[1] and a[3] == otv):
				print('Вы каким-то хреном меня выйграли!!!')
				win = 0
			elif nom == 6:
				print('Ничья!!!')
				win = 0
			if win == 0:
				break
		hodp = ''
		ex = 0
		if nom < 5:
			while ex == 0:
				hodp = input('Теперь ваш ход введите координату свободной клетки.')
				if hodp == 'a1':
					if a[1] == ' ':
						a[1] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'a2':
					if a[2] == ' ':
						a[2] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'a3':
					if a[3] == ' ':
						a[3] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'b1':
					if b[1] == ' ':
						b[1] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'b2':
					if b[2] == ' ':
						b[2] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'b3':
					if b[3] == ' ':
						b[3] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'c1':
					if c[1] == ' ':
						c[1] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'c2':
					if c[2] == ' ':
						c[2] = otv
						ex = 1
					else:
						print('Ошибка!!!')
				if hodp == 'c3':
					if c[3] == ' ':
						c[3] = otv
						ex = 1
					else:
						print('Ошибка!!!')
		nom += 1
		if nom >= 3:		
			if (a[1] == a[2] and a[2] == a[3] and a[1] == ost) or (b[1] == b[2] and b[2] == b[3] and b[1] == ost) or (c[1] == c[2] and c[2] == c[3] and c[1] == ost) or (a[1] == c[1] and c[1] == b[1] and a[1] == ost) or (a[2] == c[2] and c[2] == b[2] and a[2] == ost) or (a[3] == c[3] and c[3] == b[3] and a[3] == ost) or (a[1] == b[2] and b[2] == c[3] and a[1] == ost) or (a[3] == b[2] and b[2] == c[1] and a[3] == ost):
				print('Я победил!!!')
				win = 0
			if (a[1] == a[2] and a[2] == a[3] and a[1] == otv) or (b[1] == b[2] and b[2] == b[3] and b[1] == otv) or (c[1] == c[2] and c[2] == c[3] and c[1] == otv) or (a[1] == c[1] and c[1] == b[1] and a[1] == otv) or (a[2] == c[2] and c[2] == b[2] and a[2] == otv) or (a[3] == c[3] and c[3] == b[3] and a[3] == otv) or (a[1] == b[2] and b[2] == c[3] and a[1] == otv) or (a[3] == b[2] and b[2] == c[1] and a[3] == otv):
				print('Вы подедили!!!')
				win = 0
			elif nom == 6:
				print('Ничья!!!')
		
		
		
		