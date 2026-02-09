import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa sozlamalari
st.set_page_config(page_title="G20 & EI: To'liq Monitor", layout="wide")

# To'liq G20 va Yevropa Ittifoqi ma'lumotlar bazasi
g20_data = {
    "AQSH": {"iso": "USA", "yaim": "$27.9 Trln", "aholi": "340 Mln", "inflyatsiya": "3.1%", "per_capita": "$80,412", "osish": 2.1, "valyuta": "AQSH Dollari (USD)", "sanoat": "Moliya, Texnologiya", "trend": [2.3, -2.8, 5.9, 1.9, 2.5], "tavsif": "Dunyoning eng yirik iqtisodiyoti va global moliya markazi."},
    "Xitoy": {"iso": "CHN", "yaim": "$18.5 Trln", "aholi": "1.41 Mlrd", "inflyatsiya": "0.3%", "per_capita": "$13,136", "osish": 4.6, "valyuta": "Xitoy Yuani (CNY)", "sanoat": "Ishlab chiqarish, IT", "trend": [6.0, 2.2, 8.4, 3.0, 5.2], "tavsif": "Dunyoning ishlab chiqarish markazi va ikkinchi yirik iqtisodiyoti."},
    "Yevropa Ittifoqi": {"iso": "EUU", "yaim": "$18.3 Trln", "aholi": "448 Mln", "inflyatsiya": "2.4%", "per_capita": "$40,800", "osish": 1.0, "valyuta": "Yevro (EUR)", "sanoat": "Xizmat ko'rsatish, Sanoat", "trend": [1.8, -5.6, 5.6, 3.4, 0.6], "tavsif": "Yagona bozorga ega bo'lgan 27 ta davlatning iqtisodiy ittifoqi."},
    "Yaponiya": {"iso": "JPN", "yaim": "$4.2 Trln", "aholi": "125 Mln", "inflyatsiya": "2.5%", "per_capita": "$33,800", "osish": 1.0, "valyuta": "Yen (JPY)", "sanoat": "Robototexnika, Avtomobil", "trend": [-0.1, -4.1, 2.6, 1.0, 1.9], "tavsif": "Yuqori texnologiyalar va aniq muhandislik bo'yicha dunyo yetakchisi."},
    "Germaniya": {"iso": "DEU", "yaim": "$4.4 Trln", "aholi": "84 Mln", "inflyatsiya": "2.4%", "per_capita": "$52,824", "osish": 1.3, "valyuta": "Yevro (EUR)", "sanoat": "Mashinasozlik, Kimyo", "trend": [1.1, -3.8, 3.2, 1.8, -0.3], "tavsif": "Yevropaning iqtisodiy lokomotivi."},
    "Hindiston": {"iso": "IND", "yaim": "$3.9 Trln", "aholi": "1.43 Mlrd", "inflyatsiya": "5.1%", "per_capita": "$2,731", "osish": 6.8, "valyuta": "Hind Rupiyasi (INR)", "sanoat": "IT, Farmatsevtika", "trend": [3.9, -5.8, 9.1, 7.2, 7.8], "tavsif": "Dunyoning eng tez o'sayotgan yirik iqtisodiyoti."},
    "Buyuk Britaniya": {"iso": "GBR", "yaim": "$3.3 Trln", "aholi": "67 Mln", "inflyatsiya": "2.0%", "per_capita": "$49,100", "osish": 1.4, "valyuta": "Funt Sterling (GBP)", "sanoat": "Moliya, Bank", "trend": [1.6, -10.4, 8.7, 4.3, 0.1], "tavsif": "Global moliya va xizmat ko'rsatish markazi."},
    "Fransiya": {"iso": "FRA", "yaim": "$3.0 Trln", "aholi": "68 Mln", "inflyatsiya": "2.3%", "per_capita": "$44,400", "osish": 1.5, "valyuta": "Yevro (EUR)", "sanoat": "Aviatsiya, Hashamat", "trend": [1.8, -7.5, 6.4, 2.5, 0.9], "tavsif": "Yevropaning sanoat va turizm markazi."},
    "Italiya": {"iso": "ITA", "yaim": "$2.2 Trln", "aholi": "59 Mln", "inflyatsiya": "0.8%", "per_capita": "$37,700", "osish": 1.2, "valyuta": "Yevro (EUR)", "sanoat": "Moda, Mashina", "trend": [0.5, -9.0, 8.3, 3.9, 0.7], "tavsif": "Sifatli mahsulotlar va dizayn bo'yicha dunyo brendi."},
    "Braziliya": {"iso": "BRA", "yaim": "$2.3 Trln", "aholi": "217 Mln", "inflyatsiya": "3.8%", "per_capita": "$10,600", "osish": 2.2, "valyuta": "Braziliya Reali (BRL)", "sanoat": "Agrosanoat, Neft", "trend": [1.2, -3.3, 4.8, 3.0, 2.9], "tavsif": "Lotin Amerikasining eng yirik iqtisodiyoti."},
    "Kanada": {"iso": "CAN", "yaim": "$2.1 Trln", "aholi": "40 Mln", "inflyatsiya": "2.7%", "per_capita": "$52,700", "osish": 2.3, "valyuta": "Kanada Dollari (CAD)", "sanoat": "Energetika, Resurslar", "trend": [1.9, -5.0, 5.3, 3.8, 1.1], "tavsif": "Tabiiy resurslarga boy barqaror iqtisodiyot."},
    "Rossiya": {"iso": "RUS", "yaim": "$1.9 Trln", "aholi": "144 Mln", "inflyatsiya": "7.4%", "per_capita": "$13,200", "osish": 1.8, "valyuta": "Rossiya Rubli (RUB)", "sanoat": "Energetika, Metallurgiya", "trend": [2.2, -2.7, 5.9, -1.2, 3.6], "tavsif": "Eng yirik energiya manbalari eksportyori."},"Janubiy Koreya": {"iso": "KOR", "yaim": "$1.7 Trln", "aholi": "51 Mln", "inflyatsiya": "2.6%", "per_capita": "$33,100", "osish": 2.2, "valyuta": "Vona (KRW)", "sanoat": "Elektronika, Kema", "trend": [2.2, -0.7, 4.3, 2.6, 1.4], "tavsif": "Yuqori texnologiyalar markazi."},
    "Avstraliya": {"iso": "AUS", "yaim": "$1.7 Trln", "aholi": "26 Mln", "inflyatsiya": "4.1%", "per_capita": "$64,900", "osish": 2.1, "valyuta": "Avstraliya Dollari (AUD)", "sanoat": "Konchilik, Ta'lim", "trend": [1.9, -0.1, 5.2, 3.7, 2.0], "tavsif": "Resurslar eksporti bo'yicha yetakchi."},
    "Meksika": {"iso": "MEX", "yaim": "$1.8 Trln", "aholi": "128 Mln", "inflyatsiya": "4.7%", "per_capita": "$13,900", "osish": 2.4, "valyuta": "Meksika Pesosi (MXN)", "sanoat": "Avtomobil, Sanoat", "trend": [-0.3, -8.7, 5.8, 3.9, 3.2], "tavsif": "Shimoliy Amerika iqtisodiy hududining muhim bo'lagi."},
    "Indoneziya": {"iso": "IDN", "yaim": "$1.4 Trln", "aholi": "277 Mln", "inflyatsiya": "2.8%", "per_capita": "$4,900", "osish": 5.0, "valyuta": "Rupiya (IDR)", "sanoat": "Resurslar, Qishloq xo'jaligi", "trend": [5.0, -2.1, 3.7, 5.3, 5.0], "tavsif": "Janubi-Sharqiy Osiyoning iqtisodiy giganti."},
    "Saudiya Arabistoni": {"iso": "SAU", "yaim": "$1.1 Trln", "aholi": "36 Mln", "inflyatsiya": "1.6%", "per_capita": "$30,400", "osish": 4.2, "valyuta": "Saudiya Riali (SAR)", "sanoat": "Neft, Kimyo", "trend": [0.3, -4.1, 3.9, 8.7, -0.8], "tavsif": "Dunyodagi eng yirik neft zaxiralariga ega davlat."},
    "Turkiya": {"iso": "TUR", "yaim": "$1.1 Trln", "aholi": "85 Mln", "inflyatsiya": "64.8%", "per_capita": "$12,800", "osish": 3.0, "valyuta": "Turk Lirasi (TRY)", "sanoat": "To'qimachilik, Logistika", "trend": [0.8, 1.9, 11.4, 5.5, 4.5], "tavsif": "Yevropa va Osiyo o'rtasidagi iqtisodiy ko'prik."},
    "Argentina": {"iso": "ARG", "yaim": "$632 Mlrd", "aholi": "46 Mln", "inflyatsiya": "211.4%", "per_capita": "$13,700", "osish": -3.5, "valyuta": "Argentina Pesosi (ARS)", "sanoat": "Qishloq xo'jaligi", "trend": [-2.0, -9.9, 10.7, 5.0, -1.6], "tavsif": "Boy tabiiy resurslarga ega qishloq xo'jaligi davlati."},
    "Janubiy Afrika": {"iso": "ZAF", "yaim": "$380 Mlrd", "aholi": "60 Mln", "inflyatsiya": "5.4%", "per_capita": "$6,100", "osish": 1.6, "valyuta": "Rand (ZAR)", "sanoat": "Konchilik, Oltin", "trend": [0.3, -6.3, 4.7, 1.9, 0.6], "tavsif": "Afrika qit'asining sanoatlashgan iqtisodiyoti."}
}

# 2. Sidebar va Interfeys
st.sidebar.title("🛠️ G20 & EI Monitor")
selected_country = st.sidebar.selectbox("Davlat yoki Ittifoqni tanlang:", list(g20_data.keys()))

st.markdown(f"<h1 style='text-align: center;'>🌐 G20 & EI: Iqtisodiy Monitor</h1>", unsafe_allow_html=True)
st.markdown("---")

# 3. Globus (Ochiq ko'k okean)
fig_globe = go.Figure()
fig_globe.add_trace(go.Choropleth(
    locations=[v['iso'] for v in g20_data.values()],
    z=[v['osish'] for v in g20_data.values()],
    text=list(g20_data.keys()),
    colorscale="Viridis",
    marker_line_color='white',
    colorbar=dict(title="O'sish %", orientation='h', y=-0.2)
))

fig_globe.update_geos(
    projection_type="orthographic", showocean=True, oceancolor="LightBlue",
    showcountries=True, countrycolor="white"
)
fig_globe.update_layout(height=500, margin={"r":0,"t":0,"l":0,"b":0}, paper_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_globe, use_container_width=True)

# 4. Dinamik Ma'lumotlar Bloklari
st.markdown(f"### 📊 {selected_country}: Iqtisodiy Ko'rinish")
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
    st.metric("Valyuta", c['valyuta'])# 5. YaIM o'sish trendi diagrammasi
st.markdown("#### 📈 Oxirgi 5 yillik YaIM o'sish dinamikasi (%)")
yillar = [2019, 2020, 2021, 2022, 2023]
fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(x=yillar, y=c['trend'], mode='lines+markers', line=dict(color='#1f77b4', width=3), marker=dict(size=10)))
fig_trend.update_layout(xaxis=dict(tickmode='linear'), yaxis=dict(title='Foizda (%)'), height=300, margin=dict(l=20, r=20, t=30, b=20), paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")

st.plotly_chart(fig_trend, use_container_width=True)
st.markdown(f"Asosiy sanoat: {c['sanoat']}")
