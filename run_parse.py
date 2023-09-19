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
	updated_at = json_data['updated_at']
	followers = json_data['followers']

	print(gh_id)
	print(gh_number_id)
	print(updated_at)
	print(followers)

	#
	row = pandas.DataFrame.from_records(
		[
		{
			'gh_id' : gh_id,
			'gh_number_id' : gh_number_id,
			'updated_at' : updated_at,
			'followers' : followers
		}])

	print(row)
		#merge dataset with row, concat matches columns
	dataset = pandas.concat([dataset, row])

dataset.to_csv("parsed_files/github_user_data.csv"
							, index=False)


