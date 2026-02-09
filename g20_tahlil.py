import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# 1. Sahifa sozlamalari
st.set_page_config(page_title="G20 Davlatlari: To'liq Monitor", layout="wide")

# Ma'lumotlar bazasi (5 yillik o'sish trendi bilan)
g20_data = {
    "AQSH": {
        "iso": "USA", "yaim": "$27.9 Trln", "aholi": "340 Mln", "inflyatsiya": "3.1%", 
        "per_capita": "$80,412", "osish": 2.1, "valyuta": "AQSH Dollari (USD)", 
        "sanoat": "Moliya, Yuqori Texnologiya", 
        "trend": [2.3, -2.8, 5.9, 1.9, 2.5], # 2019-2023 yillar
        "tavsif": "AQSH dunyoning eng yirik iqtisodiyoti bo'lib, global moliya tizimining o'zagi hisoblanadi."
    },
    "Xitoy": {
        "iso": "CHN", "yaim": "$18.5 Trln", "aholi": "1.41 Mlrd", "inflyatsiya": "0.3%", 
        "per_capita": "$13,136", "osish": 4.6, "valyuta": "Xitoy Yuani (CNY)", 
        "sanoat": "Ishlab chiqarish, IT", 
        "trend": [6.0, 2.2, 8.4, 3.0, 5.2],
        "tavsif": "Xitoy dunyoning ikkinchi yirik iqtisodiyoti va eng yirik eksportyor davlatidir."
    },
    "Braziliya": {
        "iso": "BRA", "yaim": "$2.3 Trln", "aholi": "217 Mln", "inflyatsiya": "3.8%", 
        "per_capita": "$10,600", "osish": 2.2, "valyuta": "Braziliya Reali (BRL)", 
        "sanoat": "Qishloq xo'jaligi, Neft", 
        "trend": [1.2, -3.3, 4.8, 3.0, 2.9],
        "tavsif": "Braziliya Janubiy Amerikaning iqtisodiy yetakchisi bo'lib, tabiiy resurslarga juda boy."
    },
    "Germaniya": {
        "iso": "DEU", "yaim": "$4.4 Trln", "aholi": "84 Mln", "inflyatsiya": "2.4%", 
        "per_capita": "$52,824", "osish": 1.3, "valyuta": "Yevro (EUR)", 
        "sanoat": "Avtomobilsozlik, Mashinasozlik", 
        "trend": [1.1, -3.8, 3.2, 1.8, -0.3],
        "tavsif": "Germaniya Yevropaning iqtisodiy dvigateli va jahon muhandislik markazi hisoblanadi."
    },
    "Turkiya": {
        "iso": "TUR", "yaim": "$1.1 Trln", "aholi": "85 Mln", "inflyatsiya": "64.8%", 
        "per_capita": "$12,800", "osish": 3.0, "valyuta": "Turk Lirasi (TRY)", 
        "sanoat": "To'qimachilik, Qurilish", 
        "trend": [0.8, 1.9, 11.4, 5.5, 4.5],
        "tavsif": "Turkiya Yevropa va Osiyo chorrahasida joylashgan muhim sanoat va savdo markazidir."
    },
    "Hindiston": {
        "iso": "IND", "yaim": "$3.9 Trln", "aholi": "1.43 Mlrd", "inflyatsiya": "5.1%", 
        "per_capita": "$2,731", "osish": 6.8, "valyuta": "Hind Rupiyasi (INR)", 
        "sanoat": "IT, Farmatsevtika", 
        "trend": [3.9, -5.8, 9.1, 7.2, 7.8],
        "tavsif": "Hindiston dunyoning eng tez o'sayotgan yirik iqtisodiyotlaridan biri hisoblanadi."
    }
}

# 2. Sarlavha va Sidebar
st.markdown("<h1 style='text-align: center;'>🌐 G20 Davlatlari: Iqtisodiy Monitor</h1>", unsafe_allow_html=True)
st.markdown("---")

st.sidebar.header("🗺️ Boshqaruv Paneli")
selected_country = st.sidebar.selectbox("Davlatni tanlang:", list(g20_data.keys()))

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

# 4. Dinamik Ma'lumotlar Paneli (st.metric)
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
    st.metric("Valyuta", c['valyuta'])
# 5. YaIM o'sish trendi diagrammasi (YANGI QISM)
st.markdown("#### 📈 Oxirgi 5 yillik YaIM o'sish dinamikasi (%)")
yillar = [2019, 2020, 2021, 2022, 2023]
trend_data = pd.DataFrame({
    'Yil': yillar,
    'O\'sish (%)': c['trend']
})

fig_trend = go.Figure()
fig_trend.add_trace(go.Scatter(
    x=trend_data['Yil'], 
    y=trend_data['O\'sish (%)'],
    mode='lines+markers',
    line=dict(color='#1f77b4', width=3),
    marker=dict(size=10, symbol='circle'),
    name='O\'sish'
))

fig_trend.update_layout(
    xaxis=dict(tickmode='linear'),
    yaxis=dict(title='Foizda (%)'),
    margin=dict(l=20, r=20, t=30, b=20),
    height=300,
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.markdown(f"Asosiy sanoat tarmoqlari: {c['sanoat']}")
