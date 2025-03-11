# Proyecto de Predicción de Goles en la Liga MX

Este proyecto utiliza datos históricos de la Liga MX para predecir los goles de los equipos locales y visitantes en los partidos. El proyecto incluye flujos ETL para limpiar, dividir y predecir los datos, así como modelos de machine learning para realizar las predicciones.

## Descripción de Archivos

- **data/**: Contiene los datos originales y procesados, así como los modelos y predicciones.
  - `2016-2024_liga_mx_clean.csv`: Datos limpios.
  - `2016-2024_liga_mx.csv`: Datos originales.
  - `clean_2016-2024_liga_mx.csv`: Datos limpios (duplicado).
  - **models/**: Modelos entrenados para la predicción de goles.
  - **predictions/**: Predicciones generadas por los modelos.
  - **split/**: Datos divididos en conjuntos de entrenamiento y prueba.

- **etl/**: Scripts para los flujos ETL.
  - `etl_clean.py`: Limpia y transforma los datos.
  - `etl_predict.py`: Realiza predicciones utilizando los modelos entrenados.
  - `etl_split.py`: Divide los datos en conjuntos de entrenamiento y prueba.
  - `etl_train.py`: Entrena los modelos de machine learning.
  
  