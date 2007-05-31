# browsershots.org ShotFactory 0.3-beta1
# Copyright (C) 2007 Johann C. Rocholl <johann@browsershots.org>
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
GUI-specific interface functions for Mac OS X.
"""

__revision__ = "$Rev$"
__date__ = "$Date$"
__author__ = "$Author$"

import os
import time
import appscript
import MacOS
from shotfactory03 import gui as base


class Gui(base.Gui):
    """
    Special functions for Mac OS X.
    """

    def shell(self, command):
        """Run a shell command."""
        os.system(command)

    def prepare_screen(self):
        self.bottom_skip = 4
        self.safari = None
        # Set screen resolution and color depth with Lynn Pye's cscreen
        # Freeware, available from http://www.pyehouse.com/lynn/cscreen.php
        self.shell('./cscreen -x %d -y %d -d %d -f'
                   % (self.width, self.height, self.bpp))

    def screenshot(self, filename):
        """Save the full screen to a PPM file."""
        self.shell('screencapture "%s.png"' % filename)
        self.shell('pngtopnm "%s.png" > "%s"' % (filename, filename))