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
    ("empty", 1, 0, 0, 0, 0, "Not active");

INSERT INTO history 
    ('date', 'microbit', 'min_temp', 'max_temp', 'min_light', 'max_light')
VALUES
    (DATE('now', '-14 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-14 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-14 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-13 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-13 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-13 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-12 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-12 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-12 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-11 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-11 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-11 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-10 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-10 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-10 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-9 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-9 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-9 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-8 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-8 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-8 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-7 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-7 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-7 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-6 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-6 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-6 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-5 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-5 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-5 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-4 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-4 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-4 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-3 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-3 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-3 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-2 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-2 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-2 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-1 day'), 'gozip', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-1 day'), 'vizup', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255)),
    (DATE('now', '-1 day'), 'empty', 15 + ABS(RANDOM() % 10), 25 + ABS(RANDOM() % 10), ABS(RANDOM() % 10), ABS(RANDOM() % 255));