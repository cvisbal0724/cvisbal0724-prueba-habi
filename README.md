# cvisbal0724-prueba-habi

# Tecnologias a utilizar en la prueba

**PyMySQL**: Lo utilizare para conectar la base de datos

**Flask**: Lo utilizare para la creación de los endpoint solicitados


# Estructura de proyecto

La prueba la estare realizando en la estructura Modelo, controlador.


Estare usando las convensiones de Python PEP8.

# Dudas e inconvenie

## Inconveniente

Tuve un inconveniente al crear la consulta de propiedades porque intente usar CTE y no me dejo por la version que se esta utilizando de mysql.

## Solución

Cree la consulta con select anidados

# Valores recibidos en el primer requerimiento

Se espera recibir un queryparams de la siguiente manera:


Ejemplo.


/property/?year=2010,2011,2012&status=2,3,4&cirty=bogota

Todos los parametros son opcionales

**year**: rebibe 1 o varios años concatenados con comas.

**status**: rebibe 1 o varios estados concatenados con comas.

**city**: rebibe un nombre de por lo menos unas ciudad que exista en la base de datos.


# Requerimiento 2 de funcionalidad de **Me Gusta**

Para solucionar este requerimiento lo primero que debemoas hacer el extender el diagrama de la db, creando un tabla donde almacenaremos los "Me Gusta" de cada usuario por prpiedades y lo vamos a hacer d ela siguiente manera:

```

// Crear tabla

`create table i_like_property(
	id INT NOT NULL AUTO_INCREMENT,
	property_id int(11) not null,
    user_id int(11) not null,
    PRIMARY KEY (id),
    CONSTRAINT `i_like_property_property_id_fk` FOREIGN KEY (`property_id`) 
    REFERENCES `property`(`id`),
    CONSTRAINT `i_like_property_user_id_fk` FOREIGN KEY (`user_id`) 
    REFERENCES `auth_user` (`id`)    
)
`
```

## Sentencias SQL

```
// Registrar un me gusta

`insert into i_like_property(property_id, user_id)values(%id propiedad%, %id_user%)`


// Eliminar un me gusta

`delete from i_like_property where user_id=%user_id% and property_id=%property_id% limit 1`


// Consultar la cantidad de me gusta de un inmueble

`select count(id) from i_like_property where property_id=%property_id%`


// Consultar informacion de los me gusta de un inmueble

`select i.id, concat(u.first_name, ' ', u.last_name) as user,
i.user_id, u.email
from i_like_property as i
inner join auth_user as u on u.id=i.user_id
where property_id=%property_id%`


// Consultar los me gusta por usuarios

`select i.id, p.address, p.city, p.privce, p.descripcion, p.year, i.property_id
from i_like_property as i
inner join property as p on p.id=i.property_id
where i.user_id=%user_id%`

```



