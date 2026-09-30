## Descripción

Este programa interactivo por consola simula un "cuenta cuentos" que recopila diversos datos introducidos por el usuario para construir una historia personalizada. Los datos ingresados se almacenan dinámicamente en una estructura de datos inmutable y se integran en una plantilla final con formato dinámico.

## Conceptos Aplicados

* **Entrada de Datos:** Uso de la función `input()` para capturar de manera dinámica las respuestas e información del usuario en consola.
* **Estructuras de Datos (Tuplas):** Almacenamiento de las respuestas en una tupla (`word_box`) para mantener los datos organizados en un contenedor inmutable.
* **Acceso por Índice:** Recuperación de los elementos guardados mediante el índice posicional correspondiente dentro de la tupla (ej. `word_box[0]`, `word_box[1]`).
* **Salida Formateada:** Uso de f-strings para inyectar los valores almacenados directamente en el texto del cuento final.
