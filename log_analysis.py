#!/usr/bin/env python3

import psycopg2


def db_connect():
    """
    Creates the connection to the database named "news"
    and returns the connection and the database cursor.
    Returns a tuple:
        db: The database connection(first element);
        cursor: The database cursor(second element).
    """
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    return db, cursor


def execute_query(query):
    """
    Returns the result of a SQL Query.
    Argument(s):
        query: The SQL query.
    Returns a list of tuples with the results.
    """
    db, cursor = db_connect()
    cursor.execute(query)
    out = cursor.fetchall()
    db.close()
    return out


# 1. What are the most popular three articles of all time?

def print_top_articles():
    """Prints out the top 3 articles of all time."""
    sql_query1 = '''SELECT articles.title AS titles, COUNT(*) AS views from log
                JOIN articles
                ON '/article/' || articles.slug = log.path
                GROUP BY titles
                ORDER BY views DESC
                LIMIT 3'''
    result1 = execute_query(sql_query1)
    print('1. What are the most popular three articles of all time?')
    print('--------------------------------------------------------')
    for row in result1:
        print('"{}" - {} views'.format(row[0], row[1]))
    print('--------------------------------------------------------')


# 2. Who are the most popular article authors of all time?

def print_top_authors():
    """Prints a list of authors ranked by article views."""
    sql_query2 = '''SELECT authors.name, COUNT(*) AS soma
                FROM authors
                JOIN articles
                ON authors.id = articles.author
                JOIN log
                ON articles.slug = SUBSTRING(log.path,10)
                WHERE log.path LIKE '/article/%'
                GROUP BY authors.name
                ORDER BY soma DESC'''
    result2 = execute_query(sql_query2)
    print('\n2. Who are the most popular article authors of all time?')
    print('--------------------------------------------------------')
    for row in result2:
        print('{} - {} views'.format(row[0], row[1]))
    print('--------------------------------------------------------')


# 3. On which days did more than 1% of requests lead to errors?

def print_errors_over_one_percent():
    """Prints the days that had more than 1% of error requests"""
    sql_query3 = '''SELECT to_char(date,'FMMonth DD, YYYY'),
                       ROUND(error_rate,2) AS percentage
                FROM(
                    SELECT time::date AS date,
                      (SUM(CASE status WHEN '404 NOT FOUND' THEN 1 ELSE 0 END)
                      *100)::DECIMAL / COUNT(*) AS error_rate
                    FROM log
                    GROUP BY date
                    ORDER BY error_rate DESC
                    ) error
                WHERE error_rate >= 1'''
    result3 = execute_query(sql_query3)
    print('\nOn which days did more than 1% of requests lead to errors?')
    print('-----------------------------------------------------------')
    for row in result3:
        print('{} -- {}%'.format(row[0], row[1]))
    print('-----------------------------------------------------------')


if __name__ == '__main__':
    print_top_articles()
    print_top_authors()
    print_errors_over_one_percent()
