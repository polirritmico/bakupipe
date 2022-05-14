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

    1. [x] Crear nueva rama pre-deploy
    2. [ ] Hacer merge a pre-deploy
    3. [ ] Realizar test en pre-deploy
       1. [ ] A futuro: Agregar monitoreo
       2. [ ] Si falla, enviar log
    4. [ ] Hacer merge a deploy
    5. [ ] Borrar pre-deploy
    6. [ ] Ajustar versión
    7. [ ] Build
    8. [ ] Subir binarios a Artifact repo
    9. [ ] Generar logs
       1. [ ] Enviar correos-informes

