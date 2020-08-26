class TransactionFixtures:
    @staticmethod
    def create_raw_transaction_basic():
        return {
            "jsonrpc": "2.0",
            "result": "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000186a00000000000000001000af84c01239b16cee089836c2af5c7b1dbb22cdc0b4864349f7f3805909aa8cf24e4c1ff0461832e86f3624778a867d5f2ba318f92918ada7ae28d70d40c4ef1d6413802",
            "id": 1,
        }

    @staticmethod
    def get_raw_transaction_info_basic():
        return {
            "jsonrpc": "2.0",
            "result": {
                "hash": "7784f2f6eaa076fa5cf0e4d06311ad204b2f485de622231785451181e8129091",
                "confirmations": 0,
                "from": "b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f5",
                "fromAddress": "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
                "to": "305dbaac7514a06dae935e40d599caf1bd8a243c",
                "toAddress": "NQ16 61ET MB3M 2JG6 TBLK BR0D B6EA X6XQ L91U",
                "value": 100000,
                "fee": 1,
                "data": None,
                "flags": 0,
                "valid": True,
                "inMempool": False,
            },
            "id": 1,
        }

    @staticmethod
    def get_transaction_contract_creation():
        return {
            "jsonrpc": "2.0",
            "result": {
                "hash": "539f6172b19f63be376ab7e962c368bb5f611deff6b159152c4cdf509f7daad2",
                "blockHash": "96fef80f517f0b2704476dee48da147049b591e8f034e5bf93f1f6935fd51b85",
                "blockNumber": 1102500,
                "timestamp": 1590148157,
                "confirmations": 7115,
                "from": "d62d519b3478c63bdd729cf2ccb863178060c64a",
                "fromAddress": "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA",
                "to": "a22eaf17848130c9b370e42ff7d345680df245e1",
                "toAddress": "NQ87 L8PA X5U4 G4QC KCTG UGPY FLS5 D06Y 4HF1",
                "value": 5000000000,
                "fee": 0,
                "data": "d62d519b3478c63bdd729cf2ccb863178060c64af5ad55071730d3b9f05989481eefbda7324a44f8030c63b9444960db429081543939166f05116cebc37bd6975ac9f9e3bb43a5ab0b010010d2de",
                "flags": 1,
            },
            "id": 1,
        }

    @staticmethod
    def get_transaction_full():
        return {
            "jsonrpc": "2.0",
            "result": {
                "hash": "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
                "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                "blockNumber": 11608,
                "timestamp": 1523412456,
                "confirmations": 715571,
                "transactionIndex": 0,
                "from": "355b4fe2304a9c818b9f0c3c1aaaf4ad4f6a0279",
                "fromAddress": "NQ16 6MDL YQHG 9AE8 32UY 1GX1 MAPL MM7N L0KR",
                "to": "4f61c06feeb7971af6997125fe40d629c01af92f",
                "toAddress": "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
                "value": 2636710000,
                "fee": 0,
                "data": None,
                "flags": 0,
            },
            "id": 1,
        }

    @staticmethod
    def get_transaction_not_found():
        return {"jsonrpc": "2.0", "result": None, "id": 1}

    @staticmethod
    def get_transaction_receipt_not_found():
        return {"jsonrpc": "2.0", "result": None, "id": 1}

    @staticmethod
    def get_transaction_receipt_found():
        return {
            "jsonrpc": "2.0",
            "result": {
                "transactionHash": "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
                "transactionIndex": -1,
                "blockNumber": 11608,
                "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                "confirmations": 718846,
                "timestamp": 1523412456,
            },
            "id": 1,
        }

    @staticmethod
    def get_transactions_not_found():
        return {"jsonrpc": "2.0", "result": [], "id": 1}

    @staticmethod
    def get_transactions_found():
        return {
            "jsonrpc": "2.0",
            "result": [
                {
                    "hash": "a514abb3ee4d3fbedf8a91156fb9ec4fdaf32f0d3d3da3c1dbc5fd1ee48db43e",
                    "blockHash": "c5c84b23dde619aff143c738884b2293aa1dd8bf6117a7375fa9ec824e410113",
                    "blockNumber": 14653,
                    "timestamp": 1523598270,
                    "confirmations": 716919,
                    "from": "0e229e99c9af35f040fc38aa5f722a78ce88c15b",
                    "fromAddress": "NQ13 1QH9 V6E9 MUSY 0G7U 72M5 XUHA F378 HGAT",
                    "to": "4f61c06feeb7971af6997125fe40d629c01af92f",
                    "toAddress": "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
                    "value": 1317394000,
                    "fee": 0,
                    "data": None,
                    "flags": 0,
                },
                {
                    "hash": "c8c0f586b11c7f39873c3de08610d63e8bec1ceaeba5e8a3bb13c709b2935f73",
                    "blockHash": "0de50c9c490b29cdaaf68a96dcf0a420a7bb441c63f87310485c5219b604a7d3",
                    "blockNumber": 13280,
                    "timestamp": 1523515965,
                    "confirmations": 718292,
                    "from": "0e229e99c9af35f040fc38aa5f722a78ce88c15b",
                    "fromAddress": "NQ13 1QH9 V6E9 MUSY 0G7U 72M5 XUHA F378 HGAT",
                    "to": "4f61c06feeb7971af6997125fe40d629c01af92f",
                    "toAddress": "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
                    "value": 2635766000,
                    "fee": 0,
                    "data": None,
                    "flags": 0,
                },
                {
                    "hash": "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
                    "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                    "blockNumber": 11608,
                    "timestamp": 1523412456,
                    "confirmations": 719964,
                    "from": "0e229e99c9af35f040fc38aa5f722a78ce88c15b",
                    "fromAddress": "NQ13 1QH9 V6E9 MUSY 0G7U 72M5 XUHA F378 HGAT",
                    "to": "4f61c06feeb7971af6997125fe40d629c01af92f",
                    "toAddress": "NQ05 9VGU 0TYE NXBH MVLR E4JY UG6N 5701 MX9F",
                    "value": 2860228000,
                    "fee": 0,
                    "data": None,
                    "flags": 0,
                },
            ],
            "id": 1,
        }

    @staticmethod
    def send_transaction():
        return {
            "jsonrpc": "2.0",
            "result": "81cf3f07b6b0646bb16833d57cda801ad5957e264b64705edeef6191fea0ad63",
            "id": 1,
        }
