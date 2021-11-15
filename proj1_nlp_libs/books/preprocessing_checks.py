logger.info(f'The raw length of this book as a string is {len(staircase.raw)}')
logger.info(f'This book has {len(staircase.clean)} chapters\n')
for i, chapter in enumerate(staircase.clean):
  if i == 5: break
  logger.info(f'{chapter[0]} - {chapter[1]}')
  logger.info(f'There are {len(chapter)} sentences in this chapter.')
  num_words = []
  for sent in chapter:
    num_words.append(len(sent.split(' ')))
  avg_words = np.mean(num_words)
  logger.info(f'The average sentence length in this chapter is {avg_words} words\n')

for i, sent in enumerate(staircase.get_chapter(33)):
  if i == 10: break
  logger.info(sent)

# Example of running it on all the books
processed_books = {}
for title, metadata in books.items():
  logger.nl()
  logger.info(f"Book: {title}", color='yellow', attrs=['underline'])
  current_book = ProcessedBook(title=title, metadata=metadata)
  # Raw length
  logger.info(f'The raw length of this book as a string is {len(current_book.raw)}')
  # Number of chapters
  logger.info(f'This book has {len(current_book.clean)} chapters\n')
  # Sententences per chapter
  for i, chapter in enumerate(current_book.clean):
    if i == 5: 
      break
    logger.info(f'{chapter[0]} - {chapter[1]}')
    logger.info(f'There are {len(chapter)} sentences in this chapter.')
    num_words = []
    for sent in chapter:
      num_words.append(len(sent.split(' ')))
    avg_words = np.mean(num_words)
    logger.info(f'The average sentence length in this chapter is {avg_words} words\n')
  # Chapter 15
  for i, sent in enumerate(lower_ten.get_chapter(15)):
    if i == 10: break
    logger.info(sent)
