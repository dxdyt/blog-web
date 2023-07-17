---
title: vprofile-project
date: 2023-07-17T12:19:54+08:00
draft: False
featuredImage: https://images.unsplash.com/photo-1687276154629-d4acac547d55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODk1Njc0NDJ8&ixlib=rb-4.0.3
featuredImagePreview: https://images.unsplash.com/photo-1687276154629-d4acac547d55?ixid=M3w0NjAwMjJ8MHwxfHJhbmRvbXx8fHx8fHx8fDE2ODk1Njc0NDJ8&ixlib=rb-4.0.3
---

# [devopshydclub/vprofile-project](https://github.com/devopshydclub/vprofile-project)

#######
### Prerequisites
- JDK 1.8 or later
- Maven 3 or later
- MySQL 5.6 or later

### Technologies 
- Spring MVC
- Spring Security
- Spring Data JPA
- Maven
- JSP
- MySQL
### Database
Here,we used Mysql DB 
MSQL DB Installation Steps for Linux ubuntu 14.04:
- $ sudo apt-get update
- $ sudo apt-get install mysql-server

Then look for the file :
- /src/main/resources/accountsdb
- accountsdb.sql file is a mysql dump file.we have to import this dump to mysql db server
- > mysql -u <user_name> -p accounts < accountsdb.sql


