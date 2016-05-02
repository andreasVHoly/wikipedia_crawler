import wikipedia as wiki

def countWords(query):
    count = 0
    for i in query.split():
        count += 1
    if count < 200 or count > 2000:
        return False
    else:
        return True


def runQuery(topic, maxresults):
    returned = wiki.search(topic, results=maxresults, suggestion=False)
    print "Looking for topics in " + topic
    count = 0
    for i in returned:
        if count == 49:
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
        if (countWords(query)):
            f = open(topic + "/output_" + str(count) + ".txt", "w")
            f.write(result.title.encode('utf-8') + "\n\n\n")
            f.write(result.content.encode('utf-8'))
            count += 1
            print "Found file " + str(count) + "/50"
            f.close()








topic1 = "Computer Science"
topic2 = "Information Retrieval"
topic3 = "Machine Learning"
topic4 = "Data Structures"

runQuery(topic1, 1000)
runQuery(topic2, 1000)
runQuery(topic3, 1000)
runQuery(topic4, 1000)

print "done"