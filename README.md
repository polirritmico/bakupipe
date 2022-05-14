Pipeline Tool - Plan de trabajo
===============================

## Descripción

Script Python (A futuro con posibilidad de PyQt) para gestionar la pipeline y
automatizar el deploy a la rama correspondiente. El programa realiza todos los
procesos necesarios de forma automática sin mayor intervención del usuario.

Su funcionamiento inicia con un chequeo básico del sistema y la creación de las
ramas temporales correspondientes (nunca debe operar sobre alguna de las ramas
de trabajo).

Luego realiza toda la batería de tests necesarios y entrega informes de errores
si corresponde. Aprobadas las pruebas genera los binarios para todas las
plataformas soportadas.

Finalmente sube todos los archivos necesarios para cada sistema en la ubicación
correspondiente dentro del repositorio de artefactos, genera un informe del
proceso y envía las notificaciones correspondientes (correos, Trello, etc.)

## Input/Output

Comando: **bakupipe**.

    1. [x] Crear rama pre-deploy en base a rama develop
    1. [ ] Realizar test en pre-deploy
       1. [ ] A futuro: Agregar monitoreo
       1. [ ] Si falla, enviar log
    1. [ ] Hacer merge a deploy
    1. [ ] Borrar pre-deploy
    1. [ ] Ajustar versión
    1. [ ] Build
    1. [ ] Subir binarios a Artifact repo
    1. [ ] Generar logs
       1. [ ] Enviar correos-informes

