
import random
import time
import logging
#variaveis e classes
vidapersonagem = 100
vida = 100
exitocombate = True
exitominigame = True
nome = "jogador"
dano = 1
#funções

def caminhandonacidade():
	global vidapersonagem
	global nome
	global dano
	global exitocombate
	time.sleep(1)
	print("Caminhando pela cidade conheces um mercador antigo, que lhe ajuda a residir e te coloca na família.")
	time.sleep(1)
	print("após 2 mêses ele lhe oferece uma missão, escoltar sua carga junto a outros soldados, deseja aceitar a missão?")
	rmercador=input("s/n:")
	if rmercador == "s":
		time.sleep(4)
		print("o mercador agradece, durante algumas semanas você escolta suas mercadorias sem nenhum problema, mas, após isso, o antigo grupo de ladrões do qual você fazia parte surpreende o comboio, deseja lutar?")
		rlutacombandidos = input("s/n:")
		if rlutacombandidos == "s":
			vidapersonagem = 700
			dano = 2
			luta("bando de bandidos", 1200)
			if exitocombate == True:
				print("Você vence seus antigos inimigos, recebe glórias na cidade por trazer mais paz e tranquilidade a região")
			else:
				time.sleep(1)
				print(".")
				time.sleep(1)
				time.sleep(1)
				print(".")
				time.sleep(1)
				print("infelizmente com todos os seus esforços, você foi morto em combate por aqueles que um dia estiveram ao seu lado, descanse em paz.")
		else:
			time.sleep(1)
			print("o mercador percebendo sua traição, o açoita para a cidade para ser preso pelos guardas, deseja fugir ou pagar por seus crimes?")
			rdilemamercador = input("fugir/pagar:")
			if rdilemamercador == "fugir":
				fugacidade()
			elif rdilemamercador == "pagar":
				print("parabéns por sua coragem, você paga por seus crimes e então por viver uma vida na cidade. Sem muitas glórias, porém está vivo. E assim permanecerá.")
	else:
		print("você é exposto pelos moradores da cidade como pertencente ao clã dos bandidos, tem seus pertences subtraidos e é levado a masmorra")
		masmorra()
def luta(inimigo,vidatotalinimigo): #Aqui a vida padrão do inimigo é sempre 100 e a sua é sempre 120, o dano do personagem é variavel, enquanto do oponente é uma função fixa.
	time.sleep(5)
	global vidapersonagem
	global vida
	global exitocombate
	global dano
	vida = vidatotalinimigo
	def combate(vidainimigo,vidapropria):
		global vida
		global vidapersonagem
		danoatk = random.randint (1,4)
		vidainimigo = vidainimigo - (danoatk*27*dano)
		danocontrario = random.randint(3,5)
		vidapropria = vidapropria - (danocontrario*10*dano) + 2
		vida = vidainimigo
		vidapersonagem = vidapropria
		return vida and vidapersonagem
	while vida > 0 and vidapersonagem > 0:
		time.sleep(0.3)
		print("Vida do "+inimigo+":")
		print(vida)
		time.sleep(0.3)
		print("Sua vida:")
		print(vidapersonagem)
		time.sleep(0.3)
		combate(vida,vidapersonagem)
	if vida <= 0:
		time.sleep(5)
		print("Você venceu!")
		exitocombate = True
	else:
		exitocombate = False
		time.sleep(5)
		print("Você foi derrotado!")
	return exitocombate
def fugacidade():
	global vidapersonagem
	global nome
	global exitocombate
	global dano
	print('saindo da cidade...')
	time.sleep(1)
	print("você se encontra em um lindo campo verde, coberto de flores")
	time.sleep(1)
	print('andando mais um pouco encontra uma cabana de caçador abandonada, deseja permanecer?')
	rcabana = input("s/n:")
	if rcabana == ('s'):
		time.sleep(3)
		print("a cabana é aconxegante, tudo que necessita está ai, você passa 10 anos caçando e vendendo os couros e carnes para os mercadores da região, o aprendizado de armadilhas do crime não é mais necessário, agora você é conhecido como "+str(nome)+" o Caçador!")
		time.sleep(1)
		print(".")
		time.sleep(1)
		time.sleep(1)
		print(".")
		time.sleep(1)
		time.sleep(1)
		print(".")
		time.sleep(1.2)
		print("pode intentar contra um pequeno vilarejo e tornar-te um tirano")
		rintentovilarejo = input("deseja intentar? s/n:")
		if rintentovilarejo == "s":
			vidapersonagem = 250
			luta("vilarejo", 400)
			if exitocombate == True:
				print("Você torna-te tirano desse pequeno vilarejo e se fortalece, até que o rei vem tentar subjulgar-lhe, deseja se defender ou fugir?")
				rataquedorei = input("a:defender-se\nb:fugir\na/b:")
				if rataquedorei =="a":
					vidapersonagem = 1700
					dano=4
					luta("Rei de Penelopes", 2000)
					if exitocombate == True:
						print("matas o rei em combate, ganhando assim o temor dos seus cidadãos, ainda assim necessitas derrotar os exercitos permanecentes na cidade")
						dano = 2
						vidapersonagem = 1000
						luta("exercitos remanecentes",500)
				else:
					time.sleep(1.2)
					print("Você foge e é capturado pelos bandidos, obrigado a intentar contra o reinado.")
					print("Junte-se a eles ou morra!")
					rjuntarseaosbandidos = input("a:Juntar-se aos bandidos e atacar a cidade\nb:resistir até a morte\na/b:")
					if rjuntarseaosbandidos == "a":
						dano=10
						vidapersonagem=15000
						luta("Cidade de Penepoles", 20000)
						if exitocombate == True:
							print("Você e seu bando tornam-se tiranos nessa cidade, criando uma dinastia violenta por muitos anos até sua morte, traido por um companheiro.")
						else:
							print("Você é capturado e executado por conspiração em praça pública.")

					else:
						dano = 0.1
						vidapersonagem=100
						luta("clã de bandidos", 500)
						if exitocombate == False:
							print("Você foi morto por escolher não se aliar aos bandidos novamente.")
						else:
							print("Você foge mas é capturado pelos soldados do rei.")
							juntarseaoexercito()
			else:
				print("Você é capturado e levado a cidade, para que o rei decida seu destino.")
				time.sleep(1)
				print("Você é tomado como escravo e obrigado a lutar no exercito")
				juntarseaoexercito()
		else:
			print("Volta a cabana, quando és surpreendido por bandidos, porém os reconhece, deseja lutar com eles?")
			rinvasaobandidos = input("s/n:")
			if rinvasaobandidos == "s":
				vidapersonagem = 350
				luta("clã de bandidos",500)
				if exitocombate == True:
					print("Eles caem em todas as suas armadilhas e morrem, um por um. Você pilha seus corpos. Muito ouro e equipamentos, porém, esses equipamentos pertencem a cidade, deseja apropriarte ou devolver?")
					rdilemaitens=input("a:apropriarte\nb:devolver:")
					if rdilemaitens =="a":
						time.sleep(0.5)
						print("Está mais forte do que nunca, porém solitário.")
						time.sleep(1)
						print("Fim")
					else:
						print("Devolve os pertences aos cidadãos da cidade, é tido como perdoado.")
						time.sleep(1)
						caminhandonacidade()
				else:
					print("Você é cruelmente assassinado, pilhado e tem sua cabeça tomada como lição aos traidores do clã dos bandidos.")
					time.sleep(1)
					print("FIM")
			else:
				print("tornante aliados novamente, então, ve que planejam um saque a cidade, pois juntaram um grande contingente de bandidos, deseja ir junto?")
				rataqueacidadebandidos = input("s/n:")
				if rataqueacidadebandidos == "s":
					print("ótimo!")
					time.sleep(1)
					dano = 10
					vidapersonagem = 10000
					luta("cidade",10000)
					if exitocombate == True:
						print("Seu exercito estava em menor número, mesmo assim, por conta de traições ao rei vocês puderam derrota-lo, parabéns. Você é o novo rei da cidade, e só você será responsavel pelos rumos que a cidade terá a partir desse glorioso dia para o clã dos bandidos da região!")
						print("fim")
					else:
						print("É capturado e obrigado a lutar ao lado do exercito do rei.")
						time.sleep(1)
						juntarseaoexercito()
	else:
		print("Você está definhando de fome e, sem suprimentos, retorna a cidade retorna a cidade")
		time.sleep(1.5)
		print("alto lá viajante, tu eras prisioneiro nesta cidade, agora tu és escravo e servira ao nosso exercito!")
		juntarseaoexercito()
def Minigame():
		acertos = 0
		global exitominigame
		exitominigame=True
		print("Tente acertar o número que aparece na tela!")
		time.sleep(1) #colocar tempo
		print("Caso acerte você conseguira um carvão ao cavar o buraco, caso erre, encontrara uma cobra enquanto remexe o buraco, nesse caso terá de reiniciar a missão.")
		time.sleep(1) #colocar tempo
		while acertos < 10: #alterar o valor para 6 na versão final
			correto = random.randint(1,9) #aqui eu gero um numero de 1 a 9, o usuario deve pressionar o numero que aparece na tela rapidamente
			print(correto)
			valorgerado = correto
			tentativa = input()
			tentativa = int(tentativa)
			if valorgerado == tentativa:
				print("você acertou!")
				time.sleep(1.2)
				acertos = acertos + 1
				exitominigame = True
			elif valorgerado != tentativa:
				print("Você errou!")
				time.sleep(1.2)
				exitominigame = False
				break
		return exitominigame
def bferreiro():
	global vidapersonagem
	global exitobferreiro 
	exitobferreiro = random.randint(0,1)
	if exitobferreiro == 1:
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		print("Você acaba de machucar seriamente o antigo ferreiro da cidade, assim, com todo o barulho da briga os guardas e as pessoas se aglomeram, porém antes de ser preso você consegue subtrair um objeto valioso da loja do ferreiro.")
		objeto = random.randint(1,25)
		if objeto <= 5:
			print("Você conseguiu roubar um escudo de aço!")
			vidapersonagem = vidapersonagem + 50
		if objeto >5 and objeto < 25:
			vidapersonagem = vidapersonagem + 50
			print("Você conseguiu roubar uma espada de alta qualidade!")
		if objeto == 25:
			vidapersonagem = vidapersonagem + 150
			print("Você conseguiu roubar um gorro abençoado, leve como pluma!")
	elif exitobferreiro == 0:
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		time.sleep(1)
		print(".")
		print("Você foi machucado, além de pagar todo seu ouro como multa, você ainda foi preso e levado as masmorras")
		time.sleep(1.2)
		vidapersonagem = 150
		masmorra()
def juntarseaoexercito():
	global vidapersonagem
	global nome
	global dano
	print("Você torna-se um soldado do exercito do rei, luta bravamente em vários combates e aprimora tua luta, tornando-te assim chefe de um pequeno grupo, logo, por seus atos de coragem é promovido, tem glorias e os melhores equipamentos, desejas empreitar uma investida contra o reino rival, para assim assimilar teu próprio castelo?")
	rempreitada = input("s/n:")
	if rempreitada == "s":
		vidapersonagem = 4000
		dano = 5
		luta("Reinado inimigo", 5000)
		if exitocombate == True:
			print("Grande rei, agora tu comandas as fileiras de seus próprios exercitos e tens seus próprios suditos! Grande rei "+str(nome))
			time.sleep(1)
			print(nome)
			time.sleep(1)
			print(nome)
			time.sleep(1)
			print('fim')
		else:
			print("infelizmente fois gravemente ferido na batalha, assim, aleijado retorna a cidade e assume tarefas administrativas da gestão do reino do Grande rei Assuarez, da cidade de Penelopes!")
	else:
		print("aposenta-te e vive os restos do dia feliz e respeitado, com diversas estatuas em tua homenagem, por sua bravura e humildade! Servistes bem a este reino Comandante "+str(nome))
		print("fim")
def Ferreiro():
	global vidapersonagem
	time.sleep(1.2)
	print("Chegando na cidade é muito bem recebido pelos cidadãos, que lhe dão recepção agradável, afinal, nem sempre um viajante chega na cidade, e ainda maltrapido, o clima é de receptividade.")
	time.sleep(3)
	falarcomferreiro = input("Andando pela cidade existem varias pessoas, você pode escolher alguma. Um ferreiro com um anuncio na porta, \"troco espada por carvão\", deseja entrar? s/n\n")
	if falarcomferreiro == "s":
		time.sleep(1)
		print("Você:Olá senhor ferreiro, você está oferecendo uma espada gratuita?\n")
		time.sleep(1)
		RMissaoFerreiro = input("Pois não, aqui está, em troca de carvão eu posso lhe fornecer essa espada quebrada, produto das guerras de nosso generoso rei. Apenas 10 kilos de carvão serão necessários para que você receba essa espada, tem interesse nisso?s/n\n")
		if RMissaoFerreiro=="s":
			Minigame()
			if exitominigame == True:
				print("Parabéns, aqui está.\nRecebeu uma espada quebrada!")
				vidapersonagem = vidapersonagem + 25
				print("A o equipamento que conseguistes com o ferreiro é leve, os armamentos e equipamentos do exercito são interessantes. Admitira-te isso? Deseja-te assimilar-te as fileiras desse glorioso exercito?")
				rexercito = input("s/n:")
				if rexercito == "s":
					juntarseaoexercito()
				else:
					caminhandonacidade()
			else:
				print("Infelizmente você não obteve exito, deseja tentar novamente?")
				rferreiro = input("s/n:")
				if rferreiro == "s":
					Minigame()
				else:
					caminhandonacidade()
		if RMissaoFerreiro=="n":
			chancebferreiro()
	elif falarcomferreiro =="n":
		chancebferreiro()
		time.sleep(1)
		print ("tenha um ótimo dia!")
	caminhandonacidade()
def chancebferreiro():
	global exitocombate
	global vidapersonagem
	Bferreiro = random.randint(1,100)
	if Bferreiro <= 25:
		if Bferreiro <=5:
			print("Você me lembra muito meu filho que foi terrivelmente morto nas mãos de um bandido criminoso, tome filho, receba essa espada de alta qualidade com carinho")
			time.sleep(1.2)
			print("Você recebeu uma espada de alta qualidade!")
			vidapersonagem = vidapersonagem + 50
			juntarseaoexercito()
		elif Bferreiro > 5 and Bferreiro <=25:
			print("Você é o bandido que assassinou meu filho a dois anos atrás, covarde, lute comigo!")
			luta("ferreiro",150)
			if exitocombate == True:
				print("Você acaba de machucar seriamente o antigo ferreiro da cidade, assim, com todo o barulho da briga os guardas e as pessoas se aglomeram, porém antes de ser preso você consegue subtrair um objeto valioso da loja do ferreiro.")
				objeto = random.randint(1,25)
				if objeto <= 5:
					print("Você conseguiu roubar um escudo de aço!")
					vidapersonagem = vidapersonagem +75
					masmorra()
				if objeto >5 and objeto < 25:
					print("Você conseguiu roubar uma espada de alta qualidade!")
					vidapersonagem = vidapersonagem + 50
					masmorra()
				if objeto == 25:
					print("Você conseguiu roubar um gorro abençoado, leve como pluma!")
					vidapersonagem = vidapersonagem + 100
					masmorra()
			elif exitocombate == False:
				print("Você foi machucado, além de pagar todo seu ouro como multa você ainda foi preso")
				time.sleep(1.2)
				masmorra(vidapersonagem)
		if Bferreiro > 25:
			print("tenha um ótimo dia!")
	return exitocombate and vidapersonagem
def masmorra():
	global vidapersonagem
	time.sleep(1.2)
	print("Você prefere ")
	time.sleep(0.5)
	print("a:aguardar a soltura")
	time.sleep(0.5)
	print("b:tentar empreender fuga")
	sairdamasmorra = input()
	if sairdamasmorra == "a":
		exito = random.randint(1,100)
		if exito <= 50:
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print("Você foi liberado da masmorra e teve seus pertences devolvidos, porém, agora todos sabem do seu passado.")
			Caminhando2()
		else:
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print('Você continua preso')
			masmorra()
	elif sairdamasmorra == "b":
		exito = random.randint(1,100)
		if exito <= 40:
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print("Você fugiu da masmorra e conseguiu recuperar seus pertences, e teve que fugir da cidade para não ser reconhecido")
			fugacidade()
		elif exito >40 and exito < 60:
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print('Você continua preso')
			masmorra()
		else:
			time.sleep(1)
			print(".")
			time.sleep(1)
			print(".")
			time.sleep(1)
			print("Você escapou, mas recuperou apenas parte de seus pertences")
			vidapersonagem = vidapersonagem-50
			fugacidade()
	elif sairdamasmorra != "a" and sairdamasmorra != "b":
		time.sleep(1)
		print("entrada invalida")
		masmorra()
def Startgame():
	print("Alto lá! Olá viajante, o que o traz a nossa cidade?\n a:Venho de longe, estou morrendo de fome, não tenho abrigo(Mentira) \n b:Sou um bandido arrependido, desejo pagar pelos meus crimes (Verdade)\n")
	RespostaAoGuarda = input("a/b:")
	if RespostaAoGuarda == "a":
		time.sleep(0.5)
		print(".")
		time.sleep(0.5)
		print(" Entre, nosso rei é generoso (Portões abrem)")
		time.sleep(0.5)
		Ferreiro()
	if RespostaAoGuarda == "b":
		time.sleep(1)
		print(".")
		time.sleep(1)
		print("Entregue suas armas, será conduzido a masmorra imediatamente!(É conduzido as masmorras)")
		masmorra()
def Start():
	global nome
	nome = input("digite seu nome:")
	time.sleep(3)
	Startgame()
def Caminhando2(): #caso você seja solto
	time.sleep(1)
	print("Você está na cidade novamente, agora todos sabem que você é um bandido, sua unica alternativa é se aliar ao exercito do rei!")
	time.sleep(1)
	juntarseaoexercito()
#play no jogo
input("digite qualquer tecla para iniciar.")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()
input("pressione qualquer tecla para jogar novamente")
Start()