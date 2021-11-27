import json
from pathlib import Path
import time
from transformers import DistilBertTokenizerFast
from transformers import DistilBertForQuestionAnswering
import torch
from torch.utils.data import DataLoader
from transformers import AdamW


## Extracted from hugging face documentation
def read_squad(path):
    path = Path(path)
    with open(path, 'rb') as f:
        squad_dict = json.load(f)

    contexts = []
    questions = []
    answers = []
    for group in squad_dict['data']:
        for passage in group['paragraphs']:
            context = passage['context']
            for qa in passage['qas']:
                question = qa['question']
                for answer in qa['answers']:
                    contexts.append(context)
                    questions.append(question)
                    answers.append(answer)

    return contexts, questions, answers


def add_end_idx(answers, contexts):
    for answer, context in zip(answers, contexts):
        gold_text = answer['text']
        start_idx = answer['answer_start']
        end_idx = start_idx + len(gold_text)

        # sometimes squad answers are off by a character or two – fix this
        if context[start_idx:end_idx] == gold_text:
            answer['answer_end'] = end_idx
        elif context[start_idx-1:end_idx-1] == gold_text:
            answer['answer_start'] = start_idx - 1
            # When the gold label is off by one character
            answer['answer_end'] = end_idx - 1
        elif context[start_idx-2:end_idx-2] == gold_text:
            answer['answer_start'] = start_idx - 2
            # When the gold label is off by two characters
            answer['answer_end'] = end_idx - 2

## Next we need to convert our character start/end positions to token start/end positions.
## When using 🤗 Fast Tokenizers, we can use the built in char_to_token() method.


def add_token_positions(encodings, answers, tokenizer):
    start_positions = []
    end_positions = []
    for i in range(len(answers)):
        start_positions.append(encodings.char_to_token(
            i, answers[i]['answer_start']))
        end_positions.append(encodings.char_to_token(
            i, answers[i]['answer_end'] - 1))

        # if start position is None, the answer passage has been truncated
        if start_positions[-1] is None:
            start_positions[-1] = tokenizer.model_max_length
        if end_positions[-1] is None:
            end_positions[-1] = tokenizer.model_max_length

    encodings.update({'start_positions': start_positions,
                      'end_positions': end_positions})


class SquadDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings.input_ids)

def run_epochs(model, train_loader, optim, device, epochs=3):
    starttime = time.time()
    for epoch in range(epochs):
        e_starttime = time.time()
        for batch in train_loader:
            optim.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            start_positions = batch['start_positions'].to(device)
            end_positions = batch['end_positions'].to(device)
            outputs = model(input_ids, attention_mask=attention_mask,
                            start_positions=start_positions, end_positions=end_positions)
            loss = outputs[0]
            loss.backward()
            optim.step()
            b_end = time.time()
        e_endtime = time.time()

        print("Epoch Time: ", e_endtime - e_starttime, flush=True)
    endtime = time.time()
    print('Total time: ', endtime-starttime)
    model.eval()


def read_and_extract_train_val_data(train_path, test_path, question_contexts, questions, answers, num_epochs=3): 
    print("Loading data")
    train_contexts, train_questions, train_answers = read_squad(train_path)
    val_contexts, val_questions, val_answers = read_squad(test_path)

    add_end_idx(train_answers, train_contexts)
    add_end_idx(val_answers, val_contexts)

    print("Tokenizing")
    tokenizer = DistilBertTokenizerFast.from_pretrained(
        'distilbert-base-uncased')

    train_encodings = tokenizer(train_contexts, train_questions, truncation=True, padding=True)
    val_encodings = tokenizer(val_contexts, val_questions,truncation=True, padding=True)

    print("Adding Token Positions")
    add_token_positions(train_encodings, train_answers, tokenizer)
    add_token_positions(val_encodings, val_answers, tokenizer)

    print("Converting to Torch Data")
    train_dataset = SquadDataset(train_encodings)
    val_dataset = SquadDataset(val_encodings)

    print("Creating Model")
    model = DistilBertForQuestionAnswering.from_pretrained("distilbert-base-uncased")
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

    print("Using Device: ", device)
    model.to(device)
    model.train()

    print("Creating Train Loader")
    train_loader = DataLoader(train_dataset, batch_size=16, shuffle=True)
    optim = AdamW(model.parameters(), lr=5e-5)

    print("Training")
    run_epochs(model, train_loader, optim, device, num_epochs)

    return model, tokenizer
