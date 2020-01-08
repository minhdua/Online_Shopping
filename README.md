# Online shopping

### django

### Mysql
```shell
1.	install
		sudo apt-get install mysql-server
		sudo apt-get install python-mysqldb
		pip install mysqlclient
		sudo apt-get install mysql-server
2.	check Is MySQL running?
		systemctl status mysql.service
3.  connect database
    edit mysite/setting.py
    	ENGINE
      OPTIONS={
        'read_default_file':'/etc/mysql/my.cnf',
      }
      add file /etc/mysql/my.cnf
      [client]
      host = 127.0.0.1
      database = onlineshopping_db
      user = admin
      password = admin198
      default-character-set = utf8
      use Django to create the database tables
4. create  database
4.	setup
		sudo mysql -u root -p
		GRANT ALL ON django_db.* TO 'djangouser'@'localhost' IDENTIFIED BY 'mypassword';
5 show
		database:
			show databases;
			show schemas;
6 create table  python manage.py migrate
	  table
			show tables;
		  describe <tablenames>
```
### django Rest framwork

### Stripe

### Post man
- [dynamic variables](https://learning.getpostman.com/docs/postman/variables-and-environments/variables-list/)
- [database schemas](https://app.dbdesigner.net/designer/schema/291345)
