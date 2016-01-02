# proxmox-deploy is cli-based deployment tool for Proxmox
#
# Copyright (c) 2015 Nick Douma <n.douma@nekoconeko.nl>
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see http://www.gnu.org/licenses/.


class CommandInvocationException(RuntimeError):
    def __init__(self, message, stdout=None, stderr=None):
        # Call the base class constructor with the parameters it needs
        super(CommandInvocationException, self).__init__(message)
        self.stdout = stdout
        self.stderr = stderr


class SSHCommandInvocationException(CommandInvocationException):
    pass
