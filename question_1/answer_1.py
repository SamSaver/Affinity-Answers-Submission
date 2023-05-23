# Dependencies
import re
from nltk.corpus import stopwords


def read_file(file_path):
    """
    Function to read the file
    """
    # Initialize the list to store the lines of the file
    lines = []
    # Open the file in read mode
    with open(file_path, 'r') as f:
        # Read each line of the file
        lines = f.readlines()
    # Return the lines of the file
    return lines


def preprocess_text(text):
    """
    Function to preprocess the text
    """
    # Remove the newline character from the end of the text
    text = text.strip()
    # Convert the text to lowercase
    text = text.lower()
    # Remove punctuation from the text using regex
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    text = text.split()
    # Remove stopwords from the text
    text = [word for word in text if word not in stopwords.words('english')]
    # Return the preprocessed text
    return text


# List to store all the tweets
tweets = read_file(file_path='./question_1/tweets.txt')
# List to store all the slurs
slurs = read_file(file_path='./question_1/slur_words.txt')
slurs = [slur.strip() for slur in slurs]

original_tweets = tweets.copy()

# Preprocess all the tweets
tweets = [preprocess_text(tweet) for tweet in tweets]

# Remove stopwords from the tweets
tweets = [[word for word in tweet if word not in stopwords.words(
    'english')] for tweet in tweets]

i = 0
# Evaluating each tweet and calculating the degree of profanity for each tweet
for tweet in tweets:
    # Initialize the degree of profanity to 0
    degree_of_profanity = 0
    # Iterate over each word in the tweet
    for word in tweet:
        # If the word is a slur
        if word in slurs:
            # Increment the degree of profanity by 1
            degree_of_profanity += 1

    # Print the tweet and its degree of profanity
    print('*'*80)
    print(f"{original_tweets[i]} -> {degree_of_profanity} slur words found")
    print('*'*80)
    print()

    i += 1
