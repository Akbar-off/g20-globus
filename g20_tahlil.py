import streamlit as st
import plotly.express as px
import pandas as pd

# Sahifa sozlamalari
st.set_page_config(page_title="G20 Iqtisodiy Monitor", layout="wide")

# O'zbekcha ma'lumotlar
data = {
    'Davlat': ['Argentina', 'Avstraliya', 'Braziliya', 'Kanada', 'Xitoy', 'Fransiya', 'Germaniya', 
               'Hindiston', 'Indoneziya', 'Italiya', 'Yaponiya', 'Meksika', 'Rossiya', 'Saudiya Arabistoni', 
               'Janubiy Afrika', 'Janubiy Koreya', 'Turkiya', 'Buyuk Britaniya', 'AQSH'],
    'YAIM': ['$632.8 mlrd', '$1.7 trln', '$2.1 trln', '$2.1 trln', '$18.5 trln', '$3.0 trln', '$4.4 trln', 
            '$3.9 trln', '$1.4 trln', '$2.2 trln', '$4.2 trln', '$1.8 trln', '$1.9 trln', '$1.1 trln', 
            '$380.9 mlrd', '$1.7 trln', '$1.1 trln', '$3.3 trln', '$27.9 trln'],
    'Osish_Surati': [3.5, 2.1, 2.2, 2.3, 4.6, 1.5, 1.3, 6.8, 5.0, 1.2, 1.0, 2.4, 1.8, 4.2, 1.6, 2.2, 3.0, 1.4, 2.1],
    'iso_alpha': ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'IDN', 'ITA', 'JPN', 'MEX', 'RUS', 'SAU', 'ZAF', 'KOR', 'TUR', 'GBR', 'USA']
}
df = pd.DataFrame(data)

st.title("🌐 G20 Iqtisodiy Monitori")
st.markdown("---")

# Xaritani yaratish (Gradiyent rang bilan)
fig = px.choropleth(df, 
                    locations="iso_alpha", 
                    color="Osish_Surati", # O'sib boruvchi rang
                    hover_name="Davlat",
                    hover_data={'YAIM': True, 'Osish_Surati': ':.1f%'},
                    color_continuous_scale="Viridis", # Gradiyent shkalasi
                    projection="orthographic",
                    labels={'Osish_Surati': 'O\'sish'})

# Dizaynni sozlama (Ochiq ko'k okean)
fig.update_geos(
    showocean=True, oceancolor="LightBlue", # Ochiq ko'k okean
    showcountries=True, countrycolor="white"
)

# Legendani pastga qo'yish
fig.update_layout(
    height=750, 
    margin={"r":0,"t":50,"l":0,"b":50},
    coloraxis_colorbar=dict(
        title="O'sish (%)",
        thicknessmode="pixels", thickness=15,
        lenmode="pixels", len=300,
        yanchor="top", y=-0.1, # Pastga tushirish
        xanchor="center", x=0.5, # Markazga qo'yish
        orientation="h" # Gorizontal ko'rinish
    )
)

st.plotly_chart(fig, use_container_width=True)
