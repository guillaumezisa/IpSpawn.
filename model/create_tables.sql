DROP TABLE IF EXISTS USERS;
CREATE TABLE USERS (
    ID_USER   SERIAL PRIMARY KEY,
    EMAIL     varchar(100),
    PSEUDO    varchar(100),
    PASSWORD  varchar(100),
    POINTS    int,
    PP        varchar(200),
    STATUS    int,
    DATES     date
);
