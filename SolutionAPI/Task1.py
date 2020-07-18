import requests
import os

# for security reasons, the api key is stored in an environment variable
# instead of a variable here.
# please use your own api key to run this program

api_key = os.environ.get('task1_api_key')

# api_key = "YOUR_API_KEY"

URL = "http://newsapi.org/v2/everything"

def getQueryResult(query, date):
    news = []
    if (date is None):
        PARAMS = {'q':query, 'apiKey': api_key} 
    else:
        PARAMS = {'q':query, 'from': date, 'apiKey': api_key}
    response = requests.get(url = URL, params = PARAMS) 
    response_data = response.json()
    result = response_data['articles']
    
    if (len(result) > 10):
        news = result[0:10]
    else:
        news = result
    return news

def getSourceResult(sources, date):
    news = []
    if (date is None):
        PARAMS = {'sources':sources, 'apiKey': api_key} 
    else:
        PARAMS = {'sources':sources, 'from': date, 'apiKey': api_key}
    response = requests.get(url = URL, params = PARAMS) 
    response_data = response.json()
    result = response_data['articles']
    
    if (len(result) > 10):
        news = result[0:10]
    else:
        news = result
    return news

def getDateResult():
    pass

if __name__ == "__main__":
    while(True):
        print("Choose an option:")
        print("1. Query")
        print("2. Source")
        print("3. Exit")
        choice = int(input())
        if(choice == 1):
            print("Enter query:")
            query = input()
            print("Select date (Y/N)")
            date_bool = input()
            if (date_bool.lower() == "y"):
                # The free plan according to my API key plan permits me to request articles as far back as 2020-06-17.
                # Please check yours before making the query.
                print("Enter date in YYYY-MM-DD format:")
                date = input()
                result = getQueryResult(query, date)
            else:
                result = getQueryResult(query, None)
            print(result)
        elif(choice == 2):
            print("Enter source:")
            query = input()
            print("Select date (Y/N)")
            date_bool = input()
            if (date_bool.lower() == "y"):
                # The free plan according to my API key plan permits me to request articles as far back as 2020-06-17.
                # Please check yours before making the query.
                print("Enter date in YYYY-MM-DD format:")
                date = input()
                result = getSourceResult(query, date)
            else:
                result = getSourceResult(query, None)
            print(result)
        elif(choice == 3):
            break
        else:
            print("Invalid input")