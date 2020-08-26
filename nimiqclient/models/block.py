__all__ = ["Block", "BlockTemplateHeader", "BlockTemplateBody", "BlockTemplate"]

from .transaction import Transaction


class Block:
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

    def __init__(
        self,
        number,
        hash,
        pow,
        parentHash,
        nonce,
        bodyHash,
        accountsHash,
        difficulty,
        timestamp,
        confirmations,
        miner,
        minerAddress,
        extraData,
        size,
        transactions,
    ):
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
            tt = type(transaction)
            if tt is not str and tt is not Transaction:
                if tt is dict:
                    transactions[index] = Transaction(**transaction)
                else:
                    from ..nimiq_client import InternalErrorException

                    raise InternalErrorException(
                        "Couldn't parse Transaction {0}".format(transaction)
                    )
        self.transactions = transactions


class BlockTemplateHeader:
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


class BlockTemplateBody:
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

    def __init__(
        self, hash, minerAddr, extraData, transactions, prunedAccounts, merkleHashes
    ):
        self.hash = hash
        self.minerAddr = minerAddr
        self.extraData = extraData
        self.transactions = transactions
        self.prunedAccounts = prunedAccounts
        self.merkleHashes = merkleHashes


class BlockTemplate:
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
