import streamlit
import pandas

streamlit.title('My Parent New Healthy Diner')

streamlit.header('Braekfast Menu')
streamlit.text('sdfsdf')
streamlit.text('sdfsd')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

