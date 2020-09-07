__all__ = ["PeerAddressState", "PeerConnectionState", "PeerStateCommand", "Peer"]

from enum import Enum


class PeerAddressState(int, Enum):
    """
    Peer address state returned by the server.
    """

    NEW = 1
    """New peer."""
    ESTABLISHED = 2
    """Established peer."""
    TRIED = 3
    """Already tried peer."""
    FAILED = 4
    """Peer failed."""
    BANNED = 5
    """Balled peer."""


class PeerConnectionState(int, Enum):
    """
    Peer connection state returned by the server.
    """

    NEW = 1
    """New connection."""
    CONNECTING = 2
    """Connecting."""
    CONNECTED = 3
    """Connected."""
    NEGOTIATING = 4
    """Negotiating connection."""
    ESTABLISHED = 5
    """Connection established."""
    CLOSED = 6
    """Connection closed."""


class PeerStateCommand(str, Enum):
    """
    Commands to change the state of a peer.
    """

    CONNECT = "connect"
    """Connect."""
    DISCONNECT = "disconnect"
    """Disconnect."""
    BAN = "ban"
    """Ban."""
    UNBAN = "unban"
    """Unban."""

    def __str__(self):
        return self.value


class Peer:
    """
    Peer information returned by the server.

    :param id: Peer id.
    :type id: str
    :param address: Peer address.
    :type address: str
    :param addressState: Peer address state.
    :type addressState: int
    :param connectionState: Peer connection state.
    :type connectionState: PeerConnectionState, optional
    :param version: Node version the peer is running.
    :type version: int, optional
    :param timeOffset: Time offset with the peer (in miliseconds).
    :type timeOffset: int, optional
    :param headHash: Hash of the head block of the peer.
    :type headHash: str, optional
    :param latency: Latency to the peer.
    :type latency: int, optional
    :param rx: Received bytes.
    :type rx: int, optional
    :param tx: Sent bytes.
    :type tx: int, optional
    """

    def __init__(
        self,
        id,
        address,
        addressState,
        connectionState=None,
        version=None,
        timeOffset=None,
        headHash=None,
        latency=None,
        rx=None,
        tx=None,
    ):
        self.id = id
        self.address = address
        self.addressState = addressState
        self.connectionState = connectionState
        self.version = version
        self.timeOffset = timeOffset
        self.headHash = headHash
        self.latency = latency
        self.rx = rx
        self.tx = tx
