from prefect import flow, task
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

@task
def extract():
    # Lee los datos de las características (train_x) y las etiquetas (train_y)
    train_x = pd.read_csv("../data/split/2016-2024_liga_mx_train_x.csv")
    train_y = pd.read_csv("../data/split/2016-2024_liga_mx_train_y.csv")
    
    # Separar los goles de local y goles de visitante
    home_goals = train_y['home_goals']
    away_goals = train_y['away_goals']
    
    return train_x, home_goals, away_goals

@task
def transform(train_x):
    # Usar LabelEncoder para convertir las columnas categóricas (home_team, away_team, etc.)
    le_home_team = LabelEncoder()
    le_away_team = LabelEncoder()
    le_stadium = LabelEncoder()
    le_season = LabelEncoder()
    le_tournament = LabelEncoder()
    le_round = LabelEncoder()

    train_x['date'] = pd.to_datetime(train_x['date'], errors='coerce') 

    train_x['year'] = train_x['date'].dt.year
    train_x['month'] = train_x['date'].dt.month
    train_x['day'] = train_x['date'].dt.day
    train_x['hour'] = train_x['date'].dt.hour
    train_x['minute'] = train_x['date'].dt.minute
    train_x['second'] = train_x['date'].dt.second

    train_x.drop('date', axis=1, inplace=True)
    
    # Codificar columnas categóricas en train_x
    train_x['home_team'] = le_home_team.fit_transform(train_x['home_team'])
    train_x['away_team'] = le_away_team.fit_transform(train_x['away_team'])
    train_x['stadium'] = le_stadium.fit_transform(train_x['stadium'])
    train_x['season'] = le_season.fit_transform(train_x['season'])
    train_x['tournament'] = le_tournament.fit_transform(train_x['tournament'])
    
    # Mapeo para convertir las categorías de 'round' en números
    round_mapping = {
        'Round 1': 1,
        'Round 2': 2,
        'Round 3': 3,
        'Quarter-finals': 4,
        'Semi-finals': 5,
        'Final': 6
    }
    train_x['round'] = train_x['round'].map(round_mapping)
    
    # Guardar los LabelEncoders solo si es necesario
    joblib.dump(le_home_team, "../data/models/le_home_team.pkl")
    joblib.dump(le_away_team, "../data/models/le_away_team.pkl")
    joblib.dump(le_stadium, "../data/models/le_stadium.pkl")
    joblib.dump(le_season, "../data/models/le_season.pkl")
    joblib.dump(le_tournament, "../data/models/le_tournament.pkl")
    joblib.dump(le_round, "../data/models/le_round.pkl")
    
    return train_x

@task
def train_model(train_x, home_goals, away_goals):    
    # Modelo para goles de local
    home_model = RandomForestRegressor()
    home_model.fit(train_x, home_goals)
    
    # Modelo para goles de visitante
    away_model = RandomForestRegressor()
    away_model.fit(train_x, away_goals)
    
    return home_model, away_model

@task
def save_model(home_model, away_model):
    # Guardar los dos modelos entrenados
    joblib.dump(home_model, "../data/models/home_goals_model.pkl")
    joblib.dump(away_model, "../data/models/away_goals_model.pkl")

@flow
def etl_training_pipeline():
    train_x, home_goals, away_goals = extract()
    train_x = transform(train_x)
    home_model, away_model = train_model(train_x, home_goals, away_goals)
    save_model(home_model, away_model)

if __name__ == "__main__":
    etl_training_pipeline()
