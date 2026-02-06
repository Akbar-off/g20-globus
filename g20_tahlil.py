import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa sozlamalari
st.set_page_config(page_title="G20 Davlatlari: To'liq Monitor", layout="wide")

# Ma'lumotlar bazasi - G20 ning barcha 19 ta davlati kiritildi
g20_data = {
    "AQSH": {
        "iso": "USA", "yaim": "$27.9 Trln", "aholi": "340 Mln", "inflyatsiya": "3.1%", 
        "per_capita": "$80,412", "osish": 2.1, "valyuta": "AQSH Dollari (USD)", 
        "sanoat": "Moliya, Texnologiya", "tavsif": "Dunyoning eng yirik iqtisodiyoti va global moliya markazi."
    },
    "Xitoy": {
        "iso": "CHN", "yaim": "$18.5 Trln", "aholi": "1.41 Mlrd", "inflyatsiya": "0.3%", 
        "per_capita": "$13,136", "osish": 4.6, "valyuta": "Xitoy Yuani (CNY)", 
        "sanoat": "Ishlab chiqarish, IT", "tavsif": "Dunyoning ishlab chiqarish fabrikasi va ikkinchi yirik iqtisodiyoti."
    },
    "Yaponiya": {
        "iso": "JPN", "yaim": "$4.2 Trln", "aholi": "125 Mln", "inflyatsiya": "2.5%", 
        "per_capita": "$33,800", "osish": 1.0, "valyuta": "Yen (JPY)", 
        "sanoat": "Robototexnika, Avtomobil", "tavsif": "Yuqori texnologiyalar va elektronika bo'yicha dunyo yetakchisi."
    },
    "Germaniya": {
        "iso": "DEU", "yaim": "$4.4 Trln", "aholi": "84 Mln", "inflyatsiya": "2.4%", 
        "per_capita": "$52,824", "osish": 1.3, "valyuta": "Yevro (EUR)", 
        "sanoat": "Mashinasozlik, Kimyo", "tavsif": "Yevropaning iqtisodiy lokomotivi va asosiy eksportyori."
    },
    "Hindiston": {
        "iso": "IND", "yaim": "$3.9 Trln", "aholi": "1.43 Mlrd", "inflyatsiya": "5.1%", 
        "per_capita": "$2,731", "osish": 6.8, "valyuta": "Hind Rupiyasi (INR)", 
        "sanoat": "Dasturiy ta'minot, Farmatsevtika", "tavsif": "Dunyoning eng tez o'sayotgan yirik iqtisodiyotlaridan biri."
    },
    "Buyuk Britaniya": {
        "iso": "GBR", "yaim": "$3.3 Trln", "aholi": "67 Mln", "inflyatsiya": "2.0%", 
        "per_capita": "$49,100", "osish": 1.4, "valyuta": "Funt Sterling (GBP)", 
        "sanoat": "Bank ishi, Ta'lim", "tavsif": "Global moliya xizmatlari va yuqori darajadagi ta'lim markazi."
    },
    "Fransiya": {
        "iso": "FRA", "yaim": "$3.0 Trln", "aholi": "68 Mln", "inflyatsiya": "2.3%", 
        "per_capita": "$44,400", "osish": 1.5, "valyuta": "Yevro (EUR)", 
        "sanoat": "Kosmik texnika, Turizm", "tavsif": "Yevropaning qishloq xo'jaligi va aviasozlik markazi."
    },
    "Italiya": {
        "iso": "ITA", "yaim": "$2.2 Trln", "aholi": "59 Mln", "inflyatsiya": "0.8%", 
        "per_capita": "$37,700", "osish": 1.2, "valyuta": "Yevro (EUR)", 
        "sanoat": "Moda, Dizayn, Mashina", "tavsif": "Yuqori sifatli tovarlar va turizm bo'yicha yetakchi davlat."
    },
    "Braziliya": {
        "iso": "BRA", "yaim": "$2.3 Trln", "aholi": "217 Mln", "inflyatsiya": "3.8%", 
        "per_capita": "$10,600", "osish": 2.2, "valyuta": "Braziliya Reali (BRL)", 
        "sanoat": "Qishloq xo'jaligi, Konchilik", "tavsif": "Lotin Amerikasining eng yirik iqtisodiyoti va resurslar bazasi."
    },
    "Kanada": {
        "iso": "CAN", "yaim": "$2.1 Trln", "aholi": "40 Mln", "inflyatsiya": "2.7%", 
        "per_capita": "$52,700", "osish": 2.3, "valyuta": "Kanada Dollari (CAD)", 
        "sanoat": "Energetika, Yog'och", "tavsif": "Tabiiy resurslarga boy, barqaror iqtisodiy tizimga ega."
    },
    "Rossiya": {
        "iso": "RUS", "yaim": "$1.9 Trln", "aholi": "144 Mln", "inflyatsiya": "7.4%", 
        "per_capita": "$13,200", "osish": 1.8, "valyuta": "Rossiya Rubli (RUB)", 
        "sanoat": "Gaz, Neft, Metallurgiya", "tavsif": "Dunyoning eng yirik energiya manbalari eksportyori."
    },
    "Janubiy Koreya": {
        "iso": "KOR", "yaim": "$1.7 Trln", "aholi": "51 Mln", "inflyatsiya": "2.6%", 
        "per_capita": "$33,100", "osish": 2.2, "valyuta": "Vona (KRW)",
       "sanoat": "Yarimo'tkazgichlar, Kema", "tavsif": "Dunyoning eng innovatsion texnologik markazlaridan biri."
    },
    "Avstraliya": {
        "iso": "AUS", "yaim": "$1.7 Trln", "aholi": "26 Mln", "inflyatsiya": "4.1%", 
        "per_capita": "$64,900", "osish": 2.1, "valyuta": "Avstraliya Dollari (AUD)", 
        "sanoat": "Oltin, Temir rudasi", "tavsif": "Resurslar eksporti va ta'lim xizmatlari bo'yicha yetakchi."
    },
    "Meksika": {
        "iso": "MEX", "yaim": "$1.8 Trln", "aholi": "128 Mln", "inflyatsiya": "4.7%", 
        "per_capita": "$13,900", "osish": 2.4, "valyuta": "Meksika Pesosi (MXN)", 
        "sanoat": "Avtomobil, Elektronika", "tavsif": "Shimoliy Amerika bilan kuchli savdo bog'liqligiga ega."
    },
    "Indoneziya": {
        "iso": "IDN", "yaim": "$1.4 Trln", "aholi": "277 Mln", "inflyatsiya": "2.8%", 
        "per_capita": "$4,900", "osish": 5.0, "valyuta": "Indoneziya Rupiyasi (IDR)", 
        "sanoat": "Palma yog'i, Ko'mir", "tavsif": "Janubiy-Sharqiy Osiyodagi eng yirik iqtisodiyot."
    },
    "Saudiya Arabistoni": {
        "iso": "SAU", "yaim": "$1.1 Trln", "aholi": "36 Mln", "inflyatsiya": "1.6%", 
        "per_capita": "$30,400", "osish": 4.2, "valyuta": "Saudiya Riali (SAR)", 
        "sanoat": "Neft, Gaz, Kimyo", "tavsif": "Dunyodagi eng yirik neft zaxiralariga ega davlat."
    },
    "Turkiya": {
        "iso": "TUR", "yaim": "$1.1 Trln", "aholi": "85 Mln", "inflyatsiya": "64.8%", 
        "per_capita": "$12,800", "osish": 3.0, "valyuta": "Turk Lirasi (TRY)", 
        "sanoat": "To'qimachilik, Oziq-ovqat", "tavsif": "Yevropa va Osiyo o'rtasidagi asosiy logistika markazi."
    },
    "Argentina": {
        "iso": "ARG", "yaim": "$632 Mlrd", "aholi": "46 Mln", "inflyatsiya": "211.4%", 
        "per_capita": "$13,700", "osish": -3.5, "valyuta": "Argentina Pesosi (ARS)", 
        "sanoat": "Go'sht mahsulotlari, Soya", "tavsif": "Janubiy Amerikadagi muhim qishloq xo'jaligi davlati."
    },
    "Janubiy Afrika": {
        "iso": "ZAF", "yaim": "$380 Mlrd", "aholi": "60 Mln", "inflyatsiya": "5.4%", 
        "per_capita": "$6,100", "osish": 1.6, "valyuta": "Rand (ZAR)", 
        "sanoat": "Platina, Oltin, Olmos", "tavsif": "Afrika qit'asining eng sanoatlashgan davlati."
    }
}

# 2. Sidebar va Tanlov
st.sidebar.title("🛠️ G20 Monitor")
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
    projection_type="orthographic", showocean=True, oceancolor="LightBlue",
    showcountries=True, countrycolor="white"
)
fig.update_layout(height=550, margin={"r":0,"t":20,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig, use_container_width=True)

# 4. Dinamik Ma'lumotlar Bloklari
st.markdown(f"## 📊 {selected_country}: Iqtisodiy Ko'rinish")
c = g20_data[selected_country]
st.info(c['tavsif'])

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

st.markdown(f"**Asosiy sanoat:** {c['sanoat']}")
