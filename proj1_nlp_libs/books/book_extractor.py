import re
from typing import *
import numpy as np
from nlp_libs.fancy_logger.colorized_logger import ColorizedLogger
from .processed_book import ProcessedBook

logger = ColorizedLogger(logger_name='Book Extractor', color='yellow')


def createNamedDictionary(personList):
    personList.sort(key=len, reverse=True)
    name_dictionary = {}
    hasKey = False

    for potential_name_key in personList:
        title = re.findall(r'^(?:Mr\.|Mrs\.|Miss|Doctor)', potential_name_key)
        name_split_no_title = re.findall(r'(?!Mr\.|Mrs\.|Miss|Doctor)[A-Z][a-z]+', potential_name_key)
        original_length_no_title = len(name_split_no_title)

        if len(name_split_no_title) > 1:
            surname = name_split_no_title[1]
            name_split_no_title = [name_split_no_title[0]]

        print(len(name_split_no_title))
        print(name_split_no_title)
        for name in personList:
            if name in name_dictionary.keys() or (len(name_dictionary.values()) > 0 and
                                                  name in np.concatenate(
                        list(name_dictionary.values()))):
                print("Continuing on ", name)
                continue

            if re.match(fr".*({'|'.join(name_split_no_title)}).*", name):
                #                 print('\t ',re.match(fr".*({'|'.join(name_split_no_title)}).*", name))

                if original_length_no_title == 1:
                    continue

                if len(name) > len(potential_name_key):
                    raise ("This shouldn't happen with the way the sorting works")
                else:
                    if potential_name_key not in name_dictionary.keys() and name not in name_dictionary.keys():
                        print('\t Key:', potential_name_key, "\t\t Value: ", potential_name_key, )
                        name_dictionary[potential_name_key] = [potential_name_key]
                    elif potential_name_key in name_dictionary.keys():
                        print('\t Key:', potential_name_key, "\t\t Value: ", name)
                        print('\tt name_split_no_title: ', name_split_no_title)
                        if re.match(fr'.*(?!{surname}).*$', name) and len(name_split_no_title) == len(
                                re.findall(r'(?!Mr\.|Mrs\.|Miss|Doctor)[A-Z][a-z]+', name)):
                            print('\t\t >>>>>>>>>>>. SURNAME DOES NOT MATCH!!!')
                            print('\t\t >>>>>>>>>>>.potential_name_key, name')

                        name_dictionary[potential_name_key] = [
                            *name_dictionary[potential_name_key],
                            name
                        ]

                    #                     print('key: ', potential_name_key, '\tvalue', potential_name_key)
                #                     name_dictionary[potential_name_key] = [ potential_name_key ]
                continue

    return name_dictionary


def extract_surnames(unique_person_list):
    surname_list = []
    # first pass: go through, get break of first / lasts
    for name in unique_person_list:
        name_split_no_title = re.findall(r'(?!Mr\.|Mrs\.|Miss|Doctor)[A-Z][a-z]+', name)
        surname = '' if len(name_split_no_title) <= 1 else name_split_no_title[1]

        if surname != '' and surname:
            surname_list.append(surname)

    return set(surname_list)


def obtain_aliases_for_book(unique_person_list):
    unique_person_list.sort(key=len, reverse=True)
    alias_dictionary = {}
    title_regex = r'^(?:Mr\.|Mrs\.|Miss|Doctor)'
    name_with_no_title_regex = r'(?!Mr\.|Mrs\.|Miss|Doctor|Aunt)[A-Z][a-z]+'
    surnames = extract_surnames(unique_person_list)

    for personIdx in range(len(unique_person_list)):
        if len(alias_dictionary.keys()) == 0:
            alias_dictionary[unique_person_list[personIdx]] = [unique_person_list[personIdx]]

        comparator_person = unique_person_list[personIdx]
        title_comparator_person = re.findall(title_regex, comparator_person)
        name_split_no_title_comparator_person = re.findall(name_with_no_title_regex, comparator_person)

        if len(alias_dictionary.values()) > 0 and comparator_person in list(
                np.concatenate(list(alias_dictionary.values()))):
            continue
        #         print(comparator_person)
        #         print(title_comparator_person, name_split_no_title_comparator_person)

        if len(name_split_no_title_comparator_person) == 0:
            #         raise('ZERO? ', comparator_person, name_split_no_title_comparator_person)
            continue
        surname_comparator_person = '' if len(name_split_no_title_comparator_person) <= 1 else \
            name_split_no_title_comparator_person[1]
        first_name_comparator_person = name_split_no_title_comparator_person[0]

        for next_person_index in range(personIdx, len(unique_person_list)):
            next_person = unique_person_list[next_person_index]
            title_next_person = re.findall(title_regex, next_person)
            name_split_no_title_next_person = re.findall(name_with_no_title_regex, next_person)

            if len(name_split_no_title_next_person) == 0:
                #                 print(f'NEXT PERSON ZERO:{next_person} ')
                continue

            if comparator_person == next_person:
                alias_dictionary[comparator_person] = [comparator_person]
                #                 print("COnTINUING BECAUSE ADDED STUFF")
                continue

            surname_next_person = '' if len(name_split_no_title_next_person) <= 1 else \
                name_split_no_title_next_person[1]
            first_name_next_person = name_split_no_title_next_person[0]

            #             print('\t\t',next_person)
            #             print('\t\t',title_next_person, name_split_no_title_next_person, f'SURNAME {len(name_split_no_title_next_person)} {surname_next_person}')

            if first_name_next_person in surnames:
                #                 print("\t::::::::NAME IN SURNAMES::::::::", title_next_person, name_split_no_title_next_person)
                continue

            if first_name_comparator_person == first_name_next_person and len(
                    first_name_next_person) > 0:

                ### SURNAME CHECK GOES HERE *** NEED TO MAKE ABSOLUTELY SURE:
                if surname_comparator_person != '' and surname_next_person == '':
                    alias_dictionary[comparator_person] = [*alias_dictionary[comparator_person],
                                                           next_person]
                    continue

                if surname_comparator_person != '' and surname_next_person != '' and surname_comparator_person != surname_next_person:
                    continue

                #                 print("\t\t**********WHOOOOOP**********************",len(first_name_next_person), first_name_next_person, first_name_comparator_person)
                alias_dictionary[comparator_person] = [*alias_dictionary[comparator_person],
                                                       next_person]
                continue
    return alias_dictionary


def get_dictionary_of_named_occurrences(character_progression):
    namecount = {}
    for chapter in character_progression:
        for line in chapter:
            for element in line:
                if element not in namecount.keys():
                    namecount[element] = 1
                else:
                    namecount[element] = namecount[element] + 1

    sorted_dict = {}
    for key_value in sorted(namecount.items(), key=lambda x: x[1], reverse=True):
        sorted_dict[key_value[0]] = key_value[1]
    return sorted_dict


def create_alias_occurrence_dictionary(aliases, named_occurrences):
    new_named_occurrences = {}
    for key in aliases.keys():
        for named_occurrence in named_occurrences.keys():
            if named_occurrence in aliases[key]:
                key_exists = key in new_named_occurrences.keys()
                occurrences = named_occurrences[named_occurrence]
                new_named_occurrences[key] = occurrences if not key_exists else new_named_occurrences[
                                                                                    key] + occurrences

    return new_named_occurrences


def get_earliest_chapter_sentence_from_name_lists(book, name_lists, n=0, first=True):
    '''
    Takes in a list of lists, where
    each list in this list of lists is a
    list of aliases for a single character.

    Returns a dictionary with character names
    as keys and a list with chapter number as
    the first element and sentence number as the
    second element.
    '''
    first_mentioned = {}
    for aliases in name_lists:
        alias_matcher = '|'.join(aliases)
        found_match = False
        for chapter_num, chapter in enumerate(book.clean_lower):
            for sent_num, sentence in enumerate(chapter[2:]):
                match = re.search(alias_matcher, sentence)
                if match:
                    if not found_match:
                        first_mentioned[aliases[0]] = [chapter_num + 1, sent_num + 1, []]
                    found_match = True
                    if n > 0:
                        words = get_n_words(book, alias_matcher, chapter_num, sent_num, n)
                        first_mentioned[aliases[0]][-1].append(words)
                    if first:
                        break
            if first and found_match:
                break

    return first_mentioned


def get_n_words(book, alias_matcher, chapter_num, sent_num, n):
    sents = '. '.join(book.clean_lower[chapter_num][sent_num + 1: sent_num + 4])
    words = re.search(
        '((?:\S+ ){0,' + str(n) + '}\S?(?:' + alias_matcher + ')\S?(?: \S+){0,' + str(n) + '})',
        sents).group(0)
    return words


def get_co_occurence(book, name_lists, n_sents=2):
    assert len(name_lists) == 2
    mentions_a, mentions_b = {}, {}
    dets, perp = name_lists[0], name_lists[1]
    dets_matcher = '|'.join(dets)
    perp_matcher = '|'.join(perp)
    for chapter_num, chapter in enumerate(book.clean_lower):
        mentions_a[chapter_num] = []
        mentions_b[chapter_num] = []
        for sent_num, sentence in enumerate(chapter[2:]):
            match_a = re.search(dets_matcher, sentence)
            match_b = re.search(perp_matcher, sentence)
            if match_a:
                mentions_a[chapter_num].append(sent_num)
            if match_b:
                mentions_b[chapter_num].append(sent_num)
    co_occurences = []
    for chapter_a, sent_nums_a in mentions_a.items():
        for chapter_b, sent_nums_b in mentions_b.items():
            if chapter_a == chapter_b:
                for sent_num_a in sent_nums_a:
                    for sent_num_b in sent_nums_b:
                        if sent_num_a > sent_num_b and sent_num_a - sent_num_b <= n_sents:
                            sents = book.clean_lower[chapter_a][2:][sent_num_b:sent_num_a + 1]
                            co_occurences.append([chapter_a, sent_num_b, sent_num_a, sents])
                        if sent_num_b > sent_num_a and sent_num_b - sent_num_a <= n_sents:
                            sents = book.clean_lower[chapter_a][2:][sent_num_a:sent_num_b + 1]
                            co_occurences.append([chapter_a, sent_num_a, sent_num_b, sents])
    return co_occurences


def get_analysis_formats(metadata):
    suspects, perp, dets, co_ocs, crime = [], [], [], [], []

    for aliases in metadata['suspects']:
        for _, values in aliases.items():
            suspects.append(values)

    for aliases in metadata['perpetrator']:
        for _, values in aliases.items():
            perp.append(values)
            co_ocs.append(values)

    for aliases in metadata['detectives']:
        for _, values in aliases.items():
            dets.append(values)
            co_ocs.append(values)

    dets = [[alias for alias in dets[0] if alias != 'detective']]

    return suspects, perp, dets, co_ocs, crime


def get_crime_mentions(book: ProcessedBook, crime_words: List[str],
                       p_lookaheads: List[str] = None,
                       print_instances: bool = False) -> List[Tuple[int, int]]:
    """
    Takes a list of crime words and positive lookaheads, and looks for sentences that match.
    :param book:
    :param crime_words:
    :param p_lookaheads:
    :param print_instances:
    :return: A list of (chapter_ind, sentence_ind)

    Usage Example
    crime_mentions = get_crime_mentions(book=staircase,
                                        crime_words=crime_words,
                                        p_lookaheads=p_lookaheads,
                                        print_instances=True)
    """

    # Create Regex for the crime words
    crime_words_linked = '|'.join(crime_words)
    reg_exp = rf'(?:.*\s(?:{crime_words_linked}).*)'
    # Create Positive lookaheads
    if p_lookaheads:
        p_lookaheads_linked = ''.join(f"(?={look})" for look in p_lookaheads)
    else:
        p_lookaheads_linked = ''
    reg_exp = rf'(^.*{p_lookaheads_linked}{reg_exp}$)'
    logger.info(f"Regex: {reg_exp}", attrs=['underline'])
    # Get all sentences that match any of these words
    indexes = []
    for chapter_ind, chapter in enumerate(book.clean):
        for line_ind, line in enumerate(chapter):
            if re.match(reg_exp, line, re.IGNORECASE):
                indexes.append((chapter_ind, line_ind))

    if print_instances:
        logger.info("The crime words were mentioned in the following instances:")
        for index in indexes:
            logger.info(f"Chapter: {index[0]}, Sentence: {index[1]}")
            logger.info(f"{book.clean[index[0]][index[1]]}", color='cyan')

    return indexes


def get_crime_details(book: ProcessedBook, crime_mentions: List[Tuple[int, int]], max_dist: int,
                      left_margin: int = 0, right_margin: int = 2) -> Tuple[str, List[int]]:
    """
    Takes a list of crime mentions links sentences around mentions that are close to the first one.
    :param book:
    :param crime_mentions:
    :param max_dist:
    :param left_margin:
    :param right_margin:
    :return: The crime details as a string

    Usage Example
    crime_details, indices = get_crime_details(book=staircase,
                                               crime_mentions=crime_mentions,
                                               max_dist=10,
                                               left_margin=0,
                                               right_margin=2,)
    """

    def get_close_mentions(mentions):
        """ Keep only close mentions. Everytime you find a mention,
        recalculate the index of the mention. """
        closest_mention_sentence = first_mention_sentence
        _close_mentions = []
        for mention in mentions:
            if mention[1] - closest_mention_sentence <= max_dist:
                _close_mentions.append(mention)
                closest_mention_sentence = mention[1]
        return _close_mentions

    (first_mention_chapter, first_mention_sentence) = crime_mentions[0]
    # Get all mentions that are in the same chapter as the first mention
    mentions_in_same_chapter = list(filter(lambda mention: mention[0] == first_mention_chapter,
                                           crime_mentions))
    # Get all mentions from same chapter that are within "max_dist" distance
    close_mentions_idx = get_close_mentions(mentions_in_same_chapter)
    # Link the mentions
    close_mentions_range = range(close_mentions_idx[0][1] - left_margin,
                                 close_mentions_idx[-1][1] + 1 + right_margin)
    close_mentions = [book.clean[first_mention_chapter][mention] for mention in close_mentions_range]
    crime_details = '. '.join(close_mentions)

    return crime_details, close_mentions_idx
