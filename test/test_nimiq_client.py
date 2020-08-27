from nimiqclient import *
from .fixtures.account import *
from .fixtures.block import *
from .fixtures.mempool import *
from .fixtures.miner import *
from .fixtures.node import *
from .fixtures.peer import *
from .fixtures.transaction import *
from .session_stub import SessionStub

import unittest


class TestNimiqClientMethods(unittest.TestCase):
    client = None

    def setUp(self):
        self.client = NimiqClient(
            scheme="http", user="", password="", host="127.0.0.1", port=8648
        )
        self.client.session = SessionStub()

    def tearDown(self):
        pass

    def test_peerCount(self):
        SessionStub.test_data = PeerFixtures.peer_count()

        result = self.client.peer_count()

        self.assertEqual("peerCount", SessionStub.latest_request_method)

        self.assertEqual(6, result)

    def test_syncingStateWhenSyncing(self):
        SessionStub.test_data = NodeFixtures.syncing()

        result = self.client.syncing()

        self.assertEqual("syncing", SessionStub.latest_request_method)

        self.assertFalse(isinstance(result, bool))
        self.assertEqual(578430, result.startingBlock)
        self.assertEqual(586493, result.currentBlock)
        self.assertEqual(586493, result.highestBlock)

    def test_syncingStateWhenNotSyncing(self):
        SessionStub.test_data = NodeFixtures.syncing_not_syncing()

        result = self.client.syncing()

        self.assertEqual("syncing", SessionStub.latest_request_method)

        self.assertTrue(isinstance(result, bool))
        self.assertEqual(False, result)

    def test_consensusState(self):
        SessionStub.test_data = NodeFixtures.consensus_syncing()

        result = self.client.consensus()

        self.assertEqual("consensus", SessionStub.latest_request_method)

        self.assertEqual(ConsensusState.SYNCING, result)

    def test_peerListWithPeers(self):
        SessionStub.test_data = PeerFixtures.peer_list()

        result = self.client.peer_list()

        self.assertEqual("peerList", SessionStub.latest_request_method)

        self.assertEqual(len(result), 2)
        self.assertTrue(result[0] is not None)
        self.assertEqual("b99034c552e9c0fd34eb95c1cdf17f5e", result[0].id)
        self.assertEqual(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            result[0].address,
        )
        self.assertEqual(PeerAddressState.ESTABLISHED, result[0].addressState)
        self.assertEqual(PeerConnectionState.ESTABLISHED, result[0].connectionState)

        self.assertTrue(result[1] is not None)
        self.assertEqual("e37dca72802c972d45b37735e9595cf0", result[1].id)
        self.assertEqual(
            "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
            result[1].address,
        )
        self.assertEqual(PeerAddressState.FAILED, result[1].addressState)
        self.assertEqual(None, result[1].connectionState)

    def test_peerListWhenEmpty(self):
        SessionStub.test_data = PeerFixtures.peer_list_empty()

        result = self.client.peer_list()

        self.assertEqual("peerList", SessionStub.latest_request_method)

        self.assertEqual(len(result), 0)

    def test_peerNormal(self):
        SessionStub.test_data = PeerFixtures.peer_state_normal()

        result = self.client.peer_state(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e"
        )

        self.assertEqual("peerState", SessionStub.latest_request_method)
        self.assertEqual(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual("b99034c552e9c0fd34eb95c1cdf17f5e", result.id)
        self.assertEqual(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            result.address,
        )
        self.assertEqual(PeerAddressState.ESTABLISHED, result.addressState)
        self.assertEqual(PeerConnectionState.ESTABLISHED, result.connectionState)

    def test_peerFailed(self):
        SessionStub.test_data = PeerFixtures.peer_state_failed()

        result = self.client.peer_state(
            "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0"
        )

        self.assertEqual("peerState", SessionStub.latest_request_method)
        self.assertEqual(
            "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual("e37dca72802c972d45b37735e9595cf0", result.id)
        self.assertEqual(
            "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
            result.address,
        )
        self.assertEqual(PeerAddressState.FAILED, result.addressState)
        self.assertEqual(None, result.connectionState)

    def test_peerError(self):
        SessionStub.test_data = PeerFixtures.peer_state_error()

        self.assertRaises(RemoteErrorException, self.client.peer_state, "unknown")

    def test_setPeerNormal(self):
        SessionStub.test_data = PeerFixtures.peer_state_normal()

        result = self.client.set_peer_state(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            PeerStateCommand.CONNECT,
        )

        self.assertEqual("peerState", SessionStub.latest_request_method)
        self.assertEqual(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual("connect", SessionStub.latest_request_params[1])

        self.assertTrue(result is not None)
        self.assertEqual("b99034c552e9c0fd34eb95c1cdf17f5e", result.id)
        self.assertEqual(
            "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
            result.address,
        )
        self.assertEqual(PeerAddressState.ESTABLISHED, result.addressState)
        self.assertEqual(PeerConnectionState.ESTABLISHED, result.connectionState)

    def test_sendRawTransaction(self):
        SessionStub.test_data = TransactionFixtures.send_transaction()

        result = self.client.send_raw_transaction(
            "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000000010000000000000001000dc2e201b5a1755aec80aa4227d5afc6b0de0fcfede8541f31b3c07b9a85449ea9926c1c958628d85a2b481556034ab3d67ff7de28772520813c84aaaf8108f6297c580c"
        )

        self.assertEqual("sendRawTransaction", SessionStub.latest_request_method)
        self.assertEqual(
            "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000000010000000000000001000dc2e201b5a1755aec80aa4227d5afc6b0de0fcfede8541f31b3c07b9a85449ea9926c1c958628d85a2b481556034ab3d67ff7de28772520813c84aaaf8108f6297c580c",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(
            "81cf3f07b6b0646bb16833d57cda801ad5957e264b64705edeef6191fea0ad63", result
        )

    def test_createRawTransaction(self):
        SessionStub.test_data = TransactionFixtures.create_raw_transaction_basic()

        transaction = OutgoingTransaction(
            from_="NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
            fromType=AccountType.BASIC,
            to="NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U",
            toType=AccountType.BASIC,
            value=100000,
            fee=1,
            data=None,
        )

        result = self.client.create_raw_transaction(transaction)

        self.assertEqual("createRawTransaction", SessionStub.latest_request_method)

        param = SessionStub.latest_request_params[0]
        self.assertEqual(
            param.__dict__,
            {
                "from": "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
                "fromType": AccountType.BASIC,
                "to": "NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U",
                "toType": AccountType.BASIC,
                "value": 100000,
                "fee": 1,
                "data": None,
            },
        )

        self.assertEqual(
            "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000186a00000000000000001000af84c01239b16cee089836c2af5c7b1dbb22cdc0b4864349f7f3805909aa8cf24e4c1ff0461832e86f3624778a867d5f2ba318f92918ada7ae28d70d40c4ef1d6413802",
            result,
        )

    def test_sendTransaction(self):
        SessionStub.test_data = TransactionFixtures.send_transaction()

        transaction = OutgoingTransaction(
            from_="NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
            fromType=AccountType.BASIC,
            to="NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U",
            toType=AccountType.BASIC,
            value=100000,
            fee=1,
            data=None,
        )

        result = self.client.send_transaction(transaction)

        self.assertEqual("sendTransaction", SessionStub.latest_request_method)

        param = SessionStub.latest_request_params[0]
        self.assertEqual(
            param.__dict__,
            {
                "from": "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
                "fromType": AccountType.BASIC,
                "to": "NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U",
                "toType": AccountType.BASIC,
                "value": 100000,
                "fee": 1,
                "data": None,
            },
        )

        self.assertEqual(
            "81cf3f07b6b0646bb16833d57cda801ad5957e264b64705edeef6191fea0ad63", result
        )

    def test_getRawTransactionInfo(self):
        SessionStub.test_data = TransactionFixtures.get_raw_transaction_info_basic()

        result = self.client.get_raw_transaction_info(
            "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000186a00000000000000001000af84c01239b16cee089836c2af5c7b1dbb22cdc0b4864349f7f3805909aa8cf24e4c1ff0461832e86f3624778a867d5f2ba318f92918ada7ae28d70d40c4ef1d6413802"
        )

        self.assertEqual("getRawTransactionInfo", SessionStub.latest_request_method)
        self.assertEqual(
            "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000186a00000000000000001000af84c01239b16cee089836c2af5c7b1dbb22cdc0b4864349f7f3805909aa8cf24e4c1ff0461832e86f3624778a867d5f2ba318f92918ada7ae28d70d40c4ef1d6413802",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual(
            "7784f2f6eaa076fa5cf0e4d06311ad204b2f485de622231785451181e8129091",
            result.hash,
        )
        self.assertEqual("b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f5", result.from_)
        self.assertEqual(
            "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM", result.fromAddress
        )
        self.assertEqual("305dbaac7514a06dae935e40d599caf1bd8a243c", result.to)
        self.assertEqual(
            "NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U", result.toAddress
        )
        self.assertEqual(100000, result.value)
        self.assertEqual(1, result.fee)

    def test_getTransactionByBlockHashAndIndex(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_full()

        result = self.client.get_transaction_by_block_hash_and_index(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786", 0
        )

        self.assertEqual(
            "getTransactionByBlockHashAndIndex", SessionStub.latest_request_method
        )
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual(0, SessionStub.latest_request_params[1])

        self.assertTrue(result is not None)
        self.assertEqual(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
            result.hash,
        )
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.blockHash,
        )
        self.assertEqual(0, result.transactionIndex)
        self.assertEqual("355b4fe2304a9c818b9f0c3c1aaaf4ad4f6a0279", result.from_)
        self.assertEqual(
            "NQ16 6MDL YQHG 9AE8 32UY 1GX1 MAPL MM7N L0KR", result.fromAddress
        )
        self.assertEqual("4f61c06feeb7971af6997125fe40d629c01af92f", result.to)
        self.assertEqual(
            "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F", result.toAddress
        )
        self.assertEqual(2636710000, result.value)
        self.assertEqual(0, result.fee)

    def test_getTransactionByBlockHashAndIndexWhenNotFound(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_not_found()

        result = self.client.get_transaction_by_block_hash_and_index(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786", 5
        )

        self.assertEqual(
            "getTransactionByBlockHashAndIndex", SessionStub.latest_request_method
        )
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual(5, SessionStub.latest_request_params[1])

        self.assertTrue(result is None)

    def test_getTransactionByBlockNumberAndIndex(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_full()

        result = self.client.get_transaction_by_block_number_and_index(11608, 0)

        self.assertEqual(
            "getTransactionByBlockNumberAndIndex", SessionStub.latest_request_method
        )
        self.assertEqual(11608, SessionStub.latest_request_params[0])
        self.assertEqual(0, SessionStub.latest_request_params[1])

        self.assertTrue(result is not None)
        self.assertEqual(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
            result.hash,
        )
        self.assertEqual(11608, result.blockNumber)
        self.assertEqual(0, result.transactionIndex)
        self.assertEqual("355b4fe2304a9c818b9f0c3c1aaaf4ad4f6a0279", result.from_)
        self.assertEqual(
            "NQ16 6MDL YQHG 9AE8 32UY 1GX1 MAPL MM7N L0KR", result.fromAddress
        )
        self.assertEqual("4f61c06feeb7971af6997125fe40d629c01af92f", result.to)
        self.assertEqual(
            "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F", result.toAddress
        )
        self.assertEqual(2636710000, result.value)
        self.assertEqual(0, result.fee)

    def test_getTransactionByBlockNumberAndIndexWhenNotFound(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_not_found()

        result = self.client.get_transaction_by_block_number_and_index(11608, 0)

        self.assertEqual(
            "getTransactionByBlockNumberAndIndex", SessionStub.latest_request_method
        )
        self.assertEqual(11608, SessionStub.latest_request_params[0])
        self.assertEqual(0, SessionStub.latest_request_params[1])

        self.assertTrue(result is None)

    def test_getTransactionByHash(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_full()

        result = self.client.get_transaction_by_hash(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430"
        )

        self.assertEqual("getTransactionByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
            result.hash,
        )
        self.assertEqual(11608, result.blockNumber)
        self.assertEqual("355b4fe2304a9c818b9f0c3c1aaaf4ad4f6a0279", result.from_)
        self.assertEqual(
            "NQ16 6MDL YQHG 9AE8 32UY 1GX1 MAPL MM7N L0KR", result.fromAddress
        )
        self.assertEqual("4f61c06feeb7971af6997125fe40d629c01af92f", result.to)
        self.assertEqual(
            "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F", result.toAddress
        )
        self.assertEqual(2636710000, result.value)
        self.assertEqual(0, result.fee)

    def test_getTransactionByHashWhenNotFound(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_not_found()

        result = self.client.get_transaction_by_hash(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430"
        )

        self.assertEqual("getTransactionByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is None)

    def test_getTransactionByHashForContractCreation(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_contract_creation()

        result = self.client.get_transaction_by_hash(
            "539f6172b19f63be376ab7e962c368bb5f611deff6b159152c4cdf509f7daad2"
        )

        self.assertEqual("getTransactionByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "539f6172b19f63be376ab7e962c368bb5f611deff6b159152c4cdf509f7daad2",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual(
            "539f6172b19f63be376ab7e962c368bb5f611deff6b159152c4cdf509f7daad2",
            result.hash,
        )
        self.assertEqual(
            "96fef80f517f0b2704476dee48da147049b591e8f034e5bf93f1f6935fd51b85",
            result.blockHash,
        )
        self.assertEqual(1102500, result.blockNumber)
        self.assertEqual(1590148157, result.timestamp)
        self.assertEqual(7115, result.confirmations)
        self.assertEqual("d62d519b3478c63bdd729cf2ccb863178060c64a", result.from_)
        self.assertEqual(
            "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA", result.fromAddress
        )
        self.assertEqual("a22eaf17848130c9b370e42ff7d345680df245e1", result.to)
        self.assertEqual(
            "NQ87 L8PA X5U4 G4QC KCTG UGPY FLS5 D06Y 4HF1", result.toAddress
        )
        self.assertEqual(5000000000, result.value)
        self.assertEqual(0, result.fee)
        self.assertEqual(
            "d62d519b3478c63bdd729cf2ccb863178060c64af5ad55071730d3b9f05989481eefbda7324a44f8030c63b9444960db429081543939166f05116cebc37bd6975ac9f9e3bb43a5ab0b010010d2de",
            result.data,
        )
        self.assertEqual(1, result.flags)

    def test_getTransactionReceipt(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_receipt_found()

        result = self.client.get_transaction_receipt(
            "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e"
        )

        self.assertEqual("getTransactionReceipt", SessionStub.latest_request_method)
        self.assertEqual(
            "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
            SessionStub.latest_request_params[0],
        )

        self.assertTrue(result is not None)
        self.assertEqual(
            "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
            result.transactionHash,
        )
        self.assertEqual(-1, result.transactionIndex)
        self.assertEqual(11608, result.blockNumber)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.blockHash,
        )
        self.assertEqual(1523412456, result.timestamp)
        self.assertEqual(718846, result.confirmations)

    def test_getTransactionReceiptWhenNotFound(self):
        SessionStub.test_data = TransactionFixtures.get_transaction_receipt_not_found()

        result = self.client.get_transaction_receipt("unknown")

        self.assertEqual("getTransactionReceipt", SessionStub.latest_request_method)
        self.assertEqual("unknown", SessionStub.latest_request_params[0])

        self.assertTrue(result is None)

    def test_getTransactionsByAddress(self):
        SessionStub.test_data = TransactionFixtures.get_transactions_found()

        result = self.client.get_transactions_by_address(
            "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F"
        )

        self.assertEqual("getTransactionsByAddress", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(3, len(result))
        self.assertTrue(result[0] is not None)
        self.assertEqual(
            "a514abb3ee4d3fbedf8a91156fb9ec4fdaf32f0d3d3da3c1dbc5fd1ee48db43e",
            result[0].hash,
        )
        self.assertTrue(result[1] is not None)
        self.assertEqual(
            "c8c0f586b11c7f39873c3de08610d63e8bec1ceaeba5e8a3bb13c709b2935f73",
            result[1].hash,
        )
        self.assertTrue(result[2] is not None)
        self.assertEqual(
            "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
            result[2].hash,
        )

    def test_getTransactionsByAddressWhenNoFound(self):
        SessionStub.test_data = TransactionFixtures.get_transactions_not_found()

        result = self.client.get_transactions_by_address(
            "NQ10 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F"
        )

        self.assertEqual("getTransactionsByAddress", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ10 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(0, len(result))

    def test_mempoolContentHashesOnly(self):
        SessionStub.test_data = MemPoolFixtures.mempool_content_hashes_only()

        result = self.client.mempool_content()

        self.assertEqual("mempoolContent", SessionStub.latest_request_method)
        self.assertEqual(0, len(SessionStub.latest_request_params))

        self.assertEqual(3, len(result))
        self.assertTrue(result[0] is not None)
        self.assertEqual(
            "5bb722c2afe25c18ba33d453b3ac2c90ac278c595cc92f6188c8b699e8fb006a",
            result[0],
        )
        self.assertTrue(result[1] is not None)
        self.assertEqual(
            "f59a30e0a7e3348ef569225db1f4c29026aeac4350f8c6e751f669eddce0c718",
            result[1],
        )
        self.assertTrue(result[2] is not None)
        self.assertEqual(
            "9cd9c1d0ffcaebfcfe86bc2ae73b4e82a488de99c8e3faef92b05432bb94519c",
            result[2],
        )

    def test_mempoolContentFullTransactions(self):
        SessionStub.test_data = MemPoolFixtures.mempool_content_full_transactions()

        result = self.client.mempool_content(True)

        self.assertEqual("mempoolContent", SessionStub.latest_request_method)
        self.assertEqual(True, SessionStub.latest_request_params[0])

        self.assertEqual(3, len(result))
        self.assertTrue(result[0] is not None)
        self.assertEqual(
            "5bb722c2afe25c18ba33d453b3ac2c90ac278c595cc92f6188c8b699e8fb006a",
            result[0].hash,
        )
        self.assertTrue(result[1] is not None)
        self.assertEqual(
            "f59a30e0a7e3348ef569225db1f4c29026aeac4350f8c6e751f669eddce0c718",
            result[1].hash,
        )
        self.assertTrue(result[2] is not None)
        self.assertEqual(
            "9cd9c1d0ffcaebfcfe86bc2ae73b4e82a488de99c8e3faef92b05432bb94519c",
            result[2].hash,
        )

    def test_mempoolWhenFull(self):
        SessionStub.test_data = MemPoolFixtures.mempool()

        result = self.client.mempool()

        self.assertEqual("mempool", SessionStub.latest_request_method)

        self.assertTrue(result is not None)
        self.assertEqual(3, result.total)
        self.assertEqual([1], result.buckets)
        self.assertEqual(3, result.transactionsPerBucket[1])

    def test_mempoolWhenEmpty(self):
        SessionStub.test_data = MemPoolFixtures.mempool_empty()

        result = self.client.mempool()

        self.assertEqual("mempool", SessionStub.latest_request_method)

        self.assertTrue(result is not None)
        self.assertEqual(0, result.total)
        self.assertEqual([], result.buckets)
        self.assertEqual(0, len(result.transactionsPerBucket))

    def test_minFeePerByte(self):
        SessionStub.test_data = NodeFixtures.min_fee_per_byte()

        result = self.client.min_fee_per_byte()

        self.assertEqual("minFeePerByte", SessionStub.latest_request_method)

        self.assertEqual(0, result)

    def test_setMinFeePerByte(self):
        SessionStub.test_data = NodeFixtures.min_fee_per_byte()

        result = self.client.set_min_fee_per_byte(0)

        self.assertEqual("minFeePerByte", SessionStub.latest_request_method)
        self.assertEqual(0, SessionStub.latest_request_params[0])

        self.assertEqual(0, result)

    def test_mining(self):
        SessionStub.test_data = MinerFixtures.mining_state()

        result = self.client.is_mining()

        self.assertEqual("mining", SessionStub.latest_request_method)

        self.assertEqual(False, result)

    def test_setMining(self):
        SessionStub.test_data = MinerFixtures.mining_state()

        result = self.client.set_mining(False)

        self.assertEqual("mining", SessionStub.latest_request_method)
        self.assertEqual(False, SessionStub.latest_request_params[0])

        self.assertEqual(False, result)

    def test_hashrate(self):
        SessionStub.test_data = MinerFixtures.hashrate()

        result = self.client.hashrate()

        self.assertEqual("hashrate", SessionStub.latest_request_method)

        self.assertEqual(52982.2731, result)

    def test_minerThreads(self):
        SessionStub.test_data = MinerFixtures.miner_threads()

        result = self.client.miner_threads()

        self.assertEqual("minerThreads", SessionStub.latest_request_method)

        self.assertEqual(2, result)

    def test_setMinerThreads(self):
        SessionStub.test_data = MinerFixtures.miner_threads()

        result = self.client.set_miner_threads(2)

        self.assertEqual("minerThreads", SessionStub.latest_request_method)
        self.assertEqual(2, SessionStub.latest_request_params[0])

        self.assertEqual(2, result)

    def test_minerAddress(self):
        SessionStub.test_data = MinerFixtures.miner_address()

        result = self.client.miner_address()

        self.assertEqual("minerAddress", SessionStub.latest_request_method)

        self.assertEqual("NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM", result)

    def test_pool(self):
        SessionStub.test_data = MinerFixtures.pool_sushipool()

        result = self.client.pool()

        self.assertEqual("pool", SessionStub.latest_request_method)

        self.assertEqual("us.sushipool.com:443", result)

    def test_setPool(self):
        SessionStub.test_data = MinerFixtures.pool_sushipool()

        result = self.client.set_pool("us.sushipool.com:443")

        self.assertEqual("pool", SessionStub.latest_request_method)
        self.assertEqual("us.sushipool.com:443", SessionStub.latest_request_params[0])

        self.assertEqual("us.sushipool.com:443", result)

    def test_getPoolWhenNoPool(self):
        SessionStub.test_data = MinerFixtures.pool_no_pool()

        result = self.client.pool()

        self.assertEqual("pool", SessionStub.latest_request_method)

        self.assertEqual(None, result)

    def test_poolConnectionState(self):
        SessionStub.test_data = MinerFixtures.pool_connection_state()

        result = self.client.pool_connection_state()

        self.assertEqual("poolConnectionState", SessionStub.latest_request_method)

        self.assertEqual(PoolConnectionState.CLOSED, result)

    def test_poolConfirmedBalance(self):
        SessionStub.test_data = MinerFixtures.pool_confirmed_balance()

        result = self.client.pool_confirmed_balance()

        self.assertEqual("poolConfirmedBalance", SessionStub.latest_request_method)

        self.assertEqual(12000, result)

    def test_getWork(self):
        SessionStub.test_data = MinerFixtures.get_work()

        result = self.client.get_work()

        self.assertEqual("getWork", SessionStub.latest_request_method)

        self.assertEqual(
            "00015a7d47ddf5152a7d06a14ea291831c3fc7af20b88240c5ae839683021bcee3e279877b3de0da8ce8878bf225f6782a2663eff9a03478c15ba839fde9f1dc3dd9e5f0cd4dbc96a30130de130eb52d8160e9197e2ccf435d8d24a09b518a5e05da87a8658ed8c02531f66a7d31757b08c88d283654ed477e5e2fec21a7ca8449241e00d620000dc2fa5e763bda00000000",
            result.data,
        )
        self.assertEqual(
            "11fad9806b8b4167517c162fa113c09606b44d24f8020804a0f756db085546ff585adfdedad9085d36527a8485b497728446c35b9b6c3db263c07dd0a1f487b1639aa37ff60ba3cf6ed8ab5146fee50a23ebd84ea37dca8c49b31e57d05c9e6c57f09a3b282b71ec2be66c1bc8268b5326bb222b11a0d0a4acd2a93c9e8a8713fe4383e9d5df3b1bf008c535281086b2bcc20e494393aea1475a5c3f13673de2cf7314d201b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f50000000000",
            result.suffix,
        )
        self.assertEqual(503371296, result.target)
        self.assertEqual("nimiq-argon2", result.algorithm)

    def test_getWorkWithOverride(self):
        SessionStub.test_data = MinerFixtures.get_work()

        result = self.client.get_work(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", ""
        )

        self.assertEqual("getWork", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual("", SessionStub.latest_request_params[1])

        self.assertEqual(
            "00015a7d47ddf5152a7d06a14ea291831c3fc7af20b88240c5ae839683021bcee3e279877b3de0da8ce8878bf225f6782a2663eff9a03478c15ba839fde9f1dc3dd9e5f0cd4dbc96a30130de130eb52d8160e9197e2ccf435d8d24a09b518a5e05da87a8658ed8c02531f66a7d31757b08c88d283654ed477e5e2fec21a7ca8449241e00d620000dc2fa5e763bda00000000",
            result.data,
        )
        self.assertEqual(
            "11fad9806b8b4167517c162fa113c09606b44d24f8020804a0f756db085546ff585adfdedad9085d36527a8485b497728446c35b9b6c3db263c07dd0a1f487b1639aa37ff60ba3cf6ed8ab5146fee50a23ebd84ea37dca8c49b31e57d05c9e6c57f09a3b282b71ec2be66c1bc8268b5326bb222b11a0d0a4acd2a93c9e8a8713fe4383e9d5df3b1bf008c535281086b2bcc20e494393aea1475a5c3f13673de2cf7314d201b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f50000000000",
            result.suffix,
        )
        self.assertEqual(503371296, result.target)
        self.assertEqual("nimiq-argon2", result.algorithm)

    def test_getBlockTemplate(self):
        SessionStub.test_data = MinerFixtures.get_work_block_template()

        result = self.client.get_block_template()

        self.assertEqual("getBlockTemplate", SessionStub.latest_request_method)

        self.assertEqual(901883, result.header.height)
        self.assertEqual(503371226, result.target)
        self.assertEqual(
            "17e250f1977ae85bdbe09468efef83587885419ee1074ddae54d3fb5a96e1f54",
            result.body.hash,
        )

    def test_getBlockTemplateWithOverride(self):
        SessionStub.test_data = MinerFixtures.get_work_block_template()

        result = self.client.get_block_template(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", ""
        )

        self.assertEqual("getBlockTemplate", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual("", SessionStub.latest_request_params[1])

        self.assertEqual(901883, result.header.height)
        self.assertEqual(503371226, result.target)
        self.assertEqual(
            "17e250f1977ae85bdbe09468efef83587885419ee1074ddae54d3fb5a96e1f54",
            result.body.hash,
        )

    def test_submitBlock(self):
        SessionStub.test_data = BlockFixtures.submit_block()

        block_hex = "000100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000f6ba2bbf7e1478a209057000471d73fbdc28df0b717747d929cfde829c4120f62e02da3d162e20fa982029dbde9cc20f6b431ab05df1764f34af4c62a4f2b33f1f010000000000015ac3185f000134990001000000000000000000000000000000000000000007546573744e657400000000"

        self.client.submit_block(block_hex)

        self.assertEqual("submitBlock", SessionStub.latest_request_method)
        self.assertEqual(block_hex, SessionStub.latest_request_params[0])

    def test_accounts(self):
        SessionStub.test_data = AccountFixtures.accounts()

        result = self.client.accounts()

        self.assertEqual(SessionStub.latest_request_method, "accounts")

        self.assertEqual(3, len(result))

        self.assertTrue(result[0] is not None)
        account = result[0]
        self.assertEqual("f925107376081be421f52d64bec775cc1fc20829", account.id)
        self.assertEqual(
            "NQ33 Y4JH 0UTN 10DX 88FM 5MJB VHTM RGFU 4219", account.address
        )
        self.assertEqual(0, account.balance)
        self.assertEqual(AccountType.BASIC, account.type)

        self.assertTrue(result[1] is not None)
        vesting = result[1]
        self.assertEqual("ebcbf0de7dae6a42d1c12967db9b2287bf2f7f0f", vesting.id)
        self.assertEqual(
            "NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF", vesting.address
        )
        self.assertEqual(52500000000000, vesting.balance)
        self.assertEqual(AccountType.VESTING, vesting.type)
        self.assertEqual("fd34ab7265a0e48c454ccbf4c9c61dfdf68f9a22", vesting.owner)
        self.assertEqual(
            "NQ62 YLSA NUK5 L3J8 QHAC RFSC KHGV YPT8 Y6H2", vesting.ownerAddress
        )
        self.assertEqual(1, vesting.vestingStart)
        self.assertEqual(259200, vesting.vestingStepBlocks)
        self.assertEqual(2625000000000, vesting.vestingStepAmount)
        self.assertEqual(52500000000000, vesting.vestingTotalAmount)

        self.assertTrue(result[2] is not None)
        htlc = result[2]
        self.assertEqual("4974636bd6d34d52b7d4a2ee4425dc2be72a2b4e", htlc.id)
        self.assertEqual("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", htlc.address)
        self.assertEqual(1000000000, htlc.balance)
        self.assertEqual(AccountType.HTLC, htlc.type)
        self.assertEqual("d62d519b3478c63bdd729cf2ccb863178060c64a", htlc.sender)
        self.assertEqual(
            "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA", htlc.senderAddress
        )
        self.assertEqual("f5ad55071730d3b9f05989481eefbda7324a44f8", htlc.recipient)
        self.assertEqual(
            "NQ41 XNNM A1QP 639T KU2R H541 VTVV LUR4 LH7Q", htlc.recipientAddress
        )
        self.assertEqual(
            "df331b3c8f8a889703092ea05503779058b7f44e71bc57176378adde424ce922",
            htlc.hashRoot,
        )
        self.assertEqual(1, htlc.hashAlgorithm)
        self.assertEqual(1, htlc.hashCount)
        self.assertEqual(1105605, htlc.timeout)
        self.assertEqual(1000000000, htlc.totalAmount)

    def test_createAccount(self):
        SessionStub.test_data = AccountFixtures.create_account()

        result = self.client.create_account()

        self.assertEqual("createAccount", SessionStub.latest_request_method)

        self.assertTrue(result is not None)
        self.assertEqual("b6edcc7924af5a05af6087959c7233ec2cf1a5db", result.id)
        self.assertEqual("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", result.address)
        self.assertEqual(
            "4f6d35cc47b77bf696b6cce72217e52edff972855bd17396b004a8453b020747",
            result.publicKey,
        )

    def test_getBalance(self):
        SessionStub.test_data = AccountFixtures.get_balance()

        result = self.client.get_balance("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET")

        self.assertEqual("getBalance", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(1200000, result)

    def test_getAccount(self):
        SessionStub.test_data = AccountFixtures.get_account_basic()

        result = self.client.get_account("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET")

        self.assertEqual("getAccount", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual("b6edcc7924af5a05af6087959c7233ec2cf1a5db", result.id)
        self.assertEqual("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", result.address)
        self.assertEqual(1200000, result.balance)
        self.assertEqual(AccountType.BASIC, result.type)

    def test_getAccountForVestingContract(self):
        SessionStub.test_data = AccountFixtures.get_account_vesting()

        result = self.client.get_account("NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF")

        self.assertEqual("getAccount", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual("ebcbf0de7dae6a42d1c12967db9b2287bf2f7f0f", result.id)
        self.assertEqual("NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF", result.address)
        self.assertEqual(52500000000000, result.balance)
        self.assertEqual(AccountType.VESTING, result.type)
        self.assertEqual("fd34ab7265a0e48c454ccbf4c9c61dfdf68f9a22", result.owner)
        self.assertEqual(
            "NQ62 YLSA NUK5 L3J8 QHAC RFSC KHGV YPT8 Y6H2", result.ownerAddress
        )
        self.assertEqual(1, result.vestingStart)
        self.assertEqual(259200, result.vestingStepBlocks)
        self.assertEqual(2625000000000, result.vestingStepAmount)
        self.assertEqual(52500000000000, result.vestingTotalAmount)

    def test_getAccountForHashedTimeLockedContract(self):
        SessionStub.test_data = AccountFixtures.get_account_vesting_htlc()

        result = self.client.get_account("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET")

        self.assertEqual("getAccount", SessionStub.latest_request_method)
        self.assertEqual(
            "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual("4974636bd6d34d52b7d4a2ee4425dc2be72a2b4e", result.id)
        self.assertEqual("NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET", result.address)
        self.assertEqual(1000000000, result.balance)
        self.assertEqual(AccountType.HTLC, result.type)
        self.assertEqual("d62d519b3478c63bdd729cf2ccb863178060c64a", result.sender)
        self.assertEqual(
            "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA", result.senderAddress
        )
        self.assertEqual("f5ad55071730d3b9f05989481eefbda7324a44f8", result.recipient)
        self.assertEqual(
            "NQ41 XNNM A1QP 639T KU2R H541 VTVV LUR4 LH7Q", result.recipientAddress
        )
        self.assertEqual(
            "df331b3c8f8a889703092ea05503779058b7f44e71bc57176378adde424ce922",
            result.hashRoot,
        )
        self.assertEqual(1, result.hashAlgorithm)
        self.assertEqual(1, result.hashCount)
        self.assertEqual(1105605, result.timeout)
        self.assertEqual(1000000000, result.totalAmount)

    def test_blockNumber(self):
        SessionStub.test_data = BlockFixtures.block_number()

        result = self.client.block_number()

        self.assertEqual("blockNumber", SessionStub.latest_request_method)

        self.assertEqual(748883, result)

    def test_getBlockTransactionCountByHash(self):
        SessionStub.test_data = BlockFixtures.block_transaction_count_found()

        result = self.client.get_block_transaction_count_by_hash(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786"
        )

        self.assertEqual(
            "getBlockTransactionCountByHash", SessionStub.latest_request_method
        )
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(2, result)

    def test_getBlockTransactionCountByHashWhenNotFound(self):
        SessionStub.test_data = BlockFixtures.block_transaction_count_not_found()

        result = self.client.get_block_transaction_count_by_hash(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786"
        )

        self.assertEqual(
            "getBlockTransactionCountByHash", SessionStub.latest_request_method
        )
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )

        self.assertEqual(None, result)

    def test_getBlockTransactionCountByNumber(self):
        SessionStub.test_data = BlockFixtures.block_transaction_count_found()

        result = self.client.get_block_transaction_count_by_number(11608)

        self.assertEqual(
            "getBlockTransactionCountByNumber", SessionStub.latest_request_method
        )
        self.assertEqual(11608, SessionStub.latest_request_params[0])

        self.assertEqual(2, result)

    def test_getBlockTransactionCountByNumberWhenNotFound(self):
        SessionStub.test_data = BlockFixtures.block_transaction_count_not_found()

        result = self.client.get_block_transaction_count_by_number(11608)

        self.assertEqual(
            "getBlockTransactionCountByNumber", SessionStub.latest_request_method
        )
        self.assertEqual(11608, SessionStub.latest_request_params[0])

        self.assertEqual(None, result)

    def test_getBlockByHash(self):
        SessionStub.test_data = BlockFixtures.get_block_found()

        result = self.client.get_block_by_hash(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786"
        )

        self.assertEqual("getBlockByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual(1, len(SessionStub.latest_request_params))

        self.assertTrue(result is not None)
        self.assertEqual(11608, result.number)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.hash,
        )
        self.assertEqual(739224, result.confirmations)
        self.assertEqual(
            [
                "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
                "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
            ],
            result.transactions,
        )

    def test_getBlockByHashWithTransactions(self):
        SessionStub.test_data = BlockFixtures.get_block_with_transactions()

        result = self.client.get_block_by_hash(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786", True
        )

        self.assertEqual("getBlockByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual(True, SessionStub.latest_request_params[1])

        self.assertTrue(result is not None)
        self.assertEqual(11608, result.number)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.hash,
        )
        self.assertEqual(739501, result.confirmations)

        self.assertEqual(2, len(result.transactions))
        self.assertTrue(isinstance(result.transactions[0], Transaction))
        self.assertTrue(isinstance(result.transactions[1], Transaction))

    def test_getBlockByHashNotFound(self):
        SessionStub.test_data = BlockFixtures.get_block_not_found()

        result = self.client.get_block_by_hash(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786"
        )

        self.assertEqual("getBlockByHash", SessionStub.latest_request_method)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            SessionStub.latest_request_params[0],
        )
        self.assertEqual(1, len(SessionStub.latest_request_params))

        self.assertTrue(result is None)

    def test_getBlockByNumber(self):
        SessionStub.test_data = BlockFixtures.get_block_found()

        result = self.client.get_block_by_number(11608)

        self.assertEqual("getBlockByNumber", SessionStub.latest_request_method)
        self.assertEqual(11608, SessionStub.latest_request_params[0])
        self.assertEqual(1, len(SessionStub.latest_request_params))

        self.assertTrue(result is not None)
        self.assertEqual(11608, result.number)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.hash,
        )
        self.assertEqual(739224, result.confirmations)
        self.assertEqual(
            [
                "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
                "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
            ],
            result.transactions,
        )

    def test_getBlockByNumberWithTransactions(self):
        SessionStub.test_data = BlockFixtures.get_block_with_transactions()

        result = self.client.get_block_by_number(11608, True)

        self.assertEqual("getBlockByNumber", SessionStub.latest_request_method)
        self.assertEqual(11608, SessionStub.latest_request_params[0])
        self.assertEqual(True, SessionStub.latest_request_params[1])

        self.assertTrue(result is not None)
        self.assertEqual(11608, result.number)
        self.assertEqual(
            "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
            result.hash,
        )
        self.assertEqual(739501, result.confirmations)

        self.assertEqual(2, len(result.transactions))
        self.assertTrue(isinstance(result.transactions[0], Transaction))
        self.assertTrue(isinstance(result.transactions[1], Transaction))

    def test_getBlockByNumberNotFound(self):
        SessionStub.test_data = BlockFixtures.get_block_not_found()

        result = self.client.get_block_by_number(11608)

        self.assertEqual("getBlockByNumber", SessionStub.latest_request_method)
        self.assertEqual(11608, SessionStub.latest_request_params[0])
        self.assertEqual(1, len(SessionStub.latest_request_params))

        self.assertTrue(result is None)

    def test_constant(self):
        SessionStub.test_data = NodeFixtures.constant()

        result = self.client.constant("BaseConsensus.MAX_ATTEMPTS_TO_FETCH")

        self.assertEqual("constant", SessionStub.latest_request_method)
        self.assertEqual(
            "BaseConsensus.MAX_ATTEMPTS_TO_FETCH", SessionStub.latest_request_params[0]
        )

        self.assertEqual(5, result)

    def test_setConstant(self):
        SessionStub.test_data = NodeFixtures.constant()

        result = self.client.set_constant("BaseConsensus.MAX_ATTEMPTS_TO_FETCH", 10)

        self.assertEqual("constant", SessionStub.latest_request_method)
        self.assertEqual(
            "BaseConsensus.MAX_ATTEMPTS_TO_FETCH", SessionStub.latest_request_params[0]
        )
        self.assertEqual(10, SessionStub.latest_request_params[1])

        self.assertEqual(5, result)

    def test_resetConstant(self):
        SessionStub.test_data = NodeFixtures.constant()

        result = self.client.reset_constant("BaseConsensus.MAX_ATTEMPTS_TO_FETCH")

        self.assertEqual("constant", SessionStub.latest_request_method)
        self.assertEqual(
            "BaseConsensus.MAX_ATTEMPTS_TO_FETCH", SessionStub.latest_request_params[0]
        )
        self.assertEqual("reset", SessionStub.latest_request_params[1])

        self.assertEqual(5, result)

    def test_log(self):
        SessionStub.test_data = NodeFixtures.log()

        result = self.client.set_log("*", LogLevel.VERBOSE)

        self.assertEqual("log", SessionStub.latest_request_method)
        self.assertEqual("*", SessionStub.latest_request_params[0])
        self.assertEqual("verbose", SessionStub.latest_request_params[1])

        self.assertEqual(True, result)


if __name__ == "__main__":
    unittest.main()
