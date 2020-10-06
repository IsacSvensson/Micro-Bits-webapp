INSERT INTO user 
    ('username', 'password')
VALUES
    ('test', 'pbkdf2:sha256:50000$TCI4GzcX$0de171a4f4dac32e3364c7ddc7c14f3e2fa61f2d17574483f7ffbb431b4acb2f'),
    ('other', 'pbkdf2:sha256:50000$kJPKsz6N$d2d4784f1b030a9761f5ccaeeaca413f27f2ecb76d6168407af962ddce849f79');

INSERT INTO room
    ('description', 'width', 'deepth')
VALUES
    ("test", 5, 6),
    ("other test", 2, 3);

INSERT INTO microbit
    ('id', 'room', 'temp', 'light', 'position_x', 'position_y', 'status')
VALUES
    ("gozip", 1, 25, 100, 4, 2, "Active"),
    ("vizup", 1, 28, 87, 1.7, 4.8, "Active"),
    ("empty", 1, NULL, NULL, NULL, NULL, "Not active");

INSERT INTO history 
    ('date', 'microbit', 'min_temp', 'max_temp', 'min_light', 'max_light')
VALUES
    ('2020-09-30', 'gozip', 1, 99, 1, 99),
    ('2020-09-30', 'vizup', 2, 100, 2, 100),
    ('2020-09-30', 'empty', 3, 101, 31, 101),
    (DATE('now', 'localtime'), 'gozip', 1, 99, 1, 99),
    (DATE('now', 'localtime'), 'vizup', 2, 100, 2, 100),
    (DATE('now', 'localtime'), 'empty', 3, 101, 31, 101);
