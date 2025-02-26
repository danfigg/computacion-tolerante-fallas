import psutil
import time
from datetime import datetime 

def obtener_rendimiento():
    # Obtener la hora actual
    hora_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Uso de CPU
    cpu_uso = psutil.cpu_percent(interval=1)
    cpu_uso_por_nucleo = psutil.cpu_percent(interval=1, percpu=True)

    # Uso de memoria
    memoria = psutil.virtual_memory()
    memoria_uso = memoria.percent
    memoria_total = memoria.total / (1024 ** 3)  # Convertir a GB
    memoria_usada = memoria.used / (1024 ** 3)   # Convertir a GB

    # Uso de disco
    disco = psutil.disk_usage('/')
    disco_uso = disco.percent
    disco_total = disco.total / (1024 ** 3)  # Convertir a GB
    disco_usado = disco.used / (1024 ** 3)   # Convertir a GB

    # Actividad de red
    red = psutil.net_io_counters()
    bytes_enviados = red.bytes_sent / (1024 ** 2)  # Convertir a MB
    bytes_recibidos = red.bytes_recv / (1024 ** 2)  # Convertir a MB

    # Temperatura
    try:
        temperatura = psutil.sensors_temperatures()
        temp_cpu = temperatura['coretemp'][0].current if 'coretemp' in temperatura else "N/A"
    except:
        temp_cpu = "N/A"

    # Batería
    try:
        bateria = psutil.sensors_battery()
        porcentaje_bateria = bateria.percent
        estado_bateria = "Cargando" if bateria.power_plugged else "Descargando"
    except:
        porcentaje_bateria = "N/A"
        estado_bateria = "N/A"

    # Procesos que más consumen CPU
    procesos = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            if proc.info['cpu_percent'] is not None:
                procesos.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Ordenar procesos por uso de CPU
    procesos.sort(key=lambda p: p['cpu_percent'] if p['cpu_percent'] is not None else 0, reverse=True)

    # Mostrar métricas
    print(f"\n=== Monitor de Rendimiento ({hora_actual}) ===")
    print(f"CPU: {cpu_uso}%")
    print(f"CPU por núcleo: {cpu_uso_por_nucleo}")
    print(f"Memoria: {memoria_uso}% (Usada: {memoria_usada:.2f} GB / Total: {memoria_total:.2f} GB)")
    print(f"Disco: {disco_uso}% (Usado: {disco_usado:.2f} GB / Total: {disco_total:.2f} GB)")
    print(f"Red: Enviados = {bytes_enviados:.2f} MB, Recibidos = {bytes_recibidos:.2f} MB")
    print(f"Temperatura CPU: {temp_cpu}°C")
    print(f"Batería: {porcentaje_bateria}% ({estado_bateria})")
    print("\nTop 5 procesos por uso de CPU:")
    for proc in procesos[:5]:
        print(f"  {proc['name']} (PID: {proc['pid']}): CPU = {proc['cpu_percent']}%, Memoria = {proc['memory_percent']:.2f}%")
    print("==============================")

if __name__ == "__main__":
    try:
        while True:
            obtener_rendimiento()
            time.sleep(5) 
    except KeyboardInterrupt:
        print("Monitor detenido.")