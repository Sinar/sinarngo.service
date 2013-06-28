from collective.grok import gs
from sinarngo.service import MessageFactory as _

@gs.importstep(
    name=u'sinarngo.service', 
    title=_('sinarngo.service import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('sinarngo.service.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
