#Funciones


def validar(archivo):
	"""Recibe un archivo de tipo sceql y lo recorre caracter por caracter filtrando por los comandos validos del lenguaje 
	SCEQL"""

	try:
                with open(archivo) as archivo_a_recorrer:
        except IOError('Problema con el archivo')

        linea_a_devolver = ""
        sceql_comandos = ['!','=','-','_','/','\\']
        for linea in archivo_a_recorrer:
                linea = linea.rstrip('/n').replace(' ','')
                for char in linea:
                        if char in sceql_comandos>
                                linea_a_devolver += char

        
                        
                
                
 		
