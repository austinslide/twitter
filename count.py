#imports
import operator
import json
from collections import Counter
import json
from nltk.tokenize import word_tokenize
import re
#nltk remove stopwords and punctuation
from nltk.corpus import stopwords
import string
from nltk import bigrams
import vincent

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via','RT']
 #regexs for emoticons and mentions
emoticons_str = r"""
    (?:
        [:=;] # Eyes
       [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    #r'(?:@[\w_]+)', # @-mentions
    #r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs

    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]

tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)

def tokenize(s):
    return tokens_re.findall(s)

def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens

#read file
with open('data/stream_trump_cleaned.json', 'r') as f:
    for line in f:
        tweet = json.loads(line)


fname = 'data/stream_trump_cleaned.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        tweet = json.loads(line)
        tokens = preprocess(tweet['text'])
        # Create a list with all the terms
        #terms_all = [term for term in preprocess(tweet['text'])]
        terms_all = [term for term in preprocess(tweet['text']) if term not in stop]
        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))

    word_freq = count_all.most_common(20)
    labels, freq = zip(*word_freq)
    data = {'data': freq, 'x': labels}
    bar = vincent.Bar(data, iter_idx='x')
    bar.to_json('data/term_freq.json')

"""
    # Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text'])
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet['text'])
              if term not in stop and
              not term.startswith(('#', '@'))]
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if
              # we pass a list of inputs

terms_bigram = bigrams(terms_all)
"""
