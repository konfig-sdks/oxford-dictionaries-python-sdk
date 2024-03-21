import typing_extensions

from oxford_dictionaries_python_sdk.paths import PathValues
from oxford_dictionaries_python_sdk.apis.paths.domains_source_domains_language_target_domains_language import DomainsSourceDomainsLanguageTargetDomainsLanguage
from oxford_dictionaries_python_sdk.apis.paths.domains_source_language import DomainsSourceLanguage
from oxford_dictionaries_python_sdk.apis.paths.entries_source_language_word_id_sentences import EntriesSourceLanguageWordIdSentences
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id import EntriesSourceLangWordId
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id_antonyms import EntriesSourceLangWordIdAntonyms
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id_regionsregion import EntriesSourceLangWordIdRegionsregion
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id_synonyms import EntriesSourceLangWordIdSynonyms
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id_synonymsantonyms import EntriesSourceLangWordIdSynonymsantonyms
from oxford_dictionaries_python_sdk.apis.paths.entries_source_lang_word_id_filters import EntriesSourceLangWordIdFilters
from oxford_dictionaries_python_sdk.apis.paths.entries_source_translation_language_word_id_translationstarget_translation_language import EntriesSourceTranslationLanguageWordIdTranslationstargetTranslationLanguage
from oxford_dictionaries_python_sdk.apis.paths.filters import Filters
from oxford_dictionaries_python_sdk.apis.paths.filters_endpoint import FiltersEndpoint
from oxford_dictionaries_python_sdk.apis.paths.grammatical_features_source_language import GrammaticalFeaturesSourceLanguage
from oxford_dictionaries_python_sdk.apis.paths.inflections_source_lang_word_id_filters import InflectionsSourceLangWordIdFilters
from oxford_dictionaries_python_sdk.apis.paths.languages import Languages
from oxford_dictionaries_python_sdk.apis.paths.lexicalcategories_language import LexicalcategoriesLanguage
from oxford_dictionaries_python_sdk.apis.paths.regions_source_language import RegionsSourceLanguage
from oxford_dictionaries_python_sdk.apis.paths.registers_source_language import RegistersSourceLanguage
from oxford_dictionaries_python_sdk.apis.paths.registers_source_register_language_target_register_language import RegistersSourceRegisterLanguageTargetRegisterLanguage
from oxford_dictionaries_python_sdk.apis.paths.search_source_lang import SearchSourceLang
from oxford_dictionaries_python_sdk.apis.paths.search_source_search_language_translationstarget_search_language import SearchSourceSearchLanguageTranslationstargetSearchLanguage
from oxford_dictionaries_python_sdk.apis.paths.wordlist_source_lang_filters_advanced import WordlistSourceLangFiltersAdvanced
from oxford_dictionaries_python_sdk.apis.paths.wordlist_source_lang_filters_basic import WordlistSourceLangFiltersBasic
from oxford_dictionaries_python_sdk.apis.paths.stats_frequency_ngrams_source_lang_corpus_ngram_size import StatsFrequencyNgramsSourceLangCorpusNgramSize
from oxford_dictionaries_python_sdk.apis.paths.stats_frequency_word_source_lang import StatsFrequencyWordSourceLang
from oxford_dictionaries_python_sdk.apis.paths.stats_frequency_words_source_lang import StatsFrequencyWordsSourceLang

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DOMAINS_SOURCE_DOMAINS_LANGUAGE_TARGET_DOMAINS_LANGUAGE: DomainsSourceDomainsLanguageTargetDomainsLanguage,
        PathValues.DOMAINS_SOURCE_LANGUAGE: DomainsSourceLanguage,
        PathValues.ENTRIES_SOURCE_LANGUAGE_WORD_ID_SENTENCES: EntriesSourceLanguageWordIdSentences,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID: EntriesSourceLangWordId,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_ANTONYMS: EntriesSourceLangWordIdAntonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_REGIONSREGION: EntriesSourceLangWordIdRegionsregion,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMS: EntriesSourceLangWordIdSynonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMSANTONYMS: EntriesSourceLangWordIdSynonymsantonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_FILTERS: EntriesSourceLangWordIdFilters,
        PathValues.ENTRIES_SOURCE_TRANSLATION_LANGUAGE_WORD_ID_TRANSLATIONSTARGET_TRANSLATION_LANGUAGE: EntriesSourceTranslationLanguageWordIdTranslationstargetTranslationLanguage,
        PathValues.FILTERS: Filters,
        PathValues.FILTERS_ENDPOINT: FiltersEndpoint,
        PathValues.GRAMMATICAL_FEATURES_SOURCE_LANGUAGE: GrammaticalFeaturesSourceLanguage,
        PathValues.INFLECTIONS_SOURCE_LANG_WORD_ID_FILTERS: InflectionsSourceLangWordIdFilters,
        PathValues.LANGUAGES: Languages,
        PathValues.LEXICALCATEGORIES_LANGUAGE: LexicalcategoriesLanguage,
        PathValues.REGIONS_SOURCE_LANGUAGE: RegionsSourceLanguage,
        PathValues.REGISTERS_SOURCE_LANGUAGE: RegistersSourceLanguage,
        PathValues.REGISTERS_SOURCE_REGISTER_LANGUAGE_TARGET_REGISTER_LANGUAGE: RegistersSourceRegisterLanguageTargetRegisterLanguage,
        PathValues.SEARCH_SOURCE_LANG: SearchSourceLang,
        PathValues.SEARCH_SOURCE_SEARCH_LANGUAGE_TRANSLATIONSTARGET_SEARCH_LANGUAGE: SearchSourceSearchLanguageTranslationstargetSearchLanguage,
        PathValues.WORDLIST_SOURCE_LANG_FILTERS_ADVANCED: WordlistSourceLangFiltersAdvanced,
        PathValues.WORDLIST_SOURCE_LANG_FILTERS_BASIC: WordlistSourceLangFiltersBasic,
        PathValues.STATS_FREQUENCY_NGRAMS_SOURCE_LANG_CORPUS_NGRAMSIZE: StatsFrequencyNgramsSourceLangCorpusNgramSize,
        PathValues.STATS_FREQUENCY_WORD_SOURCE_LANG: StatsFrequencyWordSourceLang,
        PathValues.STATS_FREQUENCY_WORDS_SOURCE_LANG: StatsFrequencyWordsSourceLang,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DOMAINS_SOURCE_DOMAINS_LANGUAGE_TARGET_DOMAINS_LANGUAGE: DomainsSourceDomainsLanguageTargetDomainsLanguage,
        PathValues.DOMAINS_SOURCE_LANGUAGE: DomainsSourceLanguage,
        PathValues.ENTRIES_SOURCE_LANGUAGE_WORD_ID_SENTENCES: EntriesSourceLanguageWordIdSentences,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID: EntriesSourceLangWordId,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_ANTONYMS: EntriesSourceLangWordIdAntonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_REGIONSREGION: EntriesSourceLangWordIdRegionsregion,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMS: EntriesSourceLangWordIdSynonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_SYNONYMSANTONYMS: EntriesSourceLangWordIdSynonymsantonyms,
        PathValues.ENTRIES_SOURCE_LANG_WORD_ID_FILTERS: EntriesSourceLangWordIdFilters,
        PathValues.ENTRIES_SOURCE_TRANSLATION_LANGUAGE_WORD_ID_TRANSLATIONSTARGET_TRANSLATION_LANGUAGE: EntriesSourceTranslationLanguageWordIdTranslationstargetTranslationLanguage,
        PathValues.FILTERS: Filters,
        PathValues.FILTERS_ENDPOINT: FiltersEndpoint,
        PathValues.GRAMMATICAL_FEATURES_SOURCE_LANGUAGE: GrammaticalFeaturesSourceLanguage,
        PathValues.INFLECTIONS_SOURCE_LANG_WORD_ID_FILTERS: InflectionsSourceLangWordIdFilters,
        PathValues.LANGUAGES: Languages,
        PathValues.LEXICALCATEGORIES_LANGUAGE: LexicalcategoriesLanguage,
        PathValues.REGIONS_SOURCE_LANGUAGE: RegionsSourceLanguage,
        PathValues.REGISTERS_SOURCE_LANGUAGE: RegistersSourceLanguage,
        PathValues.REGISTERS_SOURCE_REGISTER_LANGUAGE_TARGET_REGISTER_LANGUAGE: RegistersSourceRegisterLanguageTargetRegisterLanguage,
        PathValues.SEARCH_SOURCE_LANG: SearchSourceLang,
        PathValues.SEARCH_SOURCE_SEARCH_LANGUAGE_TRANSLATIONSTARGET_SEARCH_LANGUAGE: SearchSourceSearchLanguageTranslationstargetSearchLanguage,
        PathValues.WORDLIST_SOURCE_LANG_FILTERS_ADVANCED: WordlistSourceLangFiltersAdvanced,
        PathValues.WORDLIST_SOURCE_LANG_FILTERS_BASIC: WordlistSourceLangFiltersBasic,
        PathValues.STATS_FREQUENCY_NGRAMS_SOURCE_LANG_CORPUS_NGRAMSIZE: StatsFrequencyNgramsSourceLangCorpusNgramSize,
        PathValues.STATS_FREQUENCY_WORD_SOURCE_LANG: StatsFrequencyWordSourceLang,
        PathValues.STATS_FREQUENCY_WORDS_SOURCE_LANG: StatsFrequencyWordsSourceLang,
    }
)
