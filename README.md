# AlgoReportTemplate

## Descripción

Este repositorio contiene una plantilla en **LaTeX** diseñada específicamente para la creación de informes y reportes en la asignatura **Algoritmos y Complejidad** del Departamento de Informática de la **Universidad Técnica Federico Santa María (UTFSM)**. La plantilla está estructurada para facilitar la redacción de tareas, reportes de laboratorio y proyectos relacionados con el análisis de algoritmos.

### Modificación de la plantilla

- Escriba sus datos en `author.tex`.
- `preamble.tex` y `tarea_main.tex` NO debe ser modificados.
- La estructura de archivos de `sections/` No debe ser modificada. Sólo agregue texto a los archivos existentes. (además de borrar las indicaciones de los archivos)
- La estructura de subsecciones y subsubsecciones de los archivos de `sections/` No debe ser modificada. Sólo agregue texto a los archivos existentes. (además de borrar las indicaciones de los archivos)
- `references.bib` contiene las referencias bibliográficas. Agregue las suyas.
- `tikz/` contiene archivos `.tex` con gráficos generados con `TikZ`. Puede agregar más archivos `.tex` con gráficos.
- `tarea_main.pdf` es el archivo de salida generado por `pdflatex`.
- `images/` contiene imágenes. Puede agregar más imágenes.
- Elimine las figuras existentes y utilice las que generará en su informe.

```bash
pablo@asus:~/Documents/AlgoReportTemplate$ tree
.
├── author.tex
├── condiciones.tex
├── images
│   └── 4_impurezas_cantmax_size10.png
├── preamble.tex
├── README.md
├── references.bib
├── sections
│   ├── abstract.tex
│   ├── appendix1.tex
│   ├── conclusions.tex
│   ├── design_analysis_brute_force.tex
│   ├── design_analysis_dynamic_programming.tex
│   ├── design_analysis.tex
│   ├── experiment_dataset.tex
│   ├── experiment_intro.tex
│   ├── experiment_results.tex
│   ├── implementations.tex
│   └── introduction.tex
├── tarea_main.bcf-SAVE-ERROR
├── tarea_main.pdf
├── tarea_main.tex
└── tikz
    ├── plot1.tex
    ├── plot2.tex
    ├── plot3.tex
    └── plot4.tex

4 directories, 24 files

```

### Entrega
Pararealizar su entrega, cambié en nombre del documento `.pdf` al formato especificado en condiciones y luego comprima el directorio con el formato especificado. 