import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa dizaynini "Dark Mode" qilish
st.set_page_config(page_title="G20 Davlatlari", layout="wide", initial_sidebar_state="expanded")

# Ma'lumotlar bazasini boyitish (2025-2026 prognozlari)
g20_data = {
    'Braziliya': {
        'iso': 'BRA', 'coords': [-14.23, -51.92], 
        'yaim': '2.3 Trillion', 'aholi': '217 Million', 
        'inflyatsiya': '3.8%', 'per_capita': '$10,600', 
        'osish': 2.2, 'valyuta': 'Brazilian Real (BRL)',
        'tavsif': "Braziliya Janubiy Amerikaning eng yirik iqtisodiyoti bo'lib, boy tabiiy resurslar va kuchli qishloq xo'jaligiga ega.",
        'exports': [('Xitoy', 'Soya', '90B$'), ('AQSH', 'Neft', '30B$')],
        'imports': [('Xitoy', 'Texnika', '25B$'), ('AQSH', 'Yoqilg\'i', '18B$')]
    },
    'AQSH': {
        'iso': 'USA', 'coords': [37.09, -95.71], 
        'yaim': '27.9 Trillion', 'aholi': '340 Million', 
        'inflyatsiya': '3.1%', 'per_capita': '$80,400', 
        'osish': 2.1, 'valyuta': 'US Dollar (USD)',
        'tavsif': "AQSH dunyoning eng yirik iqtisodiyoti bo'lib, yuqori texnologiyalar va moliya markazi hisoblanadi.",
        'exports': [('Kanada', 'Avto', '300B$'), ('Meksika', 'Kompyuter', '250B$')],
        'imports': [('Xitoy', 'Elektronika', '450B$')]
    },
    'Xitoy': {
        'iso': 'CHN', 'coords': [35.86, 104.19], 
        'yaim': '18.5 Trillion', 'aholi': '1.41 Milliard', 
        'inflyatsiya': '0.3%', 'per_capita': '$13,100', 
        'osish': 4.6, 'valyuta': 'Yuan (CNY)',
        'tavsif': "Xitoy dunyoning ishlab chiqarish fabrikasi va ikkinchi yirik iqtisodiyotidir.",
        'exports': [('AQSH', 'Elektronika', '500B$'), ('Germaniya', 'Mashinalar', '100B$')],
        'imports': [('Avstraliya', 'Ruda', '120B$')]
    }
    # Boshqa davlatlarni ham shu formatda qo'shish mumkin
}

# 2. Sidebar (Boshqaruv paneli)
st.sidebar.markdown("<h2 style='color: #4A90E2;'>🛠️ Boshqaruv Paneli</h2>", unsafe_allow_html=True)
selected_country = st.sidebar.selectbox("Davlatni tanlang:", list(g20_data.keys()))
st.sidebar.markdown("---")
show_exp = st.sidebar.checkbox("Eksport (Ko'k chiziqlar)", value=True)
show_imp = st.sidebar.checkbox("Import (Qizil chiziqlar)", value=True)

# 3. Asosiy Sarlavha
st.markdown("<h1 style='text-align: center;'>🌐 G20 Davlatlari</h1>", unsafe_allow_html=True)

# 4. Globus (Plotly)
fig = go.Figure()

# Choropleth (Ranglar)
fig.add_trace(go.Choropleth(
    locations=[v['iso'] for v in g20_data.values()],
    z=[v['osish'] for v in g20_data.values()],
    colorscale="Viridis",
    marker_line_color='white',
    colorbar=dict(title="O'sish %", orientation='h', y=-0.15)
))

# Savdo yo'llari (Chiziqlar)
if selected_country in g20_data:
    start = g20_data[selected_country]['coords']
    if show_exp:
        for p, prod, val in g20_data[selected_country]['exports']:
            if p in g20_data:
                end = g20_data[p]['coords']
                fig.add_trace(go.Scattergeo(
                    lon=[start[1], end[1]], lat=[start[0], end[0]],
                    mode='lines', line=dict(width=2, color='#00D1FF'))) # Ko'k neon
    if show_imp:
        for p, prod, val in g20_data[selected_country]['imports']:
            if p in g20_data:
                end = g20_data[p]['coords']
                fig.add_trace(go.Scattergeo(
                    lon=[start[1], end[1]], lat=[start[0], end[0]],
                    mode='lines', line=dict(width=2, color='#FF4B4B'))) # Qizil neon

fig.update_geos(
    projection_type="orthographic", showocean=True, oceancolor="#0E1117",
    showcountries=True, countrycolor="#31333F", bgcolor="rgba(0,0,0,0)"
)
fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# 5. Ma'lumotlar Paneli (Rasmdagi kabi ko'rinish)
st.markdown(f"## 📊 {selected_country}: Iqtisodiy Umumiy Ko'rinish")
c = g20_data[selected_country]
st.write(f"*{c['tavsif']}*")
# 2 qatorli ma'lumotlar (Metrics)
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("YaIM (Nominal)", f"{c['yaim']}")
    st.metric("Inflyatsiya", f"{c['inflyatsiya']}")
with col2:
    st.metric("Aholi soni", f"{c['aholi']}")
    st.metric("Aholi jon boshiga YaIM", f"{c['per_capita']}")
with col3:
    st.metric("Yillik o'sish", f"{c['osish']}%")
    st.metric("Valyuta", f"{c['valyuta']}")
