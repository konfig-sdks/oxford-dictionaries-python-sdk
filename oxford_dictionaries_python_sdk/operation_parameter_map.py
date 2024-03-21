operation_parameter_map = {
    '/entries/{source_lang}/{word_id}/{filters}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
            {
                'name': 'filters'
            },
        ]
    },
    '/entries/{source_lang}/{word_id}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/entries/{source_lang}/{word_id}/regions={region}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
            {
                'name': 'region'
            },
        ]
    },
    '/inflections/{source_lang}/{word_id}/{filters}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'filters'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/stats/frequency/ngrams/{source_lang}/{corpus}/{ngram-size}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'corpus'
            },
            {
                'name': 'ngram-size'
            },
            {
                'name': 'tokens'
            },
            {
                'name': 'contains'
            },
            {
                'name': 'punctuation'
            },
            {
                'name': 'format'
            },
            {
                'name': 'minFrequency'
            },
            {
                'name': 'maxFrequency'
            },
            {
                'name': 'minDocumentFrequency'
            },
            {
                'name': 'maxDocumentFrequency'
            },
            {
                'name': 'collate'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/stats/frequency/words/{source_lang}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'corpus'
            },
            {
                'name': 'wordform'
            },
            {
                'name': 'trueCase'
            },
            {
                'name': 'lemma'
            },
            {
                'name': 'lexicalCategory'
            },
            {
                'name': 'grammaticalFeatures'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'collate'
            },
            {
                'name': 'minFrequency'
            },
            {
                'name': 'maxFrequency'
            },
            {
                'name': 'minNormalizedFrequency'
            },
            {
                'name': 'maxNormalizedFrequency'
            },
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/stats/frequency/word/{source_lang}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'corpus'
            },
            {
                'name': 'wordform'
            },
            {
                'name': 'trueCase'
            },
            {
                'name': 'lemma'
            },
            {
                'name': 'lexicalCategory'
            },
        ]
    },
    '/search/{source_lang}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'q'
            },
            {
                'name': 'prefix'
            },
            {
                'name': 'regions'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/search/{source_search_language}/translations={target_search_language}-GET': {
        'parameters': [
            {
                'name': 'source_search_language'
            },
            {
                'name': 'target_search_language'
            },
            {
                'name': 'q'
            },
            {
                'name': 'prefix'
            },
            {
                'name': 'regions'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/entries/{source_language}/{word_id}/sentences-GET': {
        'parameters': [
            {
                'name': 'source_language'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/entries/{source_lang}/{word_id}/antonyms-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/entries/{source_lang}/{word_id}/synonyms-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/entries/{source_lang}/{word_id}/synonyms;antonyms-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'word_id'
            },
        ]
    },
    '/entries/{source_translation_language}/{word_id}/translations={target_translation_language}-GET': {
        'parameters': [
            {
                'name': 'source_translation_language'
            },
            {
                'name': 'word_id'
            },
            {
                'name': 'target_translation_language'
            },
        ]
    },
    '/grammaticalFeatures/{source_language}-GET': {
        'parameters': [
            {
                'name': 'source_language'
            },
        ]
    },
    '/lexicalcategories/{language}-GET': {
        'parameters': [
            {
                'name': 'language'
            },
        ]
    },
    '/domains/{source_domains_language}/{target_domains_language}-GET': {
        'parameters': [
            {
                'name': 'source_domains_language'
            },
            {
                'name': 'target_domains_language'
            },
        ]
    },
    '/filters-GET': {
        'parameters': [
        ]
    },
    '/languages-GET': {
        'parameters': [
            {
                'name': 'sourceLanguage'
            },
            {
                'name': 'targetLanguage'
            },
        ]
    },
    '/registers/{source_register_language}/{target_register_language}-GET': {
        'parameters': [
            {
                'name': 'source_register_language'
            },
            {
                'name': 'target_register_language'
            },
        ]
    },
    '/filters/{endpoint}-GET': {
        'parameters': [
            {
                'name': 'endpoint'
            },
        ]
    },
    '/domains/{source_language}-GET': {
        'parameters': [
            {
                'name': 'source_language'
            },
        ]
    },
    '/regions/{source_language}-GET': {
        'parameters': [
            {
                'name': 'source_language'
            },
        ]
    },
    '/registers/{source_language}-GET': {
        'parameters': [
            {
                'name': 'source_language'
            },
        ]
    },
    '/wordlist/{source_lang}/{filters_advanced}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'filters_advanced'
            },
            {
                'name': 'exclude'
            },
            {
                'name': 'exclude_senses'
            },
            {
                'name': 'exclude_prime_senses'
            },
            {
                'name': 'word_length'
            },
            {
                'name': 'prefix'
            },
            {
                'name': 'exact'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/wordlist/{source_lang}/{filters_basic}-GET': {
        'parameters': [
            {
                'name': 'source_lang'
            },
            {
                'name': 'filters_basic'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
};