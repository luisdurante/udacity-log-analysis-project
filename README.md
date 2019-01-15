
# Log Analysis

## The first project of Udacity Back End Developer Nanodegree.

The project consists in creating an internal tool to analyse a PostgreSQL database of a newspaper site with over a million rows and show the correct data that answer three main questions:

- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors? 

## Requirements
 - Python 3
 - PostgreSQL
 - psycopg2

## How to run

- ####  Download [Vagrant][Vagrant] and [Virtual Box][VM]
- #### Set up Vagrant 
    Using the terminal, go to the folder and type 'vagrant up' and a linux OS will be installed. After that, run the command 'vagrant ssh' to log in to the Virtual Machine.
- #### Go to the vagrant folder and run the database
	In your **VM** go to the **Vagrant** folder typing the command:
	>cd /vagrant
- #### Running the database  
	 You can do it by running the command:
	 >`psql -d news -f newsdata.sql`
- #### Start the program
	Inside the **Vagrant** folder you can start the program running the command:
	> python3 log_analysis.py 

[Vagrant]: <https://www.vagrantup.com/downloads.html>
[VM]: <https://www.virtualbox.org/wiki/Downloads>

