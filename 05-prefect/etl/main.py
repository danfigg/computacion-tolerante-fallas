from etl_clean import etl_clean_flow 
from etl_split import etl_split_flow
from etl_train import etl_training_pipeline
from etl_predict import etl_prediction_pipeline

def main():
    
    etl_clean_flow()
    etl_split_flow()
    etl_training_pipeline()
    etl_prediction_pipeline()

if __name__ == "__main__":
    main()
    
