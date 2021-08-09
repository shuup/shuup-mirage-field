# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2021, Shuup Commerce Inc. All rights reserved.
#
# This source code is licensed under the Shuup Commerce Inc -
# SELF HOSTED SOFTWARE LICENSE AGREEMENT executed by Shuup Commerce Inc, DBA as SHUUP®
# and the Licensee.
import shuup.apps


class ShuupAppConfig(shuup.apps.AppConfig):
    name = "shuup_addon_template"
    label = "shuup_addon_template"
    verbose_name = "Shuup Addon Template"
    provides = {}
