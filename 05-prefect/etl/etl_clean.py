from prefect import task, flow
import pandas as pd
from unidecode import unidecode


file_path = "../data/2016-2024_liga_mx.csv" 
output_path = "../data/2016-2024_liga_mx_clean.csv" 

@task
def extract():
    return pd.read_csv(file_path)

@task
def transform(df: pd.DataFrame) -> pd.DataFrame:
    """Limpia y transforma los datos en un formato adecuado."""
    
    # Eliminar filas con valores nulos en columnas clave
    df.dropna(subset=['home_team', 'away_team', 'home_goals', 'away_goals'], inplace=True)
    
    # Convertir 'date' a tipo datetime
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df.dropna(subset=['date'], inplace=True)  # Eliminar fechas inválidas
    
    # Convertir columnas de goles a tipo entero permitiendo valores nulos
    goles_columns = ['home_goals', 'away_goals']
    df[goles_columns] = df[goles_columns].apply(pd.to_numeric, errors='coerce').astype('Int64')
    
    # Convertir columnas categóricas
    categorical_columns = ['home_team', 'away_team', 'season', 'round']
    df[categorical_columns] = df[categorical_columns].astype('category')
    
    # Renombrar y dividir columna 'stage' en 'tournament' y 'round'
    df.rename(columns={'venue_name': 'stadium', 'round': 'stage'}, inplace=True)
    df[['tournament', 'round']] = df['stage'].str.split(' - ', expand=True)
    df[['tournament', 'round']] = df[['tournament', 'round']].astype('category')
    
    # Eliminar columnas innecesarias
    drop_columns = ['home_goals_extra_time', 'away_goals_extratime', 'home_goals_penalty', 'away_goals_penalty',
                    'home_goals_half_time', 'away_goals_half_time', 'home_goals_fulltime', 'away_goals_fulltime',
                    'venue_id', 'timezone', 'venue_city', 'stage', 'home_win', 'away_win', 'referee']
    df.drop(columns=drop_columns, errors='ignore', inplace=True)

    text_columns = ['home_team', 'away_team', 'season', 'round', 'stadium', 'tournament']
    for col in text_columns:
        df[col] = df[col].apply(lambda x: unidecode(str(x)))
    
    # Reorganizar las columnas
    column_order = ['id', 'date', 'stadium', 'season', 'tournament', 'round', 
                    'home_team', 'away_team', 'home_goals', 'away_goals']
    df = df[column_order]
    
    return df

@task
def load(df: pd.DataFrame):
    """Guarda el DataFrame limpio en un nuevo archivo CSV."""
    df.to_csv(output_path, index=False)

@flow(name="ETL Clean Flow")
def etl_clean_flow():
    """Ejecuta el flujo de extracción, transformación y carga (ETL)."""
    df = extract()
    cleaned_df = transform(df)
    load(cleaned_df)

if __name__ == "__main__":
    etl_clean_flow()