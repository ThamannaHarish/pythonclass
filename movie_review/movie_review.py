import nltk
import matplotlib
matplotlib.use('Agg')
import pandas as pd
import random
import string
from nltk.corpus import movie_reviews, stopwords
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Download data (only once)
nltk.download('movie_reviews')
nltk.download('stopwords')

# Q1. Load & Explore
docs = [(movie_reviews.raw(fileid), category)
        for category in movie_reviews.categories()
        for fileid in movie_reviews.fileids(category)]
random.shuffle(docs)

df = pd.DataFrame(docs, columns=["review_text", "label"])
print("Sample Reviews:\n", df.sample(5))

# Q2. Preprocess (lowercase + optional cleaning)
stop_words = set(stopwords.words('english'))
def clean(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return ' '.join(w for w in text.split() if w not in stop_words)
df['cleaned'] = df['review_text'].apply(clean)
print("\nCleaned Sample:\n", df['cleaned'].iloc[0][:300])

# Q3. Bag of Words (BoW)
vectorizer = CountVectorizer(max_features=50)
bow = vectorizer.fit_transform(df['cleaned'])
bow_df = pd.DataFrame(bow.toarray(), columns=vectorizer.get_feature_names_out())
print("\nBoW Matrix (Top 50 Words):\n", bow_df.head())

# Top 10 most frequent words
top10 = bow_df.sum().sort_values(ascending=False).head(10)
print("\nTop 10 Frequent Words:\n", top10)

# Q4. TF-IDF
tfidf = TfidfVectorizer(max_features=50)
tfidf_matrix = tfidf.fit_transform(df['cleaned'])
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf.get_feature_names_out())
print("\nTop 5 TF-IDF Words in First Review:\n", tfidf_df.iloc[0].sort_values(ascending=False).head(5))

print("\nTF-IDF gives more weight to unique words in a review compared to BoW.")

# Q5. Visualization (Bonus)
top10.plot(kind='barh', title="Top 10 Frequent Words (BoW)")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("bar_chart.png")

# Word cloud
words = ' '.join(df['cleaned'])
wc = WordCloud(width=800, height=400, background_color='white').generate(words)
plt.figure(figsize=(10, 5))
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.savefig("wordcloud.png")

print("\n✅ Plots saved: 'bar_chart.png' and 'wordcloud.png'")
