#Importar la conexion principal
from Conexion import Conexion
# Importar librerias generales Python
from typing import List,Dict, Any
#Libreria de Decimal
from decimal import Decimal
#Libreria de List
from collections import defaultdict
#Correo
import smtplib
from email.message import EmailMessage
#Json
import json

class Funcion : 
    # Datos del correo
    Host = "mail.interlub.website"     
    Puerto = 587                   
    Usuario = "mensajero@interlub.website"
    Contrasenia = "*Interlub559"
    EnvioGeneral = False

    # Funcion Principal
    
    def __init__(self, Articulo, Precio, Dolar: Decimal):

        if isinstance(Articulo, list):

            if len(Articulo) != len(Precio):
                raise ValueError("Articulos y Precios no coinciden")

            self.Data = {
                "PreciosFinales": {"Detalle": {}},
                "Ponderacion": []
            }

            for i, art in enumerate(Articulo):
                try:
                    data_temp = {
                        "Articulo": art,
                        "Precio_Nuevo": Precio[i]
                    }

                    data_temp.update(self.Deteccion(art))
                    data_temp.update(self.FormulaProducto(art))
                    data_temp.update(self.PrecioProducto(art))
                    data_temp.update(self.AreasProducto(art))
                    data_temp.update(self.ObtenerCorreos(data_temp.get('Areas')))
                    data_temp.update(self.CalculoTendencia(Precio[i], data_temp.get('Precio')))
                    data_temp.update(self.CalculoPorcentaje(Precio[i], data_temp.get('Precio'), Dolar))
                    data_temp.update(self.TransfomacionFormula(data_temp.get('ProductoFinal')))
                    data_temp.update(self.precioPonderado(data_temp.get('ProductoFinal')))
                    data_temp.update(self.PrecioFormulas(
                        data_temp.get('InventarioProducto'),
                        data_temp.get('Ponderacion'),
                        art,
                        data_temp.get('Porcentaje')
                    ))

                    # ACUMULAR DETALLE (+=)
                    detalle = data_temp.get("PreciosFinales", {}).get("Detalle", {})
                    for k, v in detalle.items():
                        v["ArticuloOrigen"] = art  # opcional
                    self.Data["PreciosFinales"]["Detalle"].update(detalle)

                    #  ACUMULAR PONDERACION (+=)
                    self.Data["Ponderacion"].extend(data_temp.get("Ponderacion", []))

                except Exception as e:
                    print(f"Error con {art}: {e}")

            # Valores dummy para correo general
            self.Data["Tendencia"] = "Positiva"
            self.Data["Precio"] = 0
            self.Data["Precio_Nuevo"] = 0
            self.Data["Articulo"] = "MULTIPLES"

            # Envios
            self.EnviarCorreo(self.Data)  
            self.ObtenerCorreoClientes(self.Data.get('Ponderacion'),self.Data.get('PreciosFinales'))

        else:
            try:
                self.Data = {
                    "Articulo": Articulo,
                    "Precio_Nuevo": Precio,
                    "Familia": None,
                    "Categoria": None,
                    "UnidadDeMedida": None,
                    "Compania": None,
                    "Precio": None,
                    "Divisa": None,
                    "Correos": None,
                    "Areas": None,
                    "Porcentaje": None,
                    "Tendencia": None,
                    "ProductoFinal": None,
                    "PreciosFinales": None,
                    "InventarioProducto": None,
                    "Ponderacion": None,
                }

                self.Data.update(self.Deteccion(Articulo))
                self.Data.update(self.FormulaProducto(Articulo))
                self.Data.update(self.PrecioProducto(Articulo))
                self.Data.update(self.AreasProducto(Articulo))
                self.Data.update(self.ObtenerCorreos(self.Data.get('Areas')))
                self.Data.update(self.CalculoTendencia(Precio, self.Data.get('Precio')))
                self.Data.update(self.CalculoPorcentaje(Precio, self.Data.get('Precio'), Dolar))
                self.Data.update(self.TransfomacionFormula(self.Data.get('ProductoFinal')))
                self.Data.update(self.precioPonderado(self.Data.get('ProductoFinal')))
                self.Data.update(self.PrecioFormulas(
                    self.Data.get('InventarioProducto'),
                    self.Data.get('Ponderacion'),
                    Articulo,
                    self.Data.get('Porcentaje')
                ))

                self.EnviarCorreo(self.Data)
                self.ObtenerCorreoClientes(self.Data.get('Ponderacion'),self.Data.get('PreciosFinales'))

            except Exception as e:
                self.error = str(e)
                self.Data = None
        
    # Inicio: Grupo de funciones para calcular porcentaje
    def CalculoTendencia(self,Precio:Decimal,PrecioSys:Decimal):
        
        # Calculo con exprecion Lambda
        Tendencia = "Positiva" if Precio > PrecioSys else "Baja"
        
        return {
            "Tendencia" : Tendencia,
        }
    


    def CalculoPorcentaje(self, Precio: Decimal, PrecioSys: Decimal, Dolar: Decimal):
        Precio = Decimal(str(Precio))
        PrecioSys = Decimal(str(PrecioSys))
        Dolar = Decimal(str(Dolar))

        Precio_MXN = Precio * Dolar
        PrecioSys_MXN = PrecioSys * Dolar

        Delta = Precio_MXN - PrecioSys_MXN

        return {
            "Porcentaje": round(Delta, 2)
        }
        # Fin: Grupo de funciones para calcular porcentaje
    
    # Inicio: Grupo de funciones para sacar la informacion
    def Deteccion(self,Articulo:str):
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Consulta Sql
        cursor.execute(f"""SELECT TOP (1) Familia,Categoria,UnidadDeMedida,Compania FROM [dbo].[dim.Articulos] where CodigoArticulo ='{Articulo}'""")
        row = cursor.fetchone()

        # Variables 
        Familia = row[0]
        Categoria = row[1]
        UnidadDeMedida = row[2]
        Compania = row[3]

        return {
            "Familia" : Familia,
            "Categoria" : Categoria,
            "UnidadDeMedida" : UnidadDeMedida,
            "Compania" : Compania
        }
    
    def PrecioProducto (self,Articulo:str):
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Consulta Sql
        cursor.execute(f"""SELECT TOP 1 [Moneda],[PrecioCompraCalculado] FROM [WH_Oro].[dbo].[fact.OrdenesCompra] where CodigoArticulo = '{Articulo}' ORDER BY [FechaCreacion] DESC""")
        row = cursor.fetchone()

        # Variables 
        Precio = row[1]
        Divisa = row[0]
        return {
            "Precio": Precio,
            "Divisa": Divisa
        }

    def AreasProducto (self,Articulo:str):
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Consulta Sql
        cursor.execute(f"""SELECT DISTINCT CodigoSegmento FROM [dbo].[fact.Ventas] where CodigoArticulo ='{Articulo}'""")
        result = cursor.fetchall()
        areas = [row[0] for row in result]

        return {
            "Areas": areas,
        } 

    def FormulaProducto(self,Articulo:str):
        #Diccionario a Retornar
        Data = {
            "ProductoFinal":{}
        }

        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Consulta Sql
        cursor.execute(f"""
            SELECT 
            f2.CodigoProductoFinal,
            STRING_AGG(f2.CodigoMateriaPrima, ', ') 
                WITHIN GROUP (ORDER BY f2.CodigoMateriaPrima) AS MateriasPrimas,
            
            STRING_AGG(CAST(f2.CantidadUnitario AS VARCHAR(20)), ', ') 
                WITHIN GROUP (ORDER BY f2.CodigoMateriaPrima) AS Porcentajes

        FROM [WH_Oro].[dbo].[dim.Formulas] f1
        JOIN [WH_Oro].[dbo].[dim.Formulas] f2
            ON f1.CodigoProductoFinal = f2.CodigoProductoFinal
        WHERE f1.CodigoMateriaPrima = '{Articulo}'
        AND f2.CodigoProductoFinal LIKE '% - G'
        GROUP BY f2.CodigoProductoFinal
        ORDER BY f2.CodigoProductoFinal
        """)
        result = cursor.fetchall()
        # Empezar a sacar los costos
        for row in result:
            materiales = [mp.strip() for mp in row[1].split(",")]
            porcentajes = [mp.strip() for mp in row[2].split(",")]

            # Convertir a formato SQL: 'A','B','C'
            mapa_porcentajes = {
                mat: float(porc)
                for mat, porc in zip(materiales, porcentajes)
            }
            materiales_sql = ",".join([f"'{mp}'" for mp in materiales])
            print(row[0])
            if row[0] ==  'IVP07331 - G':
                print(f"""
                    WITH CTE AS (
                        SELECT 
                            CodigoArticulo,
                            FechaFisica,
                            Unidad,
                            ROW_NUMBER() OVER (
                                PARTITION BY CodigoArticulo
                                ORDER BY FechaFisica DESC
                            ) AS rn
                        FROM [WH_Oro].[dbo].[fact.TransaccionesInventario]
                        WHERE CodigoArticulo IN ({materiales_sql})
                    ),
                    FormulasCTE AS (
                        SELECT
                            CodigoMateriaPrima,
                            UnidadDeFormula,
                            PorSerie,
                            ROW_NUMBER() OVER (
                                PARTITION BY CodigoMateriaPrima
                                ORDER BY CodigoMateriaPrima
                            ) AS rn
                        FROM [WH_Oro].[dbo].[dim.Formulas]
                    ),
                    OrdencompraCTE AS (
                        SELECT 
                            CodigoArticulo,
                            UnidadCompra,
                            Moneda,
                            PrecioCompraCalculado,
                            ROW_NUMBER() OVER (
                                PARTITION BY CodigoArticulo
                                ORDER BY FechaCreacion DESC
                            ) AS rn
                        FROM [WH_Oro].[dbo].[fact.OrdenesCompra]
                    )
                    SELECT 
                        c.CodigoArticulo,
                        o.PrecioCompraCalculado as Precio,
                        c.FechaFisica,
                        f.UnidadDeFormula AS Formula,
                        c.Unidad AS Inventarios,
                        a.UnidadDeMedida AS Articulos,
                        o.UnidadCompra AS Compra,
                        f.PorSerie,
                        o.Moneda
                    FROM CTE c
                    INNER JOIN [WH_Oro].[dbo].[dim.Articulos] a 
                        ON c.CodigoArticulo = a.CodigoArticulo
                    INNER JOIN FormulasCTE f
                        ON c.CodigoArticulo = f.CodigoMateriaPrima
                        AND f.rn = 1
                    INNER JOIN OrdencompraCTE o
                        ON c.CodigoArticulo = o.CodigoArticulo
                        AND o.rn = 1
                    WHERE c.rn = 1;
                """)
            cursor.execute(f"""
                WITH CTE AS (
                    SELECT 
                        CodigoArticulo,
                        FechaFisica,
                        Unidad,
                        ROW_NUMBER() OVER (
                            PARTITION BY CodigoArticulo
                            ORDER BY FechaFisica DESC
                        ) AS rn
                    FROM [WH_Oro].[dbo].[fact.TransaccionesInventario]
                    WHERE CodigoArticulo IN ({materiales_sql})
                ),
                FormulasCTE AS (
                    SELECT
                        CodigoMateriaPrima,
                        UnidadDeFormula,
                        PorSerie,
                        ROW_NUMBER() OVER (
                            PARTITION BY CodigoMateriaPrima
                            ORDER BY CodigoMateriaPrima
                        ) AS rn
                    FROM [WH_Oro].[dbo].[dim.Formulas]
                ),
                OrdencompraCTE AS (
                    SELECT 
                        CodigoArticulo,
                        UnidadCompra,
                        Moneda,
						PrecioCompraCalculado,
                        ROW_NUMBER() OVER (
                            PARTITION BY CodigoArticulo
                            ORDER BY FechaCreacion DESC
                        ) AS rn
                    FROM [WH_Oro].[dbo].[fact.OrdenesCompra]
                )
                SELECT 
                    c.CodigoArticulo,
                    o.PrecioCompraCalculado as Precio,
                    c.FechaFisica,
                    f.UnidadDeFormula AS Formula,
                    c.Unidad AS Inventarios,
                    a.UnidadDeMedida AS Articulos,
                    o.UnidadCompra AS Compra,
                    f.PorSerie,
                    o.Moneda
                FROM CTE c
                INNER JOIN [WH_Oro].[dbo].[dim.Articulos] a 
                    ON c.CodigoArticulo = a.CodigoArticulo
                INNER JOIN FormulasCTE f
                    ON c.CodigoArticulo = f.CodigoMateriaPrima
                    AND f.rn = 1
                INNER JOIN OrdencompraCTE o
                    ON c.CodigoArticulo = o.CodigoArticulo
                    AND o.rn = 1
                WHERE c.rn = 1;
            """)
            # Guardar todos los resultados
            resultados_materia = cursor.fetchall()

            # Abrir el archivo JSON
            with open("CostosAnteriores.json", "r") as f:
                mapa_delta = json.load(f)

            #Retornar la info
            materias_info = []

            for r in resultados_materia:
                codigo = r[0]

                if codigo in mapa_delta:
                    print(f"[JSON] {codigo} → {mapa_delta[codigo]} (sobrescribe {r[1]})")
                else:
                    print(f"[BD]   {codigo} → {r[1]}")
                precio = Decimal(str(mapa_delta.get(codigo, r[1])))
                porcentaje = Decimal(str(mapa_porcentajes.get(codigo, 0)))  # ojo formato

                precio_final = precio * porcentaje
                materias_info.append({
                    "CodigoArticulo": codigo,
                    "Precio": precio,
                    "Fecha": r[2],
                    "Formula": r[3],
                    "Inventarios": r[4],
                    "Articulos": r[5],
                    "Compra": r[6],
                    "Serie": r[7],
                    "Moneda": "MXN" if codigo in mapa_delta else r[8],
                    "Porcentaje": porcentaje,
                    "PrecioFinal": precio_final,
                    "Cambio": True if codigo in mapa_delta else None
                })

            Data["ProductoFinal"][row[0]] = {
                "Materias": materias_info
            }
            
        producto = Data["ProductoFinal"].get('IVP07331 - G')
        if producto:
            print(producto)
        else:
            print("No se encontró el producto")
        # Retornar la info
        return{
            "ProductoFinal": Data
        }
    
    def TransfomacionFormula (self,Informacion:Dict[str, Any]):
        resultado = {}
        # For para iterar sobre cada Formula
        for clave,valor in Informacion["ProductoFinal"].items():
            resultado[clave] = []  
            # Ciclo para iterar sobre cada una de las Materias con su respectivo condigo
            for materia in valor['Materias']:
                # Calcular si son iguales las medidas, y la cantidad Unitario
                cantidadUnitario = Decimal(str(materia['Porcentaje'])) / Decimal(str(materia['Serie']))
                FormulaUnidad = True if str(materia['Formula'])  == str(materia['Inventarios']) else False
                # Ver si necesita conversion o no, y de ahi a realizar el calculo
                Factor = 1 if FormulaUnidad else Decimal(str(self.ConversionesUnidades(str(materia['CodigoArticulo']),str(materia['Inventarios']),str(materia['Formula']))))
                cantidadEnInventario = cantidadUnitario if Factor == 1 else cantidadUnitario / Factor
                
                #Guardar los resultados
                resultado[clave].append({   
                    "Materia": materia['CodigoArticulo'],
                    "InventarioCantidad": cantidadEnInventario,
                    "Factor": Decimal(Factor),
                    "Precio": materia['Precio'],
                    "Precio": materia['Porcentaje'],
                })        
        return{
            "InventarioProducto":resultado
        }


    def PrecioFormulas(
        self,
        Informacion_Formula: Dict[str, Any],
        Ponderacion: Dict[str, Any],
        Articulo: str,
        Delta: Decimal
    ):
        resultado = {}

        resultado_detalle = {}
        productos_subiran = []
        Delta = Decimal(str(Delta))

        # Mapa: Formula → Costo Promedio
        mapa_ponderado = {
            item["Formula"]: {
                "Promedio": Decimal(str(item["Promedio"])),
                "NombreProducto": item["Articulo"]
            }
            for item in Ponderacion 
        }
        # Recorrer productos
        for clave, lista_materias in Informacion_Formula.items():
            codigo_limpio = clave.replace(" - G", "").strip()
            if codigo_limpio not in mapa_ponderado:
                continue

            impacto_total = Decimal("0")

            for item in lista_materias:
                codigo = item["Materia"]
                cantidad = Decimal(str(item["InventarioCantidad"]))
                if codigo == Articulo:
                    impacto_total += Delta * cantidad
            # SOLO guardar detalle lógica completa
            info = mapa_ponderado[codigo_limpio]

            costo_base = info["Promedio"]
            nombre = info["NombreProducto"]
            costo_nuevo = costo_base + impacto_total


            # Evitar división entre cero
            if costo_base == 0:
                continue

            porcentaje = impacto_total / costo_base

            # Solo considerar si supera el 5%
            if porcentaje >= Decimal("0.05"):
                Funcion.EnvioGeneral = True
                resultado_detalle[clave] = {
                    "CostoPromedio": round(costo_base, 2),
                    "Impacto": round(impacto_total, 2),
                    "CostoNuevo": round(costo_nuevo, 2),
                    "PorcentajeImpacto": round(porcentaje * 100, 2),
                    "SubiraPrecio": True,
                    "NombreProducto": nombre
                }
        #Ordenar de mayor a menor los porcentajes        
        resultado_detalle= dict(sorted(resultado_detalle.items(),key = lambda x : x[1]['PorcentajeImpacto'],reverse=True))
        return {
            "PreciosFinales": {
                "Subiran": productos_subiran,
                "Detalle": resultado_detalle
            }
        }

    def precioPonderado(self,Informacion: Dict[str, Any]):

        # Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Claves
        claves = ",".join(
            f"'{clave.replace('- G', '').strip()}'"
            for clave in Informacion["ProductoFinal"].keys()
        )

        print(f""" 
                SELECT 
                    v.CodigoArticulo,
                    SUM(v.CostoUnitario * v.CantidadInventario) AS Total,
                    SUM(v.CantidadInventario) AS TotalInv,
                    SUM(v.CostoUnitario * v.CantidadInventario) 
                        / NULLIF(SUM(v.CantidadInventario), 0) AS Promedio,
                    MAX(a.Articulo) AS Articulo

                FROM [WH_Oro].[dbo].[fact.Ventas] v
                LEFT JOIN [WH_Oro].[dbo].[dim.Articulos] a
                    ON a.CodigoArticulo = v.CodigoArticulo
                WHERE v.CodigoArticulo IN ({claves})
                GROUP BY v.CodigoArticulo
                HAVING 
                    SUM(v.CostoUnitario * v.CantidadInventario) <> 0
                    AND SUM(v.CantidadInventario) <> 0;
        """)

        cursor.execute (f""" 
                SELECT 
                    v.CodigoArticulo,
                    SUM(v.CostoUnitario * v.CantidadInventario) AS Total,
                    SUM(v.CantidadInventario) AS TotalInv,
                    SUM(v.CostoUnitario * v.CantidadInventario) 
                        / NULLIF(SUM(v.CantidadInventario), 0) AS Promedio,
                    MAX(a.Articulo) AS Articulo

                FROM [WH_Oro].[dbo].[fact.Ventas] v
                LEFT JOIN [WH_Oro].[dbo].[dim.Articulos] a
                    ON a.CodigoArticulo = v.CodigoArticulo
                WHERE v.CodigoArticulo IN ({claves})
                GROUP BY v.CodigoArticulo
                HAVING 
                    SUM(v.CostoUnitario * v.CantidadInventario) <> 0
                    AND SUM(v.CantidadInventario) <> 0;
        """)
        rows = cursor.fetchall()

        if not rows:
            raise ValueError("No se pudo calcular el precio ponderado")  
              
        Ponderacion = [
            {
                "Formula": row[0],
                "TotalPrecio": round(row[1],2),
                "TotalInvenrario": round(row[2],2),
                "Promedio": round(row[3],2),
                "Articulo": row[4],
                "ImpactoCambio" : self.Calculo(row[0],Informacion) or 1,

            }
            for row in rows
        ]
        return {
            "Ponderacion": Ponderacion
        }


    def Calculo(self, Articulo: str, Informacion: Dict[str, Any]):
        
        total = Decimal("0")
        # Claves
        Articulo =f'{Articulo} - G'

        materias = Informacion["ProductoFinal"][Articulo]["Materias"]

        for elemento in materias:
            if elemento["Cambio"]:
                total += Decimal(elemento["PrecioFinal"])

        return total
    # Fin: Grupo de funciones para sacar la informacion


    # Inicio: Conversiones Generales
    def ConversionesUnidades(self,Articulo:str,Nunidad:str,Vunidad:str):
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()
        # Consulta Sql
        cursor.execute(f"SELECT [Factor] FROM [WH_Oro].[dbo].[dim.ConversionesDentroDeLaClase] where Producto = '{Articulo}'")
        row = cursor.fetchone()

        if row:
            return row[0]
        
        cursor.execute(f"SELECT [Factor] FROM [WH_Oro].[dbo].[dim.ConversionesEstandar] where DesdeUnidad= '{Nunidad}' and HastaUnidad = '{Vunidad}'")
        row_n = cursor.fetchone()

        if row_n:
            return row_n[0]
        
        return 1

    # Fin: Conversiones Generales
    

    # Inicio: Grupo de funciones para Envio / Obtencion de Correos
    def ObtenerCorreos(self,id_seccion:List[str]):
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()

        #Areas limpieza
        secciones_limpias = ",".join(id_seccion)
        # Consulta Sql
        cursor.execute(f"SELECT CorreoCoordinador as Correo,Coordinador FROM [dbo].[ref.Celulas] WHERE CodigoSegmento IN ('{secciones_limpias}');")
        rows = cursor.fetchall()
        # Informacion a regresar
        correos = [
            {
                "Correo": row[0],
                "Coordinador": row[1]
            }
            for row in rows
        ]

        return {
            "Correos": correos
        }
    

    
    def EnviarCorreo(self,Data:dict):

        if not Funcion.EnvioGeneral:
            return

        tendencia = Data["Tendencia"]
        mensaje = None

        if tendencia == "Baja":
            color_tendencia = "#2a9d8f"   # verde elegante
            color_porcentaje = "#2a9d8f"
            bg_alerta = "#e6f4f1"
            mensaje = "El precio ha disminuido, lo cual representa una mejora en costos."
        else:
            color_tendencia = "#e63946"   # rojo elegante
            color_porcentaje = "#e63946"
            bg_alerta = "#fdecea"
            mensaje = "El precio ha incrementado, se recomienda revisión."

        Envion = 'Positiva' if tendencia == "Baja" else 'Negativa'

        # Variables para el envio de Informacion    
        ColorTendencia=color_tendencia
        BgAlerta=bg_alerta
        Mensaje=mensaje
        try:
            PreciosFinales = Data.get("PreciosFinales", {})
            Detalle = PreciosFinales.get("Detalle", {})
            Subiran = PreciosFinales.get("Subiran", [])
            filas_productos = ""

            for producto, valores in sorted(
                Detalle.items(),
                key=lambda x: float(x[1]["PorcentajeImpacto"]),
                reverse=True
            ):
                anterior = float(valores["CostoPromedio"])
                nuevo = float(valores["CostoNuevo"])
                diff = float(valores["PorcentajeImpacto"])
                NombreProducto = valores["NombreProducto"]

                color = "#e63946" if diff > 0 else "#2a9d8f"

                filas_productos += f"""
                    <tr>
                        <td style="border-bottom:1px solid #eee;">{NombreProducto}</td>
                        <td style="border-bottom:1px solid #eee;">{producto}</td>
                        <td style="border-bottom:1px solid #eee;">${anterior:,.2f}</td>
                        <td style="border-bottom:1px solid #eee; color:{color}; font-weight:bold;">
                            {diff:,.2f}%
                        </td>
                        <td style="border-bottom:1px solid #eee;">${nuevo:,.2f}</td>
                    </tr>
                """
            lista_suben = ""

            for producto in Subiran:
                if producto not in Detalle:  # solo los que NO tienen detalle
                    lista_suben += f"""
                        <li style="margin-bottom:5px;">{producto}</li>
                    """

            # Cuerpo del Html
            html = f"""
              <!DOCTYPE html>
                <html>
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Notificación de Precio</title>
                </head>

                <body style="margin:0; padding:0; background-color:#f4f6f8; font-family: Arial, sans-serif;">

                <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                        <td align="center" style="padding:20px;">

                            <!-- CONTENEDOR -->
                            <table width="900" cellpadding="0" cellspacing="0" 
                            style="width:100%; max-width:900px; background:#ffffff; border-radius:10px; overflow:hidden;">

                                <!-- HEADER -->
                                <tr>
                                    <td style="background:#2f3e46; color:#ffffff; padding:20px; text-align:center;">
                                        <h2 style="margin:0; font-weight:500;">Actualización de Precio</h2>
                                    </td>
                                </tr>
                                
                                <!-- DISCLAIMER -->
                                <tr>
                                    <td style="padding:20px;">
                                        <div style="background:#fdecea; color:#b71c1c; padding:15px; border-radius:8px; font-size:14px; text-align:center; font-weight:500;">
                                            Los costos mostrados en la siguiente tabla solo incluyen el costo del granel y NO incluyen el empaquetado
                                        </div>
                                    </td>
                                </tr>

                                <!-- BODY -->
                                <tr>
                                    <td style="padding:30px; color:#333;">

                                        <p style="font-size:15px; margin:0 0 15px 0;">
                                            Se ha detectado un cambio en el precio del siguiente artículo:
                                        </p>

                                        <!-- TABLA -->
                                        <h3 style="margin-top:30px; font-weight:500;">Impacto en Productos Finales</h3>

                                        <table width="100%" cellpadding="8" cellspacing="0" 
                                        style="border-collapse: collapse; margin-top:10px; font-size:14px; table-layout:fixed;">

                                            <tr style="background:#f8f9fa;">
                                                <th align="left" style="word-break:break-word;">Nombre producto</th>
                                                <th align="left" style="word-break:break-word;">Codigo producto</th>
                                                <th align="left" style="word-break:break-word;">Costo Anterior</th>
                                                <th align="left" style="word-break:break-word;">Impacto</th>
                                                <th align="left" style="word-break:break-word;">Costo Nuevo</th>
                                            </tr>

                                            {filas_productos}

                                        </table>

                                        {f"""
                                        <h3 style="margin-top:30px; font-weight:500;">Productos que podrían subir de precio</h3>

                                        <div style="background:#fff3cd; padding:15px; border-radius:8px; font-size:14px; color:#856404;">
                                            <p style="margin:0 0 10px 0;">
                                                Los siguientes productos no cuentan con información completa de costos, pero podrían verse afectados:
                                            </p>
                                            <ul style="padding-left:20px; margin:0;">
                                                {lista_suben}
                                            </ul>
                                        </div>
                                        """ if lista_suben else ""}

                                        <!-- ALERTA -->
                                        <div style="margin-top:25px; padding:15px; border-radius:8px; background:{BgAlerta}; color:{ColorTendencia}; font-size:14px;">
                                            {Mensaje}
                                        </div>

                                    </td>
                                </tr>

                                <!-- FOOTER -->
                                <tr>
                                    <td style="background:#f1f3f5; text-align:center; padding:15px; font-size:12px; color:#777;">
                                        Sistema automático de notificaciones
                                    </td>
                                </tr>

                            </table>

                        </td>
                    </tr>
                </table>

                </body>
                </html>
            """

            # Destinatario y contenido
            msg = EmailMessage()
            msg['Subject'] = f"Nueva Alerta de Costos ({Envion})"
            msg['From'] = Funcion.Usuario
            msg['To'] = 'pablo.valadez@interlub.com'
            msg.add_alternative(html, subtype="html")

            # Conectar y enviar
            with smtplib.SMTP(Funcion.Host, Funcion.Puerto) as smtp:
                smtp.starttls()  # inicia cifrado TLS
                smtp.login(Funcion.Usuario, Funcion.Contrasenia)
                smtp.send_message(msg)
        except smtplib.SMTPAuthenticationError as e:
            # Handle incorrect login details
            print(f"Authentication error: {e}. Check your username and password.")

        except smtplib.SMTPConnectError as e:
            # Handle connection issues (e.g., wrong server/port, network problems)
            print(f"Connection error: {e}. Check server address and port.")

        except Exception as e:
            # Handle any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    def ObtenerCorreoClientes(self,Ponderacion:Dict[str, Any],PrecionFinales:Dict[str, Any]):

        detalle = PrecionFinales.get("Detalle", {})

        dataPondetacion = ",\n".join([
            f"('{item['Formula']}',"
            f"{item['Promedio']},"
            f"{detalle.get(f'{item['Formula']} - G', {}).get('CostoNuevo', item['ImpactoCambio'])})"
            for item in Ponderacion
        ])

        # Objeto de Libro
        data = defaultdict(lambda: {
            "correo": None,
            "PrecioUnitario": None,
            "PrecioSugerido": None,
            "items": []
        })
        #Llamada hacia la base de datos Fabric
        conexion = Conexion()
        cursor = conexion.cursor()

       
        print(f"""
                SELECT 
                    t.[ClienteConCodigo], 
                    t.[CodigoArticulo], 
                    t.[Articulo], 
                    t.[Segmento], 
                    t.[Coordinador], 
                    t.[CorreoCoordinador],

                    ROUND(calc.PrecioActual, 2) AS PrecioUnitario,

                    t.[UtilidadBrutaPorcentaje],

                    ROUND(calc.PrecioSugerido, 2) AS PrecioSugerido,

                    ROUND(p.PorcentajeCalc, 2) AS Porcentaje

                FROM [WH_Oro].[dbo].[fact.ClientesArticulos] t

                INNER JOIN (
                    VALUES 
                        {dataPondetacion}
                ) AS datos(Formula, Promedio , ImpactoCambio)
                    ON t.CodigoArticulo = datos.Formula
                CROSS APPLY (
                    SELECT 
                        CASE 
                            WHEN t.Moneda = 'USD' THEN t.UltimoPrecioDeVenta * 17.65
                            WHEN t.Moneda = 'EUR' THEN t.UltimoPrecioDeVenta * 20.77

                            ELSE t.UltimoPrecioDeVenta
                        END AS PrecioActual,

                        CASE 
                            WHEN t.UtilidadBrutaPorcentaje IS NULL 
                                OR t.UtilidadBrutaPorcentaje >= 1 
                            THEN NULL
                            WHEN t.Moneda = 'USD' THEN ((datos.Promedio + datos.ImpactoCambio) / (1 - t.UtilidadBrutaPorcentaje)) * 17.65
                            WHEN t.Moneda = 'EUR' THEN ((datos.Promedio + datos.ImpactoCambio) / (1 - t.UtilidadBrutaPorcentaje)) * 20.77
                            ELSE (datos.Promedio + datos.ImpactoCambio) / (1 - t.UtilidadBrutaPorcentaje)
                        END AS PrecioSugerido
                ) calc

                CROSS APPLY (
                    SELECT 
                        ((calc.PrecioSugerido - calc.PrecioActual) / calc.PrecioActual) * 100 AS PorcentajeCalc
                ) p

                WHERE 
                    calc.PrecioSugerido IS NOT NULL
                    AND calc.PrecioActual > 0
                    AND p.PorcentajeCalc >= 5

                ORDER BY Porcentaje DESC;
        """)
        cursor.execute(f"""
               SELECT 
                    t.[ClienteConCodigo], 
                    t.[CodigoArticulo], 
                    t.[Articulo], 
                    t.[Segmento], 
                    t.[Coordinador], 
                    t.[CorreoCoordinador],

                    ROUND(calc.PrecioActual, 2) AS PrecioUnitario,

                    t.[UtilidadBrutaPorcentaje],

                    ROUND(calc.PrecioSugerido, 2) AS PrecioSugerido,

                    ROUND(p.PorcentajeCalc, 2) AS Porcentaje,
                    t.[Moneda],
                    ROUND (calc.PrecioImpacto,2) as PrecioImpacto

                FROM [WH_Oro].[dbo].[fact.ClientesArticulos] t

                INNER JOIN (
                    VALUES 
                    {dataPondetacion}
                ) AS datos(Formula, Promedio , ImpactoCambio)
                    ON t.CodigoArticulo = datos.Formula

                CROSS APPLY (
                    SELECT 
                        CASE 
                            WHEN t.Moneda = 'USD' THEN t.UltimoPrecioDeVenta * 17.65
                            ELSE t.UltimoPrecioDeVenta
                        END AS PrecioActual,

                        CASE 
                            WHEN t.UtilidadBrutaPorcentaje IS NULL 
                                OR t.UtilidadBrutaPorcentaje >= 1 
                            THEN NULL
                            ELSE (datos.ImpactoCambio) / (1 - t.UtilidadBrutaPorcentaje)
                        END AS PrecioSugerido,
                        CASE 
                            WHEN datos.Promedio IS NULL OR datos.ImpactoCambio IS NULL 
                            THEN 0
                            ELSE datos.Promedio + datos.ImpactoCambio
                        END AS PrecioImpacto
                ) calc

                CROSS APPLY (
                    SELECT 
                        ((calc.PrecioSugerido - calc.PrecioActual) / calc.PrecioActual) * 100 AS PorcentajeCalc
                ) p

                WHERE 
                    calc.PrecioSugerido IS NOT NULL
                    AND calc.PrecioActual > 0
                    AND p.PorcentajeCalc >= 5

                ORDER BY calc.PrecioSugerido DESC;
        """)

        # Guardado de datos
        dataCArticulos = cursor.fetchall()

        for row in dataCArticulos:
            coordinador = row[4]
            correo = row[5]

            # Guardar correo una sola vez
            if data[coordinador]["correo"] is None:
                data[coordinador]["correo"] = correo


            # Agregar items
            if  row[8] > row[6] :
                data[coordinador]["items"].append({
                    "ClienteConCodigo": row[0],
                    "CodigoArticulo": row[1],
                    "Articulo": row[2],
                    "Segmento": row[3],
                    "PrecioUnitario" :  row[6],
                    "PrecioSugerido" :  row[8],
                    "Porcentaje" :  row[9],
                    "PrecioImpacto" :  row[11],
                })
        self.EnvioInformacionClientes(data,PrecionFinales)

    def EnvioInformacionClientes(self, data: dict,PrecionFinales:Dict[str, Any]):    
          
        if not Funcion.EnvioGeneral:
            return

        #Iteracion sobre cada cordinador
        for coordinador,info in data.items():

            # Informacion del coordinador
            correo = info["correo"]
            items = info["items"]

            # Informacion general
            filas_clientes = ""

            for item in items:
                diff = float(item["Porcentaje"])
                color = "#e63946" if diff > 0 else "#2a9d8f"
                detalle = PrecionFinales.get("Detalle", {})
                clave = f"{item['CodigoArticulo']} - G"
                print(clave)
                costo_final = item["PrecioSugerido"]

                if clave in detalle:
                    print('Dentro de la metrica')
                    costo_nuevo = detalle[clave].get("CostoNuevo")
                    if costo_nuevo:
                        costo_final = costo_nuevo
                    else :
                        print(f'FUera para {clave} de la metrica')
                else:
                    continue



                filas_clientes += f"""
                    <tr>
                        <td style="border-bottom:1px solid #eee;">{item["ClienteConCodigo"]}</td>
                        <td style="border-bottom:1px solid #eee;">{item["CodigoArticulo"]}</td>
                        <td style="border-bottom:1px solid #eee;">{item["Articulo"]}</td>
                        <td style="border-bottom:1px solid #eee;">{item["Segmento"]}</td>
                        <td style="border-bottom:1px solid #eee;">$ {item["PrecioUnitario"]}</td>
                        <td style="border-bottom:1px solid #eee; color:{color}; font-weight:bold;">
                            $ {round(costo_final,2)}
                        </td>
                        <td style="border-bottom:1px solid #eee;">$ {item["PrecioSugerido"]}</td>
                    </tr>
                """
            
            html = f"""
                <!DOCTYPE html>
                <html>
                <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Notificación de Clientes</title>
                </head>

                <body style="margin:0; padding:0; background-color:#f4f6f8; font-family: Arial, sans-serif;">

                <table width="100%" cellpadding="0" cellspacing="0">
                    <tr>
                        <td align="center" style="padding:20px;">

                            <!-- CONTENEDOR -->
                            <table width="900" cellpadding="0" cellspacing="0" 
                            style="width:100%; max-width:900px; background:#ffffff; border-radius:10px; overflow:hidden;">

                                <!-- HEADER -->
                                <tr>
                                    <td style="background:#2f3e46; color:#ffffff; padding:20px; text-align:center;">
                                        <h2 style="margin:0; font-weight:500;">Clientes Afectados</h2>
                                    </td>
                                </tr>

                                <!-- BODY -->
                                <tr>
                                    <td style="padding:30px; color:#333;">

                                        <h2 style="margin:0 0 10px 0; font-weight:500;">
                                            Hola <b>{coordinador}</b>
                                        </h2>

                                        <p style="font-size:15px; margin:0 0 15px 0;">
                                            Se detectó un cambio de precios en los siguientes artículos.
                                        </p>

                                        <!-- TABLA -->
                                        <h3 style="margin-top:30px; font-weight:500;">Detalle por Cliente</h3>

                                        <table width="100%" cellpadding="8" cellspacing="0" 
                                        style="border-collapse: collapse; margin-top:10px; font-size:14px; table-layout:fixed;">

                                            <tr style="background:#f8f9fa;">
                                                <th align="left" style="word-break:break-word;">Cliente</th>
                                                <th align="left" style="word-break:break-word;">Código</th>
                                                <th align="left" style="word-break:break-word;">Artículo</th>
                                                <th align="left" style="word-break:break-word;">Segmento</th>
                                                <th align="left" style="word-break:break-word;">Anterior Precio</th>
                                                <th align="left" style="word-break:break-word;">Nuevo Costo</th>
                                                <th align="left" style="word-break:break-word;">Precio Sugerido</th>
                                            </tr>

                                            {filas_clientes}

                                        </table>

                                        <!-- ALERTA -->
                                        <div style="margin-top:25px; padding:15px; border-radius:8px; background:#ffe5e5; color:#b00020; font-size:14px;">
                                            El precio sugerido es para mantener el mismo porcentaje de rentabilidad.
                                        </div>

                                    </td>
                                </tr>

                                <!-- FOOTER -->
                                <tr>
                                    <td style="background:#f1f3f5; text-align:center; padding:15px; font-size:12px; color:#777;">
                                        Sistema automático de notificaciones
                                    </td>
                                </tr>

                            </table>

                        </td>
                    </tr>
                </table>

                </body>
                </html>
                """
            # Destinatario y contenido
            msg = EmailMessage()
            msg['Subject'] = f"Nueva Alerta de Precios Sugeridos"
            msg['From'] = Funcion.Usuario
            msg['To'] = 'pablo.valadez@interlub.com'
            #Cuerpo del Html
            msg.add_alternative(html, subtype="html")
            # Conectar y enviar
            with smtplib.SMTP(Funcion.Host, Funcion.Puerto) as smtp:
                smtp.starttls()  # inicia cifrado TLS
                smtp.login(Funcion.Usuario, Funcion.Contrasenia)
                smtp.send_message(msg)
        
    # Fin: Grupo de funciones para Envio / Obtencion de Correos



X = Funcion(
    ["IAM0012"],   # ← varios artículos
    [44.30],          # ← sus precios en el mismo orden
    17.65                    # ← dólar (uno solo)
)