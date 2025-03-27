import requests
from bs4 import BeautifulSoup
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import logging 
from dotenv import load_dotenv
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

load_dotenv()

PRODUCT_URL = os.getenv('PRODUCT_URL')
TARGET_PRICE = 1800
DISCORD_WEBHOOK_URL = os.getenv('DISCORD_WEBHOOK_URL')

def get_product_details():
    logging.info("Iniciando la obtención de los detalles del producto.")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    try:
        response = requests.get(PRODUCT_URL, headers=headers)
        logging.info(f"Solicitud enviada a {PRODUCT_URL}. Código de respuesta: {response.status_code}")
        
        if response.status_code != 200:
            logging.error(f"Error al obtener la página del producto. Código de estado: {response.status_code}")
            return None, None, None

        soup = BeautifulSoup(response.content, 'html.parser')

        price_tag = soup.find('span', class_='nds-text mr2-sm css-tbgmka e1yhcai00 text-align-start appearance-body1Strong color-primary display-inline weight-regular')
        price = None
        if price_tag:
            price_text = price_tag.text.strip()
            logging.info(f"Etiqueta de precio encontrada: {price_text}")
            price = float(price_text.replace('$', '').replace(',', ''))

        name_tag = soup.find('h1', class_='nds-text css-1h3ryhm e1yhcai00 text-align-start appearance-title4 color-primary weight-regular')  
        name = name_tag.text.strip() if name_tag else "Nombre no encontrado"

        image_tag = soup.find('img', class_='css-17pzig5') 
        image_url = image_tag['src'] if image_tag else None

        return price, name, image_url
    except Exception as e:
        logging.error(f"Error al obtener los detalles del producto: {e}")
        return None, None, None


def send_discord_notification(price, name, image_url, message_type="info"):
    payload = {
        "content": None,
        "embeds": [
            {
                "title": f"¡Alerta de precio de Nike! - {name}",
                "description": f"{message_type}: El precio actual es ${price}.",
                "image": {"url": image_url} if image_url else None,
                "color": 3066993 if message_type == "info" else 15158332  
            }
        ]
    }
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        logging.info(f"Respuesta de Discord: {response.status_code}, {response.text}")
        if response.status_code == 204:
            logging.info("Notificación enviada a Discord.")
        else:
            logging.error(f"Error al enviar notificación a Discord. Código de estado: {response.status_code}, Respuesta: {response.text}")
    except Exception as e:
        logging.error(f"Excepción al intentar enviar notificación a Discord: {e}")


def check_price_and_notify():
    price, name, image_url = get_product_details()
    if price is not None:
        logging.info(f'Precio actual: ${price}')
        if price <= TARGET_PRICE:
            send_discord_notification(price, name, image_url, message_type="info")
            logging.info(f'Notificación enviada. Precio alcanzado: ${price}')
        else:
            send_discord_notification(price, name, image_url, message_type="info")
            logging.info('El precio no ha alcanzado el objetivo, pero se envió una notificación.')
    else:
        logging.error('No se pudo obtener el precio del producto.')
        send_discord_notification(None, "Producto no encontrado", None, message_type="error")

# Definir el DAG
default_args = {
    'owner': 'Daniel',
    'start_date': datetime(2025, 3, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'airforce1_price_checker',
    default_args=default_args,
    description='Un bot que verifica el precio de unos tenis de Nike y te notifica',
    schedule_interval='@daily',
)

check_price_task = PythonOperator(
    task_id='check_price',
    python_callable=check_price_and_notify,
    dag=dag,
)