# Grab all the news article using external API
# Summarize all the news article using Chat API
# Arbitarily determine the importance of the news article
# Display the news article in the order of importance

import streamlit as st
import util.googleAPI as lms
from newsdataapi import NewsDataApiClient

api = NewsDataApiClient(apikey="pub_366235dffe4f1b254011a6776daa8c8d965e7")

st.set_page_config(page_title="News Summarizer", page_icon="📰")
st.title("News Summarizer")
st.write(
    """This page is a demo of the News Summarizer. It is a tool that will 
    fetch the latest news from different sources, and determine the importance of each news article,
    summarize them and display them in the order of importance."""
)

# Keyword input
keyword_input = st.text_input("Enter the Keyword: eg. COVID-19")

with open("const/country_names.txt", "r") as f:
    country_names = f.read().splitlines()
    # Split by \t and first put first element as key and second element as value in dictionary
    country_dict = {}
    for country in country_names:
        country_dict[country.split("\t")[0]] = country.split("\t")[1]

# Multiselect for countries
selected_countries = st.multiselect(
    "Select the countries:", country_dict.keys(), 
    max_selections=5)

with open("const/category_names.txt", "r") as f:
    category_names = f.read().splitlines()

selected_categories = st.multiselect(
    "Select the categories:", category_names, 
    max_selections=5)

# Domain range Slider   
priority = st.slider("Select the domain ranges of the news. Higher the value, more narrower the range:", 0.0, 10.0, 5.0, step=0.1)

# Submit Button
if st.button("Submit"):
    country_codes = [country_dict[country] for country in selected_countries]
    category_codes = [category.lower() for category in selected_categories]

    if not country_codes:
        country_codes = None
    if not category_codes:
        category_codes = None
    
    if priority > 6.6:
        priority = "top"
    elif priority > 3.3:
        priority = "medium"
    else:
        priority = "low"
    
    response = api.news_api(q=keyword_input, country=country_codes, category=category_codes, prioritydomain=priority,
                            full_content=True)
    
    results = response['results']
    # Filter only the title, link and content
    results = [{'title': result['title'], 'link': result['link'], 'description': result['description']} for result in results]
    chat_result = lms.determine_importance(results)
    
    # Chat result will be a string of numbers separated by commas
    # Split the string by comma and convert each element to float

    importance_list = [float(importance) for importance in chat_result.split(",")]

    # Combine results, importance_list and summary_list
    results = [{'title': result['title'], 'link': result['link'], 'description': result['description'], 'importance': importance} for result, importance in zip(results, importance_list)]
    # Sort the results by importance
    results = sorted(results, key=lambda result: result['importance'], reverse=True)

    # For each result, display on screen inside a card
    for result in results:
        st.markdown(f"### {result['title']}")
        st.write(f"[Link]({result['link']})")
        st.write(result['description'])
        st.markdown("---")
    






