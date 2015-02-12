import json
import re

twitter_data_file = 'twitter_data.txt'

#tweets_file = open(twitter_data_file, "r")
with open(twitter_data_file) as tf:
	tweets = [json.loads(line).get('text') for line in tf]

print len(tweets)

#### Function to classify the tweets by finding suitable keyword in the tweet
def tweets_related_to(word,text):
	text = text.lower()
	word = word.lower()
	match = re.search(word, text)
	if match:
		return text


#### Fetching tweets associated with different keywords and counting the number of tweets ####

#getting tweets associated with python and assigning it to python list variable
python = [tweets_related_to('python',tweet) for tweet in tweets]
#Filtering python list as it contains none values
python = filter(None, python)
print "tweets associated with python :"
print len(python)

ruby = [tweets_related_to('ruby',tweet) for tweet in tweets]
ruby = filter(None, ruby)
print "tweets associated with ruby :"
print len(ruby)

javascript = [tweets_related_to('javascript',tweet) for tweet in tweets]
javascript = filter(None, javascript)
print "tweets associated with javascript :"
print len(javascript)

#### Calculating positivity of each tweets related to different category of tweets ####
score_file = 'AFINN-111.txt'
with open(score_file) as sf:
        scores =  {line.split('\t')[0]: int(line.split('\t')[1]) for line in sf}


#### Function to calculate score of each tweet related to each category
def calculate_score(text):
	sum = 0
	for word in text.split():
		sum += scores.get(word,0)
	if sum >= 0:
		return text

#### calculating score of python related tweets and assigning tweets(having score>=0) to python_positive list 
python_positive = [calculate_score(tweet) for tweet in python]
python_positive =  filter(None, python_positive)
print "No. of Python related positive tweets are :"
print len(python_positive)

ruby_positive = [calculate_score(tweet) for tweet in ruby]
ruby_positive =  filter(None, ruby_positive)
print "No. of ruby related positive tweets are :"
print len(ruby_positive)

javascript_positive = [calculate_score(tweet) for tweet in javascript]
javascript_positive =  filter(None, javascript_positive)
print "No. of javascript related positive tweets are :"
print len(javascript_positive)

