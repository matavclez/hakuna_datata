# hakuna_datata
Competición de XXXXXX
hhhh

**core:**<br/>
Donde esta el grueso del proyecto. Es el código final que permite ejecutar todo de principio a fin. Leer, limpiar el dato, añadir nuevas variables, entrenar y predecir.<br/>
	- data_pipeline: Contiene scripts para leer, transformar, limpiar, añadir nuevas features.<br/>
	- model: Contiene scripts para crear training y testing data, entrenar modelos y escorear.<br/>
	- utils: Contiene las funciones comunes al proyecto, como leer datos.<br/>
<br/>
**docs:**<br/>
Donde subimos documentación.<br/>

**exploratorio:**<br/>
Donde podeis hacer visualizaciones, jugar con modelos... pero no es código productivo. Es un cajón de sastre de basura.<br/>
<br/>
<br/>
# Mapa de los documentos

	+--core
	|     |
	|     +--data_pipeline
	|     |	     |
	|     |	     +--rutas.py
	|     |	     |	
	|     |	     +--tables	
	|     |		    |
	|     |		    +--	model_data_table
	|     |		    +--	estimar_data_table
	|     |		    +--	model_prepro_data_table
	|     |		    +--	estimar_prepro_data_table
	|     |		    +--	model_feateng_data_table
	|     |		    +--	estimar_feateng_data_table	
	|     |	
	|     |
	|     +--model
	|     |
	|     +--utils
	|     	     |
	|     	     +--table.py	
	|
	|
	+--docs
	|
	|
	+--exploratorio
