import os
import datetime as dt
from re import findall
from pathlib import Path


def file_date(src: Path, use_name: bool = False, date_fmt: str | None = None) -> str | None:
    """Parsing date from filename by `date_fmt` or file `ctime`

    Parameters
    ----------
    date_fmt : str, None = None
        Date format in the filename
    """
    if not use_name:
        return str(dt.datetime.utcfromtimestamp(
            src.stat().st_ctime
        ).date())

    src_date = findall(date_fmt, str(src))
    if not src_date:
        return None

    # first date
    # TODO: convert to dt.date
    return src_date[0]


def files2dt_dir(src: Path, use_name: bool = False, date_fmt: str | None = None, copy: bool = False) -> None:
    """Sorting files to their `date` directory

    Parameters
    ----------
    src : Path
        Source directory to sort files from
    use_name : bool = False
        Files date by filename
    date_fmt : str, None = None
        Date format in the filename
    copy : bool = False
        Flag to `copy` files or create a new one
    """
    # TODO: output_fmt
    if not src.is_dir():
        print('Ignored, requires a directory:', src)
        exit()

    for child in src.iterdir():
        if not child.is_file():
            print('Ignored, not a file:', child)
            continue

        child_date = file_date(child, use_name=use_name, date_fmt=date_fmt)
        if child_date is None:
            print(f"Ignored, `{date_fmt = }` is not matched:", child)
            continue

        child_date = child.parent.joinpath(child_date)
        if not child_date.is_dir():
            child_date.mkdir()

        dst = child_date.joinpath(child.name)
        if dst.is_file():
            print('Ignored, file exists:', dst)
            continue

        if not copy:
            child.rename(dst)
        else:
            dst.touch()
