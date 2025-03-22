# Curso intensivo de Cosmología Observacional

Dictado en el Departamento de Física, FCEyN, UBA, del 25 de marzo al 4 de abril de 2025.





## Preparación del Entorno para el Curso intensivo de Cosmología

Durante el curso, utilizaremos Jupyter Notebook para los ejercicios prácticos. Para asegurarnos de que todos tengan el mismo entorno, sigue estos pasos: 

1) Instala Miniconda

Descarga e instala Miniconda según tu sistema operativo:
  
- [Windows](https://docs.conda.io/en/latest/miniconda.html) 
- [macOS](https://docs.conda.io/en/latest/miniconda.html) 
- [Linux](https://docs.conda.io/en/latest/miniconda.html) 




```bash
conda create -n cosmo python=3.10 notebook numpy scipy matplotlib astropy numba -y
conda activate cosmo
conda install "scipy<1.15"
pip install camb healpy
pip install pysm3
```



2) Crea un Entorno para el Curso

Abre una terminal o el Anaconda Prompt y ejecuta: 

conda create -n cosmo python=3.10 notebook numpy scipy matplotlib astropy numba -y


3) Activar el Entorno 

conda activate cosmo


4) Instalar la versión de scipy adecuada para pysm3:
 
conda install "scipy<1.15"


3) Instalamos luego, con el comando pip, los paquetes camb y healpy:




(si el comando pip no está en el sistema, instalarlo con:  conda install pip -y )


4) Instalamos el pysm3





--------------------------------


Cada vez que trabajes en el curso, activa el entorno con: 

conda activate cosmo


Para abrir Jupyter Notebook y trabajar en los ejericios, usa en el prompt: 

jupyter notebook



## Installation

Luego de tener el entorno listo, tienen que clonar el repositorio:

```bash
git clone https://github.com/cscoccola/Curso_intensivo_Cosmologia_Observacional.git
cd Curso_intensivo_Cosmologia_Observacional
```

It is recommended (even mandatory for MacOS) to install the qubic software using the Anaconda platform, with the correct architecture (arm64 for M1 and x86_64 otherwise).

```bash
conda config --add channels conda-forge
conda create --yes --name venv-qubic python==3.10
conda activate venv-qubic
conda install --yes gfortran pyfftw healpy namaster
SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip install -e .
```

On Linux, after installing gfortran, installation can be performed with the vanilla Python interpreter, except that the package NaMaster needs to be [installed](https://namaster.readthedocs.io/en/latest/installation.html) independently.

```bash
python3 -mvenv venv-qubic
source venv-qubic/bin/activate
SETUPTOOLS_ENABLE_FEATURES="legacy-editable" pip install -e .
```

For more information, please look at the QUBIC project wiki:
http://qubic.in2p3.fr/wiki/pmwiki.php/DataAnalysis/HowTo

