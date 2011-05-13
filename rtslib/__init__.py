'''
This file is part of RTSLib Community Edition.
Copyright (c) 2011 by RisingTide Systems LLC

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as
published by the Free Software Foundation, version 3 (AGPLv3).

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

import utils

from root import RTSRoot
from utils import RTSLibError, RTSLibBrokenLink

from target import LUN, MappedLUN
from target import NodeACL, NetworkPortal, TPG, Target, FabricModule

from tcm import FileIOBackstore, IBlockBackstore
from tcm import FileIOStorageObject, IBlockStorageObject
from tcm import PSCSIBackstore, RDDRBackstore, RDMCPBackstore
from tcm import PSCSIStorageObject, RDDRStorageObject, RDMCPStorageObject

__version__ = 'GIT_VERSION'
__author__ = "Jerome Martin <jxm@risingtidesystems.com>"
__url__ = "http://www.risingtidesystems.com"
__description__ = "API for RisingTide Systems generic SCSI target."
__license__ = __doc__