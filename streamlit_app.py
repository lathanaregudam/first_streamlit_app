import streamlit
import pandas
streamlit.title('My Parents New Healthy Dinner for today')
streamlit.header('Lunch Favorites')
streamlit.text('Roti')
streamlit.text('Rice,Dal')
streamlit.text('curd')
streamlit.text('🍛 🥘 Rice, Pizza')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframes(my_fruit_list)
          
