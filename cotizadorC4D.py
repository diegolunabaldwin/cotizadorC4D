import streamlit as st

# 🎯 Configuración de la App
st.title("🖨️ Cotizador de Impresión 3D - Crear4D")
st.write("Calcula el costo de impresión basado en materiales, energía y tiempo.")
st.markdown("Hecho por Diego Luna Baldwin @ Crear4D")

# 🔹 **Datos ingresados por el usuario**
st.header("📥 Datos de Costos Generales")
coste_plastico = st.number_input("💰 Coste del plástico (S/. por kg)", min_value=0.0, value=50.0)
coste_luz = st.number_input("⚡ Coste de la electricidad (S/. por kWh)", min_value=0.0, value=0.67)
consumo_medio = st.number_input("🔌 Consumo medio de la impresora (kW)", min_value=0.0, value=0.25)

coste_por_hora_luz = coste_luz * consumo_medio
st.write(f"🔹 **Coste por hora de electricidad**: S/. {coste_por_hora_luz:.2f}")

st.header("🏭 Costos de Amortización")
coste_impresora = st.number_input("🖨️ Coste de la impresora (S/.)", min_value=0.0, value=3000.0)
tiempo_amortizacion = st.number_input("⌛ Tiempo de amortización (años)", min_value=1, value=3)
dias_activa = st.number_input("📅 Días activa al año", min_value=1, max_value=365, value=300)
horas_por_dia = st.number_input("⏳ Horas activa por día", min_value=1, max_value=24, value=8)

coste_amortizacion_hora = coste_impresora / (tiempo_amortizacion * dias_activa * horas_por_dia)
st.write(f"🔹 **Coste de amortización por hora**: S/. {coste_amortizacion_hora:.2f}")

st.header("🛠️ Costos Operativos")
tasa_fallos = st.number_input("📉 Tasa de fallos (%)", min_value=0.0, max_value=100.0, value=5.0) / 100
coste_operario_hora = st.number_input("👷 Coste por hora del operario (S/. por h)", min_value=0.0, value=10.0)
tiempo_preparacion = st.number_input("⚙️ Tiempo de preparación (h)", min_value=0.0, value=0.5)
tiempo_postproduccion = st.number_input("🎨 Tiempo de postproducción (h)", min_value=0.0, value=1.0)

st.header("📦 Datos de la Pieza")
masa_pieza = st.number_input("⚖️ Masa de la pieza (kg)", min_value=0.0, value=0.2)
tiempo_impresion = st.number_input("⏱️ Tiempo de impresión (h)", min_value=0.0, value=5.0)

# 🔢 **Cálculos de costos**
coste_material = coste_plastico * masa_pieza
coste_electricidad = tiempo_impresion * coste_por_hora_luz
coste_operario_preparacion = coste_operario_hora * tiempo_preparacion
coste_operario_postproduccion = coste_operario_hora * tiempo_postproduccion
coste_amortizacion = coste_amortizacion_hora * tiempo_impresion

# 🔁 **Cálculo de fallos**
coste_total_sin_fallos = (
    coste_material + coste_electricidad +
    coste_operario_preparacion + coste_operario_postproduccion +
    coste_amortizacion
)
coste_fallos = coste_total_sin_fallos * tasa_fallos
coste_pieza_total = coste_total_sin_fallos + coste_fallos

# 🎯 **Resultados finales**
st.header("✅ Costo Total de la Impresión")
st.write(f"💰 **Costo del material**: S/. {coste_material:.2f}")
st.write(f"⚡ **Costo de electricidad**: S/. {coste_electricidad:.2f}")
st.write(f"👷 **Costo de operario (preparación)**: S/. {coste_operario_preparacion:.2f}")
st.write(f"🎨 **Costo de operario (post-producción)**: S/. {coste_operario_postproduccion:.2f}")
st.write(f"🏭 **Costo de amortización**: S/. {coste_amortizacion:.2f}")
st.write(f"⚠️ **Costo de fallos**: S/. {coste_fallos:.2f}")
st.subheader(f"💰 **Costo total de la pieza**: S/. {coste_pieza_total:.2f}")

# 📊 **Visualización de costos**
import matplotlib.pyplot as plt

labels = ["Material", "Electricidad", "Operario (Prep.)", "Operario (Post.)", "Amortización", "Fallos"]
costs = [coste_material, coste_electricidad, coste_operario_preparacion, coste_operario_postproduccion, coste_amortizacion, coste_fallos]

fig, ax = plt.subplots()
ax.pie(costs, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6'])
ax.axis('equal')
st.pyplot(fig)
