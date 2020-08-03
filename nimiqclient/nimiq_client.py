__all__ = [
    "NimiqClient",
    "InternalErrorException",
    "RemoteErrorException",
    "ConnectionErrorException",
    "ConsensusState",
    "AccountType",
    "LogLevel",
    "PeerAddressState",
    "PeerConnectionState",
    "PeerStateCommand",
    "PoolConnectionState",
    "Account",
    "VestingContract",
    "HTLC",
    "Wallet",
    "OutgoingTransaction",
    "Transaction",
    "Block",
    "BlockTemplateHeader",
    "BlockTemplateBody",
    "BlockTemplate",
    "TransactionReceipt",
    "WorkInstructions",
    "MempoolInfo",
    "Peer",
    "SyncStatus"
]

import requests
from requests.auth import HTTPBasicAuth
from enum import Enum
import logging

logger = logging.getLogger(__name__)

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

class Account():
    """
    Normal Nimiq account object returned by the server.
    """
    def __init__(self, id, address, balance, type):
        self.id = id
        """Hex-encoded 20 byte address."""
        self.address = address
        """User friendly address (NQ-address)."""
        self.balance = balance
        """Balance of the account (in smallest unit)."""
        self.type = type
        """The account type associated with the account."""

class VestingContract():
    """
    Vesting contract object returned by the server.
    """
    def __init__(self, id, address, balance, type, owner, ownerAddress, vestingStart, vestingStepBlocks, vestingStepAmount, vestingTotalAmount):
        self.id = id
        """Hex-encoded 20 byte address."""
        self.address = address
        """User friendly address (NQ-address)."""
        self.balance = balance
        """Balance of the account (in smallest unit)."""
        self.type = type
        """The account type associated with the account."""
        self.owner = owner
        """Hex-encoded 20 byte address of the owner of the vesting contract."""
        self.ownerAddress = ownerAddress
        """User friendly address (NQ-address) of the owner of the vesting contract."""
        self.vestingStart = vestingStart
        """The block that the vesting contracted commenced."""
        self.vestingStepBlocks = vestingStepBlocks
        """The number of blocks after which some part of the vested funds is released."""
        self.vestingStepAmount = vestingStepAmount
        """The amount (in smallest unit) released every vestingStepBlocks blocks."""
        self.vestingTotalAmount = vestingTotalAmount
        """The total amount (in smallest unit) that was provided at the contract creation."""

class HTLC():
    """
    Hashed Timelock Contract object returned by the server.
    """
    def __init__(self, id, address, balance, type, sender, senderAddress, recipient, recipientAddress, hashRoot, hashAlgorithm, hashCount, timeout, totalAmount):
        self.id = id
        """Hex-encoded 20 byte address."""
        self.address = address
        """User friendly address (NQ-address)."""
        self.balance = balance
        """Balance of the account (in smallest unit)."""
        self.type = type
        """The account type associated with the account."""
        self.sender = sender
        """Hex-encoded 20 byte address of the sender of the HTLC."""
        self.senderAddress = senderAddress
        """User friendly address (NQ-address) of the sender of the HTLC."""
        self.recipient = recipient
        """Hex-encoded 20 byte address of the recipient of the HTLC."""
        self.recipientAddress = recipientAddress
        """User friendly address (NQ-address) of the recipient of the HTLC."""
        self.hashRoot = hashRoot
        """Hex-encoded 32 byte hash root."""
        self.hashAlgorithm = hashAlgorithm
        """Hash algorithm."""
        self.hashCount = hashCount
        """Number of hashes this HTLC is split into."""
        self.timeout = timeout
        """Block after which the contract can only be used by the original sender to recover funds."""
        self.totalAmount = totalAmount
        """The total amount (in smallest unit) that was provided at the contract creation."""

class RawAccount():
    """
    Nimiq account returned by the server. The especific type is in the associated value.
    """
    def __init__(self, *args, **kwargs):
        type = kwargs.get("type")
        if type == AccountType.BASIC:
            self.value = Account(**kwargs)
        elif type == AccountType.VESTING:
            self.value = VestingContract(**kwargs)
        elif type == AccountType.HTLC:
            self.value = HTLC(**kwargs)

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

class Wallet():
    """
    Nimiq wallet returned by the server.
    """
    def __init__(self, id, address, publicKey, privateKey = None):
        self.id = id
        """Hex-encoded 20 byte address."""
        self.address = address
        """User friendly address (NQ-address)."""
        self.publicKey = publicKey
        """Hex-encoded 32 byte Ed25519 public key."""
        self.privateKey = privateKey
        """Hex-encoded 32 byte Ed25519 private key."""

class OutgoingTransaction():
    """
    Used to pass the data to send transaccions.
    """
    def __init__(self, from_, to, value, fee, fromType = AccountType.BASIC, toType = AccountType.BASIC, data = None):
        self.from_ = from_
        """The address the transaction is send from."""
        self.fromType = fromType
        """The account type at the given address."""
        self.to = to
        """The address the transaction is directed to."""
        self.toType = toType
        """The account type at the given address."""
        self.value = value
        """Integer of the value (in smallest unit) sent with this transaction."""
        self.fee = fee
        """Integer of the fee (in smallest unit) for this transaction."""
        self.data = data
        """Hex-encoded contract parameters or a message."""

    def __getattribute__(self, attr):
        if attr.endswith("_"):
            attr = attr[:-1]
        return self.__dict__[attr]

    def __setattribute__(self, key, value):
        if key.endswith("_"):
            key = key[:-1]
        self.__dict__[key] = value

class Transaction():
    """
    Transaction returned by the server.
    """
    def __init__(self, hash, from_, fromAddress, to, toAddress, value, fee, flags, blockHash = None, blockNumber = None, timestamp = None, confirmations = 0, transactionIndex = None, data = None, valid = None, inMempool = None):
        self.hash = hash
        """Hex-encoded hash of the transaction."""
        self.blockHash = blockHash
        """Hex-encoded hash of the block containing the transaction."""
        self.blockNumber = blockNumber
        """Height of the block containing the transaction."""
        self.timestamp = timestamp
        """UNIX timestamp of the block containing the transaction."""
        self.confirmations = confirmations
        """Number of confirmations of the block containing the transaction."""
        self.transactionIndex = transactionIndex
        """Index of the transaction in the block."""
        self.from_ = from_
        """Hex-encoded address of the sending account."""
        self.fromAddress = fromAddress
        """Nimiq user friendly address (NQ-address) of the sending account."""
        self.to = to
        """Hex-encoded address of the recipient account."""
        self.toAddress = toAddress
        """Nimiq user friendly address (NQ-address) of the recipient account."""
        self.value = value
        """Integer of the value (in smallest unit) sent with this transaction."""
        self.fee = fee
        """Integer of the fee (in smallest unit) for this transaction."""
        self.data = data
        """Hex-encoded contract parameters or a message."""
        self.flags = flags
        """Bit-encoded transaction flags."""
        self.valid = valid
        """Is valid transaction."""
        self.inMempool = inMempool
        """Transaction is in mempool."""

    def __getattribute__(self, attr):
        if attr.endswith("_"):
            attr = attr[:-1]
        return self.__dict__[attr]

    def __setattribute__(self, key, value):
        if key.endswith("_"):
            key = key[:-1]
        self.__dict__[key] = value

    @staticmethod
    def fromDict(transaction):
        if "from" in transaction:
            transaction["from_"] = transaction.pop("from")
        return Transaction(**transaction)


class Block():
    """
    Block returned by the server.
    """
    def __init__(self, number, hash, pow, parentHash, nonce, bodyHash, accountsHash, difficulty, timestamp, confirmations, miner, minerAddress, extraData, size, transactions):
        self.number = number
        """Height of the block."""
        self.hash = hash
        """Hex-encoded 32-byte hash of the block."""
        self.pow = pow
        """Hex-encoded 32-byte Proof-of-Work hash of the block."""
        self.parentHash = parentHash
        """Hex-encoded 32-byte hash of the predecessor block."""
        self.nonce = nonce
        """The nonce of the block used to fulfill the Proof-of-Work."""
        self.bodyHash = bodyHash
        """Hex-encoded 32-byte hash of the block body Merkle root."""
        self.accountsHash = accountsHash
        """Hex-encoded 32-byte hash of the accounts tree root."""
        self.difficulty = difficulty
        """Block difficulty, encoded as decimal number in string."""
        self.timestamp = timestamp
        """UNIX timestamp of the block"""
        self.confirmations = confirmations
        """Number of confirmations for this transaction (number of blocks on top of the block where this transaction was in)."""
        self.miner = miner
        """Hex-encoded 20 byte address of the miner of the block."""
        self.minerAddress = minerAddress
        """User friendly address (NQ-address) of the miner of the block."""
        self.extraData = extraData
        """Hex-encoded value of the extra data field, maximum of 255 bytes."""
        self.size = size
        """Block size in byte."""
        for index, transaction in enumerate(transactions):
            if type(transaction) is not str and type(transaction) is not Transaction:
                transactions[index] = Transaction.fromDict(transaction)
        self.transactions = transactions
        """Array of transactions. Either represented by the transaction hash or a Transaction object."""

class BlockTemplateHeader():
    """
    Block template header returned by the server.
    """
    def __init__(self, version, prevHash, interlinkHash, accountsHash, nBits, height):
        self.version = version
        """Version in block header."""
        self.prevHash = prevHash
        """32-byte hex-encoded hash of the previous block."""
        self.interlinkHash = interlinkHash
        """32-byte hex-encoded hash of the interlink."""
        self.accountsHash = accountsHash
        """32-byte hex-encoded hash of the accounts tree."""
        self.nBits = nBits
        """Compact form of the hash target for this block."""
        self.height = height
        """Height of the block in the block chain (also known as block number)."""

class BlockTemplateBody():
    """
    Block template body returned by the server.
    """
    def __init__(self, hash, minerAddr, extraData, transactions, prunedAccounts, merkleHashes):
        self.hash = hash
        """32-byte hex-encoded hash of the block body."""
        self.minerAddr = minerAddr
        """20-byte hex-encoded miner address."""
        self.extraData = extraData
        """Hex-encoded value of the extra data field."""
        self.transactions = transactions
        """Array of hex-encoded transactions for this block."""
        self.prunedAccounts = prunedAccounts
        """Array of hex-encoded pruned accounts for this block."""
        self.merkleHashes = merkleHashes
        """Array of hex-encoded hashes that verify the path of the miner address in the merkle tree.
        This can be used to change the miner address easily."""

class BlockTemplate():
    """
    Block template returned by the server.
    """
    def __init__(self, header, interlink, body, target):
        self.header = header
        """Block template header returned by the server."""
        self.interlink = interlink
        """Hex-encoded interlink."""
        self.body = body
        """Block template body returned by the server."""
        self.target = target
        """Compact form of the hash target to submit a block to this client."""

class TransactionReceipt():
    """
    Transaction receipt returned by the server.
    """
    def __init__(self, transactionHash, transactionIndex, blockHash, blockNumber, confirmations, timestamp):
        self.transactionHash = transactionHash
        """Hex-encoded hash of the transaction."""
        self.transactionIndex = transactionIndex
        """Integer of the transactions index position in the block."""
        self.blockHash = blockHash
        """Hex-encoded hash of the block where this transaction was in."""
        self.blockNumber = blockNumber
        """Block number where this transaction was in."""
        self.confirmations = confirmations
        """Number of confirmations for this transaction (number of blocks on top of the block where this transaction was in)."""
        self.timestamp = timestamp
        """Timestamp of the block where this transaction was in."""

class WorkInstructions():
    """
    Work instructions receipt returned by the server.
    """
    def __init__(self, data, suffix, target, algorithm):
        self.data = data
        """Hex-encoded block header. This is what should be passed through the hash function.
        The last 4 bytes describe the nonce, the 4 bytes before are the current timestamp.
        Most implementations allow the miner to arbitrarily choose the nonce and to update the timestamp without requesting new work instructions."""
        self.suffix = suffix
        """Hex-encoded block without the header. When passing a mining result to submitBlock, append the suffix to the data string with selected nonce."""
        self.target = target
        """Compact form of the hash target to submit a block to this client."""
        self.algorithm = algorithm
        """Field to describe the algorithm used to mine the block. Always nimiq-argon2 for now."""

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

class MempoolInfo():
    """
    Mempool information returned by the server.
    """
    def __init__(self, *args, **kwargs):
        self.total = kwargs["total"]
        """Total number of pending transactions in mempool."""
        self.buckets = kwargs["buckets"]
        """Array containing a subset of fee per byte buckets from [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0] that currently have more than one transaction."""
        transactionsPerBucket = {}
        for attr, value in kwargs.items():
            if attr.isdigit():
                transactionsPerBucket[int(attr)] = value
        self.transactionsPerBucket = transactionsPerBucket
        """Number of transaction in the bucket. A transaction is assigned to the highest bucket of a value lower than its fee per byte value."""

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

class Peer():
    """
    Peer information returned by the server.
    """
    def __init__(self, id, address, addressState, connectionState = None, version = None, timeOffset = None, headHash = None, latency= None, rx = None, tx = None):
        self.id = id
        """Peer id."""
        self.address = address
        """Peer address."""
        self.addressState = addressState
        """Peer address state."""
        self.connectionState = connectionState
        """Peer connection state."""
        self.version = version
        """Node version the peer is running."""
        self.timeOffset = timeOffset
        """Time offset with the peer (in miliseconds)."""
        self.headHash = headHash
        """Hash of the head block of the peer."""
        self.latency = latency
        """Latency to the peer."""
        self.rx = rx
        """Received bytes."""
        self.tx = tx
        """Sent bytes."""

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

class SyncStatus():
    """
    Syncing status returned by the server.
    """
    def __init__(self, startingBlock, currentBlock, highestBlock):
        self.startingBlock = startingBlock
        """The block at which the import started (will only be reset, after the sync reached his head)."""
        self.currentBlock = currentBlock
        """The current block, same as blockNumber."""
        self.highestBlock = highestBlock
        """The estimated highest block."""

class InternalErrorException(Exception):
    """
    Internal error during a JSON RPC request.
    """
    pass

class RemoteErrorException(Exception):
    """
    Exception on the remote server.
    """
    def __init__(self, message, code):
        super(RemoteErrorException, self).__init__("{0} ({1})".format(message, code))

class ConnectionErrorException(Exception):
    """
    Error with connection.
    """
    pass

class NimiqClient:
    """
    API client for the Nimiq JSON RPC server.
    """

    def __init__(self, scheme="http", user="", password="", host="127.0.0.1", port=8648, session=None):
        """
        Client initialization.
        :param scheme: Protocol squeme, "http" or "https".
        :param user: Authorized user.
        :param password: Password for the authorized user.
        :param host: Host IP address.
        :param port: Host port.
        :param session: Used to make all requests. If ommited the shared URLSession is used.
        """
        self.id = 0
        """Number in the sequence for the of the next request."""
        self.url = "{0}://{1}:{2}".format(scheme, host, port)
        """URL of the JSONRPC server."""
        self.auth = HTTPBasicAuth(user, password)
        """Base64 string containing authentication parameters."""
        if session is None:
            session = requests.Session()
        self.session = session
        """requests Session instance used in requests sent to the JSONRPC server."""

    def call(self, method, *args):
        """
        Used in all JSONRPC requests to fetch the data.
        :param method: JSONRPC method.
        :param params: Parameters used by the request.
        :retur: If succesfull, returns the model reperestation of the result, None otherwise.
        """

        # make JSON object to send to the server
        call_object = {
            "jsonrpc": "2.0",
            "method": method,
            "params": args,
            "id": self.id
        }

        logger.info("Request: {0}".format(call_object))

        # make request
        try:
            resp_object = self.session.post(
                self.url,
                json = call_object,
                auth = self.auth
            ).json()

            logger.info("Response: {0}".format(resp_object))

        # raise if there are any errors
        except Exception as error:
            if error is requests.exceptions.RequestException:
                raise ConnectionErrorException(error)
            else:
                raise InternalErrorException(error)

        error = resp_object.get("error")
        if error is not None:
            raise RemoteErrorException(error.get("message"), error.get("code"))

        # increase the JSONRPC client request id for the next request
        self.id += 1

        return resp_object.get("result")

    def accounts(self):
        """
        Returns a list of addresses owned by client.
        :return: Array of Accounts owned by the client.
        """
        result = []
        for account in self.call("accounts", []):
            result.append(RawAccount(**account).value)
        return result

    def blockNumber(self):
        """
        Returns the height of most recent block.
        :return: The current block height the client is on.
        """
        return self.call("blockNumber", [])

    def consensus(self):
        """
        Returns information on the current consensus state.
        :return: Consensus state. "established" is the value for a good state, other values indicate bad.
        """
        return ConsensusState(self.call("consensus", []))

    def constant(self, constant, value = None):
        """
        Returns or overrides a constant value.
        When no parameter is given, it returns the value of the constant. When giving a value as parameter,
        it sets the constant to the given value. To reset the constant use resetConstant() instead.
        :param string: The class and name of the constant (format should be "Class.CONSTANT").
        :param value: The new value of the constant.
        :return: The value of the constant.
        """
        params = [constant]
        if value != None:
            params.append(value)
        return self.call("constant", params)

    def createAccount(self):
        """
        Creates a new account and stores its private key in the client store.
        :return: Information on the wallet that was created using the command.
        """
        return Wallet(**self.call("createAccount", []))

    def createRawTransaction(self, transaction):
        """
        Creates and signs a transaction without sending it. The transaction can then be send via sendRawTransaction() without accidentally replaying it.
        :param transaction: The transaction object.
        :return: Hex-encoded transaction.
        """
        return self.call("createRawTransaction", [transaction])

    def getAccount(self, address):
        """
        Returns details for the account of given address.
        :param address: Address to get account details.
        :return: Details about the account. Returns the default empty basic account for non-existing accounts.
        """
        return RawAccount(**self.call("getAccount", [address])).value

    def getBalance(self, address):
        """
        Returns the balance of the account of given address.
        :param address: Address to check for balance.
        :return: The current balance at the specified address (in smalest unit).
        """
        return self.call("getBalance", [address])

    def getBlockByHash(self, hash, fullTransactions = False):
        """
        Returns information about a block by hash.
        :param hash: Hash of the block to gather information on.
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :return: A block object or None when no block was found.
        """
        result = self.call("getBlockByHash", [hash, fullTransactions])
        if result is not None:
            return Block(**result)
        else:
            return None

    def getBlockByNumber(self, height, fullTransactions = False):
        """
        Returns information about a block by block number.
        :param height: The height of the block to gather information on.
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :return: A block object or None when no block was found.
        """
        result = self.call("getBlockByNumber", [height, fullTransactions])
        if result is not None:
            return Block(**result)
        else:
            return None

    def getBlockTemplate(self, address = None, extraData = ""):
        """
        Returns a template to build the next block for mining. This will consider pool instructions when connected to a pool.
        If address and extraData are provided the values are overriden.
        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :param extraData: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :return: A block template object.
        """
        params = []
        if address != None:
            params.append(address)
            params.append(extraData)
        result = self.call("getBlockTemplate", params)
        return BlockTemplate(BlockTemplateHeader(**result.get("header")), result.get("interlink"), BlockTemplateBody(**result.get("body")), result.get("target"))

    def getBlockTransactionCountByHash(self, hash):
        """
        Returns the number of transactions in a block from a block matching the given block hash.
        :param hash: Hash of the block.
        :return: Number of transactions in the block found, or None, when no block was found.
        """
        return self.call("getBlockTransactionCountByHash", [hash])

    def getBlockTransactionCountByNumber(self, height):
        """
        Returns the number of transactions in a block matching the given block number.
        :param height: Height of the block.
        :return: Number of transactions in the block found, or None, when no block was found.
        """
        return self.call("getBlockTransactionCountByNumber", [height])

    def getTransactionByBlockHashAndIndex(self, hash, index):
        """
        Returns information about a transaction by block hash and transaction index position.
        :param hash: Hash of the block containing the transaction.
        :param index: Index of the transaction in the block.
        :return: A transaction object or None when no transaction was found.
        """
        result = self.call("getTransactionByBlockHashAndIndex", [hash, index])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionByBlockNumberAndIndex(self, height, index):
        """
        Returns information about a transaction by block number and transaction index position.
        :param height: Height of the block containing the transaction.
        :param index: Index of the transaction in the block.
        :return: A transaction object or None when no transaction was found.
        """
        result = self.call("getTransactionByBlockNumberAndIndex", [height, index])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionByHash(self, hash):
        """
        Returns the information about a transaction requested by transaction hash.
        :param hash: Hash of a transaction.
        :return: A transaction object or None when no transaction was found.
        """
        result = self.call("getTransactionByHash", [hash])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionReceipt(self, hash):
        """
        Returns the receipt of a transaction by transaction hash.
        :param hash: Hash of a transaction.
        :return: A transaction receipt object, or None when no receipt was found.
        """
        result = self.call("getTransactionReceipt", [hash])
        if result is not None:
            return TransactionReceipt(**result)
        else:
            return None

    def getTransactionsByAddress(self, address, numberOfTransactions = 1000):
        """
        Returns the latest transactions successfully performed by or for an address.
        Note that this information might change when blocks are rewinded on the local state due to forks.
        :param address: Address of which transactions should be gathered.
        :param numberOfTransactions: Number of transactions that shall be returned.
        :return: Array of transactions linked to the requested address.
        """
        result = []
        for transaction in self.call("getTransactionsByAddress", [address, numberOfTransactions]):
            result.append(Transaction.fromDict(transaction))
        return result

    def getWork(self, address = None, extraData = ""):
        """
        Returns instructions to mine the next block. This will consider pool instructions when connected to a pool.
        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :param extraData: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :return: Mining work instructions.
        """
        params = []
        if address != None:
            params.append(address)
            params.append(extraData)
        return WorkInstructions(**self.call("getWork", params))

    def hashrate(self):
        """
        Returns the number of hashes per second that the node is mining with.
        :return: Number of hashes per second.
        """
        return self.call("hashrate", [])

    def log(self, tag, level):
        """
        Sets the log level of the node.
        :param tag: Tag: If "*" the log level is set globally, otherwise the log level is applied only on this tag.
        :param level: Minimum log level to display.
        :return: True if the log level was changed, False otherwise.
        """
        return self.call("log", [tag, level])

    def mempool(self):
        """
        Returns information on the current mempool situation. This will provide an overview of the number of transactions sorted into buckets based on their fee per byte (in smallest unit).
        :return: Mempool information.
        """
        result = self.call("mempool", [])
        return MempoolInfo(**result)

    def mempoolContent(self, fullTransactions = False):
        """
        Returns transactions that are currently in the mempool.
        :param fullTransactions: If True includes full transactions, if False includes only transaction hashes.
        :return: Array of transactions (either represented by the transaction hash or a transaction object).
        """
        result = []
        for transaction in self.call("mempoolContent", [fullTransactions]):
            if type(transaction) is str:
                result.append(transaction)
            else:
                result.append(Transaction.fromDict(transaction))
        return result

    def minerAddress(self):
        """
        Returns the miner address.
        :return: The miner address configured on the node.
        """
        return self.call("minerAddress", [])

    def minerThreads(self, threads = None):
        """
        Returns or sets the number of CPU threads for the miner.
        When no parameter is given, it returns the current number of miner threads.
        When a value is given as parameter, it sets the number of miner threads to that value.
        :param threads: The number of threads to allocate for mining.
        :return: The number of threads allocated for mining.
        """
        params = []
        if threads != None:
            params.append(threads)
        return self.call("minerThreads", params)

    def minFeePerByte(self, fee = None):
        """
        Returns or sets the minimum fee per byte.
        When no parameter is given, it returns the current minimum fee per byte.
        When a value is given as parameter, it sets the minimum fee per byte to that value.
        :param fee: The new minimum fee per byte.
        :return: The new minimum fee per byte.
        """
        params = []
        if fee != None:
            params.append(fee)
        return self.call("minFeePerByte", params)

    def mining(self, state = None):
        """
        Returns true if client is actively mining new blocks.
        When no parameter is given, it returns the current state.
        When a value is given as parameter, it sets the current state to that value.
        :param state: The state to be set.
        :return: True if the client is mining, otherwise False.
        """
        params = []
        if state != None:
            params.append(state)
        return self.call("mining", params)

    def peerCount(self):
        """
        Returns number of peers currently connected to the client.
        :return: Number of connected peers.
        """
        return self.call("peerCount", [])

    def peerList(self):
        """
        Returns list of peers known to the client.
        :return: The list of peers.
        """
        result = []
        for peer in self.call("peerList", []):
            result.append(Peer(**peer))
        return result

    def peerState(self, address, command = None):
        """
        Returns the state of the peer.
        When no command is given, it returns peer state.
        When a value is given for command, it sets the peer state to that value.
        :param address: The address of the peer.
        :param command: The command to send.
        :return: The current state of the peer.
        """
        params = []
        params.append(address)
        if command != None:
            params.append(command)
        return Peer(**self.call("peerState", params))

    def pool(self, address = None):
        """
        Returns or sets the mining pool.
        When no parameter is given, it returns the current mining pool.
        When a value is given as parameter, it sets the mining pool to that value.
        :param address: The mining pool connection string ("url:port") or boolean to enable/disable pool mining.
        :return: The mining pool connection string, or None if not enabled.
        """
        params = []
        if address != None:
            params.append(address)
        return self.call("pool", params)

    def poolConfirmedBalance(self):
        """
        Returns the confirmed mining pool balance.
        :return: The confirmed mining pool balance (in smallest unit).
        """
        return self.call("poolConfirmedBalance", [])

    def poolConnectionState(self):
        """
        Returns the connection state to mining pool.
        :return: The mining pool connection state.
        """
        return PoolConnectionState(self.call("poolConnectionState", []))

    def sendRawTransaction(self, transaction):
        """
        Sends a signed message call transaction or a contract creation, if the data field contains code.
        :param transaction: The hex encoded signed transaction
        :return: The Hex-encoded transaction hash.
        """
        return self.call("sendRawTransaction", [transaction])

    def sendTransaction(self, transaction):
        """
        Creates new message call transaction or a contract creation, if the data field contains code.
        :param transaction: The OutgoingTransaction object
        :return: The Hex-encoded transaction hash.
        """
        return self.call("sendTransaction", [transaction])

    def submitBlock(self, block):
        """
        Submits a block to the node. When the block is valid, the node will forward it to other nodes in the network.
        :param block: Hex-encoded full block (including header, interlink and body). When submitting work from getWork, remember to include the suffix.
        """
        self.call("submitBlock", [block])

    def syncing(self):
        """
        Returns an object with data about the sync status or False.
        :return: An object with sync status data or False, when not syncing.
        """
        result = self.call("syncing", [])
        if type(result) is bool:
            return result
        else:
            return SyncStatus(**result)

    def getRawTransactionInfo(self, transaction):
        """
        Deserializes hex-encoded transaction and returns a transaction object.
        :param transaction: The hex encoded signed transaction.
        :return: The transaction object.
        """
        return Transaction.fromDict(self.call("getRawTransactionInfo", [transaction]))

    def resetConstant(self, constant):
        """
        Resets the constant to default value.
        :param constant: Name of the constant.
        :return: The new value of the constant.
        """
        return self.call("constant", [constant, "reset"])
