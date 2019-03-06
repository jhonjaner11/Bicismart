"""Se declaran las librerias a utilizar"""
from ubidots import ApiClient
import serial 
import time    
import sys

""" Excepcion para verificar si el arduino esta conectado o no """       
try:  
    print "CONECTADO..."  
    arduino = serial.Serial('/dev/ttyACM0',  baudrate=9600)
    time.sleep(1)
    arduino.flush()
except:  
	
    print "FALLO LA CONEXION"

""" Excepcion para verificar si conecto correctamente con la API de ubidtos """ 
try:  
    print "CONECTADO API..."  
    api = ApiClient('A1E-b690233bc1d9b91425d66a62e30621bf86c3')
    calidad_aire = api.get_variable('5c7f2e1ac03f9771519fe0c7')
except:  
    print "FALLO LA CONEXION API"

""" Los siguientes contadores se utilizan para enviar el dato a ubitods de temperatura
recibir el dato que viene de ubidots, y realizar un reset al arduino, con el fin de
hacer una limpieza a bufer """ 
contador=0
contador1=0
contador2=0

""" Ciclo donde se desarrolla todo el programa """ 
while True:
	""" se lee el dato que llega del arduino """ 
	dato=arduino.readline().strip()
	""" Contador que envia el dato cada 11 ciclos"""
	if contador == 5:	
		try:
			temp = calidad_aire.save_value({'value':dato})
		except:
			print "NO ENVIO" 
		contador=0
	""" Contador que envia el dato cada 11 ciclos"""
	
	""" Contador que reset el arduino cada 100 ciclos"""	
	if contador2 == 100:	
		arduino.close()
		arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=0.5)
		contador2=0

	""" Imprimir el dato que llega del arduino y hacer la suma a cada contador"""
	print(dato)
	contador=contador+ 1
	
contador2=contador2+ 1 
