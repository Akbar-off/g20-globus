import streamlit as st
import plotly.express as px
import pandas as pd

# Sahifa sozlamalari
st.set_page_config(page_title="G20 Iqtisodiy Monitori", layout="wide")

# O'zbekcha boyitilgan ma'lumotlar bazasi
data = {
    'Davlat': ['Argentina', 'Avstraliya', 'Braziliya', 'Kanada', 'Xitoy', 'Fransiya', 'Germaniya', 
               'Hindiston', 'Indoneziya', 'Italiya', 'Yaponiya', 'Meksika', 'Rossiya', 'Saudiya Arabistoni', 
               'Janubiy Afrika', 'Janubiy Koreya', 'Turkiya', 'Buyuk Britaniya', 'AQSH'],
    'YaIM': ['$632.8 mlrd', '$1.7 trln', '$2.1 trln', '$2.1 trln', '$18.5 trln', '$3.0 trln', '$4.4 trln', 
            '$3.9 trln', '$1.4 trln', '$2.2 trln', '$4.2 trln', '$1.8 trln', '$1.9 trln', '$1.1 trln', 
            '$380.9 mlrd', '$1.7 trln', '$1.1 trln', '$3.3 trln', '$27.9 trln'],
    'Aholi_soni': ['46 mln', '26 mln', '215 mln', '40 mln', '1.4 mlrd', '68 mln', '84 mln', 
                   '1.4 mlrd', '277 mln', '59 mln', '125 mln', '128 mln', '144 mln', '36 mln', 
                   '60 mln', '51 mln', '85 mln', '67 mln', '339 mln'],
    'Inflyatsiya': ['211.4%', '4.1%', '4.5%', '2.7%', '0.3%', '2.3%', '2.4%', 
                   '5.1%', '2.8%', '0.8%', '2.5%', '4.7%', '7.4%', '1.6%', 
                   '5.4%', '2.6%', '64.8%', '2.0%', '3.1%'],
    'Sanoati': ['Qishloq xo\'jaligi va oziq-ovqat', 'Konchilik va qishloq xo\'jaligi', 'Sanoat va xizmat ko\'rsatish', 
                'Energetika va xizmat ko\'rsatish', 'Ishlab chiqarish va texnologiya', 'Turizm va aviasozlik', 
                'Mashinasozlik va kimyo', 'Xizmat ko\'rsatish va qishloq xo\'jaligi', 'Tabiiy resurslar', 
                'Moda va avtomobilsozlik', 'Yuqori texnologiyalar va robototexnika', 'Avtomobilsozlik va neft', 
                'Energetika va harbiy sanoat', 'Neft va gaz sanoati', 'Konchilik va qishloq xo\'jaligi', 
                'Elektronika va kemasozlik', 'Tekstil va qurilish', 'Moliya va xizmat ko\'rsatish', 
                'Texnologiya va moliya'],
    'Osish_Surati': [3.5, 2.1, 2.2, 2.3, 4.6, 1.5, 1.3, 6.8, 5.0, 1.2, 1.0, 2.4, 1.8, 4.2, 1.6, 2.2, 3.0, 1.4, 2.1],
    'iso_alpha': ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'IDN', 'ITA', 'JPN', 'MEX', 'RUS', 'SAU', 'ZAF', 'KOR', 'TUR', 'GBR', 'USA']
}
df = pd.DataFrame(data)

# Sarlavha
st.title("🌐 G20 davlatlari")
st.markdown("---")

# Xaritani yaratish (Gradiyent rang bilan)
fig = px.choropleth(df, 
                    locations="iso_alpha", 
                    color="Osish_Surati", 
                    hover_name="Davlat",
                    hover_data={
                        'YaIM': True, 
                        'Aholi_soni': True, 
                        'Inflyatsiya': True, 
                        'Sanoati': True,
                        'Osish_Surati': ':.1f%'
                    },
                    color_continuous_scale="Viridis", 
                    projection="orthographic",
                    labels={'Osish_Surati': 'Iqtisodiy o\'sish'})

# Dizayn: Ochiq ko'k okean
fig.update_geos(
    showocean=True, oceancolor="LightBlue", 
    showcountries=True, countrycolor="white"
)

# Legendani (rang shkalasini) pastga gorizontal holatda qo'yish
fig.update_layout(
    height=750, 
    margin={"r":0,"t":50,"l":0,"b":100},
    coloraxis_colorbar=dict(
        title="Iqtisodiy o'sish (%)",
        thicknessmode="pixels", thickness=15,
        lenmode="pixels", len=350,
        yanchor="top", y=-0.05,
        xanchor="center", x=0.5,
        orientation="h"
    )
)

st.plotly_chart(fig, use_container_width=True)
