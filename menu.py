from os import system,name
opcion = -1;
while opcion !='0':
	if name=='nt':
		_=system('cls');
	else:
		_=system('clear');
	print ("1 - ingresar deposito");
	print ("2 - ingresar cheque");
	print ("3 - mostrar saldo");
	print ("0 - salir");
	opcion=input("ingrese opcion: ");