import gensim.models
import gensim.downloader
import numpy as np
import pandas as pd
import itertools
from typing import *


def calculate_differing_distances(word_pairs: List[Tuple[str]],
                                  sentences: List[str] = None,
                                  model_names: List[str] = None):
    skipped_words = []
    vector_dimensions = [50, 100, 200, 300]
    window_dimensions = [2, 5, 3, 10]

    if model_names is not None:
        df = pd.DataFrame(
            columns=['word1', 'word2', 'model_name', 'cosineSim', 'dotSim'])
        for model_name in model_names:
            wv = get_model_wv(model_name)
            df = get_word_pair_distances(df=df, wv=wv, word_pairs=word_pairs,
                                         model_name=model_name, skipped_words=skipped_words)
    elif sentences is not None:
        df = pd.DataFrame(
            columns=['word1', 'word2', 'vectorSize', 'windowSize', 'cosineSim', 'dotSim'])
        for vector_size in vector_dimensions:
            for window_size in window_dimensions:
                model = gensim.models.Word2Vec(
                    sentences, vector_size=vector_size, window=window_size, min_count=2)
                df = get_word_pair_distances(df=df, wv=model.wv, word_pairs=word_pairs,
                                             vector_size=vector_size, window_size=window_size,
                                             skipped_words=skipped_words)
    else:
        raise Exception("You should either set `model` or `sentences`.")

    return df


def get_word_pair_distances(df: pd.DataFrame,
                            word_pairs: List[Tuple[str]],
                            wv: gensim.models.keyedvectors.KeyedVectors,
                            skipped_words: List[str],
                            vector_size: int = None,
                            window_size: int = None,
                            model_name: str = None) -> pd.DataFrame:
    for wordPair in word_pairs:
        cos_similarity = get_distance(wordPair[0], wordPair[1],
                                      wv, skipped_words, 'cosine')
        dot_similarity = get_distance(wordPair[0], wordPair[1],
                                      wv, skipped_words, 'dot')
        if cos_similarity is None or dot_similarity is None:
            continue
        if vector_size is not None:
            data = {
                "word1": wordPair[0],
                "word2": wordPair[1],
                "vectorSize": vector_size,
                "windowSize": window_size,
                "cosineSim": cos_similarity,
                "dotSim": dot_similarity,
            }
        elif model_name is not None:
            data = {
                "word1": wordPair[0],
                "word2": wordPair[1],
                "model_name": model_name,
                "cosineSim": cos_similarity,
                "dotSim": dot_similarity,
            }
        else:
            raise Exception("You should either set `model_name` or (`vector_size` and `window_size`)")

        df = df.append(data, ignore_index=True)

    return df


def get_model_names() -> List[str]:
    return list(gensim.downloader.info()['models'].keys())


def get_model_wv(name: str) -> gensim.models.keyedvectors.KeyedVectors:
    wv = gensim.downloader.load(name)

    return wv


def get_distance(word1, word2, wv, skipped_words: List[str], dist_type='cosine'):
    if word1 not in wv.index_to_key:
        if word1 not in skipped_words:
            print(f"{word1} not in vocabulary! Skipping..")
            skipped_words.append(word1)
        return None
    elif word2 not in wv.index_to_key:
        if word2 not in skipped_words:
            print(f"{word2} not in vocabulary! Skipping..")
            skipped_words.append(word2)
        return None
    else:
        distance = wv.similarity(word1, word2) if dist_type == 'cosine' \
            else np.dot(wv[word1], wv[word2])
        return distance


def get_conf_values(conf: Dict, keys: List[str], get_all_sub_values: bool,
                    ignore_words_with_spaces: bool) -> List[str]:
    for key in keys:
        conf = conf[key]
    if get_all_sub_values:
        return [val for val_list in conf
                for val in list(val_list.values())[0]
                if not (ignore_words_with_spaces and ' ' in val)]
    else:
        return [val for val in conf if not (ignore_words_with_spaces and ' ' in val)]


def get_combinations(conf: Dict, keys_1: List[str], keys_2: List[str],
                     get_all_sub_values_1: bool, get_all_sub_values_2: bool,
                     ignore_words_with_spaces: bool) -> List[Tuple[str, str]]:
    values_1 = get_conf_values(conf, keys_1, get_all_sub_values_1, ignore_words_with_spaces)
    values_2 = get_conf_values(conf, keys_2, get_all_sub_values_2, ignore_words_with_spaces)
    combinations = list(itertools.product(values_1, values_2))
    return combinations
