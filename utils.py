#!/usr/bin/env python
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    from pathlib import Path

    from posts.utils.fs import files2dt_dir


    files_dir = Path('trash')
    files2dt_dir(files_dir, use_name=True, copy=False, date_fmt='\d{4}-\d{2}-\d{2}')
