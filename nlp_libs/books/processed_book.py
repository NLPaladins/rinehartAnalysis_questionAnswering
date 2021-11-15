import urllib.request
import re
from typing import *
from nlp_libs.fancy_logger.colorized_logger import ColorizedLogger
import spacy
import string

nlp = spacy.load('en_core_web_sm')


# logger = ColorizedLogger(logger_name='Process Book', color='cyan')

class ProcessedBook:
    protagonists: Dict
    antagonists: Dict
    crime_weapon: Dict
    crime_objects: Dict

    def __init__(self, metadata: Dict):
        """
        raw is a Project Gutenberg dump
        clean_text is a single string with some preprocessing
        lemmas is lemmatized with some more preprocessing
        """
        self.protagonists = metadata['protagonists']
        self.antagonists = metadata['antagonists']
        self.crime_weapon = metadata['crime']['crime_weapon']
        self.crime_objects = metadata['crime']['crime_objects']

        self.raw = self.read_book_from_proj_gut(metadata['url'])
        self.book_lines = self.get_book_lines_from_raw()
        self.clean_lines = self.clean_lines()
        # change from list of lines to string for spacy
        self.clean_text = ' '.join(self.clean_lines).replace('  ', ' ')
        self.lemmas = self.lemmatize()

    @staticmethod
    def read_book_from_proj_gut(book_url: str) -> str:
        req = urllib.request.Request(book_url)
        client = urllib.request.urlopen(req)
        page = client.read()
        return page.decode('utf-8')

    def get_book_lines_from_raw(self):
        raw = re.sub(r'\r\n', r'\n', self.raw)
        lines = re.findall(r'.*\n', raw)
        start = False
        text = []
        for i, line in enumerate(lines):
            # match chapters for book start and for 
            # removing chapter headers and titles
            if re.search(r'^ *((CHAPTER|Chapter) [A-Z]+\.?)\n$', line) or re.search(
                    r'^ *[IVXLCDM]+\.?\n$', line):
                start = True
                chapter_start = True
                continue
            if start:
                if not chapter_start:
                    # check for book end
                    if re.search(r'project gutenberg', line, re.IGNORECASE):
                        break
                    else:
                        text.append(line)
                else:
                    # removing chapter titles if they are there
                    if re.search(r'^([A-Z] ?)+$', line):
                        chapter_start = False
                    if re.search(r'[a-z]+', line):
                        text.append(line)
                        chapter_start = False
        return text

    def clean_lines(self):
        clean_lines = []
        for line in self.book_lines:
            line = re.sub(r'([’‘])', '', line)
            if self.pass_clean_filter(line):
                clean_lines.append(line)
        return clean_lines

    @staticmethod
    def pass_clean_filter(line: str) -> bool:
        if re.search(r'^((\[illustration:)|(illustration:))', line, re.IGNORECASE):
            return False
        if re.search('^[\* ]*\n$', line):
            return False
        else:
            return True

    def lemmatize_by_sentence(self, word_subs=None):
        lemmasWpunct = self.lemmatize(remove_punctuation=False, word_subs=word_subs)
        bySentence = ' '.join(lemmasWpunct).split(".")
        punctuation = string.punctuation

        sentenceList = []

        for sentence in bySentence:
            wordlist = []
            words = sentence.split(' ')
            for word in words:
                if word not in punctuation:
                    wordlist.append(word)

            sentenceList.append(wordlist)

        return sentenceList

    def lemmatize(self, lower=True, remove_stopwords=False, remove_punctuation=True, word_subs=None):
        # if word_subs is not None, it is expecting the format
        # ([word1, word2, ...], word_to_sub_to), where the list
        # of words in the tuple are words to change and where
        # word_to_sub_to is the word to change them to
        punctuation = string.punctuation
        text = self.clean_text
        text = re.sub(r'\u2014', ' ', text)
        if lower:
            text = text.lower()
        if word_subs:
            text = self.substitute_words_to_word(text, word_subs)
        text = nlp(text)
        lemmas = []
        for word in text:
            lemma = word.lemma_.strip()
            if lemma:
                if not remove_stopwords or (remove_stopwords and lemma not in lemmas):
                    if remove_punctuation:
                        if lemma not in punctuation:
                            lemmas.append(lemma)
                    else:
                        lemmas.append(lemma)
        return lemmas

    def substitute_words_to_word(self, text, word_subs):
        words_to_sub, word_sub = word_subs
        for word in words_to_sub:
            text = re.sub(word, word_sub, text)
        return text
