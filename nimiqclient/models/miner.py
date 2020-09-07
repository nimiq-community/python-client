__all__ = ["PoolConnectionState", "WorkInstructions"]

from enum import Enum


class PoolConnectionState(int, Enum):
    """
    Pool connection state information returned by the server.
    """

    CONNECTED = 0
    """Connected."""
    CONNECTING = 1
    """Connecting."""
    CLOSED = 2
    """Closed."""


class WorkInstructions:
    """
    Work instructions receipt returned by the server.

    :param data: Hex-encoded block header. This is what should be passed through the hash function.
        The last 4 bytes describe the nonce, the 4 bytes before are the current timestamp.
        Most implementations allow the miner to arbitrarily choose the nonce and to update the timestamp without requesting new work instructions.
    :type data: str
    :param suffix: Hex-encoded block without the header. When passing a mining result to submitBlock, append the suffix to the data string with selected nonce.
    :type suffix: str
    :param target: Compact form of the hash target to submit a block to this client.
    :type target: int
    :param algorithm: Field to describe the algorithm used to mine the block. Always nimiq-argon2 for now.
    :type algorithm: str
    """

    def __init__(self, data, suffix, target, algorithm):
        self.data = data
        self.suffix = suffix
        self.target = target
        self.algorithm = algorithm
