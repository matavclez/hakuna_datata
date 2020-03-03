"""
En este script se define la clase de la tabla model_data_table.
Heredamos los métodos de la clase Table.
Solo!!!! tenemos que definir el _ID_TABLE y que coincida con el key del diccionario de relative_paths
"""

from core.utils.table import Table

class estimate_data_table(Table):
    """
    :param usuario: En un string, insertar una de los siguientes nombres: gabriel, pablo, manuel o matias
    """

    _ID_TABLE = "estimar_data"

    def __init__(self, usuario: str):
        super().__init__(usuario)