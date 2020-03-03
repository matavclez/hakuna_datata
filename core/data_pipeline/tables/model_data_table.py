"""
En este script se define la clase de la tabla model_data_table.
Heredamos los métodos de la clase Table.
Solo!!!! tenemos que definir la ruta_parcial
"""

from core.utils.table import Table

class model_data_table(Table):
    """
    :param usuario: En un string, insertar una de los siguientes nombres: gabriel, pablo, manuel o matias
    """

    def __init__(self, usuario: str):
        super().__init__(usuario)
        self.ruta_parcial = self._relative_paths["model_data_path"]
        self.ruta_tabla = "{}/{}".format(self.ruta_base,self.ruta_parcial)


    def read(self):
        """
        Read the table (as a "view")
        :return:
        """
        return self.read(table_path=self.ruta_tabla)

    def write(self, df):
        """
        Pasa el df que quieres guardar
        :param df: Dataframe with the data to write.
        :return: Escribe un csv
        """
        return self.write(df=df,table_path=self.ruta_tabla)
		
