import pandas as pd
import sqlite3
import regex as re
import matplotlib.pyplot as plt

from wordcloud import WordCloud

# create dataframe from csv
df = pd.read_csv("emails.csv")

df.head()
# print(df.loc())
# print(df.spam == 1)

print("spam: count: " + str(len(df.spam == 1)))
print("not spam count: " + str(len(df.loc[df.spam == 0])))
# print(df.shape)
df["spam"] = df["spam"].astype(int)

df = df.drop_duplicates()
df = df.reset_index(inplace=False)[["text", "spam"]]

# print(df.shape)

clean_desc = []
for w in range(len(df.text)):
    desc = df["text"][w].lower()

    # remove punctuation
    desc = re.sub("[^a-zA-Z]", " ", desc)

    # remove tags
    desc = re.sub("&lt;/?;", " &lt;&gt; ", desc)

    # remove digits and special chars
    desc = re.sub("(\\d|\\W)+", " ", desc)

    clean_desc.append(desc)

# assign the cleaned descriptions to the data grame
df["text"] = clean_desc

# print(df.head(3))

stop_words = [
    "is",
    "you",
    "your",
    "and",
    "the",
    "to",
    "from",
    "or",
    "I",
    "for",
    "do",
    "get",
    "not",
    "here",
    "in",
    "im",
    "have",
    "on",
    "re",
    "new",
    "subject",
]

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color="black",
    stopwords=stop_words,
    max_words=1000,
    min_font_size=20,
).generate(str(df["text"]))


# plot the word cloud
fig = plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
