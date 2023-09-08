import streamlit as st

st.title("Weather Forcast App")
place = st.text_input("Enter a City")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Please slide for knowing more forecast dates")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} in {place}")
