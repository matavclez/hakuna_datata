"""
En este script se define la clase base Table.
Con esto crearemos otras clases que se encargarán de leer y guardar las tablas que generemos.
"""

import pandas as pd 
from core.data_pipeline.rutas import schema, relative_paths

class Table:
    """
    :param usuario: En un string, insertar una de los siguientes nombres: gabriel, pablo, manuel o matias
    """
    def __init__(self, usuario: str):
        self.usuario = usuario
        self.ruta_base = schema[usuario]
		self._relative_paths = relative_paths

    def read(self, table_path):
        """
        Read the table (as a "view")
        :param table_path: Table path
        :return:
        """
        return pd.read_csv(table_path)

    def write(self, df, table_path):
        """
        Write a Dataframe into the table.
        :param df: Dataframe with the data to write.
        :return: Escribe un csv
        """
        return df.to_csv(table_path,index=False)
		
