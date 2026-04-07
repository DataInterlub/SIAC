# Sistema de Anticipacion de Costos -SIAC- 

Uso del SIAC

    El SIAC es un desarrollo que permite prevenir a los vendedores las tendencias y alzas de nuestros productos finales por alguna subida de nuestros precios con respecto a una materia prima.

    El SIAC permite calcular el nuevo precio de una fórmula y/o producto con sus históricos con respecto a la información de ventas, y permitir la notificación a las personas correspondientes con respecto a la realización de algún movimiento con esta nueva información.

Plataformas para el desarrollo

    Python → Lógica en general del código
    Fabric → Bases de datos


Librerías

    smtplib → Envío de correos electrónicos con cuerpos HTML
    json → Lectura de archivos en formato JSON y manipulación de datos

Estructura del proyecto

    Sistema Alerta Costos/
    │── Conexion.py
    │── CostosAnteriores.json
    │── Funcion.py

SECCION : Punto de entrada

    X = Funcion(
        ["IAM0012"],   # Materias primas
        [44.30],       # Nuevos costos (mismo orden)
        17.65          # Tipo de cambio USD
    )
    
    Descripción : 

        La función principal actúa como punto de entrada del sistema.
        Debido a que la lógica está basada en Programación Orientada a Objetos (POO), se reciben tres parámetros principales:

        Materias primas → Colección de identificadores de artículos
        Nuevos costos → Lista de precios correspondientes (misma posición que los artículos)
        Tipo de cambio → Valor único utilizado para conversiones

    Consideraciones importantes: 
        Ambas listas deben tener la misma longitud
        Cada artículo debe corresponder a su respectivo costo
        Se pueden procesar N cantidad de elementos simultáneamente

    Ejemplo conceptual : 
        Artículo:   IAM0012   IAM0456
        Costo:      44.30     38.10


SECCION : Calculo de direcciones 

    1. def CalculoTendencia(self,Precio:Decimal,PrecioSys:Decimal)
    2. def CalculoPorcentaje(self, Precio: Decimal, PrecioSys: Decimal, Dolar: Decimal):
    
    Descripción : 
        Ambas funciones qe pertenecen al grupo de funciones para calcular comportamiento , nos permiten entendender cual es - valga la redundancia -  el comportamiento de la materia prima con respecto a su cambio.

        La primera funcon nos permite ver su su tendencia es positiva o negativa. En caso de que el precio sea menor con respecto al ultimo de precio de venta, la tendencia sera positiva. En el caso contrario negativa.

        La segunda sirve para el calculo de delta con respecto a los dos parametros que mencionamos anteriormente ... El precio anterior con respecto a sistema y/o venta, y el segundo que es el nuevo precio que se esta vendiendo.
        
    Consideraciones importantes: 
        Precio → Representa el nuevo costo de la materia prima
        PrecioSys → Representa el precio anterior (histórico o de sistema)
        Dolar → Se utiliza para conversión cuando los valores están en otra moneda
        La tendencia es positiva cuando el nuevo precio es menor al anterior
        La tendencia es negativa cuando el nuevo precio es mayor al anterior
        El cálculo porcentual depende directamente de la diferencia entre ambos valores
        Es importante validar que PrecioSys ≠ 0 para evitar divisiones inválidas

    Ejemplo conceptual : 
        Precio anterior (PrecioSys): 50
        Precio nuevo (Precio):       40

        Resultado:
            - Tendencia: Positiva (↓ baja el precio)
            - Impacto:   -20%
            Precio anterior (PrecioSys): 50
            Precio nuevo (Precio):       65

        Resultado:
            - Tendencia: Negativa (↑ sube el precio)
            - Impacto:   +30%


SECCION : Informacion General

    1. def Deteccion(self,Articulo:str):
    2. def PrecioProducto (self,Articulo:str):
    3. def AreasProducto (self,Articulo:str):
    4. def FormulaProducto(self,Articulo:str):
    5. def TransfomacionFormula (self,Informacion:Dict[str, Any]):
    6. def PrecioFormulas(self,Informacion_Formula: Dict[str, Any],Ponderacion: Dict[str, Any],Articulo: str,Delta: Decimal):
    7. def precioPonderado(self,Informacion: Dict[str, Any]):
    8. def Calculo(self, Articulo: str, Informacion: Dict[str, Any]):

    
    Descripción : 
    
        Esta funcion en esta seccion es -ConversionesUnidades-, la cual es encargada de poder tomar la medida en que esta siendo recibida la meteria prima - Kilogramos, Litros ... etc - , y es encargada de que cuadre su sistema de medicion con respecto a como se vende, como se almacena y como se compra para que todos los parametros queden de la misma forma y se pueda realizar el calculo correspondiente, y sacar asi su factor de conversion y aproximarnos al calculo de precio de una mejor manera.

        Articulo ---> Nombre del articulo
        Nunidad ---> Nueva unidad de medida
        Vunidad ---> Antigua unidad de medida

        Deteccion nos permite obtener toda la informacion relevante de la materia prima que esta siendo modificada en su precio, y dispara el sistema.

        PrecioProducto nos permite tomar el ultimo precio con respecto al registrado al sistema.

        AreasProducto nos permite obtener que areas de la empresa manejan esa formula.

        FormulaProducto nos permite visualizar con respecto a cada materia prima, y sobre todo con la que esta subiendo en ese momento o esta siendo impactada con respecto a un precio nuevo; Cuales formulas utilizan esa materia, asi pudiento extraer datos como - Moneda de compra, Codigo Articulo, Ultima fecha de transaccion, Unidad de medida en Inventarios como en Almacen y otros - .
        
        PrecioFormulas como su nombre lo indica os permite calcular parametros como si subira de precio con respcecto al parametro del 5% alguna formula, en caso de que si entonces se indexa a la informacion que va a ser retornada. Datos como - Costo Promedio , Costo Nuevo, Nombre del Producto -, son algunos de los parametros que toma.

        TransfomacionFormula se complementa con otras funciones de la seccion siguiente, que en caso de que haya una discrepancia en medidas, retornara cual seria su Factor y Porcentaje con respecto al nuevo cambio de medidas y ajuste que se le realizo.

        PrecioPonderado como su nombre lo indica busca sacar el precio ponderado de cada una de las funciones, tomando en cuenta el parametro de informacion, que son todas las formulas con su respectivo incremento de porcentaje, y indexacion de informacion de los alementos que anteriormente comentamos, que se apoya en la funcion "Calculo" para poder calcular el impacto con respecto a cada formula.

        Calculo en este caso como lo comentamos anteriormente es exclusivameente para poder sacar el impacto de cambio que la funcion de "PrecioPonderado" retorna en informacion como uno de sus parametros en un json.


        
    Consideraciones importantes: 
        Deteccion
        Punto inicial del proceso
        Obtiene información relevante de la materia prima
        Dispara todo el flujo de cálculo
        PrecioProducto
        Recupera el último precio registrado en sistema
        Sirve como base para comparar cambios
        AreasProducto
        Identifica qué áreas de la empresa utilizan el producto
        Permite segmentar el impacto
        FormulaProducto
        Obtiene las fórmulas donde se utiliza la materia prima
        Extrae datos clave como:
        Moneda de compra
        Código de artículo
        Unidad de medida
        Última transacción
        TransfomacionFormula
        Ajusta discrepancias de unidades
        Calcula factores de conversión y ajustes necesarios
        PrecioFormulas
        Calcula el impacto en cada fórmula
        Evalúa incrementos (ej. > 5%)
        Agrega información relevante:
        Costo promedio
        Costo nuevo
        Nombre del producto
        precioPonderado
        Calcula el impacto global ponderado
        Considera múltiples fórmulas y su peso relativo
        Se apoya en la función Calculo
        Calculo
        Calcula el impacto porcentual final
        Retorna resultados estructurados en formato tipo JSON

    Ejemplo conceptual : 

        - TransfomacionFormula → Ajusta unidades (kg → tambor)
        - PrecioFormulas → Calcula impacto por fórmula

        Resultado por fórmula:
        Producto A → +8%
        Producto B → +3%
        Producto C → +12%

        - precioPonderado → Calcula impacto global

        Impacto final ponderado:
        +7.5%

    Tablas utilizadas : 
    
        Articulos
        OrdenesCompra
        Ventas
        Formulas
        TransaccionesInventario

SECCION : Conversiones Generales

    1. def ConversionesUnidades(self,Articulo:str,Nunidad:str,Vunidad:str):
    
    Descripción : 
        Esta funcion en esta seccion es -ConversionesUnidades-, la cual es encargada de poder tomar la medida en que esta siendo recibida la meteria prima - Kilogramos, Litros ... etc - , y es encargada de que cuadre su sistema de medicion con respecto a como se vende, como se almacena y como se compra para que todos los parametros queden de la misma forma y se pueda realizar el calculo correspondiente, y sacar asi su factor de conversion y aproximarnos al calculo de precio de una mejor manera.

        Articulo ---> Nombre del articulo
        Nunidad ---> Nueva unidad de medida
        Vunidad ---> Antigua unidad de medida

        Solo se activa esta funcion cuando hay una discrepancia en sistemas de medicion con respecto al articulo, retornando el factor de conversion diferente a 1 para el calculo de su precio.


        
    Consideraciones importantes: 
        Articulo → Identificador o nombre de la materia prima
        Nunidad → Unidad actual o nueva (entrada)
        Vunidad → Unidad anterior o base del sistema
        La función solo se ejecuta cuando hay diferencias entre unidades
        Si las unidades coinciden, el factor de conversión es 1
        Se priorizan las conversiones específicas antes que las estándar
        El factor de conversión se utiliza para estandarizar cálculos posteriores
        Es fundamental mantener coherencia entre:
        Unidad de compra
        Unidad de almacenamiento
        Unidad de venta
        Una mala conversión puede afectar directamente el cálculo final del precio

    Ejemplo conceptual : 

        Artículo: Grasa vegetal industrial

            Sistema:
            - Unidad base: Kilogramos (kg)

            Almacen:
            - Nueva unidad: Gramos (g)

            Conversión (ConversionesEstandar):
            1 kg = 1000 g

            Resultado:
            - Factor de conversión: 0.001

        Artículo: Grasa industrial en bloque

            Sistema:
            - Unidad base: Kilogramos (kg)

            Almacen:
            - Nueva unidad: Litros

            Conversión (ConversionesDentroDeLaClase):
            1 Listros = 20 kg

            Resultado:
            - Factor de conversión: 20

    Tablas utilizadas : 
    
        ConversionesDentroDeLaClase
        ConversionesEstandar


SECCION : Envio de correos

    1. def EnviarCorreo(self,Data:dict):
    2. def ObtenerCorreoClientes(self,Ponderacion:Dict[str, Any],PrecionFinales:Dict[str, Any]):
    3. def EnvioInformacionClientes(self, data: dict,PrecionFinales:Dict[str, Any]):
    
    Descripción : 
        Se consideran 3 funciones, las cuales como su nombre lo indican tienen como objetivo final el envio de correos con la informacion adecuada.

        Para el envio de la notificacion general se utiliza la primera funcion, como parametro toma toda la informacion que anteriormete se registro en el diccionario general llamado "Data". Calcula algunas variables, ve cual es la tendencia y se envia a toda la gente que vende el producto en general en la empresa, para que vean general como les va a afectar.

        Para el envio de las notificacaciones personalizadas se utiliza la 3 funcion, que es alimentada por la segunda; La segunda es enargada de los datos de Ponderacion de cada uno de los articulos y sus precios finales, de obtener - Precio sugerido ,  Producto por persona encargada -  correo de la persona encargada ,  Nombre referente a la formula que se saco precio , y el cliente al cual corresponde -. Despues de esto le pasa la informacion a la 3 funcion, y al igual que la primera se envia ya no de manera general, si no que esta vez de una manera por individuo que meneje ese cliente.



        
    Consideraciones importantes: 
        EnviarCorreo
            Recibe un diccionario global (Data) con toda la información procesada
            Evalúa tendencias e impacto general
            Envía correos a nivel global a los vendedores
        ObtenerCorreoClientes
            Procesa información de:
                Ponderación de artículos
                Precios finales
            Obtiene:
                Precio sugerido
                Producto asignado
                Correo del responsable
                Nombre de la fórmula
                Cliente asociado
        EnvioInformacionClientes
            Recibe la información procesada
            Realiza envíos personalizados por cliente/responsable
        El flujo entre funciones es:
            Se procesan datos generales
            Se obtiene información por cliente
            Se envían notificaciones individuales

    Ejemplo conceptual : 

      Escenario:
        Se detecta un incremento en el precio de una grasa industrial

        Resultado:

        1. Envío general:
        - Se notifica a todos los vendedores
        - Se muestra el impacto global del cambio

        2. Envío personalizado:
        Cliente: Industria XYZ
        Producto: Grasa vegetal industrial
        Responsable: Juan Pérez
        Correo: juan.perez@empresa.com
        Precio sugerido: $52.30

        - Se envía un correo específico con información detallada

    Tablas utilizadas : 

        ClientesArticulos



Documentacion creada :

    07/04/2026


