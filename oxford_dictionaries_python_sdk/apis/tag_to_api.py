import typing_extensions

from oxford_dictionaries_python_sdk.apis.tags import TagValues
from oxford_dictionaries_python_sdk.apis.tags.utility_api import UtilityApi
from oxford_dictionaries_python_sdk.apis.tags.dictionary_entries_api import DictionaryEntriesApi
from oxford_dictionaries_python_sdk.apis.tags.thesaurus_api import ThesaurusApi
from oxford_dictionaries_python_sdk.apis.tags.lexi_stats_api import LexiStatsApi
from oxford_dictionaries_python_sdk.apis.tags.search_api import SearchApi
from oxford_dictionaries_python_sdk.apis.tags.wordlist_api import WordlistApi
from oxford_dictionaries_python_sdk.apis.tags.the_sentence_dictionary_api import TheSentenceDictionaryApi
from oxford_dictionaries_python_sdk.apis.tags.translation_api import TranslationApi
from oxford_dictionaries_python_sdk.apis.tags.lemmatron_api import LemmatronApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.UTILITY: UtilityApi,
        TagValues.DICTIONARY_ENTRIES: DictionaryEntriesApi,
        TagValues.THESAURUS: ThesaurusApi,
        TagValues.LEXI_STATS: LexiStatsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.WORDLIST: WordlistApi,
        TagValues.THE_SENTENCE_DICTIONARY: TheSentenceDictionaryApi,
        TagValues.TRANSLATION: TranslationApi,
        TagValues.LEMMATRON: LemmatronApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.UTILITY: UtilityApi,
        TagValues.DICTIONARY_ENTRIES: DictionaryEntriesApi,
        TagValues.THESAURUS: ThesaurusApi,
        TagValues.LEXI_STATS: LexiStatsApi,
        TagValues.SEARCH: SearchApi,
        TagValues.WORDLIST: WordlistApi,
        TagValues.THE_SENTENCE_DICTIONARY: TheSentenceDictionaryApi,
        TagValues.TRANSLATION: TranslationApi,
        TagValues.LEMMATRON: LemmatronApi,
    }
)
