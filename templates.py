#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    import datetime as dt

    from posts.templates.twitter.BangDream import create


    j = create(
        dt.date(2022, 12, 13),
        ('BangDream', 'FullCombo'),
        tuple(),
        '2 HARD'
    )
    print(j)
