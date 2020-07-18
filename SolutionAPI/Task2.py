import requests
import os

# for security reasons, the api key is stored in an environment variable
# instead of a variable here.
# please use your own api key to run this program

api_key = os.environ.get('task2_api_key')

# api_key = "YOUR_API_KEY"

URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

def writeQueryResult(query):
    urls = []
    PARAMS = {'q':query, 'api-key': api_key}
    response = requests.get(url = URL, params = PARAMS) 
    response_data = response.json()
    result = response_data['response']['docs']

    for obj in result:
        article_url = obj['web_url'] + " \n"
        urls.append(article_url)

    task_file = open("Task2.txt","w") 
    task_file.writelines(urls)

if __name__ == "__main__":
    writeQueryResult("Indigo")
    print("results written to ./Task2.txt")