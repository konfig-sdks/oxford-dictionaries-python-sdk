# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from oxford_dictionaries_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DOMAINS_SOURCE_DOMAINS_LANGUAGE_TARGET_DOMAINS_LANGUAGE = "/domains/{source_domains_language}/{target_domains_language}"
    DOMAINS_SOURCE_LANGUAGE = "/domains/{source_language}"
    ENTRIES_SOURCE_LANGUAGE_WORD_ID_SENTENCES = "/entries/{source_language}/{word_id}/sentences"
    ENTRIES_SOURCE_LANG_WORD_ID = "/entries/{source_lang}/{word_id}"
    ENTRIES_SOURCE_LANG_WORD_ID_ANTONYMS = "/entries/{source_lang}/{word_id}/antonyms"
    ENTRIES_SOURCE_LANG_WORD_ID_REGIONSREGION = "/entries/{source_lang}/{word_id}/regions&#x3D;{region}"
    ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMS = "/entries/{source_lang}/{word_id}/synonyms"
    ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMSANTONYMS = "/entries/{source_lang}/{word_id}/synonyms;antonyms"
    ENTRIES_SOURCE_LANG_WORD_ID_FILTERS = "/entries/{source_lang}/{word_id}/{filters}"
    ENTRIES_SOURCE_TRANSLATION_LANGUAGE_WORD_ID_TRANSLATIONSTARGET_TRANSLATION_LANGUAGE = "/entries/{source_translation_language}/{word_id}/translations&#x3D;{target_translation_language}"
    FILTERS = "/filters"
    FILTERS_ENDPOINT = "/filters/{endpoint}"
    GRAMMATICAL_FEATURES_SOURCE_LANGUAGE = "/grammaticalFeatures/{source_language}"
    INFLECTIONS_SOURCE_LANG_WORD_ID_FILTERS = "/inflections/{source_lang}/{word_id}/{filters}"
    LANGUAGES = "/languages"
    LEXICALCATEGORIES_LANGUAGE = "/lexicalcategories/{language}"
    REGIONS_SOURCE_LANGUAGE = "/regions/{source_language}"
    REGISTERS_SOURCE_LANGUAGE = "/registers/{source_language}"
    REGISTERS_SOURCE_REGISTER_LANGUAGE_TARGET_REGISTER_LANGUAGE = "/registers/{source_register_language}/{target_register_language}"
    SEARCH_SOURCE_LANG = "/search/{source_lang}"
    SEARCH_SOURCE_SEARCH_LANGUAGE_TRANSLATIONSTARGET_SEARCH_LANGUAGE = "/search/{source_search_language}/translations&#x3D;{target_search_language}"
    WORDLIST_SOURCE_LANG_FILTERS_ADVANCED = "/wordlist/{source_lang}/{filters_advanced}"
    WORDLIST_SOURCE_LANG_FILTERS_BASIC = "/wordlist/{source_lang}/{filters_basic}"
    STATS_FREQUENCY_NGRAMS_SOURCE_LANG_CORPUS_NGRAMSIZE = "/stats/frequency/ngrams/{source_lang}/{corpus}/{ngram-size}"
    STATS_FREQUENCY_WORD_SOURCE_LANG = "/stats/frequency/word/{source_lang}"
    STATS_FREQUENCY_WORDS_SOURCE_LANG = "/stats/frequency/words/{source_lang}"
