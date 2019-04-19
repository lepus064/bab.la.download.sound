import requests
from argparse import ArgumentParser

def download_svenska(word):
    url = "https://en.bab.la/dictionary/swedish-english/"+word
    data = requests.get(url)
    num = data.text.find('sound-inline bab-quick-sound')
    if(num == -1):
        print("The word is missing.")
    else:
        print('found')
        start = data.text.find(',',num)
        end = data.text.find(',', start+1)
        file_num = data.text[start+1:end]
        r = requests.get('https://en.bab.la/sound/swedish/'+file_num+'.mp3')
        with open(word + '.mp3', 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("word", help="The word you wnat to find")
    args = parser.parse_args()
    download_svenska(args.word)