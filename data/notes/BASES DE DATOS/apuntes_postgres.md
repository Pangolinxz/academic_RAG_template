### PostgreSQL: Notas de Clase con Explicaciones

---

#### **Instalación y Configuración**
1. **Instalación**: Sigue la guía para instalar PostgreSQL junto con pgAdmin, una interfaz gráfica para gestionar bases de datos. [Guía completa aquí](https://www.tecmint.com/install-postgresql-with-pgadmin4-on-linux-mint/).

2. **Acceso inicial**:
   ```bash
   sudo -i -u postgres
   psql
   \q
   ```
   - **sudo -i -u postgres**: Cambia al usuario predeterminado `postgres`.
   - **psql**: Accede a la consola interactiva de PostgreSQL.
   - **\q**: Sal de la consola.

3. **Inicio de pgAdmin**:
   ```bash
   source pgadmin4/bin/activate
   pgadmin4
   ```
   - Activa el entorno de pgAdmin y lanza la interfaz gráfica.

---

#### **Comandos Principales**
Estos comandos facilitan la navegación y gestión en la consola interactiva `psql`:

- **Acceso a la consola**: `psql -U postgres -W` (usuario `postgres` con contraseña).
- **Ayuda de comandos**: `\?` muestra todos los comandos disponibles.
- **Listar bases de datos**: `\l` muestra las bases disponibles.
- **Cambiar base de datos**: `\c nombre_BD` selecciona otra base activa.
- **Listar tablas**: `\dt` muestra todas las tablas de la base activa.
- **Describir tabla**: `\d nombre_tabla` detalla la estructura de una tabla.
- **Medir tiempo de ejecución**: `\timing` activa el temporizador para medir consultas.
- **Salir**: `\q` cierra la consola.

---

#### **Archivos de Configuración**
PostgreSQL utiliza tres archivos clave para la configuración:

1. **postgresql.conf**: Configura parámetros generales, como:
   - Puerto del servidor.
   - Dirección IP que escucha.
   - Máximo de conexiones.
   
2. **pg_hba.conf**: Gestiona seguridad y conexiones por IP.
3. **pg_ident.conf**: Asigna usuarios del sistema a roles en PostgreSQL.

Para encontrar estos archivos:
```sql
SHOW config_file;
```

---

#### **Jerarquía de Bases de Datos**
- **Servidor**: Computadora que ejecuta PostgreSQL.
- **Motor de base de datos**: Software que administra las bases de datos.
- **Base de datos**: Conjunto de datos organizados.
- **Esquema**: Conjunto de objetos (tablas, funciones, vistas) relacionados.
- **Tabla**: Estructura básica que organiza datos en filas y columnas.

---

#### **Particiones**
**Concepto**: Las particiones dividen una tabla grande en varias más pequeñas, mejorando el rendimiento al consultar rangos específicos.

Ejemplo: Crear una partición para datos de enero de 2010.
```sql
CREATE TABLE bitacora_viaje_2010_01 PARTITION OF bitacora_viaje
FOR VALUES FROM ('2010-01-01') TO ('2010-01-31');
```

- **Beneficio**: Reduce el costo de recorrer grandes volúmenes de datos.

---

#### **Roles y Permisos**
**Concepto**: Los roles son usuarios o grupos con permisos específicos sobre la base.

Crear un rol con acceso básico:
```sql
CREATE ROLE usuario_consulta WITH LOGIN PASSWORD '1234';
```

Asignar permisos:
```sql
GRANT SELECT, INSERT ON TABLE public.tabla TO usuario_consulta;
```

---

#### **Claves Foráneas**
**Concepto**: Relacionan datos entre tablas para mantener consistencia.

Ejemplo: Relacionar una tabla `trayecto` con las tablas `estacion` y `tren`:
```sql
CREATE TABLE trayecto (
    id SERIAL PRIMARY KEY,
    id_estacion INTEGER REFERENCES estacion(id) ON UPDATE CASCADE ON DELETE CASCADE
);
```

- **ON UPDATE CASCADE**: Si cambia la clave primaria de `estacion`, se refleja en `trayecto`.
- **ON DELETE CASCADE**: Si se elimina un registro en `estacion`, también se elimina en `trayecto`.

---

#### **Inserción Masiva**
**Concepto**: Para insertar grandes volúmenes de datos generados, puedes usar herramientas como [Mockaroo](https://mockaroo.com).

Ejemplo: Insertar datos relacionados aleatoriamente.
```sql
INSERT INTO trayecto (nombre, trenid, estacionid)
VALUES ('Ruta', (SELECT id FROM tren ORDER BY RANDOM() LIMIT 1), 
(SELECT id FROM estacion ORDER BY RANDOM() LIMIT 1));
```

---

#### **Funciones Especiales**
1. **ON CONFLICT**: Maneja conflictos al insertar datos duplicados.
   ```sql
   INSERT INTO estacion(id, nombre) VALUES (1, 'Centro')
   ON CONFLICT(id) DO UPDATE SET nombre = 'Centro Actualizado';
   ```

2. **RETURNING**: Devuelve los datos insertados.
   ```sql
   INSERT INTO estacion(nombre) VALUES ('Nueva') RETURNING id;
   ```

3. **COALESCE**: Reemplaza valores `NULL` por un valor predeterminado.
   ```sql
   SELECT COALESCE(nombre, 'Desconocido') AS nombre FROM pasajero;
   ```

4. **CASE**: Permite condicionales en las consultas.
   ```sql
   SELECT CASE WHEN fecha_nacimiento > '2015-01-01' THEN '2015 o más' ELSE '2014 o menos' END FROM pasajero;
   ```

---

#### **Vistas**
1. **Volátiles**: Actualizan los datos al ejecutarse.
   ```sql
   CREATE VIEW comparacion_2015 AS
   SELECT * FROM pasajero WHERE fecha_nacimiento > '2015-01-01';
   ```

2. **Materializadas**: Guardan datos en memoria y necesitan ser actualizadas manualmente.
   ```sql
   CREATE MATERIALIZED VIEW resumen_viajes AS
   SELECT * FROM viaje WHERE inicio > '22:00:00';
   REFRESH MATERIALIZED VIEW resumen_viajes;
   ```

---

#### **PL/pgSQL**
**Concepto**: Lenguaje para escribir funciones y procedimientos dentro de PostgreSQL.

**Procedimiento**:
```sql
DO $$
BEGIN
    RAISE NOTICE 'Hola desde PostgreSQL';
END
$$;
```

**Función**:
```sql
CREATE FUNCTION contar_pasajeros() RETURNS INTEGER AS $$
DECLARE
    contador INTEGER := 0;
BEGIN
    SELECT COUNT(*) INTO contador FROM pasajero;
    RETURN contador;
END
$$ LANGUAGE plpgsql;
```

---

#### **Triggers**
**Concepto**: Ejecutan automáticamente una acción cuando ocurre un evento en la tabla.

1. Crear la función del trigger:
   ```sql
   CREATE OR REPLACE FUNCTION trigger_func()
   RETURNS TRIGGER AS $$
   BEGIN
       INSERT INTO log_tabla (mensaje, fecha) VALUES ('Registro insertado', NOW());
       RETURN NEW;
   END
   $$ LANGUAGE plpgsql;
   ```

2. Asociar el trigger a un evento:
   ```sql
   CREATE TRIGGER after_insert
   AFTER INSERT ON tabla
   FOR EACH ROW EXECUTE FUNCTION trigger_func();
   ```

---

#### **Extensiones**
**DBLink**: Conecta a bases remotas.
```sql
CREATE EXTENSION dblink;
SELECT * FROM dblink('host=127.0.0.1 dbname=remota user=admin', 
'SELECT id, fecha FROM tabla_remota') AS t(id INTEGER, fecha DATE);
```

---

#### **Transacciones**
**Concepto**: Garantizan que un conjunto de operaciones se ejecute como una unidad (todo o nada).

Ejemplo:
```sql
BEGIN;
INSERT INTO tabla VALUES (1, 'dato');
ROLLBACK; -- o COMMIT
```

---

#### **Replicación**
**Concepto**: Separa lecturas y escrituras en bases principales y réplicas para mejorar rendimiento.

- Base maestra: Realiza escrituras.
- Réplica: Maneja consultas de solo lectura.

---

#### **Backups**
**Concepto**: Respalda datos para recuperarlos en caso de fallo.

Crear un backup en formato plano:
```bash
pg_dump dbname > backup.sql
```

Restaurar datos desde un backup:
```bash
psql -d dbname -f backup.sql
```

---

Con estas explicaciones, puedes comenzar a profundizar en PostgreSQL y optimizar su uso. ¡Buena práctica! 🚀
