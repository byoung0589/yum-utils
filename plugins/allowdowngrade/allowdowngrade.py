# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Library General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#
# by Panu Matilainen <pmatilai@laiskiainen.org>

from yum.plugins import TYPE_INTERFACE
from rpm import RPMPROB_FILTER_OLDPACKAGE 

requires_api_version = '2.4'
plugin_type = (TYPE_INTERFACE,)

def config_hook(conduit):
    parser = conduit.getOptParser()
    parser.add_option('--allow-downgrade', dest='allow_downgrade',
                      action='store_true', default=False,
                      help='Allow packages to be downgraded')

def postresolve_hook(conduit):
    opts, args = conduit.getCmdLine()
    if opts.allow_downgrade:
        tsInfo = conduit.getTsInfo()
        tsInfo.probFilterFlags.append(RPMPROB_FILTER_OLDPACKAGE)

