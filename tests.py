"""
Unitests for class FrequencyKeywords
"""
import unittest
from bs4 import BeautifulSoup

try:
    from parameterized import expand
except ModuleNotFoundError:
    print("Tu")
    from my_parametrized import expand

from frequency import FrequencyKeywords
import validate_url


class TestFrequencyKeywords(unittest.TestCase):
    """
    python -m unittest
    """
    # @dekorator
    # def test_valid_url(self):
    #     WebKeyWordCounter("https://www.google.com/")

    web_keywords = ["https://www.python.org/", "https://www.nazwa.pl/" ]
    web_non_existing = ["https://www.google.pl/index.html", ]
    web_no_keywords = ["https://allegro.pl/", "https://www.onet.pl/", "https://www.wp.pl/"]
    url_values = [
        [ "https://www.nazwa.pl/", 
            {
                "nazwa.pl" : 6,
                "poczta" : 1,
                "hosting" : 4,
                "ssl" : 7,
                "darmowe" : 1,
                "domen" : 1,
                "www" : 9,
                "certyfikaty" : 1  
            }
        ],
        ["https://www.wp.pl",
            {}
        ],
        [ "https://allegro.pl/",
            {}
        ],
        ["https://www.onet.pl/",
            {}
        ]
    ]

    html = [
        ["<h1>test tekst</h1>", ['test', 'tekst']],
        ["<a><h1>test tekst</h1></a>", []],
        ["<dfg>fdfdg</dfg>", []]
    ]


    # def test_get_keywords_frequency(self):
    #     """
    #     Should return non empty frequence value
    #     """
    #     for url in self.web_keywords:
    #         result = FrequencyKeywords.get_keywords_frequency(url)
    #         self.assertTrue(result[0]) # result[0])

    # def test_returned_value(self):
    #     for elem in self.url_values:
    #         response_dict =  FrequencyKeywords.get_keywords_frequency(elem[0])[0]
    #         self.assertEqual(elem[1], response_dict)
    
    # def test_get_keyword_list(self):
    #     """
    #     Calculate Frequency of keywords from meta tag in visible HTML tags
    #     """
    #     string_values = [
    #         [ "Ala ma kota.", ["kot"], [] ],
    #         [ "Ala   {}   kot,  345, 34534, rere, 67. 20-20", ["kot", "ala", "rere", "45543"], ["ala", "kot", "rere"] ],
    #         ["1234,  34, 34;34;3 Hello-WoRld", ["hello-world", "1234", "34"], ["1234", "34", "hello-world" ]],
    #         ["python-proggraming", ["python"], [] ],
    #         ["empty 23 key word list", [], ["empty", "23", "key", "word" ,"list"] ],
    #         ["not empty 23 key word list", ["Empty", "23y", "kEy", "wOrd" ,"liSt"], []  ]
    #     ]
    #     for arg in string_values:
    #         result = FrequencyKeywords.get_keyword_list(arg[0], arg[1])
    #         self.assertEqual(result, arg[2])

    def test_get_keywords_meta(self):
        result = []
        for test_html in self.html:
            soup = BeautifulSoup(test_html,'html.parser')
            for elem in soup.find_all(True, recursive=True): #wyciaganie danych pomiedzy tagami
                key_words_list = FrequencyKeywords.get_keyword_list(elem.find(text=True, recursive = False))
                print(key_words_list)



class TestValidationUrl(unittest.TestCase):
    borken_urls = ["https://www.wp.pl", "https://www.wp./","https://www..pl/", "https://.wp.pl/"]
    wrong_type_urls = [None, 123, bytearray('sdfsfdsdf'.encode('utf-8'))]

    @expand([])
    def test_valid_url(self):
        pass
    
    @expand([[1,2], [3,4]])
    def test_invalid_url(self):
        pass
    
    @expand([[1,2], [3,4]])
    def test_validate_url_type(self):
        pass

    @expand([[1,2], [3,4]])
    def test_incomplete_url(self):
        pass
