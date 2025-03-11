from prefect import flow, task
import pandas as pd
from sklearn.model_selection import train_test_split

file_path = "../data/2016-2024_liga_mx_clean.csv"
train_path_x = "../data/split/2016-2024_liga_mx_train_x.csv"
train_path_y = "../data/split/2016-2024_liga_mx_train_y.csv"
test_path_x = "../data/split/2016-2024_liga_mx_test_x.csv"
test_path_y = "../data/split/2016-2024_liga_mx_test_y.csv"

@task
def extract(file_path: str) -> pd.DataFrame:
    """Carga el archivo CSV en un DataFrame"""
    df = pd.read_csv(file_path)
    return df

@task
def transform(df: pd.DataFrame):
    """Divide el DataFrame en conjuntos de entrenamiento y prueba de forma aleatoria (80-20)"""
    
    # Convertir 'date' a tipo datetime si no lo está
    df['date'] = pd.to_datetime(df['date'], errors='coerce')

    # Eliminar las columnas de goles, ya que no se deben usar en el entrenamiento
    features = [column for column in df.columns if column not in ['home_goals', 'away_goals']]

    # Dividir los datos de forma aleatoria (80% entrenamiento, 20% prueba)
    X_train, X_test, y_train, y_test = train_test_split(
        df[features],  # Características
        df[['home_goals', 'away_goals']],  # Etiquetas
        test_size=0.2,  # 20% para prueba
        random_state=42,  # Semilla para reproducibilidad
    )

    return X_train, X_test, y_train, y_test

@task
def load(X_train: pd.DataFrame, X_test: pd.DataFrame, y_train: pd.DataFrame, y_test: pd.DataFrame):
    """Guarda los conjuntos de datos de entrenamiento y prueba en archivos CSV"""
    X_train.to_csv(train_path_x, index=False)
    X_test.to_csv(test_path_x, index=False)
    y_train.to_csv(train_path_y, index=False)
    y_test.to_csv(test_path_y, index=False)

@flow(name="ETL Split Flow")
def etl_split_flow():
    df = extract(file_path)
    X_train, X_test, y_train, y_test = transform(df)
    load(X_train, X_test, y_train, y_test)

if __name__ == "__main__":
    etl_split_flow()
