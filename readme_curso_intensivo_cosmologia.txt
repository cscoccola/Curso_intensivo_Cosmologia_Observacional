
###################################

Preparación del Entorno para el Curso intensivo de Cosmología

###################################

Durante el curso, utilizaremos Jupyter Notebook para los ejercicios prácticos. Para asegurarnos de que todos tengan el mismo entorno, sigue estos pasos:  

1) Instala Miniconda

Descarga e instala Miniconda según tu sistema operativo:
  
- [Windows](https://docs.conda.io/en/latest/miniconda.html)  
- [macOS](https://docs.conda.io/en/latest/miniconda.html)  
- [Linux](https://docs.conda.io/en/latest/miniconda.html)  


2) Crea un Entorno para el Curso

Abre una terminal o el Anaconda Prompt y ejecuta:  

conda create -n cosmo python=3.10 notebook numpy scipy matplotlib astropy numba -y


3) Activar el Entorno 

conda activate cosmo


4) Instalar la versión de scipy adecuada para pysm3:
 
conda install "scipy<1.15"


3) Instalamos luego, con el comando pip, los paquetes camb y healpy:

pip install camb healpy

(si el comando pip no está en el sistema, instalarlo con:  conda install pip -y )


4) Instalamos el pysm3

pip install pysm3


--------------------------------


Cada vez que trabajes en el curso, activa el entorno con:  

conda activate cosmo


Para abrir Jupyter Notebook y trabajar en los ejericios, usa en el prompt:  

jupyter notebook


###################################

Sobre el horario y las aulas

###################################

* Los días y horarios del curso son:

primer semana: martes, miércoles y jueves

segunda semana: todos los días, salvo el feriado del 2 de abril.

-----------------
Clase teórica 1: 9:30 a 11:00

Descanso

Clase teórica 2: 11:30 a 13:00

Horario de almuerzo

Clase práctica: 14:30 a 16:00
-----------------

* Deben traer sus laptops para poder realizar las actividades prácticas.


* Aula confirmada sólo para el día martes 25/03:

Por la mañana usaremos el Aula 1203 Cero+Infinito
Y por la tarde estaremos en el Aula 1115 Cero+Infinito (este aula se encuentra al lado de la 1203).



###################################

Sobre los archivos de data

###################################

Los archivos de datos que vamos a usar los pueden bajar de las páginas relevantes, o yo puedo darles acceso a un directorio data/ con los archivos previamente bajados. Notar que en los tutoriales estarán indicadas las dos opciones (una de ellas, comentada con # ).



###################################

Sobre los tutoriales

###################################

En la carpeta CMB/healpy/

tutorial_healpy.ipynb es el que hay que mirar más detenidamente. Los otros archivos tienen ejemplos de otras funcionalidades más específicas.


alpha_channel_example.ipynb muestra cómo utilizar el canal alpha para mostrar una máscara con efecto de transparencia.

newvisufunc_example.ipynb muestra muchas opciones distintas para visualizar los mapas.

blm_gauss_plot.ipynb muestra cómo hacer una función que represente un beam gaussiano (coeficientes armónicos)

map_data_to_healpix.ipynb muestra cómo visualizar un mapa genérico usando la partición de Healpix, cuando tienen las coordenadas y el valor del mapa en cada una de esas direcciones, guardados como arrays.


Compute_Planck_CMB_temperature_power_spectrum.ipynb calcula el espectro en el caso de tener un beam y una máscara (con limitaciones en lo que puede hacer healpy).

------
En esta página hay otro tutorial (jupyter notebook) que carga el espectro del CMB del best fit de Planck, lo usa para crear una realización de los coeficientes a_\ell,m (que guarda en disco) y luego usa para crear mapas a diferentes resoluciones:

https://www.zonca.dev/posts/2020-09-30-planck-spectra-healpy.html

----

En la carpeta CMB/pysm_notebooks/ hay ejemplos de cómo se utiliza pysm para generar realizaciones de mapas del CMB y contaminantes (polvo, sincrotrón)

----

En el siguiente link pueden ver la imagen gif con la ilustración de cómo se genera polarización lineal en presencia de una anisotropía cuadrupolar en el campo de radiación:

https://docs.google.com/presentation/d/1kyh8UE-5sacmH6QubrN7ya6swYE2ysXA38jFUlUc5Ls/edit?usp=sharing







