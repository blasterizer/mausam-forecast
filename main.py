import streamlit as st
from plotly import express
from backend import get_data

# Add title, input text, slider and subheader
st.title("मौसम - Forecast App")
place = st.text_input("Enter a Country / City")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Please slide for knowing more forecast dates")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    try:
        # Get the temperature and the sky data
        filtered_data = get_data(place, days)

        # Create a temperature block
        if option == "Temperature":
            temperatures = [dict["main"]["temp"] for dict in filtered_data]
            dates = [dict["dt_txt"] for dict in filtered_data]
            figure = express.line(x=dates, y=temperatures, labels={"x": "Dates", "y": "Temperatures (C)"})
            st.plotly_chart(figure)

        if option == "Sky":
            images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                      "Rain": "images/rain.png", "Snow": "images/snow.png"}
            sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
            image_paths = [images[condition] for condition in sky_conditions]
            print(sky_conditions)
            st.image(image_paths, width=115)
    except KeyError:
        st.write("This place does not exist")


