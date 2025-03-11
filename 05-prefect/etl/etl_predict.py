from prefect import flow, task
import pandas as pd
import joblib

@task
def extract_prediction_data():
    # Lee los datos de las características (test_x)
    test_x = pd.read_csv("../data/split/2016-2024_liga_mx_test_x.csv")
    
    # Asegúrate de que el dataframe tiene las mismas columnas que los datos de entrenamiento
    test_x['date'] = pd.to_datetime(test_x['date'], errors='coerce')  # Convierte la columna 'date' a datetime
    
    # Extraer componentes de la fecha
    test_x['year'] = test_x['date'].dt.year
    test_x['month'] = test_x['date'].dt.month
    test_x['day'] = test_x['date'].dt.day
    test_x['hour'] = test_x['date'].dt.hour
    test_x['minute'] = test_x['date'].dt.minute
    test_x['second'] = test_x['date'].dt.second

    # Eliminar la columna original 'date'
    test_x.drop('date', axis=1, inplace=True)
    
    return test_x

@task
def transform_prediction_data(test_x):
    # Cargar los LabelEncoders ajustados durante el entrenamiento
    le_home_team = joblib.load("../data/models/le_home_team.pkl")
    le_away_team = joblib.load("../data/models/le_away_team.pkl")
    le_stadium = joblib.load("../data/models/le_stadium.pkl")
    le_season = joblib.load("../data/models/le_season.pkl")
    le_tournament = joblib.load("../data/models/le_tournament.pkl")
    le_round = joblib.load("../data/models/le_round.pkl")
    
    # Codificar columnas categóricas en test_x
    test_x['home_team'] = le_home_team.transform(test_x['home_team'])
    test_x['away_team'] = le_away_team.transform(test_x['away_team'])
    test_x['stadium'] = le_stadium.transform(test_x['stadium'])
    test_x['season'] = le_season.transform(test_x['season'])
    test_x['tournament'] = le_tournament.transform(test_x['tournament'])

    # Mapeo para convertir las categorías de 'round' en números
    round_mapping = {
        'Round 1': 1,
        'Round 2': 2,
        'Round 3': 3,
        'Quarter-finals': 4,
        'Semi-finals': 5,
        'Final': 6
    }
    test_x['round'] = test_x['round'].map(round_mapping)
    
    return test_x

@task
def load_trained_models():
    # Cargar los modelos entrenados desde los archivos .pkl
    home_model = joblib.load("../data/models/home_goals_model.pkl")
    away_model = joblib.load("../data/models/away_goals_model.pkl")
    
    return home_model, away_model

@task
def predict_goals(test_x, home_model, away_model):
    # Realizar las predicciones para los goles de local y visitante
    home_predictions = home_model.predict(test_x)
    away_predictions = away_model.predict(test_x)

    home_predictions = home_predictions.astype(int)
    away_predictions = away_predictions.astype(int)
    
    return home_predictions, away_predictions

@task
def save_predictions(home_predictions, away_predictions):
    # Guardar las predicciones en un archivo CSV
    predictions_df = pd.DataFrame({
        'home_goals_predicted': home_predictions,
        'away_goals_predicted': away_predictions
    })
    
    predictions_df.to_csv("../data/predictions/goals_predictions.csv", index=False)

@flow
def etl_prediction_pipeline():
    # Flujo de trabajo completo para realizar predicciones
    test_x = extract_prediction_data()
    test_x = transform_prediction_data(test_x)
    home_model, away_model = load_trained_models()
    home_predictions, away_predictions = predict_goals(test_x, home_model, away_model)
    save_predictions(home_predictions, away_predictions)

if __name__ == "__main__":
    etl_prediction_pipeline()
