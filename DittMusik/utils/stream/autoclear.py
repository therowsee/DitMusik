#
# Copyright (C) 2021-2022 by therowsee@Github, < https://github.com/therowsee >.
#
# This file is part of < https://github.com/therowsee/DitMusik > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/therowsee/DitMusik/blob/master/LICENSE >
#
# All rights reserved.

import os

from config import autoclean


async def auto_clean(popped):
    try:
        rem = popped["file"]
        autoclean.remove(rem)
        count = autoclean.count(rem)
        if count == 0:
            if (
                "vid_" not in rem
                or "live_" not in rem
                or "index_" not in rem
            ):
                try:
                    os.remove(rem)
                except:
                    pass
    except:
        pass
