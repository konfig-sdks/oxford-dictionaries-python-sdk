# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from oxford_dictionaries_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    UTILITY = "Utility"
    DICTIONARY_ENTRIES = "Dictionary entries"
    THESAURUS = "Thesaurus"
    LEXI_STATS = "LexiStats"
    SEARCH = "Search"
    WORDLIST = "Wordlist"
    THE_SENTENCE_DICTIONARY = "The Sentence Dictionary"
    TRANSLATION = "Translation"
    LEMMATRON = "Lemmatron"
