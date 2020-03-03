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
    _ID_TABLE = ""

    def __init__(self, usuario: str):
        self.usuario = usuario
        self.ruta_base = schema[usuario]
        self._relative_paths = relative_paths
        self.ruta_parcial = self._get_ruta_parcial()
        self.ruta_tabla = self._get_ruta_tabla()

    def _get_ruta_parcial(self):
        if self._ID_TABLE == "":
            ruta_parcial = ""
        else:
            ruta_parcial = self._relative_paths[self._ID_TABLE]
        return ruta_parcial

    def _get_ruta_tabla(self):
        if self._ID_TABLE == "":
            ruta_tabla = self.ruta_base
        else:
            ruta_tabla = "{}/{}".format(self.ruta_base,self.ruta_parcial)
        return ruta_tabla

    def read(self):
        """
        Read the table (as a "view")
        :return:
        """
        return pd.read_csv(self.ruta_tabla)

    def write(self, df):
        """
        Write a Dataframe into the table.
        :param df: Dataframe with the data to write.
        :return: Escribe un csv
        """
        return df.to_csv(self.ruta_tabla, index=False)
		
