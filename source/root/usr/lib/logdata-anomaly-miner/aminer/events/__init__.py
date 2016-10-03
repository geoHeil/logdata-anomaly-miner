# This file contains interface definition useful implemented by
# classes in this directory and for use from code outside this
# directory. All classes are defined in separate files, only the
# namespace references are added here to simplify the code.

class EventHandlerInterface:
  """This is the common interface of all components that can be
  notified on significant log data mining events. To avoid interference
  with the analysis process, the listener may only perform fast
  actions within the call. Longer running tasks have to be performed
  asynchronously."""

  def receiveEvent(self, eventType, eventMessage, sortedLogLines, eventData,
      eventSource):
    """Receive information about a detected event.
    @param eventType is a string with the event type class this
    event belongs to. This information can be used to interpret
    type-specific eventData objects. Together with the eventMessage
    and sortedLogLines, this can be used to create generic log messages.
    @param sortedLogLines sorted list of log lines that were considered
    when generating the event, as far as available to the time
    of the event. The list has to contain at least one line.
    @param eventData type-specific event data object, should not
    be used unless listener really knows about the eventType.
    @param eventSource reference to detector generating the event"""
    raise Exception('Interface method called')


class EventSourceInterface:
  """This is the common interface of all event sources. Component
  not implementing this interface may still emit events without
  support for callbacks."""

  def whitelistEvent(self, eventType, sortedLogLines, eventData,
      whitelistingData):
    """Whitelist an event generated by this source using the information
    emitted when generating the event.
    @return a message with information about whitelisting
    @throws NotImplementedError if this source does not support
    whitelisting per se
    @throws Exception when whitelisting of this special event
    using given whitelistingData was not possible."""
    raise Exception('Interface method called')


# Add also the namespace references to classes defined in this
# directory.

from DefaultMailNotificationEventHandler import DefaultMailNotificationEventHandler
from SimpleUnparsedAtomHandler import SimpleUnparsedAtomHandler
from StreamPrinterEventHandler import StreamPrinterEventHandler
from SyslogWriterEventHandler import SyslogWriterEventHandler
from Utils import VolatileLogarithmicBackoffEventHistory
