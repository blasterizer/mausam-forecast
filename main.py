import streamlit as st
import plotly.express as px

st.title("Weather Forcast App")
place = st.text_input("Enter a City")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Please slide for knowing more forecast dates")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")


def get_data():
    temperatures = [10, 15, 20]
    dates = ["22-25-10", "22-26-10", "22-27-10"]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


d,t = get_data()

figure = px.line(x=d, y=t, labels={"x": "Dates", "y": "Temperatures (C)"})
st.plotly_chart(figure)


