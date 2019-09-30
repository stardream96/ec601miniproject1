
#author Linfeng
'''
This code take the local json file and output it to a list 
of text for each tweets and write the result to an txt file
'''

import json    

def text_extractor():
	tweets = ['']
	tweets_dict_list = []
	tweet_text_lists_https_rmv = []
	print("reading json...")
	with open('tweet.json') as json_file:
		ind = 0
		for line in json_file:
			if line[0:2] == '}{':
				tweets[ind]+='}'
				tweets.append('')
				ind+=1
				tweets[ind]+='{'
			else:
				tweets[ind]+=line
		for item in tweets:
			tt = json.loads(item)
			tweets_dict_list.append(tt)
			tweet_text_lists_https_rmv.append(tt['text'].split('https')[0])
		#print(tweet_text_lists_https_rmv)
	f = open('text.txt','w')
	print("writing to file")
	for item in tweet_text_lists_https_rmv:
		f.write(item+'\n')
	f.close()
	return tweet_text_lists_https_rmv
