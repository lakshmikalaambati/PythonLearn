from urllib.request import urlopen
story=urlopen('http://sixty-north.com/c/t.txt')
story_word=[]
for line in story:
    line_words=line.decode('utf-8').split()
    for word in line_words:
        story_word.append(word)
story.close())
print(story_word)