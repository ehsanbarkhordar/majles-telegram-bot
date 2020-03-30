#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bot.view import main
from db.models import create_tables

if __name__ == '__main__':
    create_tables()
    main()
