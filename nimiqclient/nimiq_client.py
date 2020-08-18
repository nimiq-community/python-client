__all__ = [
    "NimiqClient",
    "InternalErrorException",
    "RemoteErrorException"
]

from .models.account import *
from .models.block import *
from .models.mempool import *
from .models.miner import *
from .models.node import *
from .models.peer import *
from .models.transaction import *

import requests
from requests.auth import HTTPBasicAuth
from enum import Enum
import logging

logger = logging.getLogger(__name__)

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
            "params": (list(args),),
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

    def __get_account(self, data):
        """
        Get the specific account type from the dictionary data.

        :param data: The dictionary containing the data.
        :type data: dict
        :return: Account object.
        :rtype: Account or VestingContract or HTLC
        """
        type = data.get("type")
        if type == AccountType.HTLC:
            return HTLC(**data)
        elif type == AccountType.VESTING:
            return VestingContract(**data)
        else:
            return Account(**data)

    def accounts(self):
        """
        Returns a list of addresses owned by client.

        :return: List of Accounts owned by the client.
        :rtype: list of (Account or VestingContract or HTLC)
        """
        return [self.__get_account(account) for account in self.__call("accounts")]

    def blockNumber(self):
        """
        Returns the height of most recent block.

        :return: The current block height the client is on.
        :rtype: int
        """
        return self.__call("blockNumber")

    def consensus(self):
        """
        Returns information on the current consensus state.

        :return: Consensus state. "established" is the value for a good state, other values indicate bad.
        :rtype: ConsensusState
        """
        return ConsensusState(self.__call("consensus"))

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
        if value is not None:
            return self.__call("constant", constant, value)
        else:
            return self.__call("constant", constant)

    def createAccount(self):
        """
        Creates a new account and stores its private key in the client store.

        :return: Information on the wallet that was created using the command.
        :rtype: Wallet
        """
        return Wallet(**self.__call("createAccount"))

    def createRawTransaction(self, transaction):
        """
        Creates and signs a transaction without sending it. The transaction can then be send via sendRawTransaction() without accidentally replaying it.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: Hex-encoded transaction.
        :rtype: str
        """
        return self.__call("createRawTransaction", transaction)

    def getAccount(self, address):
        """
        Returns details for the account of given address.

        :param address: Address to get account details.
        :type address: str
        :return: Details about the account. Returns the default empty basic account for non-existing accounts.
        :rtype: Account or VestingContract or HTLC
        """
        return self.__get_account(self.__call("getAccount", address))

    def getBalance(self, address):
        """
        Returns the balance of the account of given address.

        :param address: Address to check for balance.
        :type address: str
        :return: The current balance at the specified address (in smalest unit).
        :rtype: int
        """
        return self.__call("getBalance", address)

    def getBlockByHash(self, hash, fullTransactions = None):
        """
        Returns information about a block by hash.

        :param hash: Hash of the block to gather information on.
        :type hash: str
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type fullTransactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = None
        if fullTransactions is not None:
            result = self.__call("getBlockByHash", hash, fullTransactions)
        else:
            result = self.__call("getBlockByHash", hash)
        return Block(**result) if result is not None else None

    def getBlockByNumber(self, height, fullTransactions = None):
        """
        Returns information about a block by block number.

        :param height: The height of the block to gather information on.
        :type height: int
        :param fullTransactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type fullTransactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = None
        if fullTransactions is not None:
            result = self.__call("getBlockByNumber", height, fullTransactions)
        else:
            result = self.__call("getBlockByNumber", height)
        return Block(**result) if result is not None else None

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
        result = None
        if address is not None:
            result = self.__call("getBlockTemplate", address, extraData)
        else:
            result = self.__call("getBlockTemplate")
        return BlockTemplate(BlockTemplateHeader(**result.get("header")), result.get("interlink"), BlockTemplateBody(**result.get("body")), result.get("target"))

    def getBlockTransactionCountByHash(self, hash):
        """
        Returns the number of transactions in a block from a block matching the given block hash.

        :param hash: Hash of the block.
        :type hash: str
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self.__call("getBlockTransactionCountByHash", hash)

    def getBlockTransactionCountByNumber(self, height):
        """
        Returns the number of transactions in a block matching the given block number.

        :param height: Height of the block.
        :type height: int
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self.__call("getBlockTransactionCountByNumber", height)

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
        result = self.__call("getTransactionByBlockHashAndIndex", hash, index)
        if result is not None:
            return Transaction(**result)
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
        result = self.__call("getTransactionByBlockNumberAndIndex", height, index)
        if result is not None:
            return Transaction(**result)
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
        result = self.__call("getTransactionByHash", hash)
        if result is not None:
            return Transaction(**result)
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
        result = self.__call("getTransactionReceipt", hash)
        if result is not None:
            return TransactionReceipt(**result)
        else:
            return None

    def getTransactionsByAddress(self, address, numberOfTransactions = None):
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
        result = None
        if numberOfTransactions is not None:
            result = self.__call("getTransactionsByAddress", address, numberOfTransactions)
        else:
            result = self.__call("getTransactionsByAddress", address)
        return [Transaction(**tx) for tx in result]

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
        result = None
        if address is not None:
            result = self.__call("getWork", address, extraData)
        else:
            result = self.__call("getWork")
        return WorkInstructions(**result)

    def hashrate(self):
        """
        Returns the number of hashes per second that the node is mining with.

        :return: Number of hashes per second.
        :rtype: float
        """
        return self.__call("hashrate")

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
        return self.__call("log", tag, level)

    def mempool(self):
        """
        Returns information on the current mempool situation. This will provide an overview of the number of transactions sorted into buckets based on their fee per byte (in smallest unit).

        :return: Mempool information.
        :rtype: MempoolInfo
        """
        result = self.__call("mempool")
        return MempoolInfo(**result)

    def mempoolContent(self, fullTransactions = None):
        """
        Returns transactions that are currently in the mempool.

        :param fullTransactions: If True includes full transactions, if False includes only transaction hashes.
        :type fullTransactions: bool, optional
        :return: List of transactions (either represented by the transaction hash or a transaction object).
        :rtype: list of (Transaction or str)
        """
        result = None
        if fullTransactions is not None:
            result = self.__call("mempoolContent", fullTransactions)
        else:
            result = self.__call("mempoolContent")
        return [tx if type(tx) is str else Transaction(**tx) for tx in result]

    def minerAddress(self):
        """
        Returns the miner address.

        :return: The miner address configured on the node.
        :rtype: str
        """
        return self.__call("minerAddress")

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
        if threads is not None:
            return self.__call("minerThreads", threads)
        else:
            return self.__call("minerThreads")

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
        if fee is not None:
            return self.__call("minFeePerByte", fee)
        else:
            return self.__call("minFeePerByte")

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
        if state is not None:
            return self.__call("mining", state)
        else:
            return self.__call("mining")

    def peerCount(self):
        """
        Returns number of peers currently connected to the client.

        :return: Number of connected peers.
        :rtype: int
        """
        return self.__call("peerCount")

    def peerList(self):
        """
        Returns list of peers known to the client.

        :return: The list of peers.
        :rtype: list of (Peer)
        """
        return [Peer(**peer) for peer in self.__call("peerList")]

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
        result = None
        if command is not None:
            result = self.__call("peerState", address, command)
        else:
            result = self.__call("peerState", address)
        return Peer(**result)

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
        if address is not None:
            return self.__call("pool", address)
        else:
            return self.__call("pool")

    def poolConfirmedBalance(self):
        """
        Returns the confirmed mining pool balance.

        :return: The confirmed mining pool balance (in smallest unit).
        :rtype: int
        """
        return self.__call("poolConfirmedBalance")

    def poolConnectionState(self):
        """
        Returns the connection state to mining pool.

        :return: The mining pool connection state.
        :rtype: PoolConnectionState
        """
        return PoolConnectionState(self.__call("poolConnectionState"))

    def sendRawTransaction(self, transaction):
        """
        Sends a signed message call transaction or a contract creation, if the data field contains code.

        :param transaction: The hex encoded signed transaction
        :type transaction: str
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self.__call("sendRawTransaction", transaction)

    def sendTransaction(self, transaction):
        """
        Creates new message call transaction or a contract creation, if the data field contains code.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self.__call("sendTransaction", transaction)

    def submitBlock(self, block):
        """
        Submits a block to the node. When the block is valid, the node will forward it to other nodes in the network.

        :param block: Hex-encoded full block (including header, interlink and body). When submitting work from getWork, remember to include the suffix.
        :type block: Block
        """
        self.__call("submitBlock", block)

    def syncing(self):
        """
        Returns an object with data about the sync status or False.

        :return: An object with sync status data or False, when not syncing.
        :rtype: SyncStatus
        """
        result = self.__call("syncing")
        if type(result) is not bool:
            return SyncStatus(**result)
        else:
            return result

    def getRawTransactionInfo(self, transaction):
        """
        Deserializes hex-encoded transaction and returns a transaction object.

        :param transaction: The hex encoded signed transaction.
        :type transaction: str
        :return: The transaction object.
        :rtype: Transaction
        """
        return Transaction(**self.__call("getRawTransactionInfo", transaction))

    def resetConstant(self, constant):
        """
        Resets the constant to default value.

        :param constant: Name of the constant.
        :type constant: str
        :return: The new value of the constant.
        :rtype: int
        """
        return self.__call("constant", constant, "reset")
