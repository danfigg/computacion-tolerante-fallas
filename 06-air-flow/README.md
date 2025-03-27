# Airflow DAG: Airforce 1 Price Checker

Este proyecto utiliza **Apache Airflow** para automatizar la verificación diaria del precio de un producto (en este caso, los tenis **Nike Airforce 1**) en el sitio web de Nike. Si el precio alcanza o está por debajo de un precio objetivo, se envía una notificación a un canal de **Discord** utilizando un webhook.

## Características

- **Automatización diaria**: El DAG se ejecuta automáticamente todos los días para verificar el precio del producto.
- **Notificaciones en Discord**: Envía un mensaje al canal de Discord configurado, indicando si el precio ha alcanzado el objetivo o si aún no lo ha hecho.

## Requisitos

- **Apache Airflow**: Configurado y en funcionamiento.
- **Python 3.7+**
- Dependencias adicionales:
  Se encuentran en `requeriments.txt`

## Instalación

Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/danfigg/computacion-tolerante-fallas.git
   cd 06-air-flow/apache/airflow
   ```

## Ejecución

Ejecuta docker
   ```bash
   docker compose up -d
   ```
Accede a `http://localhost:8080` e inicias sesión. Podrás ver los Dags

### Vista del DAG en Airflow
A continuación, se muestra cómo se ve el DAG en la interfaz de Airflow:

![Vista del DAG en Airflow](/images/airflow_dag_view.png)

### Notificación en Discord
Ejemplo de una notificación enviada al canal de Discord configurado:

![Notificación en Discord](/images/discord_notification.png)
