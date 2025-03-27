# Proyecto de Predicción de Goles en la Liga MX

Este proyecto utiliza datos históricos de la Liga MX para predecir los goles de los equipos locales y visitantes en los partidos. El proyecto incluye flujos ETL para limpiar, dividir y predecir los datos, así como modelos de machine learning para realizar las predicciones.

## Descripción de Archivos

Este repositorio está organizado en diferentes carpetas y archivos para facilitar el flujo de trabajo del proyecto.

### `data/`
Contiene los datos originales, los datos limpios y procesados, así como los modelos y las predicciones generadas por los modelos.

- `2016-2024_liga_mx_clean.csv`: Datos limpios y preprocesados, listos para ser utilizados en los modelos de predicción.
- `2016-2024_liga_mx.csv`: Datos originales obtenidos del dataset de Kaggle.
  
### `models/`
Contiene los modelos entrenados que se utilizan para la predicción de los goles.

- `home_goals_model.pkl`: Modelo entrenado para predecir los goles del equipo local.
- `away_goals_model.pkl`: Modelo entrenado para predecir los goles del equipo visitante.
- `le_home_team.pkl`: `LabelEncoder` entrenado para la columna `home_team`.
- `le_away_team.pkl`: `LabelEncoder` entrenado para la columna `away_team`.
- `le_stadium.pkl`: `LabelEncoder` entrenado para la columna `stadium`.
- `le_season.pkl`: `LabelEncoder` entrenado para la columna `season`.
- `le_tournament.pkl`: `LabelEncoder` entrenado para la columna `tournament`.
- `le_round.pkl`: `LabelEncoder` entrenado para la columna `round`.

### `predictions/`
Contiene las predicciones generadas por los modelos de machine learning.

- `goals_predictions.csv`: Predicciones de los goles para los equipos locales y visitantes.

### `split/`
Contiene los datos divididos en conjuntos de entrenamiento y prueba.

- `train_x.csv`: Conjunto de datos de características de entrenamiento.
- `test_x.csv`: Conjunto de datos de características de prueba.
- `train_y.csv`: Conjunto de etiquetas de entrenamiento (goles).
- `test_y.csv`: Conjunto de etiquetas de prueba (goles).

### `etl/`
Scripts para los flujos ETL que manejan la limpieza, transformación, división y predicción de los datos.

- `etl_clean.py`: Limpia y transforma los datos originales, eliminando los valores nulos, duplicados y realizando otras transformaciones necesarias.
- `etl_predict.py`: Utiliza los modelos entrenados para realizar las predicciones de goles (locales y visitantes).
- `etl_split.py`: Divide los datos en conjuntos de entrenamiento y prueba, listos para ser utilizados en los modelos.
- `etl_train.py`: Entrena los modelos de machine learning utilizando los datos de entrenamiento.

## Requisitos

Este proyecto requiere Python 3.x y las siguientes librerías:

- `pandas`
- `scikit-learn`
- `joblib`
- `prefect`

Puedes instalar las dependencias ejecutando el siguiente comando:

```bash
pip install -r requirements.txt
```

## Repositorio de obtención de dataset
El dataset utilizado en este proyecto proviene del repositorio de Kaggle. Puedes obtenerlo desde el siguiente enlace:

- [Dataset Liga MX (2016-2024)](https://www.kaggle.com/datasets/gerardojaimeescareo/ligamx-matches-2016-2022?resource=download&select=2016-2024_liga_mx.csv)

### Descripción del Dataset

El dataset contiene información sobre los partidos de la Liga MX desde 2016 hasta 2024, incluyendo detalles clave como:

- **Fecha del partido**: La fecha y hora exacta de los partidos.
- **Equipos**: Los equipos que jugaron como locales y visitantes.
- **Estadio**: El estadio en el que se jugó el partido.
- **Temporada**: La temporada de la Liga MX a la que pertenece el partido.
- **Torneo**: El tipo de torneo (liga regular, liguilla, etc.).
- **Ronda**: La fase del torneo (por ejemplo, cuartos de final, semifinales).
- **Goles**: Los goles anotados por el equipo local y el equipo visitante.

### Preprocesamiento de los Datos

El flujo ETL incluye los siguientes pasos para el procesamiento de los datos:

1. **Limpieza**: Se eliminan los valores nulos, se corrigen los formatos incorrectos y se eliminan las columnas innecesarias.
2. **Transformación**: Se extraen características temporales de la columna `date` (año, mes, día, etc.) y se codifican las variables categóricas (equipos, estadio, torneo, etc.) utilizando `LabelEncoder`.
3. **División**: Se dividen los datos en conjuntos de entrenamiento y prueba, asegurando que los modelos entrenados no estén sobreajustados.
4. **Entrenamiento**: Se entrenan modelos de machine learning para predecir los goles de los equipos locales y visitantes.

## Flujo de Trabajo

1. **Obtener el Dataset**: Descarga el archivo CSV desde Kaggle.
2. **Limpiar y Preprocesar los Datos**: Ejecuta el script `etl_clean.py` para limpiar y transformar los datos.
3. **Dividir los Datos**: Ejecuta el script `etl_split.py` para dividir los datos en conjuntos de entrenamiento y prueba.
4. **Entrenar los Modelos**: Ejecuta el script `etl_train.py` para entrenar los modelos de machine learning.
5. **Realizar Predicciones**: Ejecuta el script `etl_predict.py` para generar las predicciones de goles de los equipos locales y visitantes.
