import random
import time
import logging

vidainimigo = 100
vidapropria = 120
while vidainimigo > 0 and vidapropria > 0:
	dano = random.randint (1,2)
	vidainimigo = vidainimigo - (dano*2*9)
	danocontrario = random.randint(1,2)
	vidapropria = vidapropria - (danocontrario*10) + (2*1)
	print("vida inimigo:"+str(vidainimigo))
	print("sua vida:"+str(vidapropria))