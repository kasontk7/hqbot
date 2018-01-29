#export GOOGLE_APPLICATION_CREDENTIALS=~/Desktop/gvision/apikey.json
from google import google
from pprint import pprint

import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
# Instantiates a client (Change the line below******)
vision_client = vision.Client('1e1809ccc6301a0101b9f129f1cfe63248af94f1')

# The name of the image file to annotate (Change the line below 'image_path.jpg' ******)
file_name = os.path.join(os.path.dirname(__file__),'hq.jpg') # Your image path from current directory

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()
    image = vision_client.image(content=content)

#gets all text in the image
scan = []
for text in image.detect_text():
    scan.append(text.description)
#    pprint(text.description)

#scan[0] is all the text, and now q is a list of the question, and answer options
q = scan[0].split('?')

def print_biggest(current, other1, other2):
    if (current > other1 and current > other2):
        return "<--- This one"
    return ""

commonwords = ["a","an","the","he","she","they","and","or","if","of","when","how","is","was","from","no","in","to","has","have","had"]

question = q[0]
#print(q[0], q[1])
#answers is a list of the answer options
second = q[1].split('\n')
a = second[1].lower()
b = second[2].lower()
c = second[3].lower()
answers = [a, b, c]
print(a)
print(b)
print(c)

a1 = a.split()
b1 = b.split()
c1 = c.split()

a_count = 0
b_count = 0
c_count = 0

a_alt = 0
b_alt = 0
c_alt = 0

reverse = [0, 0, 0]

num_page = 3
search_results = google.search(question, num_page)

for x in search_results:
        sentence = x.description.lower()
#        print(sentence)
        if a in sentence:
            a_count += 1
        if b in sentence:
            b_count += 1
        if c in sentence:
            c_count += 1

for x in search_results:
    sentence = x.description.lower()
    #        print(sentence)
    for y in a1:
        if ((y not in commonwords) and (y in sentence)):
            a_alt += 1
    for y in b1:
        if ((y not in commonwords) and (y in sentence)):
            b_alt += 1
    for y in c1:
        if ((y not in commonwords) and (y in sentence)):
            c_alt += 1

#for x in range(3):
#    results = google.search(answers[x], num_page)
#    for y in results:
#        sentence = y.description.lower()
#        for z in question:
#            if ((z not in commonwords) and (z in sentence)):
#                reverse[x] += 1
#
#a_reverse = reverse[0]
#b_reverse = reverse[1]
#c_reverse = reverse[2]
print("")
print("Perfect matches in the search results: ")
print("a. ", a_count, print_biggest(a_count, b_count, c_count))
print("b. ", b_count, print_biggest(b_count, a_count, c_count))
print("c. ", c_count, print_biggest(c_count, a_count, b_count))
print("")
#print("Search answers, then match keywords: ")
#print("a. ", a_reverse, print_biggest(a_reverse, b_reverse, c_reverse))
#print("b. ", b_reverse, print_biggest(b_reverse, a_reverse, c_reverse))
#print("c. ", c_reverse, print_biggest(c_reverse, a_reverse, b_reverse))
#print("")
print("Individual word matches (only use for tiebreaker): ")
print("a. ", a_alt, print_biggest(a_alt, b_alt, c_alt))
print("b. ", b_alt, print_biggest(b_alt, a_alt, c_alt))
print("c. ", c_alt, print_biggest(c_alt, a_alt, b_alt))
