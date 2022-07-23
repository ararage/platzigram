Proyecto basado en el curso de Platzi - Platzigram

Creditos a pablotrinidad

Proyecto original : https://github.com/pablotrinidad/platzigram

# Pasos

* Tener tu base de datos corriendo

* Crear entorno virtual
```
$ virtualenv env
```
* Activar tu entorno virtual
```
$ source env/bin/activate
```
* Instalar dependencias
```
$ pip install -r requirements.txt
```
* Cargar variables de entorno
```
$ source environ.rc
```
* Correr el proyecto
```
$ ./platzigram/manage.py runserver
```

Si es necesario aplicar migraciones no olvides correrlas de esta forma
```
$ ./platzigram/manage.py migrate
```