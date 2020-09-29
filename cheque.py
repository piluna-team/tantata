
class Cheques:

	def __init__(self):
		self.importe=0;
		self.nroChequera=0;
		self.fechaEmicion='0';
		self.fechaPago='0';
		self.nombre='0';
		self.apellido='0';

	def intro(self):
		self.importe=float(input("ingrese el importe"));
		self.nroChequera=int(input("ingrese el numero de chequera")); 
		self.nombre=input("ingrese el nombre");
		self.apellido=input("ingrese el apellido");

	def mostrar(self):
		print("ingresos: ",self.importe);
		print("numero de chequera: ",self.nroChequera);
		print("nombre: ",self.nombre);
		print("apellido: ",self.apellido);
		print(self.fechaEmicion[0],self.fechaEmicion[1], self.fechaEmicion[2]);
		print(self.fechaPago[0],self.fechaPago[1], self.fechaPago[2]);
	
	def cargarFecha(self):
		d1=int(input("ingrese numero de dia de emicion:"));
		m1=int(input("ingrese numero de mes de emicion:"));
		a1=int(input("ingrese numero de año de emicion:"));
		self.fechaEmicion=(d1,m1,a1);
		d2=int(input("ingrese numero de dia de pago:"));
		m2=int(input("ingrese numero de mes de pago:"));
		a2=int(input("ingrese numero de año de pago:"));
		self.fechaPago=(d2,m2,a2);



def ingresarCheque():
	Cheque=Cheques();
	Cheque.intro();	
	Cheque.cargarFecha();
	Cheque.mostrar();

	
	