from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

def analysis(sentence):


    MODEL = f"cardiffnlp/twitter-roberta-base-sentiment"
    tokenizer=AutoTokenizer.from_pretrained(MODEL)
    model=AutoModelForSequenceClassification.from_pretrained(MODEL)

    encoded_text=tokenizer(sentence, return_tensors='pt')
    output = model(**encoded_text)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    scores_dict = {
        'neg' : scores[0],
        'neu' : scores[1],
        'pos' : scores[2]
    }
    return(scores_dict)