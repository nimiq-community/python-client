__all__ = ["NimiqClient", "InternalErrorException", "RemoteErrorException"]

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
    """

    def __init__(
        self, scheme="http", user="", password="", host="127.0.0.1", port=8648
    ):
        self.id = 0
        self.url = "{0}://{1}:{2}".format(scheme, host, port)
        self.auth = HTTPBasicAuth(user, password)
        self.session = requests.Session()

    def _call(self, method, *args):
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
            "params": list(args),
            "id": self.id,
        }

        # make request
        req_error = None
        try:
            resp_object = self.session.post(
                self.url, json=call_object, auth=self.auth
            ).json()

        except Exception as e:
            req_error = e

        # raise if there was any error
        if req_error is not None:
            raise InternalErrorException(req_error)

        error = resp_object.get("error")
        if error is not None:
            raise RemoteErrorException(error.get("message"), error.get("code"))

        return resp_object.get("result")

    def _get_account(self, data):
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
        return [self._get_account(account) for account in self._call("accounts")]

    def block_number(self):
        """
        Returns the height of most recent block.

        :return: The current block height the client is on.
        :rtype: int
        """
        return self._call("blockNumber")

    def consensus(self):
        """
        Returns information on the current consensus state.

        :return: Consensus state. "established" is the value for a good state, other values indicate bad.
        :rtype: ConsensusState
        """
        return ConsensusState(self._call("consensus"))

    def constant(self, constant):
        """
        Returns the value of the constant.

        :param constant: The class and name of the constant (format should be "Class.CONSTANT").
        :type constant: str
        :return: The value of the constant.
        :rtype: int
        """
        return self._call("constant", constant)

    def set_constant(self, constant, value=None):
        """
        Overrides the value of a constant. It sets the constant to the given value. To reset the constant use reset_constant() instead.

        :param constant: The class and name of the constant (format should be "Class.CONSTANT").
        :type constant: str
        :param value: The new value of the constant.
        :type value: int, optional
        :return: The new value of the constant.
        :rtype: int
        """
        return self._call("constant", constant, value)

    def create_account(self):
        """
        Creates a new account and stores its private key in the client store.

        :return: Information on the wallet that was created using the command.
        :rtype: Wallet
        """
        return Wallet(**self._call("createAccount"))

    def create_raw_transaction(self, transaction):
        """
        Creates and signs a transaction without sending it. The transaction can then be send via sendRawTransaction() without accidentally replaying it.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: Hex-encoded transaction.
        :rtype: str
        """
        return self._call("createRawTransaction", transaction)

    def get_account(self, address):
        """
        Returns details for the account of given address.

        :param address: Address to get account details.
        :type address: str
        :return: Details about the account. Returns the default empty basic account for non-existing accounts.
        :rtype: Account or VestingContract or HTLC
        """
        return self._get_account(self._call("getAccount", address))

    def get_balance(self, address):
        """
        Returns the balance of the account of given address.

        :param address: Address to check for balance.
        :type address: str
        :return: The current balance at the specified address (in smalest unit).
        :rtype: int
        """
        return self._call("getBalance", address)

    def get_block_by_hash(self, hash, include_transactions=None):
        """
        Returns information about a block by hash.

        :param hash: Hash of the block to gather information on.
        :type hash: str
        :param include_transactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type include_transactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = None
        if include_transactions is not None:
            result = self._call("getBlockByHash", hash, include_transactions)
        else:
            result = self._call("getBlockByHash", hash)
        return Block(**result) if result is not None else None

    def get_block_by_number(self, height, include_transactions=None):
        """
        Returns information about a block by block number.

        :param height: The height of the block to gather information on.
        :type height: int
        :param include_transactions: If True it returns the full transaction objects, if False only the hashes of the transactions.
        :type include_transactions: bool, optional
        :return: A block object or None when no block was found.
        :rtype: Block or None
        """
        result = None
        if include_transactions is not None:
            result = self._call("getBlockByNumber", height, include_transactions)
        else:
            result = self._call("getBlockByNumber", height)
        return Block(**result) if result is not None else None

    def get_block_template(self, address=None, extra_data=""):
        """
        Returns a template to build the next block for mining. This will consider pool instructions when connected to a pool.
        If address and extra_data are provided the values are overriden.

        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :type address: str
        :param extra_data: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :type extra_data: str
        :return: A block template object.
        :rtype: BlockTemplate
        """
        result = None
        if address is not None:
            result = self._call("getBlockTemplate", address, extra_data)
        else:
            result = self._call("getBlockTemplate")
        return BlockTemplate(
            BlockTemplateHeader(**result.get("header")),
            result.get("interlink"),
            BlockTemplateBody(**result.get("body")),
            result.get("target"),
        )

    def get_block_transaction_count_by_hash(self, hash):
        """
        Returns the number of transactions in a block from a block matching the given block hash.

        :param hash: Hash of the block.
        :type hash: str
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self._call("getBlockTransactionCountByHash", hash)

    def get_block_transaction_count_by_number(self, height):
        """
        Returns the number of transactions in a block matching the given block number.

        :param height: Height of the block.
        :type height: int
        :return: Number of transactions in the block found, or None, when no block was found.
        :rtype: int or None
        """
        return self._call("getBlockTransactionCountByNumber", height)

    def get_transaction_by_block_hash_and_index(self, hash, index):
        """
        Returns information about a transaction by block hash and transaction index position.

        :param hash: Hash of the block containing the transaction.
        :type hash: str
        :param index: Index of the transaction in the block.
        :type index: int
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self._call("getTransactionByBlockHashAndIndex", hash, index)
        if result is not None:
            return Transaction(**result)
        else:
            return None

    def get_transaction_by_block_number_and_index(self, height, index):
        """
        Returns information about a transaction by block number and transaction index position.

        :param height: Height of the block containing the transaction.
        :type height: int
        :param index: Index of the transaction in the block.
        :type index: int
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self._call("getTransactionByBlockNumberAndIndex", height, index)
        if result is not None:
            return Transaction(**result)
        else:
            return None

    def get_transaction_by_hash(self, hash):
        """
        Returns the information about a transaction requested by transaction hash.

        :param hash: Hash of a transaction.
        :type hash: str
        :return: A transaction object or None when no transaction was found.
        :rtype: Transaction or None
        """
        result = self._call("getTransactionByHash", hash)
        if result is not None:
            return Transaction(**result)
        else:
            return None

    def get_transaction_receipt(self, hash):
        """
        Returns the receipt of a transaction by transaction hash.

        :param hash: Hash of a transaction.
        :type hash: str
        :return: A transaction receipt object, or None when no receipt was found.
        :rtype: TransactionReceipt or None
        """
        result = self._call("getTransactionReceipt", hash)
        if result is not None:
            return TransactionReceipt(**result)
        else:
            return None

    def get_transactions_by_address(self, address, number_of_transactions=None):
        """
        Returns the latest transactions successfully performed by or for an address.
        Note that this information might change when blocks are rewinded on the local state due to forks.

        :param address: Address of which transactions should be gathered.
        :type address: str
        :param number_of_transactions: Number of transactions that shall be returned.
        :type number_of_transactions: int, optional
        :return: List of transactions linked to the requested address.
        :rtype: list of (Transaction)
        """
        result = None
        if number_of_transactions is not None:
            result = self._call(
                "getTransactionsByAddress", address, number_of_transactions
            )
        else:
            result = self._call("getTransactionsByAddress", address)
        return [Transaction(**tx) for tx in result]

    def get_work(self, address=None, extra_data=""):
        """
        Returns instructions to mine the next block. This will consider pool instructions when connected to a pool.

        :param address: The address to use as a miner for this block. This overrides the address provided during startup or from the pool.
        :type address: str
        :param extra_data: Hex-encoded value for the extra data field. This overrides the extra data provided during startup or from the pool.
        :type extra_data: str
        :return: Mining work instructions.
        :rtype: WorkInstructions
        """
        result = None
        if address is not None:
            result = self._call("getWork", address, extra_data)
        else:
            result = self._call("getWork")
        return WorkInstructions(**result)

    def hashrate(self):
        """
        Returns the number of hashes per second that the node is mining with.

        :return: Number of hashes per second.
        :rtype: float
        """
        return self._call("hashrate")

    def set_log(self, tag, level):
        """
        Sets the log level of the node.

        :param tag: Tag: If "*" the log level is set globally, otherwise the log level is applied only on this tag.
        :type tag: str
        :param level: Minimum log level to display.
        :type level: LogLevel
        :return: True if the log level was changed, False otherwise.
        :rtype: bool
        """
        return self._call("log", tag, level)

    def mempool(self):
        """
        Returns information on the current mempool situation. This will provide an overview of the number of transactions sorted into buckets based on their fee per byte (in smallest unit).

        :return: Mempool information.
        :rtype: MempoolInfo
        """
        result = self._call("mempool")
        return MempoolInfo(**result)

    def mempool_content(self, include_transactions=None):
        """
        Returns transactions that are currently in the mempool.

        :param include_transactions: If True includes full transactions, if False includes only transaction hashes.
        :type include_transactions: bool, optional
        :return: List of transactions (either represented by the transaction hash or a transaction object).
        :rtype: list of (Transaction or str)
        """
        result = None
        if include_transactions is not None:
            result = self._call("mempoolContent", include_transactions)
        else:
            result = self._call("mempoolContent")
        return [tx if type(tx) is str else Transaction(**tx) for tx in result]

    def miner_address(self):
        """
        Returns the miner address.

        :return: The miner address configured on the node.
        :rtype: str
        """
        return self._call("minerAddress")

    def miner_threads(self):
        """
        Returns the number of CPU threads for the miner.

        :return: The number of threads allocated for mining.
        :rtype: int
        """
        return self._call("minerThreads")

    def set_miner_threads(self, threads=None):
        """
        Sets the number of CPU threads for the miner.

        :param threads: The number of threads to allocate for mining.
        :type threads: int, optional
        :return: The new number of threads allocated for mining.
        :rtype: int
        """
        return self._call("minerThreads", threads)

    def min_fee_per_byte(self):
        """
        Returns the minimum fee per byte.

        :return: The new minimum fee per byte.
        :rtype: int
        """
        return self._call("minFeePerByte")

    def set_min_fee_per_byte(self, fee=None):
        """
        Sets the minimum fee per byte.

        :param fee: The new minimum fee per byte.
        :type fee: int, optional
        :return: The new minimum fee per byte.
        :rtype: int
        """
        return self._call("minFeePerByte", fee)

    def is_mining(self):
        """
        Returns true if client is actively mining new blocks.

        :return: True if the client is mining, otherwise False.
        :rtype: bool
        """
        return self._call("mining")

    def set_mining(self, state=None):
        """
        Sets the client mining state.

        :param state: The state to be set.
        :type state: bool
        :return: True if the client is mining, otherwise False.
        :rtype: bool
        """
        return self._call("mining", state)

    def peer_count(self):
        """
        Returns number of peers currently connected to the client.

        :return: Number of connected peers.
        :rtype: int
        """
        return self._call("peerCount")

    def peer_list(self):
        """
        Returns list of peers known to the client.

        :return: The list of peers.
        :rtype: list of (Peer)
        """
        return [Peer(**peer) for peer in self._call("peerList")]

    def peer_state(self, address):
        """
        Returns the state of the peer.

        :param address: The address of the peer.
        :type address: str
        :return: The current state of the peer.
        :rtype: Peer
        """
        return Peer(**self._call("peerState", address))

    def set_peer_state(self, address, command=None):
        """
        Returns the state of the peer.

        :param address: The address of the peer.
        :type address: str
        :param command: The command to send.
        :type command: PeerStateCommand
        :return: The new state of the peer.
        :rtype: Peer
        """
        return Peer(**self._call("peerState", address, command))

    def pool(self):
        """
        Returns the mining pool.

        :return: The mining pool connection string, or None if not enabled.
        :rtype: str or None
        """
        return self._call("pool")

    def set_pool(self, address=None):
        """
        Sets the mining pool.

        :param address: The mining pool connection string ("url:port") or boolean to enable/disable pool mining.
        :type address: str, optional
        :return: The new mining pool connection string, or None if not enabled.
        :rtype: str or None
        """
        return self._call("pool", address)

    def pool_confirmed_balance(self):
        """
        Returns the confirmed mining pool balance.

        :return: The confirmed mining pool balance (in smallest unit).
        :rtype: int
        """
        return self._call("poolConfirmedBalance")

    def pool_connection_state(self):
        """
        Returns the connection state to mining pool.

        :return: The mining pool connection state.
        :rtype: PoolConnectionState
        """
        return PoolConnectionState(self._call("poolConnectionState"))

    def send_raw_transaction(self, transaction):
        """
        Sends a signed message call transaction or a contract creation, if the data field contains code.

        :param transaction: The hex encoded signed transaction
        :type transaction: str
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self._call("sendRawTransaction", transaction)

    def send_transaction(self, transaction):
        """
        Creates new message call transaction or a contract creation, if the data field contains code.

        :param transaction: The transaction object.
        :type transaction: OutgoingTransaction
        :return: The Hex-encoded transaction hash.
        :rtype: str
        """
        return self._call("sendTransaction", transaction)

    def submit_block(self, block):
        """
        Submits a block to the node. When the block is valid, the node will forward it to other nodes in the network.

        :param block: Hex-encoded full block (including header, interlink and body). When submitting work from getWork, remember to include the suffix.
        :type block: Block
        """
        self._call("submitBlock", block)

    def syncing(self):
        """
        Returns an object with data about the sync status or False.

        :return: An object with sync status data or False, when not syncing.
        :rtype: SyncStatus
        """
        result = self._call("syncing")
        if type(result) is not bool:
            return SyncStatus(**result)
        else:
            return result

    def get_raw_transaction_info(self, transaction):
        """
        Deserializes hex-encoded transaction and returns a transaction object.

        :param transaction: The hex encoded signed transaction.
        :type transaction: str
        :return: The transaction object.
        :rtype: Transaction
        """
        return Transaction(**self._call("getRawTransactionInfo", transaction))

    def reset_constant(self, constant):
        """
        Resets the constant to default value.

        :param constant: Name of the constant.
        :type constant: str
        :return: The new value of the constant.
        :rtype: int
        """
        return self._call("constant", constant, "reset")
