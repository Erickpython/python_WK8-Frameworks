from collections import Counter
from wordcloud import WordCloud
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("./metadata.csv", low_memory=False)
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    # FIX: correct dropna usage
    df = df.dropna(subset=["title", "publish_time"]).copy()
    return df

df = load_data()

# App title
st.title("COVID-19 RESEARCH PUBLICATIONS DASHBOARD")

# Sidebar filters
st.sidebar.header("Filters")
year_filter = st.sidebar.multiselect(
    "Select Year(s):",
    options=df["publish_time"].dt.year.dropna().unique(),
    default=df["publish_time"].dt.year.dropna().unique()
)
df_filtered = df[df["publish_time"].dt.year.isin(year_filter)]

# Publications by year
st.subheader("Publications by Year")
pubs_per_year = df_filtered["publish_time"].dt.year.value_counts().sort_index()

fig, ax = plt.subplots()
sns.barplot(x=pubs_per_year.index, y=pubs_per_year.values, ax=ax, palette="viridis")
ax.set_xlabel("Year")           # FIXED
ax.set_ylabel("Number of Publications")
ax.set_title("Publications per Year")
st.pyplot(fig)

# Top 20 journals
st.subheader("Top 20 Journals")
top_journals = df_filtered["journal"].value_counts().head(20)

fig, ax = plt.subplots()
sns.barplot(
    x=top_journals.values,
    y=top_journals.index,
    palette="mako",
    ax=ax
)
ax.set_xlabel("Number of Papers")  # FIXED
ax.set_ylabel("Journal")
ax.set_title("Top 20 Journals")
st.pyplot(fig)

# Word cloud of paper titles
st.subheader("Word Cloud of Paper Titles")
text = " ".join(df_filtered["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)
