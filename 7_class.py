# -*- coding: utf-8 -*-

#   Paquetes de terceros
"""
PyPi (python package index) es un repositorio de terceros
    que pueden utilizar en proyectos de Python
    para instalar un package es necesario usar la herramienta
     pip
    la forma de instalar un package es ejecutando el comando
    pip install nombre_del_package
    Tambien se puede agrupar  la instalacion de varios package
        a la vez con el archivo requirements.txt

PyPi () Es como ir de compras lo instalas si no te gusta lo desinstalas y listo
    lo importante es buscar los paquetes que puedan resolver tus problemas

 los requirements.txt son la forma ordenada de saber cuales package necesitamos
    para nuestros proyectos


AmbientesVirtuales():
    Es una buena practica crear un ambiente virtual por cada proyecto
    de Python en el que se trabajen

    Esto evita conflictos de packages en el interprete principal

    pip install virtualenv
    virtualenv venv
    source venv/bin/activate
    deactivate


    como instalar virtualenv
    which virtualenv(para saber si esta instalado)
            si sale un path de virtualenv es por que ya esta installed

    mkdir servidor      (carpeta portadora)
    pwd                 (ubicanion dentro de la shell)

    virtualenv venv     (Crea el entorno virtual con nombre venv)
    source venv/bin/activate    (para activar el entorno virtual)
    pip freeze          (saber que programas estan corriendo en el entorno)

    herramienta_favorita_de (David Aroesti):
            pip install flask
                (python_2019 se instalo flask)

    resultado :
            ➜  python_2019 pip freeze
                    Click==7.0
                    Flask==1.0.2
                    itsdangerous==1.1.0
                    Jinja2==2.10
                    MarkupSafe==1.1.0
                    pkg-resources==0.0.0
                    Werkzeug==0.14.1


    [shell$] touch requirements.txt
            Aqui es donde se gurdan los nombre de los programas
            que estemos usando en el entorno virtual para que luego
            pueda ser usado  por otra persona
                Ej:
            (Flask==1.0.2)

    [shell$] pip install -r requirements.txt
            lee los archivos dentro de requirements y trata
            autoinstalar los

Nota:(Python es uno de los lenguajes mas populares para escribir servidores web
        y los servidores web se utilizan como backend para las aplicaciones que se
        conectan a internet . )

    creamos otro archivo  7_subclass_main.py
    alli escribimos un par de lineas de codigo para corre
    el servidor

        ➜  python_2019 python 7_subclass_main.py
             * Serving Flask app "7_subclass_main" (lazy loading)
             * Environment: production
               WARNING: Do not use the development server in a production environment.
               Use a production WSGI server instead.
             * Debug mode: off
             * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
            127.0.0.1 - - [01/Feb/2019 20:36:58] "GET / HTTP/1.1" 200 -
            127.0.0.1 - - [01/Feb/2019 20:36:58] "GET /favicon.ico HTTP/1.1" 404 -
            ^C%
         ➜ resultado del script

         
