"""Collection of DTOs and class for interacting with the service"""
import gzip
import http.client
import json

SERVER_URL = "devrecruitmentchallenge.com"
API_KEY = ""

class ChallengeInfo(object):
    """Information regarding a challenge"""
    def __init__(self, cid, challenge_type, name, description):
        self.cid = cid
        self.challenge_type = challenge_type.lower()
        self.name = name
        self.description = description

class Tweet(object):
    """A single tweet to be analysed"""
    def __init__(self, tid, time, source, tweet):
        self.tid = tid
        self.time = time
        self.source = source
        self.tweet = tweet

class Challenge(object):
    """A Challenge definition"""
    def __init__(self, info, tweets):
        self.info = info
        self.tweets = tweets

class ChallengeResult(object):
    """Response from a challenge submission"""
    def __init__(self, submission_id, mark):
        self.submission_id = submission_id
        self.mark = mark

class Product(object):
    """A product definition"""
    def __init__(self, name, product_type):
        self.name = name
        self.product_type = product_type

class Company(object):
    """A company definition"""
    def __init__(self, name, ticker, products, industry):
        self.name = name
        self.ticker = ticker
        self.products = [Product(p["name"], p["productType"]) for p in products]
        self.industry = industry

def get_challenge_list():
    """Get the list of challenges"""
    data = get_json("/api/challenges/")
    return [ChallengeInfo(k["id"], k["challengeType"], k["name"], k["description"])
            for k in data["challenges"]]

def get_challenge(cid):
    """Get the details of a specific challenge"""
    data = get_json("/api/challenges/{}".format(cid))
    info_json = data["challenge"]
    info = ChallengeInfo(info_json["id"], info_json["challengeType"], ["name"], 
                         info_json["description"])
    tweets = [Tweet(k["id"], k["time"], k["source"], k["tweet"]) for k in data["tweets"]]
    return Challenge(info, tweets)

def get_company_info():
    """Get details on all companies"""
    data = get_json("/api/world/companies")
    companies = [Company(k["name"], k["ticker"], k["products"], k["industry"]) for k in data["companies"]]
    return companies

def get_positive_words():
    """Get a list of positive words"""
    data = get_json("/api/words/positive")
    return [x for x in data["words"]]

def get_neutral_words():
    """Get a list of neutral words"""
    data = get_json("/api/words/neutral")
    return [x for x in data["words"]]

def get_negative_words():
    """Get a list of negative words"""
    data = get_json("/api/words/negative")
    return [x for x in data["words"]]

def post_pertweet_submission(submission):
    """Post a per-tweet challenge submission and return the result"""
    j = json.dumps(submission)
    data = post_json("/api/submissions/pertweet", j)
    return ChallengeResult(data["submissionId"], data["mark"])

def post_aggregated_submission(submission):
    """Post an aggregated challenge submission and return the result"""
    j = json.dumps(submission)
    data = post_json("/api/submissions/aggregated", j)
    return ChallengeResult(data["submissionId"], data["mark"])

def get_json(url):
    """Return json result of GET"""
    connection = http.client.HTTPConnection(SERVER_URL)
    headers = {
        "Authorization": "ApiKey {}".format(API_KEY),
        "Accept-encoding": "gzip"
    }
    connection.request("GET", url, headers=headers)
    response = connection.getresponse()
    raw_content = response.read()
    if response.getheader("Content-encoding") == "gzip":
        content = gzip.decompress(raw_content).decode()
    else:
        content = raw_content.decode()
    print("GET {} {} ({} bytes)".format(response.status, url, len(raw_content)))
    #print(content)
    if response.status != 200:
        print(content)
        raise ValueError("GET of {} was not successful".format(url))
    return json.loads(content)

def post_json(url, j):
    """Return json result of a POST"""
    connection = http.client.HTTPConnection(SERVER_URL)
    headers = {"Authorization": "ApiKey {}".format(API_KEY), "Content-type": "application/json"}
    connection.request("POST", url, j, headers=headers)
    response = connection.getresponse()
    content = response.read().decode()
    print("POST {} {} ({} bytes)".format(response.status, url, len(content)))
    #print(content)
    if response.status != 200:
        print(content)
        raise ValueError("POST to {} was not successful. Sent JSON '{}'".format(url, j))
    return json.loads(content)