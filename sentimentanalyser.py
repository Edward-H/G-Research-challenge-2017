"""Analyse tweets"""
import webhandler

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for i2, c2 in enumerate(s2):
        distances_ = [i2+1]
        for i1, c1 in enumerate(s1):
            if c1 == c2:
                distances_.append(distances[i1])
            else:
                distances_.append(1 + min((distances[i1], distances[i1 + 1], distances_[-1])))
        distances = distances_
    return distances[-1]

class SentimentAnalyser(object):
    def __init__(self):
        self.negative_words = webhandler.get_negative_words()
        self.neutral_words = webhandler.get_neutral_words()
        self.positive_words = webhandler.get_positive_words()
        self.companies = webhandler.get_company_info()
        self.company_names = [c.name for c in self.companies]
        #print(self.companies)

    def analyse_tweet(self, tweet):
        """Analyse a tweet, extracting the subject and sentiment"""
        sentiment = 0
        subject = None

        seen_not = False
        for word in tweet.split(" "):
            if word == "not":
                seen_not = True
            elif word in self.positive_words:
                sentiment = sentiment + 1
            elif word in self.negative_words:
                sentiment = sentiment - 1
            if word in self.company_names:
                subject = word
            else:
                for company in self.company_names:
                    if levenshtein_distance(company, word) <= 3:
                        subject = company
                        break

        if seen_not:
            sentiment = -sentiment
        return [(subject or self.companies[0].name, sentiment)]

