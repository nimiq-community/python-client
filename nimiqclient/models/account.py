__all__ = ["AccountType", "Account", "VestingContract", "HTLC", "Wallet"]

__metaclass__ = type

from enum import Enum


class AccountType(int, Enum):
    """
    Type of a Nimiq account.
    """

    BASIC = 0
    """Normal Nimiq account."""
    VESTING = 1
    """Vesting contract."""
    HTLC = 2
    """Hashed Timelock Contract."""


class Account:
    """
    Normal Nimiq account object returned by the server.

    :param id: Hex-encoded 20 byte address.
    :type id: str
    :param address: User friendly address (NQ-address).
    :type address: str
    :param balance: Balance of the account (in smallest unit).
    :type balance: int
    :param type: The account type associated with the account.
    :type type: AccountType
    """

    def __init__(self, id, address, balance, type):
        self.id = id
        self.address = address
        self.balance = balance
        self.type = type


class VestingContract(Account):
    """
    Vesting contract object returned by the server.

    :param id: Hex-encoded 20 byte address.
    :type id: str
    :param address: User friendly address (NQ-address).
    :type address: str
    :param balance: Balance of the account (in smallest unit).
    :type balance: int
    :param type: The account type associated with the account.
    :type type: AccountType
    :param owner: Hex-encoded 20 byte address of the owner of the vesting contract.
    :type owner: str
    :param ownerAddress: User friendly address (NQ-address) of the owner of the vesting contract.
    :type ownerAddress: str
    :param vestingStart: The block that the vesting contracted commenced.
    :type vestingStart: int
    :param vestingStepBlocks: The number of blocks after which some part of the vested funds is released.
    :type vestingStepBlocks: int
    :param vestingStepAmount: The amount (in smallest unit) released every vestingStepBlocks blocks.
    :type vestingStepAmount: int
    :param vestingTotalAmount: The total amount (in smallest unit) that was provided at the contract creation.
    :type vestingTotalAmount: int
    """

    def __init__(
        self,
        id,
        address,
        balance,
        type,
        owner,
        ownerAddress,
        vestingStart,
        vestingStepBlocks,
        vestingStepAmount,
        vestingTotalAmount,
    ):
        super(VestingContract, self).__init__(id, address, balance, type)
        self.owner = owner
        self.ownerAddress = ownerAddress
        self.vestingStart = vestingStart
        self.vestingStepBlocks = vestingStepBlocks
        self.vestingStepAmount = vestingStepAmount
        self.vestingTotalAmount = vestingTotalAmount


class HTLC(Account):
    """
    Hashed Timelock Contract object returned by the server.

    :param id: Hex-encoded 20 byte address.
    :type id: str
    :param address: User friendly address (NQ-address).
    :type address: str
    :param balance: Balance of the account (in smallest unit).
    :type balance: int
    :param type: The account type associated with the account.
    :type type: AccountType
    :param sender: Hex-encoded 20 byte address of the sender of the HTLC.
    :type sender: str
    :param senderAddress: User friendly address (NQ-address) of the sender of the HTLC.
    :type senderAddress: str
    :param recipient: Hex-encoded 20 byte address of the recipient of the HTLC.
    :type recipient: str
    :param recipientAddress: User friendly address (NQ-address) of the recipient of the HTLC.
    :type recipientAddress: str
    :param hashRoot: Hex-encoded 32 byte hash root.
    :type hashRoot: str
    :param hashAlgorithm: Hash algorithm.
    :type hashAlgorithm: int
    :param hashCount: Number of hashes this HTLC is split into.
    :type hashCount: int
    :param timeout: Block after which the contract can only be used by the original sender to recover funds.
    :type timeout: int
    :param totalAmount: The total amount (in smallest unit) that was provided at the contract creation.
    :type totalAmount: int
    """

    def __init__(
        self,
        id,
        address,
        balance,
        type,
        sender,
        senderAddress,
        recipient,
        recipientAddress,
        hashRoot,
        hashAlgorithm,
        hashCount,
        timeout,
        totalAmount,
    ):
        super(HTLC, self).__init__(id, address, balance, type)
        self.sender = sender
        self.senderAddress = senderAddress
        self.recipient = recipient
        self.recipientAddress = recipientAddress
        self.hashRoot = hashRoot
        self.hashAlgorithm = hashAlgorithm
        self.hashCount = hashCount
        self.timeout = timeout
        self.totalAmount = totalAmount


class Wallet:
    """
    Nimiq wallet returned by the server.

    :param id: Hex-encoded 20 byte address.
    :type id: str
    :param address: User friendly address (NQ-address).
    :type address: str
    :param publicKey: Hex-encoded 32 byte Ed25519 public key.
    :type publicKey: str
    :param privateKey: Hex-encoded 32 byte Ed25519 private key.
    :type privateKey: str, optional
    """

    def __init__(self, id, address, publicKey, privateKey=None):
        self.id = id
        self.address = address
        self.publicKey = publicKey
        self.privateKey = privateKey
