<h1 align="center" style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Sistema de Anticipación de Costos - SIAC</h1>

<p align="center" style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Sistema inteligente para el análisis y prevención de variaciones de costos en productos.
</p>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Uso del SIAC</h2>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
El <b>SIAC</b> es un desarrollo diseñado para <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">anticipar tendencias y alzas</span> en los costos de productos finales, 
derivadas de cambios en los precios de materias primas.
</p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
Este sistema permite a los vendedores tomar decisiones informadas mediante el análisis de datos históricos y variaciones actuales.
</p>

<br>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 Calcula el <b>nuevo precio</b> de fórmulas y productos.<br>
 Analiza <b>históricos de ventas</b>.<br>
 Detecta <b>impactos por cambios en materia prima</b>.<br>
 Genera <b>notificaciones automáticas</b> a los responsables.
</p>
</div>

<br>

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Funcionalidades principales</h2>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li> Análisis de tendencias de costos</li>
    <li> Cálculo automatizado de precios</li>
    <li> Sistema de alertas y notificaciones</li>
    <li> Evaluación de impacto por cambios en insumos</li>
</ul>

<br>

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Plataformas para el desarrollo</h2>

<table style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;width:100%; border-collapse: collapse; color:#CCC;">
    <tr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#2A2A2A;">
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Tecnología</th>
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Uso</th>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Python</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Lógica general del sistema</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;"> Fabric</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Gestión de bases de datos</td>
    </tr>
</table>

<br>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">
<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Librerías</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
    <li><b>smtplib</b> → Envío de correos electrónicos con soporte para cuerpos HTML</li>
    <li><b>json</b> → Lectura y manipulación de archivos en formato JSON</li>
</ul>

</div>

<br>
<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Punto de entrada</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">

<pre style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD; margin:0;">
X = Funcion(
    ["IAM0012"],   # Materias primas
    [44.30],       # Nuevos costos (mismo orden)
    17.65          # Tipo de cambio USD
)
</pre>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Descripción</h3>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
La función principal actúa como el <b>punto de entrada del sistema</b>.
Debido a que la arquitectura está basada en <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Programación Orientada a Objetos (POO)</span>, 
se reciben tres parámetros fundamentales:
</p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li> <b>Materias primas</b> → Colección de identificadores de artículos</li>
    <li> <b>Nuevos costos</b> → Lista de precios correspondientes (misma posición que los artículos)</li>
    <li> <b>Tipo de cambio</b> → Valor único utilizado para conversiones</li>
</ul>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Consideraciones importantes</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
    <li> Ambas listas deben tener la misma longitud</li>
    <li> Cada artículo debe corresponder a su respectivo costo</li>
    <li> Se pueden procesar <b>N cantidad de elementos</b> simultáneamente</li>
</ul>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Ejemplo conceptual</h3>

<table style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;width:100%; border-collapse: collapse; color:#CCC;">
    <tr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#2A2A2A;">
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Artículo</th>
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">IAM0012</th>
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">IAM0456</th>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Costo</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">44.30</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">38.10</td>
    </tr>
</table>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Este modelo permite mantener una relación directa entre cada artículo y su costo mediante índices.
</p>
<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Cálculo de direcciones</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">

<pre style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD; margin:0;">
1. def CalculoTendencia(self, Precio: Decimal, PrecioSys: Decimal)
2. def CalculoPorcentaje(self, Precio: Decimal, PrecioSys: Decimal, Dolar: Decimal)
</pre>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Descripción</h3>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
Ambas funciones pertenecen al conjunto encargado de analizar el <b>comportamiento de las materias primas</b> 
respecto a sus variaciones de precio.
</p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
La primera función determina si la <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">tendencia es positiva o negativa</span>, 
mientras que la segunda calcula el <b>impacto porcentual (delta)</b> entre el precio anterior y el nuevo.
</p>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; margin-top:10px;">
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 <b>CalculoTendencia</b> → Define si el precio va a la baja o al alza.<br>
 <b>CalculoPorcentaje</b> → Calcula la variación porcentual entre ambos precios.
</p>
</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Consideraciones importantes</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li> <b>Precio</b> → Representa el nuevo costo de la materia prima</li>
    <li> <b>PrecioSys</b> → Representa el precio anterior (histórico o de sistema)</li>
    <li> <b>Dolar</b> → Se utiliza para conversión cuando los valores están en otra moneda</li>
    <li> Tendencia <b>positiva</b> → Cuando el nuevo precio es menor al anterior</li>
    <li> Tendencia <b>negativa</b> → Cuando el nuevo precio es mayor al anterior</li>
    <li> El cálculo porcentual depende directamente de la diferencia entre ambos valores</li>
    <li>Validar que <b>PrecioSys ≠ 0</b> para evitar divisiones inválidas</li>
</ul>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Ejemplo conceptual</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
<b>Escenario 1:</b><br>
Precio anterior: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">50</span><br>
Precio nuevo: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">40</span>
</p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li> Tendencia: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#2a9d8f;">Positiva</b> (↓ baja el precio)</li>
    <li> Impacto: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#2a9d8f;">-20%</b></li>
</ul>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
<b>Escenario 2:</b><br>
Precio anterior: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">50</span><br>
Precio nuevo: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">65</span>
</p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li> Tendencia: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#e63946;">Negativa</b> (↑ sube el precio)</li>
    <li> Impacto: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#e63946;">+30%</b></li>
</ul>

</div>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Estas funciones son clave para la toma de decisiones, ya que permiten identificar rápidamente el impacto de cambios en costos.
</p>


<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Información General</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">

<pre style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD; margin:0;">
1. def Deteccion(self, Articulo: str)
2. def PrecioProducto(self, Articulo: str)
3. def AreasProducto(self, Articulo: str)
4. def FormulaProducto(self, Articulo: str)
5. def TransfomacionFormula(self, Informacion: Dict[str, Any])
6. def PrecioFormulas(self, Informacion_Formula: Dict[str, Any], Ponderacion: Dict[str, Any], Articulo: str, Delta: Decimal)
7. def precioPonderado(self, Informacion: Dict[str, Any])
8. def Calculo(self, Articulo: str, Informacion: Dict[str, Any])
</pre>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Descripción</h3>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
     - Esta sección agrupa las funciones encargadas de procesar la <b>información general del sistema</b> y ejecutar el flujo completo de análisis.
    </p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
     - Dentro de este conjunto destaca el módulo de <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Conversión de Unidades</span>, el cual permite homologar las unidades de medida 
    (<i>kilogramos, litros, piezas, etc.</i>) para asegurar consistencia entre compra, almacenamiento y venta.
    
    </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - Deteccion nos permite obtener toda la informacion relevante de la materia prima que esta siendo modificada en su precio, y dispara el sistema.
    </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - PrecioProducto nos permite tomar el ultimo precio con respecto al registrado al sistema.
    </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - AreasProducto nos permite obtener que areas de la empresa manejan esa formula.
        </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - FormulaProducto nos permite visualizar con respecto a cada materia prima, y sobre todo con la que esta subiendo en ese momento o esta siendo impactada con respecto a un precio nuevo; Cuales formulas utilizan esa materia, asi pudiento extraer datos como - Moneda de compra, Codigo Articulo, Ultima fecha de transaccion, Unidad de medida en Inventarios como en Almacen y otros - .
        </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - PrecioFormulas como su nombre lo indica os permite calcular parametros como si subira de precio con respcecto al parametro del 5% alguna formula, en caso de que si entonces se indexa a la informacion que va a ser retornada. Datos como - Costo Promedio , Costo Nuevo, Nombre del Producto -, son algunos de los parametros que toma.
        </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - TransfomacionFormula se complementa con otras funciones de la seccion siguiente, que en caso de que haya una discrepancia en medidas, retornara cual seria su Factor y Porcentaje con respecto al nuevo cambio de medidas y ajuste que se le realizo.
        </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - PrecioPonderado como su nombre lo indica busca sacar el precio ponderado de cada una de las funciones, tomando en cuenta el parametro de informacion, que son todas las formulas con su respectivo incremento de porcentaje, y indexacion de informacion de los alementos que anteriormente comentamos, que se apoya en la funcion "Calculo" para poder calcular el impacto con respecto a cada formula.
        </p>
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
         - Calculo en este caso como lo comentamos anteriormente es exclusivameente para poder sacar el impacto de cambio que la funcion de "PrecioPonderado" retorna en informacion como uno de sus parametros en un json.
        </p>
.



<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Funciones clave</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li> <b>Deteccion</b> → Punto inicial del proceso, obtiene información y dispara el flujo</li>
    <li> <b>PrecioProducto</b> → Recupera el último precio registrado</li>
    <li> <b>AreasProducto</b> → Identifica las áreas impactadas</li>
    <li> <b>FormulaProducto</b> → Obtiene fórmulas relacionadas con la materia prima</li>
    <li> <b>TransfomacionFormula</b> → Ajusta discrepancias de unidades</li>
    <li> <b>PrecioFormulas</b> → Calcula impacto por fórmula</li>
    <li> <b>precioPonderado</b> → Calcula impacto global ponderado</li>
    <li> <b>Calculo</b> → Genera el impacto final estructurado</li>
</ul>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Consideraciones importantes</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
    <li><b>Deteccion</b> inicia todo el flujo del sistema</li>
    <li><b>PrecioProducto</b> sirve como base comparativa</li>
    <li><b>AreasProducto</b> permite segmentar el impacto</li>
    <li><b>FormulaProducto</b> extrae información clave:
        <ul>
            <li>Moneda de compra</li>
            <li>Código de artículo</li>
            <li>Unidad de medida</li>
            <li>Última transacción</li>
        </ul>
    </li>
    <li><b>TransfomacionFormula</b> calcula factores de conversión</li>
    <li><b>PrecioFormulas</b> evalúa incrementos (ej. > 5%)</li>
    <li><b>precioPonderado</b> calcula impacto global basado en múltiples fórmulas</li>
    <li><b>Calculo</b> retorna resultados en formato tipo JSON</li>
</ul>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Ejemplo conceptual</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 <b>TransfomacionFormula</b> → Ajusta unidades (kg → tambor)<br>
 <b>PrecioFormulas</b> → Calcula impacto por fórmula
</p>

<br>

<table style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;width:100%; border-collapse: collapse; color:#CCC;">
    <tr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#2A2A2A;">
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Producto</th>
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Impacto</th>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Producto A</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333; color:#e63946;">+8%</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Producto B</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">+3%</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Producto C</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333; color:#e63946;">+12%</td>
    </tr>
</table>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 <b>precioPonderado</b> → Calcula impacto global
</p>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#2A2A2A; padding:10px; border-radius:8px; text-align:center;">
<span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A; font-size:18px;"><b>Impacto final ponderado: +7.5%</b></span>
</div>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Tablas utilizadas</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li> Articulos</li>
    <li> OrdenesCompra</li>
    <li> Ventas</li>
    <li> Formulas</li>
    <li> TransaccionesInventario</li>
</ul>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Este conjunto de funciones representa el núcleo del sistema, integrando datos, lógica de negocio y análisis de impacto.
</p>


<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Conversiones Generales</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">

<pre style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD; margin:0;">
1. def ConversionesUnidades(self, Articulo: str, Nunidad: str, Vunidad: str)
</pre>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Descripción</h3>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;" >
La función <b>ConversionesUnidades</b> es responsable de garantizar la <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">homologación de unidades de medida</span> 
dentro del sistema.
</p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;" >
Su objetivo es convertir correctamente las unidades en las que se recibe la materia prima 
(<i>kilogramos, litros, gramos, etc.</i>) para alinearlas con los esquemas de 
<b>compra, almacenamiento y venta</b>, permitiendo así cálculos consistentes y precisos.
</p>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; margin-top:10px;">
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 <b>Articulo</b> → Nombre o identificador del producto<br>
 <b>Nunidad</b> → Nueva unidad de medida<br>
 <b>Vunidad</b> → Unidad anterior o base
</p>
</div>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
Esta función se activa únicamente cuando existe una <b>discrepancia entre unidades</b>, 
retornando un <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">factor de conversión distinto de 1</span> que será utilizado en cálculos posteriores.
</p>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Consideraciones importantes</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
    <li> <b>Articulo</b> → Identificador de la materia prima</li>
    <li> <b>Nunidad</b> → Unidad actual o de entrada</li>
    <li> <b>Vunidad</b> → Unidad base del sistema</li>
    <li> La función solo se ejecuta cuando hay diferencias entre unidades</li>
    <li> Si las unidades coinciden, el factor de conversión es <b>1</b></li>
    <li> Se priorizan conversiones específicas antes que las estándar</li>
    <li> El factor de conversión estandariza todos los cálculos posteriores</li>
    <li>Es fundamental mantener coherencia entre:
        <ul>
            <li>Unidad de compra</li>
            <li>Unidad de almacenamiento</li>
            <li>Unidad de venta</li>
        </ul>
    </li>
    <li> Una mala conversión impacta directamente el cálculo final del precio</li>
</ul>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Ejemplo conceptual</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
<b>Escenario 1:</b> Conversión estándar
</p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li>Artículo: <b>Grasa vegetal industrial</b></li>
    <li>Unidad base (sistema): <b>kg</b></li>
    <li>Unidad nueva (almacén): <b>g</b></li>
    <li>Conversión: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">1 kg = 1000 g</span></li>
    <li>Resultado: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#2a9d8f;">Factor = 0.001</b></li>
</ul>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
<b>Escenario 2:</b> Conversión específica
</p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li>Artículo: <b>Grasa industrial en bloque</b></li>
    <li>Unidad base (sistema): <b>kg</b></li>
    <li>Unidad nueva (almacén): <b>litros</b></li>
    <li>Conversión personalizada: <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">1 litro = 20 kg</span></li>
    <li>Resultado: <b style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#e63946;">Factor = 20</b></li>
</ul>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Tablas utilizadas</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li> ConversionesDentroDeLaClase</li>
    <li> ConversionesEstandar</li>
</ul>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Este módulo asegura la consistencia en unidades, siendo fundamental para la precisión del sistema SIAC.
</p>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Envío de correos</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; border-left:4px solid #B0895A;">

<pre style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD; margin:0;">
1. def EnviarCorreo(self, Data: dict)
2. def ObtenerCorreoClientes(self, Ponderacion: Dict[str, Any], PrecionFinales: Dict[str, Any])
3. def EnvioInformacionClientes(self, data: dict, PrecionFinales: Dict[str, Any])
</pre>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Descripción</h3>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
Esta sección gestiona el <b>sistema de notificaciones</b>, encargado de comunicar los cambios de precios y su impacto 
a los distintos niveles de la organización.
</p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;" >
Se utilizan tres funciones principales que trabajan en conjunto para realizar envíos tanto 
<span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">generales</span> como <span style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">personalizados</span>.
</p>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px; margin-top:10px;">
<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
 <b>EnviarCorreo</b> → Notificación global a vendedores<br>
 <b>ObtenerCorreoClientes</b> → Procesamiento de datos por cliente<br>
 <b>EnvioInformacionClientes</b> → Envío individual por responsable
</p>
</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Flujo de funcionamiento</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;"> Se procesan los datos generales del sistema</li>
    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;"> Se obtiene la información específica por cliente</li>
    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;"> Se envían notificaciones individuales a responsables</li>
</ul>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;">Consideraciones importantes</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;"><b>EnviarCorreo</b>
        <ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Recibe el diccionario global <b>Data</b></li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Evalúa tendencias e impacto general</li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Envía correos a todos los vendedores</li>
        </ul>
    </li>

<li><b>ObtenerCorreoClientes</b>
        <ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Procesa información de ponderación y precios finales</li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Obtiene:
                <ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
                    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Precio sugerido</li>
                    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Producto asignado</li>
                    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Correo del responsable</li>
                    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Nombre de la fórmula</li>
                    <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Cliente asociado</li>
                </ul>
            </li>
        </ul>
    </li>

<li><b>EnvioInformacionClientes</b>
        <ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Recibe la información procesada</li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Envía correos personalizados por cliente</li>
        </ul >
    </li>

<li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;"> El flujo sigue la secuencia:
        <ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Procesamiento general</li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Segmentación por cliente</li>
            <li style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">Envío individual</li>
        </ul>
    </li>
</ul>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Ejemplo conceptual</h3>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:15px; border-radius:10px;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;">
<b >Escenario:</b><br>
Se detecta un incremento en el precio de una grasa industrial
</p>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;"><b>1. Envío general</b></p>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC;">
    <li> Se notifica a todos los vendedores</li>
    <li> Se muestra el impacto global del cambio</li>
</ul>

<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#DDD;"><b>2. Envío personalizado</b></p>

<table style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;width:100%; border-collapse: collapse; color:#CCC;">
    <tr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#2A2A2A;">
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Campo</th>
        <th style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Valor</th>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Cliente</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Industria XYZ</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Producto</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Grasa vegetal industrial</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Responsable</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Juan Pérez</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Correo</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">juan.perez@empresa.com</td>
    </tr>
    <tr>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333;">Precio sugerido</td>
        <td style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;padding:10px; border:1px solid #333; color:#B0895A;">$52.30</td>
    </tr>
</table>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;" >
Se envía un correo específico con información detallada al responsable correspondiente.
</p>

</div>

<br>

<h3 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Tablas utilizadas</h3>

<ul style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;">
    <li>ClientesArticulos</li>
</ul>

<br>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#888;">
Este módulo permite una comunicación eficiente y segmentada, asegurando que la información llegue a las personas correctas en el momento adecuado.
</p>


<hr style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;border: 1px solid #333;">

<h2 style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A;"> Documentación</h2>

<div style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;background-color:#1E1E1E; padding:20px; border-radius:10px; text-align:center;">

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#CCC; margin:0;">
 <b>Fecha de creación</b>
</p>

<p style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#B0895A; font-size:18px; margin-top:10px;">
<b>07 / 04 / 2026</b>
</p>

</div>

<br>

<p align="center" style="font-family: 'Inter', 'Segoe UI', 'Roboto', sans-serif;color:#666;">
Versión inicial del sistema documentada correctamente 
</p>


