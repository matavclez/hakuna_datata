"""
La idea es que cada uno defina aqui una carpeta en la que guardará el dato en su local (Completar Schema Personal)
Será una carpeta llamada datos_cajamar. Dentro de ella todos tendremos la misma estructura, que es la siguiente:

.datos_cajamar
			|
			+--datos_originales
			|				|
			|				+--Modelar_UH2020.txt
			|				|
			|				+--Estimar_UH2020.txt
			|
			+--datos_preprocesado
			|				|
			|				+--modelar_prepro_UH2020.txt
			|				|
			|				+--estimar_prepro_UH2020.txt
			|
			+--datos_feature_eng
			 				|
			 				+--modelar_feateng_UH2020.txt
			 				|
			 				+--estimar_feateng_UH2020.txt



"""


# Schema personal ###################################################################################
schema = {
	"gabriel" : "/datos_cajamar",
	"pablo"   : "/datos_cajamar",
	"manuel"  : "/datos_cajamar",
	"matias"  : "/Users/matiasbbva/Desktop/DATA_SCIENCE/Hackaton/6_Cajamar/datos_cajamar"
}


# RELATIVE PATHS ####################################################################################
relative_paths = {
	# Datos originales
	"model_data"			:	"Modelar_UH2020.txt",
	"estimar_data"			:	"Estimar_UH2020.txt",
	# Datos originales tratados (preparados para leer, sin erratas, ) IGUAL NO ES NECESARIO ESTE PASO
	"model_prepro_data"	:		"modelar_prepro_UH2020.txt",
	"estimar_prepro_data"	:	"estimar_prepro_UH2020.txt",
	# Datos prepro a los que añadimos variables nuevas
	"model_feateng_data"	:	"modelar_feateng_UH2020.txt",
	"estimar_feateng_data"	:	"estimar_feateng_UH2020.txt"
}