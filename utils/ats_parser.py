import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

# Load English model
nlp = spacy.load("en_core_web_sm")

def extract_keywords(text):
    # Step 1: Process the text
    doc = nlp(text)

    # Step 2: Keep only important words (no stopwords like 'the', 'is')
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]

    # Step 3: Use TF-IDF to find important keywords
    vectorizer = TfidfVectorizer(max_features=10)
    vectorizer.fit([" ".join(tokens)])

    return vectorizer.get_feature_names_out()

# Example Job Description
jd = "We are hiring a Data Scientist with skills in Python, SQL, Machine Learning, and Deep Learning."
print("Keywords:", extract_keywords(jd))
