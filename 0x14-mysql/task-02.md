In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server **(web-01)** to replicate from.

 -Create a database named `tyrell_corp`.
 -Within the `tyrell_corp` database create a table named `nexus6` and add at least one entry to it.
 -Make sure that `holberton_user` has `SELECT` permissions on your table so that we can check that the table exists and is not empty.


```sh
sudo mysql
```

```sql
CREATE DATABASE IF NOT EXISTS tyrell_corp;
USE tyrell_corp;
CREATE TABLE IF NOT EXISTS nexus6(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL,
    PRIMARY KEY(id)
);
INSERT INTO nexus6 (name) VALUES ('Leon');
GRANT SELECT ON *.* TO 'holberton_user'@'localhost';
```
