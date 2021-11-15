other_suspects = [['gertrude innes', 'miss gertrude innes', 'miss gertrude', 'gertrude', 'miss innes', 'mis’ innes'],
                  ['john bailey', 'jack bailey', 'mr. bailey', 'bailey', 'alex', 'alexander graham'],
                  ['halsey innes', 'mr. halsey', 'halsey', 'mr. innes']]

dets_perp = [['mr. jamieson', 'mr. winters', 'detective', 'jamieson', 'winters'],
             ['anne watson', 'mrs. watson', 'mis’ watson']]

title, metadata = list(books.items())[0]
staircase = ProcessedBook(title=title, metadata=metadata)

suspects = get_earliest_chapter_sentence_from_name_lists(book, other_suspects, 3, first=True)
perp = get_earliest_chapter_sentence_from_name_lists(book, [dets_perp[1]], 3, first=True)
dets_list = [[alias for alias in dets_perp[0] if alias != 'detective']]
dets = get_earliest_chapter_sentence_from_name_lists(book, dets_list, 3, first=True)
co_ocs = get_co_occurence(book, dets_perp, n_sents=2)
