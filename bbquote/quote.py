import requests

def get_quote():

    url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
    response = requests.get(url).json()[0]

    return response['quote'], response['author']

if __name__ == '__main__':
    quote, author = get_quote()
    print(f'"{quote}" \n>{author}')
