#!/usr/bin/env python3

def return_evens(num_list):
    even_num = [num for num in num_list if num % 2 == 0]
    return even_num


def make_exclamation(sentence_list):
    strings_with_exclamation_mark = [stri + "!" for stri in sentence_list]
    return strings_with_exclamation_mark

