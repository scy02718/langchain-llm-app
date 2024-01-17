from newsdataapi import NewsDataApiClient

"""# API key authorization, Initialize the client with your API key

api = NewsDataApiClient(apikey="pub_366235dffe4f1b254011a6776daa8c8d965e7")

# You can pass empty or with request parameters {ex. (country = "us")}

response = api.news_api( q= "ronaldo" , country = "us")
print(response)

with open("util/sources.txt", "w") as f:
    for result in response['results']:
        f.write(result['title'] + "\n")"""

with open("util/country_names.txt", "r") as f:
    country_names = f.read().splitlines()
    # Split by \t and first put first element as key and second element as value in dictionary
    country_dict = {}
    for country in country_names:
        country_dict[country.split("\t")[0]] = country.split("\t")[1]
    
    print(country_dict)