import json #read csv files
import pandas #for data structures
import os 
import glob

if not os.path.exists("parsed_files"):
  os.mkdir("parsed_files")


#We want to set up a new data frame, and save it.

dataset = pandas.DataFrame()

#create a csv with columns

for json_file_name in glob.glob("json_files/*.json"):
	# json_file_name = "json_files/dAAAb.json"

	f = open(json_file_name, "r")
	json_data = json.load(f)
	f.close()

	# print(json_data)
	# homework: 
	gh_id = json_data['login']
	gh_number_id = json_data['id']
	node_id = json_data['node_id']
	avatar_url = json_data['avatar_url']
	gravatar_id = json_data['gravatar_id']
	url = json_data['url']
	html_url = json_data['html_url']
	followers_url = json_data['followers_url']
	gists_url = json_data['gists_url']
	starred_url = json_data['starred_url']
	subscriptions_url = json_data['subscriptions_url']
	organizations_url = json_data['organizations_url']
	repos_url = json_data['repos_url']
	events_url = json_data['events_url']
	received_events_url = json_data['received_events_url']
	type_ = json_data['type']
	site_admin = json_data['site_admin']
	name = json_data['name']
	company = json_data['company']
	blog = json_data['blog']
	location = json_data['location']
	email = json_data['email']
	hireable = json_data['hireable']
	bio = json_data['bio']
	twitter_username = json_data['twitter_username']
	public_repos = json_data['public_repos']
	public_gists = json_data['public_gists']
	created_at = json_data['created_at']
	updated_at = json_data['updated_at']
	followers = json_data['followers']
	following = json_data['following']

	# print(gh_id)
	# print(gh_number_id)
	# print(updated_at)
	# print(followers)

	#
	row = pandas.DataFrame.from_records(
		[
		{
			'gh_id' : gh_id,
			'gh_number_id' : gh_number_id,
			'node_id' : node_id,
			'avatar_url' : avatar_url,
			'gravatar_id' : gravatar_id,
			'url' : url,
			'html_url' : html_url,
			'followers_url' : followers_url,
			'gists_url' : gists_url,
			'starred_url' : starred_url,
			'subscriptions_url' : subscriptions_url,
			'organizations_url' : organizations_url,
			'repos_url' : repos_url,
			'events_url' : events_url,
			'received_events_url' : received_events_url,
			'type' : type_,
			'site_admin' : site_admin,
			'name' : name,
			'company' : company,
			'blog' : blog,
			'location' : location,
			'email' : email,
			'hireable' : hireable,
			'bio' : bio,
			'twitter_username' : twitter_username,
			'public_repos' : public_repos,
			'created_at' : created_at,
			'updated_at' : updated_at,
			'followers' : followers,
			'following' : following
		}])

	print(row)
		#merge dataset with row, concat matches columns
	dataset = pandas.concat([dataset, row])

dataset.to_csv("parsed_files/github_user_data.csv"
							, index=False)