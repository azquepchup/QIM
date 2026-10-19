# QIM - Apuntes de Química e Ingeniería en Materiales (UNAM)

Repositorio personal con apuntes, guías y material de estudio. Aunque el contenido está enfocado y estructurado siguiendo el plan de estudios de la carrera de Química e Ingeniería en Materiales (QIM) de la Facultad de Química, UNAM, cualquier estudiante o persona interesada en la química puede consultarlo y utilizarlo.

*English: Personal repository containing notes, guides, and study material. Although the content is focused on the Materials Chemistry and Engineering degree at UNAM, it is open and useful for anyone interested in chemistry.*

**Nota / Note:** Este repositorio está en constante actualización. Poco a poco iré subiendo y puliendo el material de cada materia.
*(This repository is constantly being updated. Little by little I will upload and polish the material for each subject.)*

## Materias disponibles / Available Subjects

Aquí puedes encontrar los apuntes en formato PDF para leer o descargar directamente (haz clic en el nombre):
*(Here you can find the notes in PDF format to read or download directly)*:

*   [Química General II](Quimica_General_II/main_QG2.pdf)
*   [Química de Materiales](Quimica_de_Materiales/main_QM.pdf)
*   [Termodinámica](Thermodynamics/main_Ther.pdf)
*   [Balance de Materia y Energía](Balance_de_Materia_y_Energia/main_BME.pdf)
*   [Seguridad Química](Seguridad_Quimica/main_SQ.pdf)

*(Nota: si algún enlace aún no funciona, es porque sigo subiendo los archivos, compilando o puliendo el código).*
*(Note: if a link does not work yet, it is because I am still uploading the files, compiling, or polishing the code).*

## Estructura del repositorio / Repository Structure

Cada materia tiene su propia carpeta. Dentro de cada una, encontrarás:
*(Each subject has its own folder. Inside each one, you will find):*
*   El archivo principal de LaTeX (`main_*.tex`). *(The main LaTeX file).*
*   Los archivos de secciones (clases, unidades, etc.). *(Section files such as classes, units, etc.).*
*   La carpeta de imágenes utilizadas en los documentos. *(The folder containing images used in the documents).*
*   El PDF compilado listo para leer. *(The compiled PDF ready to be read).*
*   Scripts auxiliares de Python (como generadores de gráficas). *(Auxiliary Python scripts, such as plot generators).*

Todas las rutas dentro del código son relativas, lo que significa que puedes descargar el repositorio en cualquier computadora y compilarlo sin necesidad de cambiar rutas absolutas.
*(All paths within the code are relative, meaning you can download the repository on any computer and compile it without changing absolute paths).*

## Requisitos e Instalación / Requirements and Installation

Para compilar los archivos desde el código fuente, necesitas tener instalado **TeX Live** (con los paquetes básicos y de idioma), **Biber** y **latexmk**.
*(To compile the files from source code, you need to have **TeX Live** (with basic and language packages), **Biber**, and **latexmk** installed).*

*   **Arch Linux:**
    ```bash
    sudo pacman -S texlive-meta texlive-lang biber latexmk
    ```
*   **Debian/Ubuntu:**
    ```bash
    sudo apt install texlive-full biber latexmk
    ```
*   **Windows:** Se recomienda instalar [MiKTeX](https://miktex.org/) o [TeX Live](https://tug.org/texlive/windows.html).

## Compilación / Compilation

Para compilar cualquier archivo principal, abre la terminal en la carpeta de la materia y usa `latexmk` (el cual ya maneja las múltiples pasadas necesarias para el índice y la bibliografía):
*(To compile any main file, open the terminal in the subject folder and use `latexmk` (which already handles the multiple passes needed for the index and bibliography))*:

```bash
cd Quimica_de_Materiales
latexmk -pdf main_QM.tex
```

## Entorno de Desarrollo / Development Environment

Este material es escrito, compilado y mantenido utilizando:
*(This material is written, compiled, and maintained using):*
*   **Sistema Operativo:** Arch Linux (con el gestor de ventanas Hyprland). *(OS: Arch Linux with Hyprland window manager).*
*   **Editor de Código:** Code - OSS (con la extensión LaTeX Workshop). *(Code Editor: Code - OSS with LaTeX Workshop extension).*
*   **Visor PDF:** Okular (con SyncTeX configurado para saltar entre el código y el PDF). *(PDF Viewer: Okular with SyncTeX configured to jump between code and PDF).*
*   **Control de Versiones:** Git y GitHub. *(Version Control: Git and GitHub).*

## Autor / Author

**Uriel Sánchez Méndez**
Estudiante de Química e Ingeniería en Materiales (UNAM) y Matemáticas (UnADM).
*(Student of Materials Chemistry and Engineering at UNAM and Mathematics at UnADM).*