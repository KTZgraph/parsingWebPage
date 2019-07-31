#coding=utf-8
from requests import get as request_GET
from collections import Counter
from bs4 import BeautifulSoup
from string import punctuation
from re import split as regex_split
import logging

class FrequencyKeywords:
    """Calculate Frequency of keywords in visible content of website.
        Similar to finding word (Ctrl+F) in webrowser but only for keywords from HTML meta tag.

    Args:
        url: (str) url of webiste.
        set_logger: default True,

    Attributes:
        url: (str)
        frequeny: (dict)
        status_code :(int)
    """
    def __init__(self, url, set_logger=True):
        """
        Dynamiczne tworzenie atrybutów klasy na podstawie słownika
        """
        if set_logger:
            self.set_logger()

        self.url = url
        self.frequency, self.status_code  = self.get_keywords_frequency(url)

    def set_logger(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel = logging.INFO #ustawianie poziomu logowania błedów
        self.file_handler = logging.FileHandler(self.__class__.__name__ + '.log') #nazwa pliku z logiem ma sie konczyć log
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        self.file_handler .setFormatter(formatter)

    @staticmethod
    def get_keywords_frequency(url):
        """Calculate Frequency of keywords from meta tag in visible HTML tags.
        Args:
            url: (str) url of webiste.
        Returns:
            frequeny: (dict) frequency of keywords from visible HTML tags.
            status_code : (int) status code from GET request on page 
        """
        CHUNK_SIZE = 8096
        UNVISIBLE_TAGS = [ "th", "td","strong","noscript","id", "iframe", "label", "br","class", "base","span" , "title", "button", 
        "script", "style", "ul", "small", "div", "meta", "nav", "time", "tbody", "tr", "body", "img", "code",  "form", "header",
         "pre", "input", "body", "section", "em", "td", "link", "fieldset", "blockquote"]
        keyword_counter = Counter()
        keywords = []
        status_code = None

        get_response = request_GET(url, stream=False) #stream dla dużych plików
        status_code = get_response.status_code
        for chunk in get_response.iter_content(CHUNK_SIZE):
            html = BeautifulSoup(chunk, 'html.parser')
            for elem in html.find_all(True, recursive=True): #wyciaganie danych pomiedzy tagami
                if elem.find('meta'): #wchozi tylko jesli nie ma ustawionych keywords
                    tmp_k = FrequencyKeywords.get_keywords_meta(elem)
                    if tmp_k:
                        keywords = tmp_k
                else:
                    if elem.name not in UNVISIBLE_TAGS:
                        key_words_list = FrequencyKeywords.get_keyword_list(elem.find(text=True, recursive = False), keywords)
                        if key_words_list:
                            keyword_counter.update(key_words_list)
                elem.extract()

        if not keywords:
            return {}, status_code
        
        frequency = {}
        for key, value in keyword_counter.items():
            if key in keywords:
                frequency[key] = value

        return frequency, status_code

    @staticmethod
    def get_keywords_meta(elem):
        """Returns list of words from HTML meta tag.
        Args:
            elem: 
        Returns:
            keywords: list of keywords webpage without duplicates.
        """
        web_keywords = elem.find('meta', attrs={'name': 'keywords'})
        if web_keywords:
            keywords_content = web_keywords.get("content")
            keywords = [ str(i).strip(punctuation).lower() for i in regex_split(";|,| ", keywords_content)] #split by , OR space
            return keywords

    @staticmethod
    def get_keyword_list(text, keywords=None):
        """Calculate Frequency of keywords from meta tag in visible HTML tags.
        Args:
            text: (str) text from HTML tag.
            keywords: (list) list of unique lower keywords from website. Default is None.
        Returns:
            word_list: (list) list of words which are in keywords arguments.
                if keyword is None return parsed list words from text argument.
        """
        if text:
            word_list = [str(i).strip(punctuation).lower() for i in text.split()]
            if keywords:
                key_list = list(filter(lambda x: x in keywords, word_list))
                return key_list
            return word_list

    def __str__(self):
        """
        Returns string of object frequency attribute.
        """
        if self.frequency:
            return '\n'.join([ str(k) + " : " + str(v) for k,v in  self.frequency.items()])
        else:
            return "{}"

if __name__ == "__main__":
    urls = []
    urls.append("https://www.python.org/")
    urls.append("https://www.google.pl/index.html") #brak
    urls.append("https://www.google.pl/") #brak
    urls.append("https://pl.wikipedia.org/") #brak
    urls.append("https://allegro.pl/") #brak
    urls.append("https://www.nazwa.pl/") #keywords po przecinku
    urls.append("https://www.onet.pl/")
    urls.append("https://www.wp.pl/")

    for url in urls:
        response_dict_obj = FrequencyKeywords(url)
        print("---------------------------------------------------")
        print(response_dict_obj)

