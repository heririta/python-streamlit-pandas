import pandas as pd 
import streamlit as st 


st.header("Create A Series Object From Python List")

st.write("---")
st.header("List [String]")

ice_cream = ["chocolate", "vanila","Strawberry", "Rum Raisin"]
st.write(ice_cream)
st.write(type(ice_cream))

ice_cream_series = pd.Series(ice_cream)
st.write(ice_cream_series)
st.write(type(ice_cream_series))

st.write("---")
st.header("List [Integer]")

lottery = [5, 7 , 8, 12, 16, 23]
st.write(lottery)
st.write(type(lottery))

lottery_series = pd.Series(lottery)
st.write(lottery_series)
st.write(type(lottery_series))

st.write("---")
st.header("List [Boolean]")

registrations = [True, False, False, True, False]
st.write(registrations)
st.write(type(registrations))

registrations_series = pd.Series(registrations)
st.write(registrations_series)
st.write(type(registrations_series))


