import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa sozlamalari (Dark mode uslubida)
st.set_page_config(page_title="G20 Davlatlari", layout="wide", initial_sidebar_state="expanded")

# Ma'lumotlar bazasi (Aniq ko'rsatkichlar)
g20_data = {
    'AQSH': {
        'iso': 'USA', 'coords': [37.09, -95.71], 'yaim': '$27.9 trln', 'aholi': '340 mln', 'inflyatsiya': '3.1%', 
        'sanoat': 'Texnologiya, moliya', 'osish': 2.1,
        'exports': [('Xitoy', 'Samolyot', '150B$'), ('Kanada', 'Mashina', '300B$')],
        'imports': [('Xitoy', 'Elektronika', '450B$'), ('Yaponiya', 'Avto', '120B$')]
    },
    'Xitoy': {
        'iso': 'CHN', 'coords': [35.86, 104.19], 'yaim': '$18.5 trln', 'aholi': '1.41 mlrd', 'inflyatsiya': '0.3%', 
        'sanoat': 'Ishlab chiqarish', 'osish': 4.6,
        'exports': [('AQSH', 'Elektronika', '500B$'), ('Germaniya', 'Avto qismlar', '100B$')],
        'imports': [('Avstraliya', 'Ruda', '120B$'), ('Rossiya', 'Neft', '80B$')]
    },
    'Braziliya': {
        'iso': 'BRA', 'coords': [-14.23, -51.92], 'yaim': '$2.1 trln', 'aholi': '215 mln', 'inflyatsiya': '4.3%', 
        'sanoat': 'Qishloq xo\'jaligi', 'osish': 2.2,
        'exports': [('Xitoy', 'Soya', '90B$'), ('Argentina', 'Avto', '15B$')],
        'imports': [('AQSH', 'Yoqilg\'i', '18B$'), ('Germaniya', 'Kimyo', '10B$')]
    }
    # Boshqa davlatlarni ham shu formatda qo'shish mumkin
}

# 2. Sidebar (Boshqaruv paneli)
st.sidebar.title("🛠️ Boshqaruv Paneli")
st.sidebar.markdown("---")
selected_country = st.sidebar.selectbox("Davlatni tanlang:", list(g20_data.keys()))
show_exp = st.sidebar.checkbox("Eksportni ko'rsatish (Ko'k)", value=True)
show_imp = st.sidebar.checkbox("Importni ko'rsatish (Qizil)", value=True)

# 3. Asosiy Sarlavha
st.markdown("<h1 style='text-align: center; color: white;'>🌐 G20 Davlatlari</h1>", unsafe_allow_html=True)

# 4. Globus yaratish
fig = go.Figure()

# Choropleth (Rangli davlatlar)
fig.add_trace(go.Choropleth(
    locations=[v['iso'] for v in g20_data.values()],
    z=[v['osish'] for v in g20_data.values()],
    text=list(g20_data.keys()),
    colorscale="Viridis",
    marker_line_color='white',
    showscale=True,
    colorbar=dict(title="O'sish %", orientation='h', y=-0.1)
))

# Savdo chiziqlari (Eksport va Import)
if selected_country in g20_data:
    start = g20_data[selected_country]['coords']
    
    if show_exp:
        for p, prod, val in g20_data[selected_country]['exports']:
            if p in g20_data:
                end = g20_data[p]['coords']
                fig.add_trace(go.Scattergeo(
                    lon=[start[1], end[1]], lat=[start[0], end[0]],
                    mode='lines+markers', line=dict(width=2, color='deepskyblue'),
                    hoverinfo='text', text=f"Eksport -> {p}: {prod} ({val})"))

    if show_imp:
        for p, prod, val in g20_data[selected_country]['imports']:
            if p in g20_data:
                end = g20_data[p]['coords']
                fig.add_trace(go.Scattergeo(
                    lon=[start[1], end[1]], lat=[start[0], end[0]],
                    mode='lines+markers', line=dict(width=2, color='crimson'),
                    hoverinfo='text', text=f"Import <- {p}: {prod} ({val})"))

fig.update_geos(
    projection_type="orthographic", showocean=True, oceancolor="#1a1c23",
    showcountries=True, countrycolor="#444", bgcolor="rgba(0,0,0,0)"
)
fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# 5. Pastki ko'rsatkichlar (Metrics)
st.markdown(f"### 📊 {selected_country} haqida batafsil")
c = g20_data[selected_country]
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info(f"YaIM (Nominal)\n\n{c['yaim']}")
with col2:
    st.info(f"Aholi soni\n\n{c['aholi']}")
with col3:
    st.info(f"Inflyatsiya\n\n{c['inflyatsiya']}")
with col4:
    st.info(f"Iqtisodiy o'sish\n\n{c['osish']}%")

st.success(f"Asosiy sanoat tarmoqlari: {c['sanoat']}")
