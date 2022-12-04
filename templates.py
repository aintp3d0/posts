#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    import datetime as dt

    from posts.templates.twitter import create


    j = create(
        dt.date(2022, 12, 2),
        ('BangDream', 'FullCombo'),
        tuple(),
        '4 HARD'
    )
    print(j)
