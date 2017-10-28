"""Analyse tweets"""
import webhandler
import myparser

class SentimentAnalyser(object):
    def __init__(self):
        self.negative_words = webhandler.get_negative_words()
        self.neutral_words = webhandler.get_neutral_words()
        self.positive_words = webhandler.get_positive_words()
        self.positive_words += ["wish"]
        self.companies = webhandler.get_company_info()
        self.company_names = [c.name for c in self.companies]
        self.products = [(c.products,c.name) for c in self.companies]
        self.product_names = []
        for (ps, c) in self.products:
          for p in ps:
            self.product_names += [(p.name, c)]
        #print(self.product_names)
        self.comparisons = [("worse", -1), ("better", 1), ("prefer", 1)]


    def analyse_tweet(self, tweet):
        """Analyse a tweet, extracting the subject and sentiment"""
        sentiment = 0
        subjects = []

        is_comparison = False # sentiment will be the LHS of the comparison
        seen_not = False
        for word in myparser.parse(tweet,self.company_names,True):
            if word == "not" or word == "don't":
                seen_not = True
            elif word in self.positive_words:
                sentiment = sentiment + 1
            elif word in self.negative_words:
                sentiment = sentiment - 1
            if word in self.company_names:
                subjects += [word]
            for (p, c) in self.product_names:
                if word == p:
                   subjects += [c]
            for (c,s) in self.comparisons:
                if word == c:
                   sentiment = s
                   is_comparison = True
        if seen_not:
            sentiment = -sentiment

        subjects += [None, None]
        if is_comparison:
           return[(subjects[0], sentiment), (subjects[1], -sentiment)]
        else:
           return [(subjects[0], sentiment)]

