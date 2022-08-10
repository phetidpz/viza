import random,os,sys,requests
Ba = 0
A = '\033[2;34m'#ازرق
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ا
G = '0123456789'
TY = '123456789'
print('\033[2;32m'+'    𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑀𝑌 𝑊𝑂𝑅𝐿𝐷    \n')
print(Y+'''  ♡ ㅤ  ❍ㅤ    ⎙ㅤ  ⌲\n
  ˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ  ˢʰᵃʳᵉ ''')
print(B+" 𝐼𝑇'𝑆 𝐴𝐿𝐿 𝑂𝑁 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 𖢺")
print(" 𝑀𝑌 𝐔𝑆𝐸𝑅 𝐼𝑁 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀     \n 𝑇𝐻𝐼𝑆 𝐼𝑆 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 ==> @K_HACKER_ANONYMOUS    \n 𝑴𝒀 𝑵𝑨𝑴𝑬 𝑰𝑺 ==> @Krisanjit 𖣧 ")
print(Z+'='*58)
print(F+'  𝐖𝐇𝐀𝐓 𝐃𝐎 𝐘𝐎𝗨 𝐖𝐀𝐍𝐓 𝐌𝐘 𝐃𝐄𝐀𝐑      ')
print('')
bw = input(Y+'(1) 𝘋𝘖 𝘠𝘖𝘜 𝘞𝘈𝘕𝘛 𝘛𝘖 𝘏𝘈𝘊𝘒 𝘉I𝘕 𝘝𝘐𝘚𝘈   \n(2) 𝘉𝘐𝘕 𝘐𝘕𝘍𝘖 \n(3) 𝘋𝘖 𝘠𝘖𝘜 𝘞𝘈𝘕𝘛 𝘛𝘖 𝘔𝘈𝘒𝘌 𝘝𝘐𝘚𝘈𝘚    \n\n𝘊𝘏𝘖𝘖𝘚𝘌  => ')
print(Z+'-'*58)
if bw == '1':
	os.system('clear')
	print(F+'    𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑀𝑌 𝑊𝑂𝑅𝐿𝐷    \n')
	print(Y+'''  ♡ ㅤ  ❍ㅤ    ⎙ㅤ  ⌲\n
  ˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ  ˢʰᵃʳᵉ ''')
	print(B+" 𝐼𝑇'𝑆 𝐴𝐿𝐿 𝑂𝑁 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 𖢺")
	print(" 𝑀𝑌 𝐔𝑆𝐸𝑅 𝐼𝑁 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀     \n 𝑇𝐻𝐼𝑆 𝐼𝑆 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 ==> @K_HACKER_ANONYMOUS    \n 𝑴𝒀 𝑵𝑨𝑴𝑬 𝑰𝑺 ==> @Krisanjit 𖣧 ")
	print(Z+'='*58)
	print(F+'  𝐖𝐇𝐀𝐓 𝐃𝐎 𝐘𝐎𝗨 𝐖𝐀𝐍𝐓 𝐌𝐘 𝐃𝐄𝐀𝐑      ')
	print('')
	token = input(B+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘛𝘖𝘒𝘌𝘕  => ')
	ID = input(B+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘐𝘋  => ')
	
	while True:
		ml = '3'+str(''.join((random.choice(G) for i in range(5))))
		xc = '4'+str(''.join((random.choice(G) for i in range(5))))
		za = [ml,xc]
		v = (random.choice(za))
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		response = reg.text
		if '"country"' in response:
		  	f = requests.get(api)
		  	res = f.json()
		  	z = res['country']['emoji']
		  	m = res['scheme']
		  	k = res['country']['name']
		  	g = res['country']['currency']
		  	u = v
		  	p = k +' '+z
		  	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=®
 HI NEW BIN FROM KRISANJIT
*---------------------------------------*
- BIN =>  {u}
- CoUnTrY =>  {p}
- CaRd TyBe => {m}
- The CuRrEnCy => {g}
*---------------------------------------*
- FROM : Krisanjit''')
		  	i = requests.post(tlg)
		  	print(F+'Available =>  '+v)
		  	print(k+' '+z)
		  	print(g)
		  	print(m)
		else:
			print(Z+'Not Available =>  '+v)
if bw == '2':
	print(Z+'='*58)
	tok = input(B+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘛𝘖𝘒𝘌𝘕  => ')
	id = input(B+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘐𝘋 => ')
	while True:
		v = input(F+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘉𝘐𝘕  =>  ')
		api = f'https://lookup.binlist.net/{v}'
		reg = requests.get(api)
		res = reg.json()
		z = res['country']['emoji']
		m = res['scheme']
		k = res['country']['name']
		g = res['country']['currency']
		print(B+k+z)
		print(B+m)
		print(B+g)
		u = v
		p = k +' '+z
		print('Done Send Your Bot ! ')
		print(Z+'='*58)
		tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text=®
 HI NEW BIN FROM KRISANJIT
*---------------------------------------*
- BIN =>  {u}
- CoUnTrY =>  {p}
- CaRd TyBe => {m}
- The CuRrEnCy => {g}
*---------------------------------------*
- FROM : Krisanjit''')
		i = requests.post(tlg)
if bw == '3':
	os.system('clear')
	print(F+'    𝑊𝐸𝐿𝐶𝑂𝑀𝐸 𝑇𝑂 𝑀𝑌 𝑊𝑂𝑅𝐿𝐷    \n')
	print(Y+'''  ♡ ㅤ  ❍ㅤ    ⎙ㅤ  ⌲\n
  ˡᶦᵏᵉ  ᶜᵒᵐᵐᵉⁿᵗ  ˢᵃᵛᵉ  ˢʰᵃʳᵉ ''')
	print(B+" 𝐼𝑇'𝑆 𝐴𝐿𝐿 𝑂𝑁 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 𖢺")
	print(" 𝑀𝑌 𝐔𝑆𝐸𝑅 𝐼𝑁 𝐼𝑁𝑆𝑇𝐴𝐺𝑅𝐴𝑀     \n 𝑇𝐻𝐼𝑆 𝐼𝑆 𝑀𝑌 𝐴𝐶𝐶𝑂𝐔𝑁𝑇 ==> @K_HACKER_ANONYMOUS    \n 𝑴𝒀 𝑵𝑨𝑴𝑬 𝑰𝑺 ==> @Krisanjit 𖣧 ")
	print(Z+'='*58)
	print(F+'  𝐖𝐇𝐀𝐓 𝐃𝐎 𝐘𝐎𝗨 𝐖𝐀𝐍𝐓 𝐌𝐘 𝐃𝐄𝐀𝐑      ')
	print('')
	tok = input(Z1+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘛𝘖𝘒𝘌𝘕  => ')
	id = input(Z1+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘐𝘋  => ')
	os.system(f'rm -rf krisanjit.txt')
	B = input(B+'(1) 𝑉𝐼𝑍𝐴 𝑅𝐴𝑁𝐷𝑂𝑀   \n(2) 𝑉𝐼𝑍𝐴 𝐹𝑅𝑂𝑀 b𝐼𝑁   \n𝘊𝘏𝘖𝘖𝘚𝘌  => ')	
def bae():
	print(A+'='*58)
	if B == '2':
		ba = input('\033[1;31m'+'𝘠𝘖𝘜𝘙 𝘉𝘐𝘕 5 o尺 6 ? => ')
		if ba == '6':
			bi = input(F+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘉𝘐𝘕  => ')
		if ba == '5':
			bi = input(F+'𝘌𝘕𝘛𝘌𝘙 𝘠𝘖𝘜𝘙 𝘉𝘐𝘕  => ')
	G = '0123456789'
	Z = ['2023','2024','2025','2026','2027','2028']
	Ba = 0
	while Ba < 20:
	   		if B == '1':
    				v = str(''.join((random.choice(G) for i in range(16))))
    				b = str(''.join((random.choice(TY) for i in range(2))))
    				a = str(''.join((random.choice(G) for i in range(3))))
    				p = str(random.choice(Z))
    				h = v+'|'+'0'+b+'|'+p+'|'+a
    				print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
    				g = open('krisanjit.txt', 'a')
    				g.write(h+ '\n')
    				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    				i = requests.post(tlg)
    				Ba = Ba + 1
	   		if B == '2':
	   			if ba == '5':
    					v = str(''.join((random.choice(G) for i in range(11))))
    					b = str(''.join((random.choice(TY) for i in range(2))))
    					a = str(''.join((random.choice(G) for i in range(3))))
    					p = str(random.choice(Z))
    					h = bi+v+'|'+'0'+b+'|'+p+'|'+a
    					print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
    					g = open('krisanjit.txt', 'a')
    					g.write(h+ '\n')
    					Ba = Ba + 1
    					tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
    					i = requests.post(tlg)
	   			if ba == '6':
	   				v = str(''.join((random.choice(G) for i in range(10))))
	   				b = str(''.join((random.choice(TY) for i in range(1))))
	   				a = str(''.join((random.choice(G) for i in range(3))))
	   				p = str(random.choice(Z))
	   				h = bi+v+'|'+'0'+b+'|'+p+'|'+a
	   				print(X+'𝘝𝘐𝘚𝘈 ==> '+'\033[2;36m'+h)
	   				g = open('krisanjit.txt', 'a')
	   				g.write(h+ '\n')
	   				Ba = Ba + 1
	   				tlg = (f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={id}&text={h} + \n''')
	   				i = requests.post(tlg)
	   		

bae()  				