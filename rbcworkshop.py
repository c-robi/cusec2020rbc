import requests
import json
url = 'https://memeservice.cfapps.io/api/memes'


def filter_memes(meme_array):
	return list(filter(lambda x: x['points'] > 60000, meme_array))

def count_points(meme_array):
	return sum(map(lambda x: x['points'], meme_array))

def min_1000(meme_array):
	# Sort array (but don't affect the original)
	sorted_array = sorted(meme_array, key=lambda x: x['points'], reverse=True)

	# Get the 1000th entry if it exists, otherwise get the last entry
	return sorted_array[min(len(sorted_array) - 1, 999)]['points']


response = requests.get(url)
meme_array = json.loads(response.text)

# Get list
print(meme_array[0])
print('Original size {0}'.format(len(meme_array)))

# Filter the list. Print them since there's not too many
meme_array_filtered = filter_memes(meme_array)
print(meme_array_filtered[0])
print('Size filtered {0}'.format(len(meme_array_filtered)))
for meme in meme_array_filtered:
	print(meme)

# Count total number of points
meme_array_count = count_points(meme_array)
print('Total number of points = {0}'.format(meme_array_count))

# Determine minimum
meme_min_1000 = min_1000(meme_array)
print('Min number of points for top 1000 = {0}'.format(meme_min_1000))