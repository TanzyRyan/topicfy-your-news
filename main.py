# Topicfy your News

import feedparser
import newspaper
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def article_scraper(url, articles):
    '''
    From the given URL, add news articles into the articles list
    '''
    # get the RSS feed and turn it into a usable object
    feed = feedparser.parse(url)
    
    # add each article in the feed into articles list
    for entry in feed.entries:
        # obtain full article of the entry
        article = newspaper.Article(entry.link)

        # fetches the HTML and convert it into readable object
        article.download()
        article.parse()

        # store article contents as a dictionary within articles list
        articles.append({
            'title': article.title,
            'author': article.authors,
            'publish_date': article.publish_date,
            'content': article.text
        })


def produce_cluster(contents, n_clusters):
    '''
    perform k-mean clustering using TF-IDF vectorisation on the contents of the new articles
    '''
    # clean the the contents
    contents

    # convert text into vector of numeric values, keeping the top 2000 words, includes unigrams and bigrams
    vectoriser = TfidfVectorizer(max_features=100, ngram_range=(1, 2), stop_words='english')
    # sparse matrix with articles as rows, word(s) as columns, importance of each word(s) as the value
    X = vectoriser.fit_transform(contents)

    # use kmean clustering based on the results of the TF-IDF vectors
    model = KMeans(n_clusters=n_clusters, random_state=42)
    model.fit(X)

    return model.labels_, model, vectoriser

def get_top_keywords_per_cluster(model, vectoriser, top_n):
    '''
    extracts the top top_n-th most common key word for each cluster
    '''
    # extract all word and phrases used by the vectoriser
    terms = vectoriser.get_feature_names_out()
    # initiate list containing key words of each cluster 
    keywords_per_cluster = []

    for i in range(model.n_clusters):
        # get the average term weights in the cluster
        center = model.cluster_centers_[i]
        # get the top terms based on indices
        top_indices = center.argsort()[-top_n:][::-1]
        top_terms = [terms[j] for j in top_indices]
        keywords_per_cluster.append(top_terms)
        
    return keywords_per_cluster


# Your feed URL
feed_url = 'https://www.smh.com.au/rss/feed.xml'
articles = []
article_scraper(feed_url, articles)

titles = [article['title'] for article in articles if article['title']]
contents = [article['content'] for article in articles if article['content']]

labels, model, vectoriser = produce_cluster(contents, n_clusters=5)

top_keywords = get_top_keywords_per_cluster(model, vectoriser, top_n=5)

for cluster_num in range(model.n_clusters):
    print(f"\nCluster {cluster_num+1}: (keywords: {', '.join(top_keywords[cluster_num])})")
    for i, title in enumerate(titles):
        if labels[i] == cluster_num:
            print(f"- {title}")