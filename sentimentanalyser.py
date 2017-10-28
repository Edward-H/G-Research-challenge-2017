"""Analyse tweets"""
import webhandler

class SentimentAnalyser(object):
    def __init__(self):
        self.negative_words = webhandler.get_negative_words()
        self.neutral_words = webhandler.get_neutral_words()
        self.positive_words = webhandler.get_positive_words()
        self.companies = webhandler.get_company_info()

    def analyse_tweet(self, tweet):
        """Analyse a tweet, extracting the subject and sentiment"""
        sentiment = 0

        seen_not = False
        for word in tweet.split(" "):
            if word == "not":
                seen_not = True
            elif word in self.positive_words:
                sentiment = sentiment + 1
            elif word in self.negative_words:
                sentiment = sentiment - 1

        if seen_not:
            sentiment = -sentiment

        return [(self.companies[0].name, sentiment)]
