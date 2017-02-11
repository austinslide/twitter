import json
import pandas as pd
import matplotlib.pyplot as plt
import re
tweets_data_path = 'output.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue
print len(tweets_data)
#create pandas dataframe
tweets = pd.DataFrame()
#create columsn in dataframe
tweets['text'] = map(lambda tweet: tweet.get('text', None),tweets_data)
tweets['lang'] = list(map(lambda tweet: tweet.get('lang', None), tweets_data))
#tweets['lang'] = map(lambda tweet: tweet[u'lang'], tweets_data)

#tweets['country'] = map(lambda tweet: tweet[u'place'][u'country'] if tweet['place'] != None else None, tweets_data)

#plot
tweets_by_lang = tweets['lang'].value_counts()
print len(tweets_by_lang)
print (tweets_by_lang)

fig, ax = plt.subplots()
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=10)
ax.set_xlabel('Languages', fontsize=15)
ax.set_ylabel('Number of tweets' , fontsize=15)
ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')
plt.show()

#tweets_by_country = tweets['country'].value_counts()
#print len(tweets_by_country)
#print tweets_by_country

#fig, ax = plt.subplots()
#ax.tick_params(axis='x', labelsize=10)
#ax.tick_params(axis='y', labelsize=10)
#ax.set_xlabel('Countries', fontsize=15)
#ax.set_ylabel('Number of tweets' , fontsize=15)
#ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
#tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
#plt.show()

def word_in_text(word, text):
    if text == None:
        return False
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    return False

tweets['trump'] = tweets['text'].apply(lambda tweet: word_in_text('trump', tweet))
tweets['theresa'] = tweets['text'].apply(lambda tweet: word_in_text('theresa', tweet))
tweets['clinton'] = tweets['text'].apply(lambda tweet: word_in_text('clinton', tweet))

print tweets['trump'].value_counts()[True]
print tweets['theresa'].value_counts()[True]
print tweets['clinton'].value_counts()[True]

world_leaders = ['trump', 'May', 'clinton']
tweets_by_leader = [tweets['trump'].value_counts()[True], tweets['theresa'].value_counts()[True], tweets['clinton'].value_counts()[True]]

x_pos = list(range(len(world_leaders)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_leader, width, alpha=1, color='g')

# Setting axis labels and ticks
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Trump vs. May vs. Clinton (Raw data)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(world_leaders)
plt.grid()
plt.show()
#vaguely sentiment analysis ish
tweets['idiot'] = tweets['text'].apply(lambda tweet: word_in_text('idiot', tweet))
tweets['moron'] = tweets['text'].apply(lambda tweet: word_in_text('moron', tweet))

tweets['relevant'] = tweets['text'].apply(lambda tweet: word_in_text('idiot', tweet) or word_in_text('moron', tweet))

print tweets['idiot'].value_counts()[True]
print tweets['moron'].value_counts()[True]
print tweets['relevant'].value_counts()[True]


print tweets[tweets['relevant'] == True]['trump'].value_counts()[True]
print tweets[tweets['relevant'] == True]['theresa'].value_counts()[True]
print tweets[tweets['relevant'] == True]['clinton'].value_counts()[True]

tweets_by_sentiment = [tweets[tweets['relevant'] == True]['trump'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['theresa'].value_counts()[True],
                      tweets[tweets['relevant'] == True]['clinton'].value_counts()[True]]
x_pos = list(range(len(world_leaders)))
width = 0.8
fig, ax = plt.subplots()
plt.bar(x_pos, tweets_by_sentiment, width,alpha=1,color='g')
ax.set_ylabel('Number of tweets', fontsize=15)
ax.set_title('Ranking: Trump vs. May vs. Clinton (Idiot or Moron)', fontsize=10, fontweight='bold')
ax.set_xticks([p + 0.4 * width for p in x_pos])
ax.set_xticklabels(world_leaders)
plt.grid()
plt.show()
