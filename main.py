# -*- coding: utf-8 -*-
import aiml
import os

#Buscar proximo programa


kernel = aiml.Kernel()

print "Escolha qual chatbot: (1) Rede Globo | (2) Banco Neon | (3) Casas Bahia"
try:
    mode=int(raw_input('Digite:'))
except ValueError:
    print "Not a number"

if mode == 1:
	os.system("rm programacao.json")
	os.system("scrapy runspider programacao_spider.py -o programacao.json")
	from read_programacao import read_programacao
	p = read_programacao()
	kernel.learn("std-startup-tv.xml");
elif mode == 2:
	kernel.learn("std-startup-neon.xml");
elif mode == 3:
	kernel.learn("std-startup-casasbahia.xml");
else:
	print "Opção Inválida"

kernel.respond("load aiml b")

if mode == 1:
	print "Próximo episódio da Rede Globo: " + str(p["programa"].encode('utf-8')) + " as " + p["time"].encode('utf-8')
# Press CTRL-C to break this loop
while True:
    print kernel.respond(raw_input("Enter your message >> "))


