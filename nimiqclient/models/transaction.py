__all__ = ["OutgoingTransaction", "Transaction", "TransactionReceipt"]

from .account import AccountType
import json


class TXBase:
    """
    Enables accessing the attribute 'from' from outside using 'from_'.
    """

    def __getattr__(self, attr):
        if attr == "from_":
            return self.__dict__.__getitem__("from")
        else:
            return self.__dict__.__getitem__(attr)

    def __setattr__(self, attr, value):
        if attr == "from_":
            self.__dict__.__setitem__("from", value)
        else:
            self.__dict__.__setitem__(attr, value)

    def __repr__(self):
        return json.dumps(self.__dict__)


def preprocess_args(func):
    """
    Decorator to change the parameter 'from' to 'from_' during deserialization.
    """

    def inner(*args, **kwargs):
        if "from" in kwargs:
            kwargs["from_"] = kwargs.pop("from")
        func(*args, **kwargs)

    return inner


class OutgoingTransaction(TXBase):
    """
    Used to pass the data to send transaccions.

    :param from_: The address the transaction is send from.
    :type from_: str
    :param fromType: The account type at the given address.
    :type fromType: AccountType, optional
    :param to: The address the transaction is directed to.
    :type to: str
    :param toType: The account type at the given address.
    :type toType: AccountType, optional
    :param value: Integer of the value (in smallest unit) sent with this transaction.
    :type value: int
    :param fee: Integer of the fee (in smallest unit) for this transaction.
    :type fee: int
    :param data: Hex-encoded contract parameters or a message.
    :type data: str, optional
    """

    def __init__(
        self,
        from_,
        to,
        value,
        fee,
        fromType=AccountType.BASIC,
        toType=AccountType.BASIC,
        data=None,
    ):
        self.from_ = from_
        self.fromType = fromType
        self.to = to
        self.toType = toType
        self.value = value
        self.fee = fee
        self.data = data


class Transaction(TXBase):
    """
    Transaction returned by the server.

    :param hash: Hex-encoded hash of the transaction.
    :type hash: str
    :param blockHash: Hex-encoded hash of the block containing the transaction.
    :type blockHash: str, optional
    :param blockNumber: Height of the block containing the transaction.
    :type blockNumber: int, optional
    :param timestamp: UNIX timestamp of the block containing the transaction.
    :type timestamp: int, optional
    :param confirmations: Number of confirmations of the block containing the transaction.
    :type confirmations: int, optional
    :param transactionIndex: Index of the transaction in the block.
    :type transactionIndex: int, optional
    :param from_: Hex-encoded address of the sending account.
    :type from_: str
    :param fromAddress: Nimiq user friendly address (NQ-address) of the sending account.
    :type fromAddress: str
    :param to: Hex-encoded address of the recipient account.
    :type to: str
    :param toAddress: Nimiq user friendly address (NQ-address) of the recipient account.
    :type toAddress: str
    :param value: Integer of the value (in smallest unit) sent with this transaction.
    :type value: int
    :param fee: Integer of the fee (in smallest unit) for this transaction.
    :type fee: int
    :param data: Hex-encoded contract parameters or a message.
    :type data: str, optional
    :param flags: Bit-encoded transaction flags.
    :type flags: int
    :param valid: Is valid transaction.
    :type valid: bool, optional
    :param inMempool: Transaction is in mempool.
    :type inMempool: bool, optional
    """

    @preprocess_args
    def __init__(
        self,
        hash,
        from_,
        fromAddress,
        to,
        toAddress,
        value,
        fee,
        flags,
        blockHash=None,
        blockNumber=None,
        timestamp=None,
        confirmations=0,
        transactionIndex=None,
        data=None,
        valid=None,
        inMempool=None,
    ):
        self.hash = hash
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.timestamp = timestamp
        self.confirmations = confirmations
        self.transactionIndex = transactionIndex
        self.from_ = from_
        self.fromAddress = fromAddress
        self.to = to
        self.toAddress = toAddress
        self.value = value
        self.fee = fee
        self.data = data
        self.flags = flags
        self.valid = valid
        self.inMempool = inMempool


class TransactionReceipt:
    """
    Transaction receipt returned by the server.

    :param transactionHash: Hex-encoded hash of the transaction.
    :type transactionHash: str
    :param transactionIndex: Integer of the transactions index position in the block.
    :type transactionIndex: int
    :param blockHash: Hex-encoded hash of the block where this transaction was in.
    :type blockHash: str
    :param blockNumber: Block number where this transaction was in.
    :type blockNumber: int
    :param confirmations: Number of confirmations for this transaction (number of blocks on top of the block where this transaction was in).
    :type confirmations: int
    :param timestamp: Timestamp of the block where this transaction was in.
    :type timestamp: int
    """

    def __init__(
        self,
        transactionHash,
        transactionIndex,
        blockHash,
        blockNumber,
        confirmations,
        timestamp,
    ):
        self.transactionHash = transactionHash
        self.transactionIndex = transactionIndex
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.confirmations = confirmations
        self.timestamp = timestamp
