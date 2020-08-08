class NodeFixtures():
    @staticmethod
    def consensusSyncing():
        return {
                "jsonrpc": "2.0",
                "result": "syncing",
                "id": 1
            }

    @staticmethod
    def constant():
        return {
                "jsonrpc": "2.0",
                "result": 5,
                "id": 1
            }

    @staticmethod
    def log():
        return {
                "jsonrpc": "2.0",
                "result": True,
                "id": 1
            }

    @staticmethod
    def minFeePerByte():
        return {
                "jsonrpc": "2.0",
                "result": 0,
                "id": 1
            }

    @staticmethod
    def syncingNotSyncing():
        return {
                "jsonrpc": "2.0",
                "result": False,
                "id": 1
            }

    @staticmethod
    def syncing():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "startingBlock": 578430,
                    "currentBlock": 586493,
                    "highestBlock": 586493
                },
                "id": 1
            }
