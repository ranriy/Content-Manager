# Content-Manager
Rest API where an instructor and student manage their Webinars &amp; Courses

## Architectural overview
Relational database contains the following tables: course, content, subject, tag, content_courses(a joining table)
* webinar or video content can have many courses and a course can belong to multiple webinars (M:M)
* A course can have many subjects (1:M)
* Both courses and webnars/videos can have many tags (1:M)

## Tools and Technologies
* Django's rest framework - helps with restful routes, filtering backend and api view
* storage - sqlite3 db
* Libraries - A list can be found in the reqiurements.txt file
