# Proyecto de Clasificación de Noticias con Apache Airflow

Este proyecto se enfoca en la clasificación de noticias de un periódico local mediante un flujo de trabajo estructurado y automatizado utilizando Apache Airflow. El proceso completo, desde la extracción de las noticias diarias hasta la clasificación y el envío de un informe, se ejecuta de manera eficiente y parametrizada para una única ejecución diaria. A continuación, se describen los pasos clave del flujo de trabajo:

## Pasos del Flujo de Trabajo

### 1. Extracción de Noticias

Se inicia con la extracción y registro de las noticias diarias del periódico local mediante un proceso de web scrapping. Esto se logra ejecutando un script diseñado específicamente para esta tarea. Las noticias se obtienen de la fuente original y se almacenan en un formato adecuado para su procesamiento posterior.

### 2. Clasificación de Noticias

Las noticias extraídas se clasifican automáticamente en categorías de Positivas, Negativas o Neutras utilizando un modelo de lenguaje previamente importado desde Hugging Face. Este modelo, basado en BERT y entrenado en corpus en español, ha sido afinado específicamente para la tarea de clasificación de noticias. La clasificación proporciona información valiosa sobre el tono y la orientación de las noticias.

### 3. Almacenamiento en MongoDB

Las noticias recién clasificadas se almacenan en una base de datos MongoDB para su posterior acceso y consulta. Cada noticia se guarda junto con su etiqueta de clasificación correspondiente, lo que facilita el análisis y la recuperación de datos históricos.

### 4. Generación de Informe y Envío por Correo Electrónico

El último paso del flujo de trabajo consiste en la generación de un informe que incluye las noticias positivas y negativas del día. Este informe se envía automáticamente por correo electrónico a la dirección especificada, lo que permite a los interesados recibir y revisar fácilmente las noticias más relevantes.

## Ejecución Diaria

Este flujo de trabajo está diseñado para ejecutarse una vez al día, garantizando que las noticias sean procesadas y clasificadas de manera puntual. Los parámetros de configuración se han ajustado para adaptarse a esta frecuencia.

¡Gracias por revisar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto con nosotros.

---
