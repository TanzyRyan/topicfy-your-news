# Topicfy-You-News
A program that groups new articles together based on similarities within their contents and the topic it discusses.

## Description
This program first scraps news articles from a provided RSS feed using the Newspaper module in Python. Based on the article's content, it will use TF-IDF vectorisation to convert each word into numerical value in order to perform K-mean clustering and group articles that have similar topics. Both K-mean clustering and TF-IDF vectorisation are implemented using scikit-learn.

## Example Usage
In this useage example, we will be using a RSS feed provided by Sydney Morning Herald (https://www.smh.com.au/rss/feed.xml, NOTE: the contents of the RSS does change so the contents may be different to the ones shown in the image below) as well as setting the number of clusters to 5.


![topicfy-your-news-img2](https://github.com/user-attachments/assets/210426d2-ac00-43d3-84b2-8cf52c7f5a2c)

## Future Improvements
For future improvements, the cluster accurancy and topic separation could be further enhanced to produce a more distinct clusters.
