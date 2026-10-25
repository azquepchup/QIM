# QIM - Apuntes de Química e Ingeniería en Materiales (UNAM)

Repositorio personal con apuntes, guías y material de estudio. Aunque el contenido está enfocado y estructurado siguiendo el plan de estudios de la carrera de Química e Ingeniería en Materiales (QIM) de la Facultad de Química, UNAM, cualquier estudiante o persona interesada en la química puede consultarlo y utilizarlo.

*English: Personal repository containing notes, guides, and study material. Although the content is focused on the Materials Chemistry and Engineering degree at UNAM, it is open and useful for anyone interested in chemistry.*

> **Nota / Note:** Este repositorio está en constante actualización. Poco a poco iré subiendo y puliendo el material de cada materia. *Lo siento porque no están completos todos los semestres aún, espero pronto tenerlos listos.*
> *(This repository is constantly being updated. Little by little I will upload and polish the material for each subject. I am sorry that not all semesters are complete yet, I hope to have them ready soon.)*

## 🧭 ¿Cómo navegar por este repositorio? / How to navigate this repository?

Para que puedas encontrar y descargar los apuntes fácilmente, el repositorio está organizado en tres capas:
*(So you can easily find and download the notes, the repository is organized in three layers):*

1. **Elige tu semestre:** Selecciona una de las carpetas de abajo. *(Choose your semester: Select one of the folders below).*
2. **Elige la materia:** Dentro del semestre, verás una lista con las materias disponibles. *(Choose the subject: Inside the semester, you will see a list of available subjects).*
3. **Descarga el PDF:** Al entrar a la materia, lo primero que verás será un **botón azul gigante** para descargar el PDF directo a tu celular o compu, además de información sobre el profesor y los archivos fuente. *(Download the PDF: When you enter the subject, the first thing you will see is a giant blue button to download the PDF directly to your phone or computer, as well as information about the professor and source files).*

## 📖 Materias por Semestre / Subjects by Semester

Haz clic en el semestre que buscas:
*(Click on the semester you are looking for):*

*   [**Semestre 2**](./Semestre_2/)
*   [**Semestre 3**](./Semestre_3/)

*(Los semestres anteriores y posteriores se irán agregando conforme avance la carrera).*
*(Previous and later semesters will be added as the degree progresses).*

---

### 🛠️ Para desarrolladores / For developers

*Si solo quieres leer los apuntes en PDF, puedes ignorar esta sección.*
*(If you just want to read the notes in PDF, you can ignore this section).*

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

Para compilar cualquier archivo principal, abre la terminal en la carpeta de la materia correspondiente y usa `latexmk` (el cual ya maneja las múltiples pasadas necesarias para el índice y la bibliografía).
*(To compile any main file, open the terminal in the subject folder and use `latexmk` (which already handles the multiple passes needed for the index and bibliography)).*

*Ejemplo para compilar Química de Materiales:*
*(Example to compile Materials Chemistry):*

```bash
cd Semestre_3/Quimica_de_Materiales
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