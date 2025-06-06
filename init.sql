-- Book database
CREATE DATABASE IF NOT EXISTS BookDB;
USE BookDB;

-- Dropping exisiting tables to start from scratch
DROP TABLE IF EXISTS ReadCount;
DROP TABLE IF EXISTS Book_User;
DROP TABLE IF EXISTS Book_Genre;
DROP TABLE IF EXISTS Book_Creator;
DROP TABLE IF EXISTS Book_Series;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS BookType;
DROP TABLE IF EXISTS Creator;
DROP TABLE IF EXISTS Language;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Role;
DROP TABLE IF EXISTS Rating;
DROP TABLE IF EXISTS Shelf;
DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Series;

-- Initiating tables

-- Tables without foreign keys
CREATE TABLE IF NOT EXISTS Series (
	ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Name NVARCHAR(255) NOT NULL,
	Description LONGTEXT
);


CREATE TABLE IF NOT EXISTS User (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Username NVARCHAR(50) NOT NULL,
    FirstName NVARCHAR(50) NOT NULL,
    FamilyNamePreposition NVARCHAR(50),  -- Tussenvoegsel
    LastName NVARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS BookType (
	ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	Type NVARCHAR(50) NOT NULL,
	Description NVARCHAR(255)
	
);

CREATE TABLE IF NOT EXISTS Language  (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Language NVARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Genre NVARCHAR(50) NOT NULL,
    Description NVARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Role (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Role NVARCHAR(50) NOT NULL,
    Description NVARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Rating (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Rating INT NOT NULL,
    Description NVARCHAR(255)    
);

CREATE TABLE IF NOT EXISTS Shelf (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Shelf NVARCHAR(50) NOT NULL,
    Description NVARCHAR(255)
);

CREATE TABLE IF NOT EXISTS Publisher (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL,
    Country NVARCHAR(50)
);

CREATE TABLE IF NOT EXISTS  Creator (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    FamilyNamePreposition NVARCHAR(50),  -- Tussenvoegsel
    LastName NVARCHAR(50) NOT NULL,
    Nationality NVARCHAR(50),
    Birthday DATE,
    Pseudonym BOOLEAN,
    RealFirstName NVARCHAR(50),
    RealFamilyNamePreposition NVARCHAR(50),
    RealLastName NVARCHAR(50)
);

-- Tables with foreign keys
CREATE TABLE IF NOT EXISTS Book (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ISBN NVARCHAR(13) NOT NULL,
    Title NVARCHAR(255) NOT NULL,
    Subtitle NVARCHAR(255),
    Description LONGTEXT,
    OriginalPublicationDate DATE NOT NULL,
    EditionPublicationDate DATE,
    EditionLanguageID INT UNSIGNED,
    OriginalLanguageID INT UNSIGNED,  
    PublisherID INT UNSIGNED,    
    NumberOfPages INT NOT NULL,
    BookTypeID INT UNSIGNED,
    CONSTRAINT `fk_edition_language`
        FOREIGN KEY (EditionLanguageID) REFERENCES Language (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_original_language`
        FOREIGN KEY (OriginalLanguageID) REFERENCES Language (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_publisher`
        FOREIGN KEY (PublisherID) REFERENCES Publisher (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_type`
    	FOREIGN KEY (BookTypeID) REFERENCES BookType (ID)
    	ON DELETE RESTRICT
    	ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS Book_Genre (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    BookID INT UNSIGNED,
    GenreID INT UNSIGNED,
    CONSTRAINT `fk_book_to_genre`
        FOREIGN KEY (BookID) REFERENCES Book (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_genre_to_book`
        FOREIGN KEY (GenreID) REFERENCES Genre (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS Book_Series (
	ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	BookID INT UNSIGNED,
	SeriesID INT UNSIGNED,
	Entry INT UNSIGNED,
	CONSTRAINT `fk_book_to_series`
		FOREIGN KEY(BookID) REFERENCES Book (ID)
		ON DELETE RESTRICT
		ON UPDATE RESTRICT,
	CONSTRAINT `fk_series_to_book`
		FOREIGN KEY(SeriesID) REFERENCES Series (ID)
		ON DELETE RESTRICT
		ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS ReadCount (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    BookID INT UNSIGNED,
    UserID INT UNSIGNED,
    Cnt INT UNSIGNED,
   CONSTRAINT `fk_reader_cnt`
    	FOREIGN KEY (UserID) REFERENCES User (ID)
    	ON DELETE CASCADE
    	ON UPDATE RESTRICT,
    CONSTRAINT `fk_read_cnt`
        FOREIGN KEY (BookID) REFERENCES Book (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS Book_Creator (
    ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    BookID INT UNSIGNED NOT NULL,
    CreatorID INT UNSIGNED NOT NULL,
    RoleID int UNSIGNED NOT NULL,
    CONSTRAINT `fk_book_to_creator`
        FOREIGN KEY (BookID) REFERENCES Book (ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_creator_to_book`
        FOREIGN KEY (CreatorID) REFERENCES Creator (ID)
        ON DELETE CASCADE
        ON UPDATE restrict,
    CONSTRAINT `fk_role_creator`
        FOREIGN KEY (RoleID) REFERENCES Role (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT
);

CREATE TABLE IF NOT EXISTS Book_User (
	ID INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	UserID INT UNSIGNED NOT NULL,
	BookID INT UNSIGNED NOT NULL,
	RatingID INT UNSIGNED,
    CurrentShelf INT UNSIGNED,
    Owned BOOLEAN NOT NULL,
    CONSTRAINT `fk_rating`
        FOREIGN KEY (RatingID) REFERENCES Rating (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_shelf`
        FOREIGN KEY (CurrentShelf) REFERENCES Shelf (ID)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT `fk_reader`
    	FOREIGN KEY (UserID) REFERENCES User (ID)
    	ON DELETE CASCADE
    	ON UPDATE RESTRICT,
    CONSTRAINT `fk_shelved_book`
    	FOREIGN KEY (BookID) REFERENCES Book (ID)
    	ON DELETE CASCADE
    	ON UPDATE RESTRICT
);