# Introducción a la terminal y linea de comandos

- Instalar WSL
    1. Dentro de Windows PowerShell escribe la siguiente instrucción y presiona la tecla **Enter**:     wsl --install
    2. Reinicia el equipo:
    3. Ingresa el **username** y **password** de tu preferencia. Recuerda muy bien tu password, ya que deberás usarla al utilizar el sistema operativo Ubuntu desde WSL.
    4. Para acceder nuevamente a Ubuntu en WSL abre la aplicación  **Terminal** desde inicio de Windows.
    
- Aprendiendo a Caminar en la terminal
    - **Sistema de Archivos en Linux**
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled.png)
        
    - Comandos de movimiento:
        
        
        | **Comando** | Utilidad | Parametros |
        | --- | --- | --- |
        | ls | listar | l, h, d |
        | cd | change directory |  |
        | clear | limpiar la pantalla (CTRL+L) |  |
        | pwd | print working directory |  |
        | . .. | operadores de ruta relativa |  |
        | file  | da propiedades de un archivo |  |
        
- Manipulando archivos y directorios
    
    
    | Comando | Descripción | Parámetros |
    | --- | --- | --- |
    | Tree | arbol de archivos | -L 2 (Profundidad) |
    | mkdir | Creación de directorios |  |
    | touch | Creación de archivos | Se pueden crear varios a la vez |
    | cp | Copiar archivos |  |
    | mv | Mover un archivo |  |
    | mv | También puede remover archivos |  |
    | rm | Remover | r, i, f (recursive, interactive, force) |
    
- Explorando el contenido de nuestros archivos
    
    
    | Comando | Descripción | Parámetros |
    | --- | --- | --- |
    | head | primeras lineas | n 15  |
    | tail | últimas lineas | n 15 |
    | less | interactividad al explorar archivo de texto | usar “/” en la interfaz para buscar  |
    | xdg-open | abre con el editor de texto predeterminado |  |
    | CTRL+C | Mata el proceso actual |  |
    | Nautilus | Abre el sistema de archivos default |  |
    | Cat | Muestra el contenido | se pueden concatenar varios archivos |
- ¿Qué es un comando?
    - Un comando puede ser 4 cosas
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%201.png)
        
    - Crear un alias
        
        ```bash
        alias arbol2nivel="tree . -L 2"
        ```
        
    - Ver documentación de un comando
        
        >**Help comando**
        
        >**Man comando**
        
        >**Whatis comando**
        
    
- WildCards
    
    Sirven para seleccionar archivos en base a patrones en su nombre, ej. mover todos los archivos “.py” de la carpeta actual a otra carpeta
    
    | Wildcard |  |  |
    | --- | --- | --- |
    | * | Cantidad n de caracteres | *.txt |
    | ? | remplace por otro cualquiera | archivo.?? |
    | [[:upper:]] | Remplace por mayusculas | [[:upper:]]*.py |
    | [ad] | contiene a o d | [ad]*.py |
    
- Redirecciones
    
    ### Diagrama de Flujo de la Terminal
    
    ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%202.png)
    
    - Operadores de Redirecciones
        
        
        | Operador | Definición |  |
        | --- | --- | --- |
        | > (en el fondo1>) | Enviar y sobreescribir | solo stdout |
        | >> | Enviar y adicionar | solo stdout |
        | 2> | enviar y adicionar | solo stderr |
        | al final 2>&1 | para que el comando redirija sea un stderr o un stdout | ambos |
        | < | Redirigir el input |  |
        
        **Ejemplo de stdin redirection**
        
        ```bash
        sort < animals.txt
        ```
        
- Pipe operator
    
    **Permite tomar la salida de un comando y pasarla como entrada de otro comando**
    
    ```bash
    	ls -lh | sort | tee output.txt | less
    ```
    
- Encadenando comandos: operadores de control
    
    ### Ejecución de manera síncrona (uno tras otro)
    
    ```bash
    ls; mkdir NuevaCarpeta; ls
    ```
    
    ### Ejecución asíncrona
    
    ```bash
    ls & cd NuevaCarpeta & ls
    ```
    
    ### Operador Condicional y Síncrona
    
    ```bash
    		mkdir nuevo &cd nuevo& 
    ```
    
    ### Operador OR
    
    ```bash
    mkdir nuevo || mkdir OtroNombre
    ```
    
- Manejo de permisos
    - Tipo de archivos
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%203.png)
        
    - Tipos de Modo
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%204.png)
        
    - Modo simbólico
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%205.png)
        
- Modificando permisos en la terminal
    
    ```bash
    chmod 755 mitexto.txt
    chmod u-r mitexto.txt   "quita los permisos de lectura al user"
    ```
    
    ```bash
    chmod u-x,go=w mitexto.txt
    ```
    
    - Administración de Usuarios
        
        
        | Comando | Descripción |
        | --- | --- |
        | whoami | dice qué usuario se es |
        | id | info de user actual |
        | su | switch user |
        | su root | pasa al root |
        | sudo | da permisos de root desde otro usuario |
    
- Variables de entorno
    - Link simbólicos
        
        ```bash
        ln -s Documents/Dev Desarrollo
        ```
        
        **Nota:** Los links simbólicos no tienen permisos, a pesar de que aparecen con todos
        
    - Variables de Entorno
        
        ```bash
        printenv
        ```
        
        ### Algunas Variables de Entorno Fundamentales
        
        - $HOME
        - $PATH : Rutas de los binarios donde se ejecutan el sistema
        
        ### .bashrc
        
        Lugar donde están todas las variables del sistema, tanto aliases como variables de entorno
        
        ![Untitled](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Untitled%206.png)
        
- Comandos de Búsqueda
    
    
    | Comando | Descripción | EJ |
    | --- | --- | --- |
    | wich | devuelve la ruta de los binarios |  |
    | find | permite encontrar un archivo (permite usar wildcards) | find ./ -*name* *.txt | less
    
    find ./  -*type* d -name Documents | less
    
    -*size*   , -*exec*
     |
    | whereis | Como wich pero mejor |  |
    
- Usando el comando Grep
    
    Permite encontrar coincidencias en archivos de texto basado en expresiones regulares
    
    ```bash
    grep REGEX file
    grep -i RegexWithoutCaseSensitive file
    grep -c REGEXToCount fil
    grep -vi RegexThatNotMatch
    ```
    
    ```bash
    wc file   #Comando Word Count#
    ```
    
    > Aprender Expresiones Regulares (REGEX)
    > 
    
- Utilidades de red
    
    
    | Comando | Descripción |
    | --- | --- |
    | ifconfig | información de la interfaz |
    | ping | envia ping a la direccion |
    | curl |  |
    | wget | descarga el archivo de la direccion desde red |
    | traceroute | muestra los pasos que se dan para llegar a un host |
    | netstat -i | muestra info de los dispositivos de red |
- Creación de archivos comprimidos
    
    ```bash
    tar -cvzf ToCompress.tar.gz Tocompress
    #Compress verbose formatoGZIP file#
    tar -xzvf ToCompress.tar.gz
    ```
    
    ```bash
    zip -r ToCompressInZip ToCompress
    unzip ToCompressInZip
    ```
    
- Manejo de Procesos
    
    
    | Comando | Descripción | EJ |
    | --- | --- | --- |
    | ps | lista procesos de la terminal |  |
    | kill | mata un proceso |  |
    | top | panel de todos los procesos. | man top para todos los parametros |
    | htop | versión avanzada de top |  |
- Procesos en Foreground y Background
    
    ### Forma 1
    
    cat > mi_nota.txt : Se mata con CTRL+D
    
    CTRL+Z : Pausa un proceso y lo manda a background
    
    jobs : Muestra todos los procesos
    
    fg #proceso : trae al foreground
    
    ### Forma 2
    
    cat > mi_nota.txt &
    
    bg 1
    
- Editores de texto en la terminal
    - **Vi**
        - Tiene Resaltador de sintaxis
        - Con el ESC se entra al menú del editor
        - Con el “/” se pueden buscar coincidencias
        - :wq permite guardar y salir
        - El parametro ! fuerza instrucciones
    - **Vim**
    
- Libros Recomendados
    
    [LinuxBasicsForHackers](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/linuxbasicsforhackers.pdf)
    
    [TheLinuxCommandLine](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/The_Linux_Command_Line_-_A_Complete_Introduction.pdf)
    
    [GrepPocketReference](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/greppocketref.pdf)
    
    [RegularExpressionsPocketReference](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/RegExp_perl_python_java_etc.pdf)
    
    [LinuxPocketGuide.pdf](Introduccio%CC%81n%20a%20la%20terminal%20y%20linea%20de%20comandos%20aa5a98a559e642d387461df517649658/Linux_Pocket_Guide.pdf)