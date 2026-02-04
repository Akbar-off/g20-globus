import streamlit as st
import plotly.express as px
import pandas as pd

# Sahifa sozlamalari
st.set_page_config(page_title="G20 Bayroqlar Monitori", layout="wide")

# O'zbekcha ma'lumotlar va ranglar
data = {
    'Davlat': ['Argentina', 'Avstraliya', 'Braziliya', 'Kanada', 'Xitoy', 'Fransiya', 'Germaniya', 
               'Hindiston', 'Indoneziya', 'Italiya', 'Yaponiya', 'Meksika', 'Rossiya', 'Saudiya Arabistoni', 
               'Janubiy Afrika', 'Janubiy Koreya', 'Turkiya', 'Buyuk Britaniya', 'AQSH'],
    'YAIM': ['$632.8 mlrd', '$1.7 trln', '$2.1 trln', '$2.1 trln', '$18.5 trln', '$3.0 trln', '$4.4 trln', 
            '$3.9 trln', '$1.4 trln', '$2.2 trln', '$4.2 trln', '$1.8 trln', '$1.9 trln', '$1.1 trln', 
            '$380.9 mlrd', '$1.7 trln', '$1.1 trln', '$3.3 trln', '$27.9 trln'],
    'Bayroq_Rangi': ['#74ACDF', '#00008B', '#009739', '#FF0000', '#DE2910', '#002395', '#000000', 
                    '#FF9933', '#FF0000', '#009246', '#BC002D', '#006847', '#1C3578', '#006C35', 
                    '#007A4D', '#FFFFFF', '#E30A17', '#012169', '#B22234'],
    'iso_alpha': ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'IDN', 'ITA', 'JPN', 'MEX', 'RUS', 'SAU', 'ZAF', 'KOR', 'TUR', 'GBR', 'USA']
}
df = pd.DataFrame(data)

st.title("🌐 G20 Davlatlari: Bayroq Rangidagi Globus")
st.markdown("---")

# Xaritani yaratish
fig = px.choropleth(df, 
                    locations="iso_alpha", 
                    color="Davlat", 
                    hover_name="Davlat",
                    hover_data={'YAIM': True, 'Bayroq_Rangi': False, 'Davlat': False},
                    color_discrete_sequence=df['Bayroq_Rangi'], 
                    projection="orthographic")

# Dizaynni sozlash
fig.update_geos(
    showocean=True, oceancolor="#1a1a2e", 
    showcountries=True, countrycolor="white",
    lataxis_showgrid=False, lonaxis_showgrid=False # To'r chiziqlarini ham olib tashladik, yanada toza chiqadi
)

# Legendani olib tashlash va rang ko'rsatkichini yashirish
fig.update_layout(
    height=750, 
    margin={"r":0,"t":50,"l":0,"b":0},
    showlegend=False, # Legendani butunlay o'chiradi
    coloraxis_showscale=False # Agar rang shkalasi bo'lsa, uni ham yashiradi
)

st.plotly_chart(fig, use_container_width=True)
