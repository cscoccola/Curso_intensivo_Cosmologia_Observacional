



Preparación del Entorno para el Curso intensivo de Cosmología

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





