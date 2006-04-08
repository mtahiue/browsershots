# -*- coding: utf-8 -*-
# browsershots.org
# Copyright (C) 2006 Johann C. Rocholl <johann@browsershots.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston,
# MA 02111-1307, USA.

"""
Home page.
"""

__revision__ = '$Rev$'
__date__ = '$Date$'
__author__ = '$Author$'

from shotserver03.interface import xhtml
from shotserver03.segments import recent, inputurl, browsers, sponsors

def title():
    return "Test Your Design"

def body():
    # xhtml.write_tag_line('p', "<b>Status:</b> A design study, a technology preview, a work in progress.")
    recent.write()

    xhtml.write_open_tag_line('form', action="/post/submit/", method="post")
    inputurl.write()
    browsers.write()

    sponsors.write()
    xhtml.write_close_tag_line('form')
