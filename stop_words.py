
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


print(set(stopwords.words('english')))

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [v for v in word_tokens if v not in stop_words]

print(word_tokens)
print(filtered_sentence)
