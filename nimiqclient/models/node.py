__all__ = ["ConsensusState", "SyncStatus", "LogLevel"]

from enum import Enum


class ConsensusState(str, Enum):
    """
    Consensus state returned by the server.
    """

    CONNECTING = "connecting"
    """Connecting."""
    SYNCING = "syncing"
    """Syncing blocks."""
    ESTABLISHED = "established"
    """Consensus established."""

    def __str__(self):
        return self.value


class SyncStatus:
    """
    Syncing status returned by the server.

    :param startingBlock: The block at which the import started (will only be reset, after the sync reached his head).
    :type startingBlock: int
    :param currentBlock: The current block, same as blockNumber.
    :type currentBlock: int
    :param highestBlock: The estimated highest block.
    :type highestBlock: int
    """

    def __init__(self, startingBlock, currentBlock, highestBlock):
        self.startingBlock = startingBlock
        self.currentBlock = currentBlock
        self.highestBlock = highestBlock


class LogLevel(str, Enum):
    """
    Used to set the log level in the JSONRPC server.
    """

    TRACE = "trace"
    """Trace level log."""
    VERBOSE = "verbose"
    """Verbose level log."""
    DEBUG = "debug"
    """Debugging level log."""
    INFO = "info"
    """Info level log."""
    WARN = "warn"
    """Warning level log."""
    ERROR = "error"
    """Error level log."""
    ASSERT = "assert"
    """Assertions level log."""

    def __str__(self):
        return self.value
