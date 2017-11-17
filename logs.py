#! /usr/bin/env python3

import psycopg2
dbName = "news"

# Top three articles of all time?
queryOne = "select title,views from articleView limit 3"

# Top three authors of all time?
queryTwo = """select authors.name,sum(articleView.views) as views from
articleView,authors where authors.id = articleView.author
group by authors.name order by views desc"""

# Days with 1% of requests leading to errors?
queryThree = "select * from errorLogView where \"% Error\" > 1"

# store results
queryOneResult = dict()
queryOneResult['head'] = "\n1. The top 3 articles of all time are:\n"

queryTwoResult = dict()
queryTwoResult['head'] = "\n2. The top 3 authors of all time are:\n"

queryThreeResult = dict()
queryThreeResult['head'] = """\n3. Days with more than 1% of requests
leading to error:\n"""


# returns the result of query
def getQueryResult(query):
    db = psycopg2.connect(database=dbName)
    c = db.cursor()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results


# prints the results of array passed as parameter
def showQueryResults(queryResult):
    print (queryResult['head'])
    for result in queryResult['results']:
        print ('\t' + str(result[0]) + ' =>> ' + str(result[1]) + ' views')


# prints the results of array passed as parameter
def showErrorQueryResults(queryResult):
    print (queryResult['head'])
    for result in queryResult['results']:
        print ('\t' + str(result[0]) + ' =>> ' + str(result[1]) + ' %')


# stores the result of the query
queryOneResult['results'] = getQueryResult(queryOne)
queryTwoResult['results'] = getQueryResult(queryTwo)
queryThreeResult['results'] = getQueryResult(queryThree)

# display clean output
showQueryResults(queryOneResult)
showQueryResults(queryTwoResult)
showErrorQueryResults(queryThreeResult)
