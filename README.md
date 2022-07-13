BakuPipe :factory::calling:
===========================

## Descripción

Script Python (ToDo: PyQt) para gestionar la pipeline y automatizar el deploy a
la rama correspondiente. El programa realiza todos los procesos necesarios de
forma automática sin mayor intervención del usuario.

Su funcionamiento inicia con un chequeo básico del sistema y la creación de las
ramas temporales correspondientes (nunca debe operar sobre alguna de las ramas
de trabajo).

Luego realiza toda la batería de tests necesarios y entrega informes de errores
si corresponde. Aprobadas las pruebas genera los binarios para todas las
plataformas soportadas.

Finalmente sube todos los archivos necesarios para cada sistema en la ubicación
correspondiente dentro del repositorio de artefactos, genera un informe del
proceso y envía las notificaciones correspondientes (correos, Trello, etc.)

![sceenshot](docs/screenshot.png)

## ToDo:

> ### Main
> * [x]  greetings
> * [x]  get all tests
> * [x]  chose target branch: DEF develop
> * [x]  confirm
> ------------------------------------------------------------------------------
> * [x]  make new temp branch
> * [x]    if exist, remove and regenerate
> * [x]  go to temp branch
> * [x]  begin tests
> * [x]    TODO: pre and post build tests
> * [x]  if Error:
> * [x]    terminate tests.
> * [ ]    generate log of failed test
> * [ ]    if option, generate all logs
> * [ ]    raise expection
> * [ ]  if warning:
> * [ ]    generate log, store, and show at end.
> * [ ]    Continue
> * [ ]  if log, generate
> ------------------------------------------------------------------------------
> * [x]  Build selected plataforms
> * [x]  Move binaries and all needed files to proper locations by plataform
> * [x]  Second phase tests
> * [x]    TODO: pre and post build tests
> * [x]  Same as 46-56
> * [x]  begin tests
> * [x]    TODO: pre and post build tests
> * [x]  if Error:
> * [x]    terminate tests.
> * [ ]    generate log of failed test
> * [ ]    if option, generate all logs
> * [x]    RETURN
> * [ ]  if warning:
> * [ ]    generate log, store, and show at end.
> * [ ]    Continue
> * [ ]  if log, generate
> ------------------------------------------------------------------------------
> #### ALL OK:
> * [ ]  Generate version name and adjust files
> * [ ]  Merge pre-deploy to deploy
> * [ ]  Remove pre-deploy
> * [ ]  Upload commits to artifact repo(sync)
> * [ ]  Generate Logs, and send them
> - [x] Preparar y chequear repositorio
> - [x] Leer y preparar archivos de test
> - [x] Crear rama pre-deploy en base a rama develop
> - [x] Realizar test en pre-deploy
> - [x] Hacer merge a deploy
> - [ ] Borrar pre-deploy
> - [ ] Ajustar versión
> - [ ] Build
> - [ ] Subir binarios a Artifact repo
> - [ ] Generar logs
>    - [ ] Enviar correos-informes

## Test de desarrollo

Los distintos test se encuentran dentro de la carpeta `/test/`, dentro de cada
archivo correspondiente. Utilizan la librería Unittest de python y para evitar
problemas de imports, se recomienda utilizar el siguiente comando:

```console
foo@bar: ~/bakupipe $ python -m unittest discover . -b
```
`-b` sirve para descartar outputs de test aprobados, se muestran si hay error.

## Enlaces a repositorios y documentación Bakumapu

* **Repositorio de documentación:** https://github.com/polirritmico/Bakumapu-docs
* **Documentación en HTML:** https://polirritmico.github.io/Bakumapu-docs/
* **Repositorio de código:** https://github.com/polirritmico/Bakumapu

## Requisitos

Para subir los artefactos a Drive de momento se utiliza `drive`: 
https://github.com/odeke-em/drive

