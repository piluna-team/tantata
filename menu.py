from saldo import mostrarSaldo
from deposito import ingresarDeposito
from cheque import ingresarCheque
from os import system,name

pop = True;
while pop == True:	
	menu= """
	1- ingresar deposito:
	2 - ingresar cheque:
	3 - mostrar saldo:
	4 - salir:
	"""
	print (menu);
	opcion=int(input("ingrese opcion: "));
	if opcion== 1:
		ingresarDeposito()
	elif opcion == 2:
		ingresarCheque()
	elif opcion == 3:
		mostrarSaldo()
	elif opcion == 4:
		pop=False;
	else:
		print("opcion incorrecta");

	_=system("pause");
	if name=='nt':
		_=system('cls');
	else:
		_=system('clear');