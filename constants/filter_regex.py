from telegram.ext import Filters


def vocabulary_regex(vocabulary_str):
    return Filters.regex('^' + vocabulary_str + '$')
