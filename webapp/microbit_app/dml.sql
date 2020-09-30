DELETE FROM user;
DELETE FROM history;
DELETE FROM room;
DELETE FROM microbit;

INSERT INTO user
    ('username', 'password')
    VALUES ('admin', 'pbkdf2:sha256:150000$Iie6oZMs$a8f6aba2fd335f9ace9f3ca00a06fe4a855040da2307cd768e0ec7a2e4405921')
;
