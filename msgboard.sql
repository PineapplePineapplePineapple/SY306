-- msgboard.sql
-- SQL statements that created our USERS and MESSAGES tables
-- Jacob Harrison

-- USERS table has Username, Name, Password, and Role with Username being the primary key and 'regular' being the default for Role
CREATE TABLE USERS (Username varchar(20) NOT NULL, Name varchar(50) NOT NULL, Password varchar(30) NOT NULL, Role varchar(7) NOT NULL DEFAULT 'regular', PRIMARY KEY (Username));

-- MESSAGES table has MID, Content, Username, and Time with MID being the primary key and Username being the foreign key referencing the USERS table
CREATE TABLE MESSAGES (MID int NOT NULL AUTO_INCREMENT, Content varchar(5000) NOT NULL, Username varchar(20) NOT NULL, Time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, PRIMARY KEY (MID), FOREIGN KEY (Username) REFERENCES USERS(Username) ON DELETE CASCADE ON UPDATE CASCADE );
