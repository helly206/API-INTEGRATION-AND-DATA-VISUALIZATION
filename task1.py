import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Add custom styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #83a4d4, #b6fbff);
    }
    .stMetric {
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 10px;
        padding: 15px;
        margin: 10px 0;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border-radius: 20px;
        padding: 10px 25px;
        font-size: 16px;
    }
    h1 {
        color: #1e3d59;
        text-align: center;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()

def main():
    st.title("🌤️ Weather Dashboard")
    
    api_key = "ea7001e8a20197e795db6fe1c0c7de87"
    
    cities = ["Mumbai", "Delhi", "Bangalore", "Surat", "Ahmedabad",
               "Rajkot", "Botad", "Jamnagar"]
    selected_city = st.selectbox("Select a city:", cities)
    
    if st.button("Get Weather"):
        with st.container():
            data = get_weather(selected_city, api_key)
            temp = data['main']['temp']
            st.header(f"Temperature in {selected_city}: {temp}°C")
            
            # Create temperature visualization
            temp_data = {
                'Metric': ['Current', 'Feels Like'],
                'Temperature': [temp, data['main']['feels_like']]
            }
            fig = px.bar(temp_data, x='Metric', y='Temperature',
                        title='Temperature Comparison',
                        color_discrete_sequence=['#1e88e5'])
            st.plotly_chart(fig)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.metric("Humidity", f"{data['main']['humidity']}%")
                st.metric("Wind Speed", f"{data['wind']['speed']} m/s")
            
            with col2:
                st.metric("Feels Like", f"{data['main']['feels_like']}°C")
                st.metric("Weather", data['weather'][0]['description'])

if __name__ == "__main__":
    main()
