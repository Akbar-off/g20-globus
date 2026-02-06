import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa dizayni va sarlavhasi
st.set_page_config(page_title="G20 Davlatlari", layout="wide")

# Ma'lumotlar bazasi (Valyuta va barcha iqtisodiy ko'rsatkichlar)
g20_data = {
    'AQSH': {
        'iso': 'USA', 'yaim': '$27.9 Trln', 'aholi': '340 Mln', 
        'inflyatsiya': '3.1%', 'per_capita': '$80,412', 'osish': 2.1, 
        'valyuta': 'AQSH Dollari (USD)', 'sanoat': 'Moliya, Yuqori Texnologiya',
        'tavsif': "AQSH dunyoning eng yirik iqtisodiyoti bo'lib, global moliya tizimining o'zagi hisoblanadi."
    },
    'Xitoy': {
        'iso': 'CHN', 'yaim': '$18.5 Trln', 'aholi': '1.41 Mlrd', 
        'inflyatsiya': '0.3%', 'per_capita': '$13,136', 'osish': 4.6, 
        'valyuta': 'Xitoy Yuani (CNY)', 'sanoat': 'Ishlab chiqarish, IT',
        'tavsif': "Xitoy dunyoning ikkinchi yirik iqtisodiyoti va eng yirik eksportyor davlatidir."
    },
    'Braziliya': {
        'iso': 'BRA', 'yaim': '$2.3 Trln', 'aholi': '217 Mln', 
        'inflyatsiya': '3.8%', 'per_capita': '$10,600', 'osish': 2.2, 
        'valyuta': 'Braziliya Reali (BRL)', 'sanoat': 'Qishloq xo\'jaligi, Neft sanoati',
        'tavsif': "Braziliya Janubiy Amerikaning iqtisodiy yetakchisi bo'lib, tabiiy resurslarga juda boy."
    },
    'Germaniya': {
        'iso': 'DEU', 'yaim': '$4.4 Trln', 'aholi': '84 Mln', 
        'inflyatsiya': '2.4%', 'per_capita': '$52,824', 'osish': 1.3, 
        'valyuta': 'Yevro (EUR)', 'sanoat': 'Avtomobilsozlik, Mashinasozlik',
        'tavsif': "Germaniya Yevropaning iqtisodiy dvigateli va jahon muhandislik markazi hisoblanadi."
    },
    'Turkiya': {
        'iso': 'TUR', 'yaim': '$1.1 Trln', 'aholi': '85 Mln', 
        'inflyatsiya': '64.8%', 'per_capita': '$12,800', 'osish': 3.0, 
        'valyuta': 'Turk Lirasi (TRY)', 'sanoat': 'To'qimachilik, Qurilish, Turizm',
        'tavsif': "Turkiya Yevropa va Osiyo chorrahasida joylashgan muhim sanoat va savdo markazidir."
    },
    'Rossiya': {
        'iso': 'RUS', 'yaim': '$1.9 Trln', 'aholi': '144 Mln', 
        'inflyatsiya': '7.4%', 'per_capita': '$13,200', 'osish': 1.8, 
        'valyuta': 'Rossiya Rubli (RUB)', 'sanoat': 'Energetika, Harbiy sanoat',
        'tavsif': "Rossiya dunyoning eng yirik energiya resurslari eksportyorlaridan biri hisoblanadi."
    }
}

# 2. Asosiy Sarlavha
st.markdown("<h1 style='text-align: center;'>🌐 G20 Davlatlari</h1>", unsafe_allow_html=True)
st.markdown("---")

# 3. Sidebar (Tanlash paneli)
st.sidebar.header("🗺️ Boshqaruv Paneli")
selected_country = st.sidebar.selectbox("Davlatni tanlang:", list(g20_data.keys()))

# 4. Globus (Plotly)
fig = go.Figure()

fig.add_trace(go.Choropleth(
    locations=[v['iso'] for v in g20_data.values()],
    z=[v['osish'] for v in g20_data.values()],
    colorscale="Viridis",
    marker_line_color='white',
    colorbar=dict(title="O'sish %", orientation='h', y=-0.2)
))

fig.update_geos(
    projection_type="orthographic", showocean=True, oceancolor="#0E1117",
    showcountries=True, countrycolor="white", bgcolor="rgba(0,0,0,0)"
)
fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# 5. Ma'lumotlar Paneli (st.metric bloklari)
st.markdown(f"## 📊 {selected_country}: Iqtisodiy Umumiy Ko'rinish")
c = g20_data[selected_country]

# Qisqa tavsif (Rasmdagi kabi matn)
st.info(c['tavsif'])

# Ma'lumotlar bloklari (Metrics)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("YaIM (Nominal)", c['yaim'])
    st.metric("Inflyatsiya darajasi", c['inflyatsiya'])

with col2:
    st.metric("Aholi soni", c['aholi'])
    st.metric("Jon boshiga YaIM", c['per_capita'])

with col3:
    st.metric("Yillik o'sish", f"{c['osish']}%")
    st.metric("Rasmiy valyuta", c['valyuta'])

st.markdown(f"Asosiy sanoat tarmoqlari: {c['sanoat']}")
