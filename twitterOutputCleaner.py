#for cleaning the output of a stream download from twitter
#takes negative word used in error and creates a clean output file
bad_words = ['limit']

with open('data/stream_trump.json') as oldfile, open('data/stream_trump_cleaned.json', 'w') as newfile:
    for line in oldfile:
        if not any(bad_word in line for bad_word in bad_words):
            newfile.write(line)
