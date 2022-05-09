Pipeline Tool - Plan de trabajo
===============================

## Current ToDo

Test de goto\_branch()

## Descripción

Herramienta Python (a futuro con posibilidad de PyQt) para gestionar el
pipeline. Se utilizará al momento de hacer un merga hacia deploy. Ahí se activa
la batería de test (GUT) y luego en caso de aprobarse se pasa a a construir los
builds para las distintas plataformas, y a continuación subirlas al
repositorio, generar logs y enviar correos o informes.


## Input/Output

Comando: **bakupipe deploy**.

    1. [ ] Crear nueva rama pre-deploy
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

