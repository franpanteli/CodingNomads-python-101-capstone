import requests

min_len = 4 #minimum length of the random name we want to generate
max_len = 6 #maximum length of the random name we want to generate
URL = f"https://uzby.com/api.php?min={min_len}&max={max_len}" #url of the API we are making the call to

response = requests.get(URL) #make a get request
print(response.text) #print result of the get request

# -> one of the things you find with this is that it takes time for the API to generate the random name into the
    #terminal when the code is run
# -> the virtual environment has to activated for this to work
# -> this is done using source bin/activate, when cd'd into the directory in the CLI
# -> an example of an error is "Name cannot be shorter than 2 characters"
    # -> this is when the minimum length of the word is 0 (the same as the maximum)