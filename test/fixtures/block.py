class BlockFixtures:
    @staticmethod
    def block_number():
        return {"jsonrpc": "2.0", "result": 748883, "id": 1}

    @staticmethod
    def block_transaction_count_found():
        return {"jsonrpc": "2.0", "result": 2, "id": 1}

    @staticmethod
    def block_transaction_count_not_found():
        return {"jsonrpc": "2.0", "result": None, "id": 1}

    @staticmethod
    def get_block_found():
        return {
            "jsonrpc": "2.0",
            "result": {
                "number": 11608,
                "hash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                "pow": "00000015f5b8c5315e001ad23b6d0aa5a1d201c21e523c19d3a4844705997ed2",
                "parentHash": "4772b0a8da82a15590f73886fd763164246f982652c16355da10d99fbcb844ac",
                "nonce": 1713217,
                "bodyHash": "703fb0545f0361407599134cc8277bab69d0caeccedfc54ee8559ec4b061be75",
                "accountsHash": "2d9395ed6877c85db1aa6a4868b9190a515c3f0c6e7a95e4621f93ac5d55b24b",
                "difficulty": "2953.5300598756",
                "timestamp": 1523412456,
                "confirmations": 739224,
                "miner": "638ea89b26961884ff3b1b4a5a65968c28be7599",
                "minerAddress": "NQ94 CE7A H6R6 JQC8 9YRT 3D55 LRCN HGLB UVCR",
                "extraData": "",
                "size": 643,
                "transactions": [
                    "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
                    "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
                ],
            },
            "id": 1,
        }

    @staticmethod
    def get_block_not_found():
        return {"jsonrpc": "2.0", "result": None, "id": 1}

    @staticmethod
    def get_block_with_transactions():
        return {
            "jsonrpc": "2.0",
            "result": {
                "number": 11608,
                "hash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                "pow": "00000015f5b8c5315e001ad23b6d0aa5a1d201c21e523c19d3a4844705997ed2",
                "parentHash": "4772b0a8da82a15590f73886fd763164246f982652c16355da10d99fbcb844ac",
                "nonce": 1713217,
                "bodyHash": "703fb0545f0361407599134cc8277bab69d0caeccedfc54ee8559ec4b061be75",
                "accountsHash": "2d9395ed6877c85db1aa6a4868b9190a515c3f0c6e7a95e4621f93ac5d55b24b",
                "difficulty": "2953.5300598756",
                "timestamp": 1523412456,
                "confirmations": 739501,
                "miner": "638ea89b26961884ff3b1b4a5a65968c28be7599",
                "minerAddress": "NQ94 CE7A H6R6 JQC8 9YRT 3D55 LRCN HGLB UVCR",
                "extraData": "",
                "size": 643,
                "transactions": [
                    {
                        "hash": "78957b87ab5546e11e9540ce5a37ebbf93a0ebd73c0ce05f137288f30ee9f430",
                        "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                        "blockNumber": 11608,
                        "timestamp": 1523412456,
                        "confirmations": 739502,
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
                    {
                        "hash": "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
                        "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                        "blockNumber": 11608,
                        "timestamp": 1523412456,
                        "confirmations": 739502,
                        "transactionIndex": 1,
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
            },
            "id": 1,
        }

    @staticmethod
    def submit_block():
        return {"jsonrpc": "2.0", "id": 1}
