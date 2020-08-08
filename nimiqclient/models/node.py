__all__ = [
	"ConsensusState",
	"SyncStatus"
]

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

class SyncStatus():
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
