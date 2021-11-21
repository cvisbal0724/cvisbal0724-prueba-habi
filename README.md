# cvisbal0724-prueba-habi

# Tecnologias a utilizar en la prueba

**PyMySQL**: Lo utilizare para conectar la base de datos

**Flask**: Lo utilizare para la creación de los endpoint solicitados


# Estructura de proyecto

La prueba la estare realizando en la estructura Modelo, controlador.


Estare usando las convensiones de Python PEP8.

# Dudas e inconvenie

## inconveniente

Tuve un inconveniente al crear la consulta de propiedades porque intente usar CTE y no me dejo por la version que se esta utilizando de mysql.

## Solución

Cree la consulta con select anidados

# valores recibidos en el primer requerimiento

Se espera recibir un queryparams de la siguiente manera:

/property/?year=2010,2011,2012&status=2,3,4&cirty=bogota

Todos los parametros son opcionales

**year**: rebibe 1 o varios años concatenados con comas.

**status**: rebibe 1 o varios estados concatenados con comas.

**city**: rebibe un nombre de por lo menos unas ciudad que exista en la base de datos.





