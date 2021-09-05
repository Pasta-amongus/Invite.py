import datetime,os,fortnitepy

from Fortnite import colored
TimeInUTC = datetime.datetime.utcnow().strftime('%H:%M:%S')

async def event_friend_add(self, Friend):
    TimeInUTC = datetime.datetime.utcnow().strftime('%H:%M:%S')
    if self.Settings["InviteFriendOnFriendAdded"] or Friend.id in self.Settings["GiveFullAccessTo"]:
        try:
            await Friend.invite()
