import streamlit as st

import data_app as da

import ml_app as ma



def main():
    # sidebar
    st.sidebar.subheader("Twitter US Airline Sentiment")
    st.sidebar.info("Analyze how travelers in February 2015 expressed their feelings on Twitter")
    user_menu = st.sidebar.radio('Select an Option',('Explore Tweets','Predict Tweet'))
    st.sidebar.success("Made by Sendrela Gulzar\nwith :heart:")

    if user_menu == 'Explore Tweets':
        # EDA
        da.main()

    if user_menu == 'Predict Tweet':
        # Predictor
        ma.main()



if(__name__ == '__main__'):
    main()
