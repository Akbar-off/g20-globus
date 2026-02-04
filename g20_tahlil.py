import streamlit as st
import plotly.express as px
import pandas as pd

# Sahifa sozlamalari
st.set_page_config(page_title="G20 Bayroqdor Monitor", layout="wide")

# O'zbekcha ma'lumotlar va bayroq ranglari
data = {
    'Davlat': ['Argentina', 'Avstraliya', 'Braziliya', 'Kanada', 'Xitoy', 'Fransiya', 'Germaniya', 
               'Hindiston', 'Indoneziya', 'Italiya', 'Yaponiya', 'Meksika', 'Rossiya', 'Saudiya Arabistoni', 
               'Janubiy Afrika', 'Janubiy Koreya', 'Turkiya', 'Buyuk Britaniya', 'AQSH'],
    'YAIM_Nominal': ['$632.8 mlrd', '$1.7 trln', '$2.1 trln', '$2.1 trln', '$18.5 trln', '$3.0 trln', '$4.4 trln', 
                     '$3.9 trln', '$1.4 trln', '$2.2 trln', '$4.2 trln', '$1.8 trln', '$1.9 trln', '$1.1 trln', 
                     '$380.9 mlrd', '$1.7 trln', '$1.1 trln', '$3.3 trln', '$27.9 trln'],
    'Aholi_Soni': ['46 mln', '26 mln', '215 mln', '40 mln', '1.4 mlrd', '68 mln', '84 mln', 
                   '1.4 mlrd', '277 mln', '59 mln', '125 mln', '128 mln', '144 mln', '36 mln', 
                   '60 mln', '51 mln', '85 mln', '67 mln', '339 mln'],
    'Inflyatsiya': ['211.4%', '4.1%', '4.5%', '2.7%', '0.3%', '2.3%', '2.4%', 
                   '5.1%', '2.8%', '0.8%', '2.5%', '4.7%', '7.4%', '1.6%', 
                   '5.4%', '2.6%', '64.8%', '2.0%', '3.1%'],
    'Bayroq_Rangi': ['#74ACDF', '#00008B', '#009739', '#FF0000', '#DE2910', '#002395', '#000000', 
                    '#FF9933', '#FF0000', '#009246', '#BC002D', '#006847', '#1C3578', '#006C35', 
                    '#007A4D', '#FFFFFF', '#E30A17', '#012169', '#B22234'],
    'iso_alpha': ['ARG', 'AUS', 'BRA', 'CAN', 'CHN', 'FRA', 'DEU', 'IND', 'IDN', 'ITA', 'JPN', 'MEX', 'RUS', 'SAU', 'ZAF', 'KOR', 'TUR', 'GBR', 'USA']
}
df = pd.DataFrame(data)

st.title("🌐 G20 Iqtisodiy Monitor: Bayroq Ranglarida")
st.markdown("---")

# Interaktiv globus
fig = px.choropleth(df, 
                    locations="iso_alpha", 
                    color="Davlat", 
                    hover_name="Davlat",
                    hover_data={
                        'YAIM_Nominal': True, 
                        'Aholi_Soni': True, 
                        'Inflyatsiya': True,
                        'Bayroq_Rangi': False,
                        'Davlat': False
                    },
                    color_discrete_sequence=df['Bayroq_Rangi'],
                    projection="orthographic")

# Dizayn (Do'stingiznikidek ko'k okean bilan)
fig.update_geos(
    showocean=True, oceancolor="#1a1a2e",
    showcountries=True, countrycolor="white"
)

fig.update_layout(height=750, margin={"r":0,"t":50,"l":0,"b":0}, showlegend=False)

st.plotly_chart(fig, use_container_width=True)

# Pastki jadval
st.subheader("📊 Davlatlar haqida batafsil ma'lumot")
st.dataframe(df[['Davlat', 'YAIM_Nominal', 'Aholi_Soni', 'Inflyatsiya']], use_container_width=True)
