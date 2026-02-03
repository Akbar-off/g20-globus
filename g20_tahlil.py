import streamlit as st
import pandas as pd
import plotly.express as px

# Sahifa sozlamalari
st.set_page_config(page_title="G20 Global Globus", layout="wide")

st.title("🌍 G20 Davlatlari: Global Iqtisodiy Globus")
st.write("Sichqoncha yordamida globusni aylantiring!")

# G20 ma'lumotlari va bayroq emojilari
data = {
    'Country': ['United States 🇺🇸', 'China 🇨🇳', 'Japan 🇯🇵', 'Germany 🇩🇪', 'India 🇮🇳', 
                'United Kingdom 🇬🇧', 'France 🇫🇷', 'Italy 🇮🇹', 'Brazil 🇧🇷', 'Canada 🇨🇦', 
                'Russia 🇷🇺', 'South Korea 🇰🇷', 'Australia 🇦🇺', 'Mexico 🇲🇽', 
                'Indonesia 🇮🇩', 'Saudi Arabia 🇸🇦', 'Turkey 🇹🇷', 'Argentina 🇦🇷', 'South Africa 🇿🇦'],
    'ISO_Code': ['USA', 'CHN', 'JPN', 'DEU', 'IND', 'GBR', 'FRA', 'ITA', 'BRA', 'CAN', 
                 'RUS', 'KOR', 'AUS', 'MEX', 'IDN', 'SAU', 'TUR', 'ARG', 'ZAF'],
    'GDP_Billions': [27360, 18530, 4210, 4450, 3930, 3340, 3030, 2250, 2130, 2140, 
                     2020, 1760, 1740, 1810, 1470, 1110, 1100, 650, 380]
}

df = pd.DataFrame(data)

# Shar (Globus) ko'rinishidagi xarita
fig = px.choropleth(df, 
                    locations="ISO_Code",
                    color="GDP_Billions",
                    hover_name="Country",
                    # Davlatlarni yorqinroq (bayroq ranglariga yaqinroq) bo'yash
                    color_continuous_scale="Viridis",
                    projection="orthographic") # Globus shakli

fig.update_geos(
    showcountries=True, 
    countrycolor="Gold", # Chegaralarni oltin rangda qilish
    showocean=True, 
    oceancolor="MidnightBlue", # Ummonni to'q ko'k qilish
    showlakes=True, 
    lakecolor="Aqua"
)

fig.update_layout(
    height=700, 
    margin={"r":0,"t":50,"l":0,"b":0},
    paper_bgcolor="black", # Orqa fonni qora qilish (koinot effekti)
    font_color="white"
)

st.plotly_chart(fig, use_container_width=True)