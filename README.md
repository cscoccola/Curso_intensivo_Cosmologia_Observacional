# Curso intensivo de Cosmología Observacional

Dictado en el Departamento de Física, FCEyN, UBA, del 25 de marzo al 4 de abril de 2025.





## Preparación del Entorno para el Curso intensivo de Cosmología

Durante el curso, utilizaremos Jupyter Notebook para los ejercicios prácticos. Para asegurarnos de que todos tengan el mismo entorno, sigue estos pasos: 


### 1) Instalar Miniconda:

Descargar e instalar Miniconda según el sistema operativo:
  
- [Windows](https://docs.conda.io/en/latest/miniconda.html) 
- [macOS](https://docs.conda.io/en/latest/miniconda.html) 
- [Linux](https://docs.conda.io/en/latest/miniconda.html) 


### 2) Crear un entorno con los paquetes necesarios:

```bash
conda create -n cosmo python=3.10 notebook numpy scipy matplotlib astropy numba -y
conda activate cosmo
conda install "scipy<1.15"
pip install camb healpy
pip install pysm3
```


--------------------------------


Cada vez que trabajes en el curso, activa el entorno con: 

conda activate cosmo


Para abrir Jupyter Notebook y trabajar en los ejericios, usa en el prompt: 

jupyter notebook



### 3) Clonar el repositorio:

Luego de tener el entorno listo, tienen que clonar el repositorio:

```bash
git clone https://github.com/cscoccola/Curso_intensivo_Cosmologia_Observacional.git
cd Curso_intensivo_Cosmologia_Observacional
```

Más detalles en el archivo: 

readme_curso_intensivo_cosmologia.txt

