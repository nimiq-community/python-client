__all__ = [
    "NimiqClient",
    "InternalErrorException",
    "RemoteErrorException",
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

__metaclass__ = type

import requests
from requests.auth import HTTPBasicAuth
from enum import Enum
import json
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
    def __init__(self, id, address, balance, type, owner, ownerAddress, vestingStart, vestingStepBlocks, vestingStepAmount, vestingTotalAmount):
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
    def __init__(self, id, address, balance, type, sender, senderAddress, recipient, recipientAddress, hashRoot, hashAlgorithm, hashCount, timeout, totalAmount):
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

class RawAccount():
    """
    Nimiq account returned by the server. The especific type is in the associated value.
    """
    def __init__(self, **kwargs):
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

    def __str__(self):
        return self.value

class Wallet():
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
    def __init__(self, id, address, publicKey, privateKey = None):
        self.id = id
        self.address = address
        self.publicKey = publicKey
        self.privateKey = privateKey

class OutgoingTransaction():
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
    def __init__(self, from_, to, value, fee, fromType = AccountType.BASIC, toType = AccountType.BASIC, data = None):
        self.from_ = from_
        self.fromType = fromType
        self.to = to
        self.toType = toType
        self.value = value
        self.fee = fee
        self.data = data

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

class Transaction():
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
    def __init__(self, hash, from_, fromAddress, to, toAddress, value, fee, flags, blockHash = None, blockNumber = None, timestamp = None, confirmations = 0, transactionIndex = None, data = None, valid = None, inMempool = None):
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

    @staticmethod
    def fromDict(transaction):
        """
        Create Transaction object from dict

        :param transaction: dict with transaction data.
        :type: dict
        :return: Transaction object.
        :rtype: Transaction
        """
        if "from" in transaction:
            transaction["from_"] = transaction.pop("from")
        return Transaction(**transaction)

class Block():
    """
    Block returned by the server.

    :param number: Height of the block.
    :type number: int
    :param hash: Hex-encoded 32-byte hash of the block.
    :type hash: str
    :param pow: Hex-encoded 32-byte Proof-of-Work hash of the block.
    :type pow: str
    :param parentHash: Hex-encoded 32-byte hash of the predecessor block.
    :type parentHash: str
    :param nonce: The nonce of the block used to fulfill the Proof-of-Work.
    :type nonce: int
    :param bodyHash: Hex-encoded 32-byte hash of the block body Merkle root.
    :type bodyHash: str
    :param accountsHash: Hex-encoded 32-byte hash of the accounts tree root.
    :type accountsHash: str
    :param difficulty: Block difficulty, encoded as decimal number in string.
    :type difficulty: str
    :param timestamp: UNIX timestamp of the block.
    :type timestamp: int
    :param confirmations: Number of confirmations for this transaction (number of blocks on top of the block where this transaction was in).
    :type confirmations: int
    :param miner: Hex-encoded 20 byte address of the miner of the block.
    :type miner: str
    :param minerAddress: User friendly address (NQ-address) of the miner of the block.
    :type minerAddress: str
    :param extraData: Hex-encoded value of the extra data field, maximum of 255 bytes.
    :type extraData: str
    :param size: Block size in byte.
    :type size: int
    :param transactions: List of transactions. Either represented by the transaction hash or a Transaction object.
    :type transactions: list of (Transaction or str)
    """
    def __init__(self, number, hash, pow, parentHash, nonce, bodyHash, accountsHash, difficulty, timestamp, confirmations, miner, minerAddress, extraData, size, transactions):
        self.number = number
        self.hash = hash
        self.pow = pow
        self.parentHash = parentHash
        self.nonce = nonce
        self.bodyHash = bodyHash
        self.accountsHash = accountsHash
        self.difficulty = difficulty
        self.timestamp = timestamp
        self.confirmations = confirmations
        self.miner = miner
        self.minerAddress = minerAddress
        self.extraData = extraData
        self.size = size
        for index, transaction in enumerate(transactions):
            if type(transaction) is not str and type(transaction) is not Transaction:
                transactions[index] = Transaction.fromDict(transaction)
        self.transactions = transactions

class BlockTemplateHeader():
    """
    Block template header returned by the server.

    :param version: Version in block header.
    :type version: int
    :param prevHash: 32-byte hex-encoded hash of the previous block.
    :type prevHash: str
    :param interlinkHash: 32-byte hex-encoded hash of the interlink.
    :type interlinkHash: str
    :param accountsHash: 32-byte hex-encoded hash of the accounts tree.
    :type accountsHash: str
    :param nBits: Compact form of the hash target for this block.
    :type nBits: int
    :param height: Height of the block in the block chain (also known as block number).
    :type height: int
    """
    def __init__(self, version, prevHash, interlinkHash, accountsHash, nBits, height):
        self.version = version
        self.prevHash = prevHash
        self.interlinkHash = interlinkHash
        self.accountsHash = accountsHash
        self.nBits = nBits
        self.height = height

class BlockTemplateBody():
    """
    Block template body returned by the server.

    :param hash: 32-byte hex-encoded hash of the block body.
    :type hash: str
    :param minerAddr: 20-byte hex-encoded miner address.
    :type minerAddr: str
    :param extraData: Hex-encoded value of the extra data field.
    :type extraData: str
    :param transactions: List of hex-encoded transactions for this block.
    :type transactions: str
    :param prunedAccounts: List of hex-encoded pruned accounts for this block.
    :type prunedAccounts: str
    :param merkleHashes: List of hex-encoded hashes that verify the path of the miner address in the merkle tree. This can be used to change the miner address easily.
    :type merkleHashes: str
    """
    def __init__(self, hash, minerAddr, extraData, transactions, prunedAccounts, merkleHashes):
        self.hash = hash
        self.minerAddr = minerAddr
        self.extraData = extraData
        self.transactions = transactions
        self.prunedAccounts = prunedAccounts
        self.merkleHashes = merkleHashes

class BlockTemplate():
    """
    Block template returned by the server.

    :param header: Block template header returned by the server.
    :type header: BlockTemplateHeader
    :param interlink: Hex-encoded interlink.
    :type interlink: str
    :param body: Block template body returned by the server.
    :type body: BlockTemplateBody
    :param target: Compact form of the hash target to submit a block to this client.
    :type target: int
    """
    def __init__(self, header, interlink, body, target):
        self.header = header
        self.interlink = interlink
        self.body = body
        self.target = target

class TransactionReceipt():
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
    def __init__(self, transactionHash, transactionIndex, blockHash, blockNumber, confirmations, timestamp):
        self.transactionHash = transactionHash
        self.transactionIndex = transactionIndex
        self.blockHash = blockHash
        self.blockNumber = blockNumber
        self.confirmations = confirmations
        self.timestamp = timestamp

class WorkInstructions():
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

class MempoolInfo():
    """
    Mempool information returned by the server.
    """
    def __init__(self, **kwargs):
        self.total = kwargs["total"]
        """Total number of pending transactions in mempool."""
        self.buckets = kwargs["buckets"]
        """List containing a subset of fee per byte buckets from [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0] that currently have more than one transaction."""
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
    def __init__(self, id, address, addressState, connectionState = None, version = None, timeOffset = None, headHash = None, latency= None, rx = None, tx = None):
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

class NimiqClient:
    """
    API client for the Nimiq JSON RPC server.

    :param scheme: Protocol squeme, "http" or "https".
    :type scheme: str, optional
    :param user: Authorized user.
    :type user: str, optional
    :param password: Password for the authorized user.
    :type password: str, optional
    :param host: Host IP address.
    :type host: str, optional
    :param port: Host port.
    :type port: int, optional
    :param session: Used to make all requests. If ommited requests.Session() is used.
    :type session: Session, optional
    """

    def __init__(self, scheme="http", user="", password="", host="127.0.0.1", port=8648, session=None):
        self.id = 0
        self.url = "{0}://{1}:{2}".format(scheme, host, port)
        self.auth = HTTPBasicAuth(user, password)
        if session is None:
            session = requests.Session()
        self.session = session

    def __call(self, method, *args):
        """
        Used in all JSONRPC requests to fetch the data.

        :param method: JSONRPC method.
        :type method: str
        :param params: Parameters used by the request.
        :type params: list
        :return: If succesfull, returns the model reperestation of the result, None otherwise.
        :rtype: dict
        """

        # increase the JSONRPC client request id
        self.id += 1

        # make JSON object to send to the server
        call_object = {
            "jsonrpc": "2.0",
            "method": method,
            "params": args,
            "id": self.id
        }

        logger.info("Request: {0}".format(call_object))

        # make request
        requestError = None
        try:
            resp_object = self.session.post(
                self.url,
                json = call_object,
                auth = self.auth
            ).json()

            logger.info("Response: {0}".format(resp_object))

        except Exception as e:
            requestError = e

        # raise if there was any error
        if requestError is not None:
            raise InternalErrorException(requestError)

        error = resp_object.get("error")
        if error is not None:
            raise RemoteErrorException(error.get("message"), error.get("code"))

        return resp_object.get("result")

    def accounts(self):
        """
        Returns a list of addresses owned by client.

        :return: List of Accounts owned by the client.
        :rtype: list of (Account or VestingContract or HTLC)
        """
        result = []
        for account in self.__call("accounts", []):
            result.append(RawAccount(**account).value)
        return result

    def blockNumber(self):
        """
        Returns the height of most recent block.

        :return: The current block height the client is on.
        :rtype: int
        """
        return self.__call("blockNumber", [])

    def consensus(self):
        """
        Returns information on the current consensus state.

        :return: Consensus state. "established" is the value for a good state, other values indicate bad.
        :rtype: ConsensusState
        """
        return ConsensusState(self.__call("consensus", []))

    def constant(self, constant, value = None):
        """
        Returns or overrides a constant value.
        When no parameter is given, it returns the value of the constant. When giving a value as parameter,
        it sets the constant to the given value. To reset the constant use resetConstant() instead.

        :param constant: The class and name of the constant (format should be "Class.CONSTANT").
        :type constant: str
        :param value: The new value of the constant.
        :type value: int, optional
        :return: The value of the constant.
        :rtype: int
        """
        params = [constant]
        if value != None:
            params.append(value)
        return self.__call("constant", params)

    def createAccount(self):
        """
        Creates a new account and stores its private key in the client store.

        :return: Information on the wallet that was created using the command.
        :rtype: Wallet
        """
        return Wallet(**self.__call("createAccount", []))

    def createRawTransaction(self, transaction):
        """
        Creates and signs a transaction without sending it. The transaction can then be send via sendRawTransaction() without accidentally replaying it.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: Hex-encoded transaction.
        :rtype: str
        """
        return self.__call("createRawTransaction", [transaction])

    def getAccount(self, address):
        """
        Returns details for the account of given address.

        :param address: Address to get account details.
        :type address: str
        :return: Details about the account. Returns the default empty basic account for non-existing accounts.
        :rtype: Account or VestingContract or HTLC
        """
        return RawAccount(**self.__call("getAccount", [address])).value

    def getBalance(self, address):
        """
        Returns the balance of the account of given address.

        :param address: Address to check for balance.
        :type address: str
        :return: The current balance at the specified address (in smalest unit).
        :rtype: int
        """
        return self.__call("getBalance", [address])

    def getBlockByHash(self, hash, fullTransactions = False):
        """
        Returns information about a block by hash.

        :param hash: Hash of the block to gather information on.
        :type hash: str
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type fullTransactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = self.__call("getBlockByHash", [hash, fullTransactions])
        if result is not None:
            return Block(**result)
        else:
            return None

    def getBlockByNumber(self, height, fullTransactions = False):
        """
        Returns information about a block by block number.

        :param height: The height of the block to gather information on.
        :type height: int
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type fullTransactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = self.__call("getBlockByNumber", [height, fullTransactions])
        if result is not None:
            return Block(**result)
        else:
            return None

    def getBlockTemplate(self, address = None, extraData = ""):
        """
        Returns a template to build the next block for mining. This will consider pool instructions when connected to a pool.
        If address and extraData are provided the values are overriden.

        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :type address: str
        :param extraData: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :type extraData: str
        :return: A block template object.
        :rtype: BlockTemplate
        """
        params = []
        if address != None:
            params.append(address)
            params.append(extraData)
        result = self.__call("getBlockTemplate", params)
        return BlockTemplate(BlockTemplateHeader(**result.get("header")), result.get("interlink"), BlockTemplateBody(**result.get("body")), result.get("target"))

    def getBlockTransactionCountByHash(self, hash):
        """
        Returns the number of transactions in a block from a block matching the given block hash.

        :param hash: Hash of the block.
        :type hash: str
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self.__call("getBlockTransactionCountByHash", [hash])

    def getBlockTransactionCountByNumber(self, height):
        """
        Returns the number of transactions in a block matching the given block number.

        :param height: Height of the block.
        :type height: int
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self.__call("getBlockTransactionCountByNumber", [height])

    def getTransactionByBlockHashAndIndex(self, hash, index):
        """
        Returns information about a transaction by block hash and transaction index position.

        :param hash: Hash of the block containing the transaction.
        :type hash: str
        :param index: Index of the transaction in the block.
        :type index: int
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self.__call("getTransactionByBlockHashAndIndex", [hash, index])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionByBlockNumberAndIndex(self, height, index):
        """
        Returns information about a transaction by block number and transaction index position.

        :param height: Height of the block containing the transaction.
        :type height: int
        :param index: Index of the transaction in the block.
        :type index: int
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self.__call("getTransactionByBlockNumberAndIndex", [height, index])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionByHash(self, hash):
        """
        Returns the information about a transaction requested by transaction hash.

        :param hash: Hash of a transaction.
        :type hash: str
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self.__call("getTransactionByHash", [hash])
        if result is not None:
            return Transaction.fromDict(result)
        else:
            return None

    def getTransactionReceipt(self, hash):
        """
        Returns the receipt of a transaction by transaction hash.

        :param hash: Hash of a transaction.
        :type hash: str
        :return: A transaction receipt object, or None when no receipt was found.
        :rtype: TransactionReceipt or None
        """
        result = self.__call("getTransactionReceipt", [hash])
        if result is not None:
            return TransactionReceipt(**result)
        else:
            return None

    def getTransactionsByAddress(self, address, numberOfTransactions = 1000):
        """
        Returns the latest transactions successfully performed by or for an address.
        Note that this information might change when blocks are rewinded on the local state due to forks.

        :param address: Address of which transactions should be gathered.
        :type address: str
        :param numberOfTransactions: Number of transactions that shall be returned.
        :type numberOfTransactions: int, optional
        :return: List of transactions linked to the requested address.
        :rtype: list of (Transaction)
        """
        result = []
        for transaction in self.__call("getTransactionsByAddress", [address, numberOfTransactions]):
            result.append(Transaction.fromDict(transaction))
        return result

    def getWork(self, address = None, extraData = ""):
        """
        Returns instructions to mine the next block. This will consider pool instructions when connected to a pool.

        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :type address: str
        :param extraData: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :type extraData: str
        :return: Mining work instructions.
        :rtype: WorkInstructions
        """
        params = []
        if address != None:
            params.append(address)
            params.append(extraData)
        return WorkInstructions(**self.__call("getWork", params))

    def hashrate(self):
        """
        Returns the number of hashes per second that the node is mining with.

        :return: Number of hashes per second.
        :rtype: float
        """
        return self.__call("hashrate", [])

    def log(self, tag, level):
        """
        Sets the log level of the node.

        :param tag: Tag: If "*" the log level is set globally, otherwise the log level is applied only on this tag.
        :type tag: str
        :param level: Minimum log level to display.
        :type level: LogLevel
        :return: True if the log level was changed, False otherwise.
        :rtype: bool
        """
        return self.__call("log", [tag, level])

    def mempool(self):
        """
        Returns information on the current mempool situation. This will provide an overview of the number of transactions sorted into buckets based on their fee per byte (in smallest unit).

        :return: Mempool information.
        :rtype: MempoolInfo
        """
        result = self.__call("mempool", [])
        return MempoolInfo(**result)

    def mempoolContent(self, fullTransactions = False):
        """
        Returns transactions that are currently in the mempool.

        :param fullTransactions: If True includes full transactions, if False includes only transaction hashes.
        :type fullTransactions: bool, optional
        :return: List of transactions (either represented by the transaction hash or a transaction object).
        :rtype: list of (Transaction or str)
        """
        result = []
        for transaction in self.__call("mempoolContent", [fullTransactions]):
            if type(transaction) is str:
                result.append(transaction)
            else:
                result.append(Transaction.fromDict(transaction))
        return result

    def minerAddress(self):
        """
        Returns the miner address.

        :return: The miner address configured on the node.
        :rtype: str
        """
        return self.__call("minerAddress", [])

    def minerThreads(self, threads = None):
        """
        Returns or sets the number of CPU threads for the miner.
        When no parameter is given, it returns the current number of miner threads.
        When a value is given as parameter, it sets the number of miner threads to that value.

        :param threads: The number of threads to allocate for mining.
        :type threads: int, optional
        :return: The number of threads allocated for mining.
        :rtype: int
        """
        params = []
        if threads != None:
            params.append(threads)
        return self.__call("minerThreads", params)

    def minFeePerByte(self, fee = None):
        """
        Returns or sets the minimum fee per byte.
        When no parameter is given, it returns the current minimum fee per byte.
        When a value is given as parameter, it sets the minimum fee per byte to that value.

        :param fee: The new minimum fee per byte.
        :type fee: int, optional
        :return: The new minimum fee per byte.
        :rtype: int
        """
        params = []
        if fee != None:
            params.append(fee)
        return self.__call("minFeePerByte", params)

    def mining(self, state = None):
        """
        Returns true if client is actively mining new blocks.
        When no parameter is given, it returns the current state.
        When a value is given as parameter, it sets the current state to that value.

        :param state: The state to be set.
        :type state: bool
        :return: True if the client is mining, otherwise False.
        :rtype: bool
        """
        params = []
        if state != None:
            params.append(state)
        return self.__call("mining", params)

    def peerCount(self):
        """
        Returns number of peers currently connected to the client.

        :return: Number of connected peers.
        :rtype: int
        """
        return self.__call("peerCount", [])

    def peerList(self):
        """
        Returns list of peers known to the client.

        :return: The list of peers.
        :rtype: list of (Peer)
        """
        result = []
        for peer in self.__call("peerList", []):
            result.append(Peer(**peer))
        return result

    def peerState(self, address, command = None):
        """
        Returns the state of the peer.
        When no command is given, it returns peer state.
        When a value is given for command, it sets the peer state to that value.

        :param address: The address of the peer.
        :type address: str
        :param command: The command to send.
        :type command: PeerStateCommand
        :return: The current state of the peer.
        :rtype: Peer
        """
        params = []
        params.append(address)
        if command != None:
            params.append(command)
        return Peer(**self.__call("peerState", params))

    def pool(self, address = None):
        """
        Returns or sets the mining pool.
        When no parameter is given, it returns the current mining pool.
        When a value is given as parameter, it sets the mining pool to that value.

        :param address: The mining pool connection string ("url:port") or boolean to enable/disable pool mining.
        :type address: str, optional
        :return: The mining pool connection string, or None if not enabled.
        :rtype: str or None
        """
        params = []
        if address != None:
            params.append(address)
        return self.__call("pool", params)

    def poolConfirmedBalance(self):
        """
        Returns the confirmed mining pool balance.

        :return: The confirmed mining pool balance (in smallest unit).
        :rtype: int
        """
        return self.__call("poolConfirmedBalance", [])

    def poolConnectionState(self):
        """
        Returns the connection state to mining pool.

        :return: The mining pool connection state.
        :rtype: PoolConnectionState
        """
        return PoolConnectionState(self.__call("poolConnectionState", []))

    def sendRawTransaction(self, transaction):
        """
        Sends a signed message call transaction or a contract creation, if the data field contains code.

        :param transaction: The hex encoded signed transaction
        :type transaction: str
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self.__call("sendRawTransaction", [transaction])

    def sendTransaction(self, transaction):
        """
        Creates new message call transaction or a contract creation, if the data field contains code.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self.__call("sendTransaction", [transaction])

    def submitBlock(self, block):
        """
        Submits a block to the node. When the block is valid, the node will forward it to other nodes in the network.

        :param block: Hex-encoded full block (including header, interlink and body). When submitting work from getWork, remember to include the suffix.
        :type block: Block
        """
        self.__call("submitBlock", [block])

    def syncing(self):
        """
        Returns an object with data about the sync status or False.

        :return: An object with sync status data or False, when not syncing.
        :rtype: SyncStatus
        """
        result = self.__call("syncing", [])
        if type(result) is bool:
            return result
        else:
            return SyncStatus(**result)

    def getRawTransactionInfo(self, transaction):
        """
        Deserializes hex-encoded transaction and returns a transaction object.

        :param transaction: The hex encoded signed transaction.
        :type transaction: str
        :return: The transaction object.
        :rtype: Transaction
        """
        return Transaction.fromDict(self.__call("getRawTransactionInfo", [transaction]))

    def resetConstant(self, constant):
        """
        Resets the constant to default value.

        :param constant: Name of the constant.
        :type constant: str
        :return: The new value of the constant.
        :rtype: int
        """
        return self.__call("constant", [constant, "reset"])
