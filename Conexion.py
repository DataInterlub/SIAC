import pyodbc


class Conexion:

    Fab_conexion = None # Conexion inactiva o activa


    def __init__(self):
        self.__server = "ni2jzh64akxerj5jj6zxv7h4vm-pkliwnv5xniu3fqo3wgrfcn4qu.datawarehouse.fabric.microsoft.com,1433"
        self.__database = "WH_Oro"
        self.__username = "pablo.valadez@interlub.com" 
        try:
            if Conexion.Fab_conexion is None:

                Conexion.Fab_conexion = pyodbc.connect(
                    "DRIVER={ODBC Driver 18 for SQL Server};"
                    f"SERVER={self.__server};"
                    f"DATABASE={self.__database};"
                    "Authentication=ActiveDirectoryInteractive;"
                    f"UID={self.__username};"  
                    "Encrypt=yes;"
                )
        except pyodbc.Error as e:

            print("Error al conectar a SQL Server")
            print(e)

            Conexion.Fab_conexion = None
    def cursor(self):
        return Conexion.Fab_conexion.cursor()