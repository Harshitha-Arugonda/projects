import string
from collections import Counter
import matplotlib.pyplot as plt

# File paths
text_file_path = "read.txt"
emotions_file_path = "emotions.txt"
graph_file_path = "graph.png"

# Read text file
try:
    with open(text_file_path, encoding='utf-8') as file:
        text = file.read()
except FileNotFoundError:
    print(f"File '{text_file_path}' not found.")
    exit(1)

# Convert to lowercase
lower_case = text.lower()

# Removing punctuations
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Splitting text into words
tokenized_words = cleaned_text.split()

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# Removing stop words from the tokenized words list
final_words = [word for word in tokenized_words if word not in stop_words]

# NLP Emotion Algorithm
emotion_list = []
try:
    with open(emotions_file_path, encoding='utf-8') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)
except FileNotFoundError:
    print(f"File '{emotions_file_path}' not found.")
    exit(1)

# Counting each emotion in the emotion list
w = Counter(emotion_list)

# Plotting the emotions on the graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()

# Saving the graph
plt.savefig(graph_file_path)
plt.show()
