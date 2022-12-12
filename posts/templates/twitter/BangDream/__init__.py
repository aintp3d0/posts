import datetime as dt
from typing import Iterable

from posts.utils.e import Symbols as S
from posts.utils.dt import jp_date
from posts.utils.str import startwith


def create(
        date: dt.date,
        tags: Iterable,
        mentions: Iterable,
        message: str
):
    """
    Returns
    -------
    str
        `date`
        `tags`
        `mentions`

        `message`
    """
    date = jp_date(date)
    r = f"{date}"

    if tags:
        r = f"{r}\n{', '.join(startwith(tag, S.hashtag) for tag in tags)}"

    if mentions:
        r = f"{r}\n{', '.join(startwith(mention, S.at) for mention in mentions)}"

    if message:
        r = f"{r}\n\n{message}"

    return r.strip()
