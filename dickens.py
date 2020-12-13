from urllib.request import urlopen

#http://sixty-north.com/c/t.txt


def fetchWords(siteName):
    story = urlopen(siteName)
    story_words = []
    for line in story:
        line_words = line.decode('utf-8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def printWords(story_words):
    for word in story_words:
        print(word)


def main():
    words = fetchWords(eval(input()))
    printWords(words)


if __name__ == '__main__':
    main()
