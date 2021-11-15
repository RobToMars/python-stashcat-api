# -*- coding: UTF-8 -*-# enable debugging

"""
Channels endpoints:
/channels/addModeratorStatus
/channels/availableInvites
/channels/changePermissions
/channels/confirmMembershipRequest
/channels/create
/channels/createInvite
/channels/declineMembershipRequest
/channels/delete
/channels/edit
/channels/editDescription
/channels/editPassword
/channels/encryptionUpgradeAvailable
/channels/files
/channels/info
/channels/join
/channels/members
/channels/quit
/channels/recommendations
/channels/removeModeratorStatus
/channels/removeUser
/channels/rename
/channels/setUserWritePermissions
/channels/subscripted
/channels/upgradeChannelEncryption
/channels/visible
"""

# Package Python library
from messenger.endpoint import Endpoint, endpoint


class Channels(Endpoint):
    def __init__(self, messenger):
        self.name = "channels"
        self.messenger = messenger

    @endpoint
    def addModeratorStatus(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def availableInvites(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def changePermissions(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def confirmMembershipRequest(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def create(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def createInvite(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def declineMembershipRequest(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def delete(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def edit(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def editDescription(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def editPassword(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def encryptionUpgradeAvailable(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def files(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def info(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def join(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def members(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def quit(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def recommendations(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def removeModeratorStatus(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def removeUser(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def rename(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def setUserWritePermissions(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def subscripted(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def upgradeChannelEncryption(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")

    @endpoint
    def visible(self, response):
        # TODO + JSONError:
        print(f"Response: {response}")
