use com_data;
CREATE TABLE base_dict(
#id int(11) NOT NULL auto_increment,
word varchar(20) NOT NULL,
emotion varchar(8) default NULL,
PRIMARY KEY(word)
)ENGINE = MyISAM DEFAULT CHARSET=utf8