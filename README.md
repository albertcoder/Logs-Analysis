# Logs-Analysis
An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like. This is a Python program using the psycopg2 module to connect to the database.

## Steps to run:

1. Install python3, vagrant and virtual box.
2. Clone the repository from https://github.com/udacity/fullstack-nanodegree-vm . Move into the vagrant sub-directory. Make sure you stay in this directory throughout the program execution.
3. Copy the contents of https://github.com/albertcoder/Logs-Analysis in vagrant sub-directory of the above repository.
4. Download the newsdata.sql file from https://www.dropbox.com/s/hna6pqgeq63dj7j/newsdata.sql.zip?dl=0 . You can download it without signing into dropbox. 
5. Turn on the Virtual Machine:
  -   $ vagrant up
  -   $ vagrant ssh
6. Run the command from terminal to load data in the database:
  - $   psql -d news -f newsdata.sql
7. Create view articleView using:
  - $ create view articleView as select title,author,count(*) as views from articles,log where 
  log.path like concat('%',articles.slug) group by articles.title,articles.author 
  order by views desc;
8. Create view errorLogView using:
  - $ create view errorLogView as select date(time),round(100.0*sum(case log.status when '200 OK' 
  then 0 else 1 end)/count(log.status),2) as "% Error" from log group by date(time) 
  order by "% Error" desc;
9. Time to run the program:
  - $ python3 logs.py
