from typing import *
from itertools import groupby
# Hugging face
from transformers import pipeline
from tqdm import tqdm, tqdm_notebook

nlp = pipeline("question-answering")


def ask_question(question: str, sentences: List[str], window: int, max_words: int = 512) -> List[Dict]:
    print("Total number of sentences: ", len(sentences))
    answers = []
    window_splits = tqdm(list(enumerate(sentences))[::window])
    inner_ind = 0
    previous_block = [None]
    for ind, _ in window_splits:
        description = f"Start index {ind}, end index {ind + inner_ind} ({inner_ind} sents used)."
        description += f" Current length of text block: {previous_block[0]}"
        window_splits.set_description(description)
        current_block = [0, '']
        for inner_ind, sentence in enumerate(sentences[ind:]):
            previous_block = current_block.copy()
            current_block[0] += len(sentence.split(' '))
            current_block[1] += ' ' + sentence
            if current_block[0] > max_words:
                answer = nlp(question=question, context=previous_block[1])
                answers.append(answer)
                break
    return answers


def get_sorted_grouped_answers(answers: List[Dict]):
    group_key = lambda item: item['answer']
    sort_key = lambda item: item['mean_score']
    answers = sorted(answers, key=group_key)

    mean_score_answers = []
    for key, values in groupby(answers, group_key):
        values = list(values)
        sum_score = 0.0
        for val in values:
            sum_score += val['score']
        avg_score = sum_score / len(values)
        mean_score_answers.append({"answer": key, "mean_score": avg_score})

    return sorted(mean_score_answers, key=sort_key, reverse=True)
