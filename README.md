# QIM - Apuntes de Química e Ingeniería en Materiales (UNAM)

Repositorio personal con apuntes, guías y material de estudio de la carrera de Química e Ingeniería en Materiales (QIM) de la Facultad de Química, UNAM.

**Nota:** Este repositorio está en constante actualización. Poco a poco iré subiendo y puliendo el material de cada materia.

## Materias disponibles

Aquí puedes encontrar los apuntes en formato PDF para leer o descargar directamente (haz clic en el nombre):

*   [Química General II](Quimica_General_II/main_QG2.pdf)
*   [Química de Materiales](Quimica_de_Materiales/main_QM.pdf)
*   [Termodinámica](Thermodynamics/main_Ther.pdf)
*   [Balance de Materia y Energía](Balance_de_Materia_y_Energia/main_BME.pdf)
*   [Seguridad Química](Seguridad_Quimica/main_SQ.pdf)

Si algún enlace aún no funciona, es porque sigo subiendo los archivos o puliendo el código.

## Estructura del repositorio

Cada materia tiene su propia carpeta. Dentro de cada una, encontrarás:
*   El archivo principal de LaTeX (`main_*.tex`).
*   Los archivos de secciones (clases, unidades, etc.).
*   La carpeta de imágenes utilizadas en los documentos.
*   El PDF compilado listo para leer.

## Compilación (Para usuarios de LaTeX)

Si quieres clonar el repositorio y compilar los archivos tú mismo, necesitas tener instalado TeX Live y Biber.

Para compilar cualquier archivo principal, abre la terminal en la carpeta de la materia y usa `latexmk`:

```bash
cd Quimica_de_Materiales
latexmk -pdf main_QM.tex