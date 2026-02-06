import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa sozlamalari
st.set_page_config(page_title="G20 Davlatlari", layout="wide")

# Ma'lumotlar bazasi (Barcha G20 davlatlari kiritildi)
g20_data = {
    "AQSH": {
        "iso": "USA", "yaim": "$27.9 Trln", "aholi": "340 Mln", "inflyatsiya": "3.1%", 
        "per_capita": "$80,412", "osish": 2.1, "valyuta": "AQSH Dollari (USD)", 
        "sanoat": "Moliya, Yuqori Texnologiya", "tavsif": "AQSH dunyoning eng yirik iqtisodiyoti bo'lib, global moliya tizimining o'zagi hisoblanadi."
    },
    "Xitoy": {
        "iso": "CHN", "yaim": "$18.5 Trln", "aholi": "1.41 Mlrd", "inflyatsiya": "0.3%", 
        "per_capita": "$13,136", "osish": 4.6, "valyuta": "Xitoy Yuani (CNY)", 
        "sanoat": "Ishlab chiqarish, IT", "tavsif": "Xitoy dunyoning ikkinchi yirik iqtisodiyoti va eng yirik eksportyor davlatidir."
    },
    "Braziliya": {
        "iso": "BRA", "yaim": "$2.3 Trln", "aholi": "217 Mln", "inflyatsiya": "3.8%", 
        "per_capita": "$10,600", "osish": 2.2, "valyuta": "Braziliya Reali (BRL)", 
        "sanoat": "Qishloq xo'jaligi, Neft", "tavsif": "Braziliya Janubiy Amerikaning iqtisodiy yetakchisi bo'lib, tabiiy resurslarga juda boy."
    },
    "Germaniya": {
        "iso": "DEU", "yaim": "$4.4 Trln", "aholi": "84 Mln", "inflyatsiya": "2.4%", 
        "per_capita": "$52,824", "osish": 1.3, "valyuta": "Yevro (EUR)", 
        "sanoat": "Avtomobilsozlik, Mashinasozlik", "tavsif": "Germaniya Yevropaning iqtisodiy dvigateli va jahon muhandislik markazi hisoblanadi."
    },
    "Turkiya": {
        "iso": "TUR", "yaim": "$1.1 Trln", "aholi": "85 Mln", "inflyatsiya": "64.8%", 
        "per_capita": "$12,800", "osish": 3.0, "valyuta": "Turk Lirasi (TRY)", 
        "sanoat": "To'qimachilik, Qurilish, Turizm", "tavsif": "Turkiya Yevropa va Osiyo chorrahasida joylashgan muhim sanoat va savdo markazidir."
    },
    "Hindiston": {
        "iso": "IND", "yaim": "$3.9 Trln", "aholi": "1.43 Mlrd", "inflyatsiya": "5.1%", 
        "per_capita": "$2,731", "osish": 6.8, "valyuta": "Hind Rupiyasi (INR)", 
        "sanoat": "IT, Farmatsevtika", "tavsif": "Hindiston dunyoning eng tez o'sayotgan yirik iqtisodiyotlaridan biri hisoblanadi."
    },
    "Rossiya": {
        "iso": "RUS", "yaim": "$1.9 Trln", "aholi": "144 Mln", "inflyatsiya": "7.4%", 
        "per_capita": "$13,200", "osish": 1.8, "valyuta": "Rossiya Rubli (RUB)", 
        "sanoat": "Energetika, Harbiy sanoat", "tavsif": "Rossiya dunyoning eng yirik energiya resurslari eksportyorlaridan biri hisoblanadi."
    },
    "Yaponiya": {
        "iso": "JPN", "yaim": "$4.2 Trln", "aholi": "125 Mln", "inflyatsiya": "2.5%", 
        "per_capita": "$33,800", "osish": 1.0, "valyuta": "Yen (JPY)", 
        "sanoat": "Robototexnika, Avtomobilsozlik", "tavsif": "Yaponiya yuqori texnologiyalar va aniq muhandislik sohasida dunyo yetakchisidir."
    },
    "Italiya": {
        "iso": "ITA", "yaim": "$2.2 Trln", "aholi": "59 Mln", "inflyatsiya": "0.8%", 
        "per_capita": "$37,700", "osish": 1.2, "valyuta": "Yevro (EUR)", 
        "sanoat": "Moda, Mashinasozlik", "tavsif": "Italiya Yevropaning eng kuchli ishlab chiqarish bazalaridan biri hisoblanadi."
    },
    "Kanada": {
        "iso": "CAN", "yaim": "$2.1 Trln", "aholi": "40 Mln", "inflyatsiya": "2.7%", 
        "per_capita": "$52,700", "osish": 2.3, "valyuta": "Kanada Dollari (CAD)", 
        "sanoat": "Energetika, Texnologiya", "tavsif": "Kanada boy tabiiy resurslar va rivojlangan xizmat ko'rsatish sohasiga ega."
    }
}

# 2. Sarlavha va Sidebar
st.markdown("<h1 style='text-align: center;'>🌐 G20 Davlatlari: Iqtisodiy Monitor</h1>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.header("🗺️ Boshqaruv Paneli")
selected_country = st.sidebar.selectbox("Davlatni tanlang:", list(g20_data.keys()))

# 3. Globus (Ochiq ko'k okean)
fig = go.Figure()
fig.add_trace(go.Choropleth(
    locations=[v['iso'] for v in g20_data.values()],
    z=[v['osish'] for v in g20_data.values()],
    text=list(g20_data.keys()),
    colorscale="Viridis",
    marker_line_color='white',
    colorbar=dict(title="O'sish %", orientation='h', y=-0.2)
))

fig.update_geos(
    projection_type="orthographic", 
    showocean=True, 
    oceancolor="LightBlue", # Okean ochiq ko'k
    showcountries=True, 
    countrycolor="white"
)

fig.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# 4. Dinamik Ma'lumotlar Paneli (st.metric)
st.markdown(f"### 📊 {selected_country}: Iqtisodiy Ko'rinish")
c = g20_data[selected_country]

# Tavsif bloki
st.info(c['tavsif'])

# Ma'lumot bloklari (st.metric)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("YaIM (Nominal)", c['yaim'])
    st.metric("Inflyatsiya", c['inflyatsiya'])

with col2:
    st.metric("Aholi soni", c['aholi'])
    st.metric("Jon boshiga YaIM", c['per_capita'])

with col3:
    st.metric("Yillik o'sish", f"{c['osish']}%")
    st.metric("Valyuta", c['valyuta'])

st.markdown(f"Asosiy sanoat tarmoqlari: {c['sanoat']}")
