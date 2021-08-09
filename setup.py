# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the Shuup Commerce Inc -
# SELF HOSTED SOFTWARE LICENSE AGREEMENT executed by Shuup Commerce Inc, DBA as SHUUP®
# and the Licensee.
import setuptools

try:
    import shuup_setup_utils
except ImportError:
    shuup_setup_utils = None


if __name__ == "__main__":
    setuptools.setup(
        cmdclass=(shuup_setup_utils.COMMANDS if shuup_setup_utils else {}),
        setup_requires=["setuptools>=34.0", "setuptools-gitver"],
        gitver=True,
    )
