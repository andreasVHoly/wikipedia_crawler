import wikipedia as wiki

def countWords(query):
    count = 0
    for i in query.split():
        count += 1
    if count < 200:
        print "File was too small"
        return False
    elif count > 2000:
        print "File was too large"
        return False
    else:
        print "File accepted with " + str(count) + " words"
        return True


def runQuery(topic, maxresults, target):
    returned = wiki.search(topic, results=maxresults, suggestion=False)
    print "Looking for topics in " + topic
    count = 0
    for i in returned:
        if count == target:
            break

        try:
            result = wiki.page(i)
        except wiki.exceptions.DisambiguationError:
            print "DisambiguationError"
            continue
        except wiki.exceptions.PageError:
            print "PageError"
            continue
        except:
            print "fok knows"
            continue


        query = result.content.encode('utf-8')
        if countWords(query):
            f = open(topic + "/output_" + str(count) + ".txt", "w")
            f.write(result.title.encode('utf-8') + "\n\n\n")
            f.write(result.content.encode('utf-8'))
            count += 1
            print "Found file " + str(count+1) + "/50"
            f.close()



topic1 = "Computer Science"
topic2 = "Information Retrieval"
topic3 = "Machine Learning"
topic4 = "Data Structures"
topic5 = "3D Printing"
topic6 = "Computer Network"
topic7 = "Parallel Computing"
topic8 = "Human Computer Interaction"
topic9 = "Mobile Application Development"
topic10 = "Cloud Computing"

runQuery(topic1, 1000, 20)
runQuery(topic2, 1000, 20)
runQuery(topic3, 1000, 20)
runQuery(topic4, 1000, 20)
runQuery(topic5, 1000, 20)
runQuery(topic6, 1000, 20)
runQuery(topic7, 1000, 20)
runQuery(topic8, 1000, 20)
runQuery(topic9, 1000, 20)
runQuery(topic10, 1000, 20)
print "Done Processing"