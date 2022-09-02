# PythonGUI
Aplicaciones visuales hechas con la libreria tkinter de python

### Concepto de grid en Tk
| Grids   | Grids con Span |
| :---: | :---: |
| ![Image Text](https://github.com/facumruiz/PythonGUI/blob/main/Form2CSV/img/Tkinter-grid-Grid-Geometry.png?raw=true)  | ![Image Text](https://github.com/facumruiz/PythonGUI/blob/main/Form2CSV/img/Tkinter-grid-columnspan-rowspan.png?raw=true) |
| Explicacion | Explicacion |
| Cada fila y columna de la cuadrícula se identifica mediante un índice. De forma predeterminada, la primera fila tiene un índice de cero, la segunda fila tiene un índice de uno, y así sucesivamente. Asimismo, las columnas de la cuadrícula tienen índices de cero, uno, dos, etc. | Para colocar varios widgets en una celda, use Frameo LabelFramepara envolver los widgets y coloque Frameo LabelFrameen la celda. El ancho de una columna depende del ancho del widget que contiene. De manera similar, la altura de una fila depende de la altura de los widgets contenidos dentro de la fila. Las filas y las columnas pueden abarcar. A continuación se ilustra una cuadrícula que tiene la celda (1,1) que abarca dos columnas y la celda (0,2) que abarca dos filas |


![Image Text](https://github.com/facumruiz/PythonGUI/blob/main/Form2CSV/img/Tkinter-grid-Sticky-Options.png) 

| Sticky   | Descripcion |
| --- | --- |
| N   | Norte o centro superior |
| S   | Centro Sur o Inferior |
| E   | Centro Este o Derecha |
| W   | Oeste o Centro Izquierdo |
| NW   | Noroeste o arriba a la izquierda |
| NE   | Noreste o arriba a la derecha |
| SE   | Sudeste o abajo a la derecha |
| SW   | Sudoeste o abajo a la izquierda |
| NS   | NS estira el widget verticalmente. Sin embargo, deja el widget centrado horizontalmente. |
| EW   | EW estira el widget horizontalmente. Sin embargo, deja el widget centrado verticalmente. |


# FORM2CSV
Formulario de Registro con labels, inputs y button. Visual con grids responsive.

![Image Text](https://github.com/facumruiz/PythonGUI/blob/main/Form2CSV/img/formbuttonlabel.PNG)

### Funcion button: agregar_datos()
Agrega los datos del formulario a un excel. Proxima actualizacion... formato csv
