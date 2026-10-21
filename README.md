# EA1 – Carga y Creación de Dataset

## 1. Descripción del proyecto

Este proyecto se desarrolla como parte de la actividad **EA1 – Carga y Creación de Dataset** de IU Digital. Su objetivo es cargar un dataset público desde Hugging Face, convertirlo en un DataFrame de pandas, realizar transformaciones de datos y generar un archivo de texto con un resumen descriptivo.

El proyecto está desarrollado en Python y utiliza Google Colab como entorno de ejecución.

## 2. Objetivos

- Cargar un dataset público desde Hugging Face.
- Implementar una clase para la carga de datos y su conversión a un DataFrame.
- Crear una clase para resumir y exportar información del DataFrame a un archivo `.txt`.
- Realizar al menos cuatro transformaciones diferentes sobre los datos.
- Analizar las dimensiones, los tipos de datos, los valores nulos y las estadísticas descriptivas.
- Gestionar y documentar el código mediante un repositorio de GitHub.

## 3. Dataset utilizado

- **Nombre:** Iris.
- **Identificador en Hugging Face:** `scikit-learn/iris`.
- **Split utilizado:** `train`.
- **Formato de trabajo:** DataFrame de pandas.
- **Registros originales:** 150.
- **Columnas originales:** 6.

El dataset contiene información sobre las dimensiones de los sépalos y pétalos de flores Iris, además de una columna que identifica la especie.

## 4. Tecnologías y herramientas

- **Python:** lenguaje de programación.
- **Google Colab:** entorno para ejecutar y documentar el notebook.
- **Hugging Face Datasets:** biblioteca para cargar el dataset.
- **Pandas:** biblioteca para manipular y analizar los datos.
- **Git y GitHub:** herramientas para el control de versiones y el almacenamiento del proyecto.

## 5. Estructura del proyecto

```text
EA1-Carga-Creacion-Dataset/
│
├── hf_dataset_loader.py
├── dataset_summarizer.py
├── EA1_Carga_Creacion_Dataset.ipynb
├── resumen_dataset.txt
└── README.md
```

### Descripción de los archivos

- **`hf_dataset_loader.py`:** contiene la clase `HFDatasetLoader`, encargada de cargar el dataset desde Hugging Face y convertirlo en un DataFrame de pandas.
- **`dataset_summarizer.py`:** contiene la clase `DatasetSummarizer`, encargada de generar un resumen del DataFrame y guardarlo en un archivo de texto.
- **`EA1_Carga_Creacion_Dataset.ipynb`:** notebook de Google Colab donde se importan las clases, se carga el dataset, se realizan las transformaciones y se muestran los resultados.
- **`resumen_dataset.txt`:** archivo generado con las dimensiones del dataset transformado, los tipos de datos, los valores nulos y las estadísticas descriptivas.
- **`README.md`:** documento que describe el proyecto, sus objetivos, las herramientas utilizadas y el procedimiento realizado.

## 6. Clases implementadas

### 6.1. Clase HFDatasetLoader

Esta clase permite cargar un dataset público de Hugging Face mediante la función `load_dataset` de la biblioteca `datasets`.

Su método `load_dataframe()` convierte el dataset cargado en un DataFrame de pandas para facilitar su manipulación y análisis.

### 6.2. Clase DatasetSummarizer

Esta clase recibe un DataFrame y construye un resumen de su contenido. Incluye información sobre:

- Cantidad de filas y columnas.
- Tipos de datos de cada columna.
- Cantidad de valores nulos.
- Estadísticas descriptivas.

Finalmente, permite guardar el resumen en el archivo `resumen_dataset.txt`.

## 7. Transformaciones realizadas

Se realizaron cuatro transformaciones sobre el dataset original:

### Transformación 1. Renombrar columnas

Se cambiaron los nombres de las columnas para facilitar su comprensión y mantener una nomenclatura consistente.

Por ejemplo:
- `SepalLengthCm` → `longitud_sepalo`
- `SepalWidthCm` → `ancho_sepalo`
- `PetalLengthCm` → `petal_length`
- `PetalWidthCm` → `petal_width`
- `Species` → `target`

### Transformación 2. Seleccionar columnas

Se seleccionaron las siguientes cuatro columnas:

- `longitud_sepalo`
- `petal_length`
- `petal_width`
- `target`

El resultado fue un DataFrame de **150 filas y 4 columnas**.

### Transformación 3. Filtrar registros

Se aplicó un filtro para conservar únicamente las flores cuya longitud del pétalo fuera mayor que 3.0 cm.

La condición aplicada fue:

`petal_length > 3.0`

El resultado fue un DataFrame de **99 filas y 4 columnas**.

### Transformación 4. Crear una nueva columna

Se creó la columna `area_petalo_estimada`, multiplicando la longitud del pétalo por su ancho:

`area_petalo_estimada = petal_length * petal_width`

Esta columna representa una estimación sencilla basada en las dimensiones del pétalo; no corresponde a un cálculo botánico exacto de su área.

El resultado final fue un DataFrame de **99 filas y 5 columnas**.

## 8. Resultados obtenidos

Después de ejecutar las transformaciones, se generó el archivo `resumen_dataset.txt`.

Los resultados fueron:

| Indicador | Resultado |
|---|---:|
| Filas originales | 150 |
| Columnas originales | 6 |
| Filas finales | 99 |
| Columnas finales | 5 |
| Valores nulos en las columnas finales | 0 |

El resumen también contiene los tipos de datos y las estadísticas descriptivas de las variables numéricas y categóricas.

## 9. Instalación de dependencias

Para ejecutar el proyecto en un entorno Python, instala las siguientes bibliotecas:

```bash
pip install datasets pandas
```

## 10. Ejecución del proyecto

1. Abre el notebook `EA1_Carga_Creacion_Dataset.ipynb` en Google Colab.
2. Sube al entorno los archivos `hf_dataset_loader.py` y `dataset_summarizer.py`, o ejecuta las celdas que los crean.
3. Ejecuta las celdas en orden para importar las clases y cargar el dataset desde Hugging Face.
4. Ejecuta las cuatro transformaciones y verifica los resultados mostrados.
5. Ejecuta la clase `DatasetSummarizer` para generar `resumen_dataset.txt`.

Se requiere conexión a Internet para descargar el dataset de Hugging Face cuando no esté disponible en la caché local.

## 11. Control de versiones

El proyecto se organiza en un repositorio de GitHub para conservar los archivos y registrar los cambios realizados durante el desarrollo.


**Repositorio de GitHub:** [https://github.com/DuvanRamirez-SoftwareEngineer/EA1-Carga-Creacion-Dataset.git]

## 12. Conclusión

La actividad permitió aplicar conceptos de carga, transformación y análisis de datos utilizando Python, Hugging Face Datasets y pandas. Mediante dos clases se organizó el proceso de carga y resumen, mientras que las cuatro transformaciones permitieron modificar la estructura del DataFrame, seleccionar variables, filtrar registros y crear una nueva característica derivada.

Finalmente, se generó un archivo de texto con información descriptiva del conjunto de datos transformado y se documentó el proyecto para facilitar su ejecución y revisión.

---

**Actividad:** EA1 – Carga y Creación de Dataset  
**Institución:** IU Digital  
**Lenguaje:** Python  
**Entorno de ejecución:** Google Colab  
**Fuente de datos:** Hugging Face
**Estudiante:** Duván Oswaldo Ramírez Duarte 
