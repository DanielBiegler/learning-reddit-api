#!/usr/bin/python
import praw
import csv

def main():
	# read sensitive data in
	with open('client_id') as f_id, open('client_secret') as f_secret:
		client_id = f_id.readline()
		client_secret = f_secret.readline()
	
	reddit = praw.Reddit(client_id=client_id,
						client_secret=client_secret,
						user_agent='Bieglerbot by /u/danielbiegler')

	submission = reddit.submission(url='https://www.reddit.com/r/videos/comments/79i4cj/youtube_user_demonstrating_how_facebook_listens/')

	content_rows = []
	submission.comments.replace_more(limit=99999)
	for top_level_comment in submission.comments.list():
		content_rows.append([top_level_comment.author, 
							top_level_comment.created_utc, 
							top_level_comment.score, 
							top_level_comment.body])

	# persist collected data to csv
	with open('comments.csv', 'w') as csvfile:
		label_row = ['username', 'comment_created_utc', 'comment_score', 'comment_text']
		writer = csv.writer(csvfile, delimiter=',')
		writer.writerow(label_row)
		writer.writerows(content_rows)

if __name__ == '__main__':
	main()
