📌 Cotizador de Impresión 3D - Crear4D

Este es un cotizador avanzado de impresión 3D desarrollado en Streamlit, diseñado para calcular los costos exactos de fabricación de piezas impresas en 3D. Permite ingresar variables como costos de material, electricidad, amortización de la impresora, tiempo de impresión, tasas de fallos y costos operativos para obtener un precio preciso por pieza impresa.

🚀 Características

✅ Cálculo detallado del costo de impresión basado en múltiples factores. ✅ Permite definir los costos de material, electricidad, operarios y amortización de la impresora. ✅ Estima los costos de fallos considerando la tasa de errores en la producción. ✅ Muestra un desglose del costo por hora de operación. ✅ Interfaz simple e intuitiva con Streamlit.

📥 Instalación y Ejecución

🔧 Requisitos previos

Asegúrate de tener Python 3.8 o superior instalado en tu sistema. Además, necesitas instalar las siguientes dependencias:

pip install streamlit numpy matplotlib

▶️ Cómo ejecutar la aplicación

Clona este repositorio y entra en la carpeta del proyecto:

git clone https://github.com/diegolunabaldwin/cotizadorC4D.git
cd cotizadorC4D

Ejecuta la aplicación con Streamlit:

streamlit run cotizadorC4D.py

La aplicación se abrirá en tu navegador automáticamente.

📊 Parámetros de Entrada

El usuario debe ingresar los siguientes datos para obtener el costo de impresión:

💰 Costos básicos:

Costo del plástico (S/ por kg)

Costo de electricidad (S/ por kWh)

Consumo medio de la impresora (kW)

🏭 Costos de amortización:

Costo de la impresora (S/)

Tiempo de amortización (años)

Días de actividad al año

Horas de impresión por día

⚙️ Costos operativos:

Tasa de fallos (%)

Costo por hora del operador (S/)

Tiempo de preparación (h)

Tiempo de postproducción (h)

📏 Datos de la pieza:

Masa de la pieza (kg)

Tiempo de impresión (h)

📊 Fórmulas Utilizadas

El sistema calcula el costo total de la pieza con la siguiente ecuación:

Coste pieza = (Coste plástico + Coste electricidad + Coste operario (preparación + postproducción) + Coste amortización) + Coste fallos

Donde:

Coste electricidad = Tiempo impresión × Coste por hora de luz
Coste operario = (Coste por hora del operador × Tiempo preparación) + (Coste por hora del operador × Tiempo postproducción)
Coste amortización = Coste de amortización × Tiempo impresión
Coste fallos = (Suma de todos los costos) × Tasa de fallos

📈 Visualización de Resultados

La app genera:

✅ Cálculo del costo total de la pieza impresa.✅ Gráficos que desglosan los costos por material, energía y operarios.✅ Resumen visual con métricas clave de costos.

🛠️ Mejoras Futuras

🔹 Integración con un sistema de estimación de tiempo basado en modelos de IA.🔹 Soporte para diferentes tecnologías de impresión (FDM, SLA, etc.).🔹 Opción para importar datos de un archivo CSV o desde un Slicer.

🏆 Contribuciones

¡Las contribuciones son bienvenidas! Si deseas mejorar el sistema o agregar nuevas funciones, haz un fork y envía un pull request.

📧 Para dudas o sugerencias, contáctame en d.luna@pucp.edu.pe

📜 Licencia

Este proyecto está bajo la Licencia MIT - puedes usarlo, modificarlo y compartirlo libremente. 🎉
