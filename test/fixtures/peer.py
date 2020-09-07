class PeerFixtures:
    @staticmethod
    def peer_count():
        return {"jsonrpc": "2.0", "result": 6, "id": 1}

    @staticmethod
    def peer_list_empty():
        return {"jsonrpc": "2.0", "result": [], "id": 1}

    @staticmethod
    def peer_list():
        return {
            "jsonrpc": "2.0",
            "result": [
                {
                    "id": "b99034c552e9c0fd34eb95c1cdf17f5e",
                    "address": "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
                    "addressState": 2,
                    "connectionState": 5,
                    "version": 2,
                    "timeOffset": -188,
                    "headHash": "59da8ba57c1f0ffd444201ca2d9f48cef7e661262781be7937bb6ef0bdbe0e4d",
                    "latency": 532,
                    "rx": 2122,
                    "tx": 1265,
                },
                {
                    "id": "e37dca72802c972d45b37735e9595cf0",
                    "address": "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
                    "addressState": 4,
                },
            ],
            "id": 1,
        }

    @staticmethod
    def peer_state_error():
        return {
            "jsonrpc": "2.0",
            "error": {"code": 1, "message": "Invalid or unknown peer address"},
            "id": 1,
        }

    @staticmethod
    def peer_state_failed():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "e37dca72802c972d45b37735e9595cf0",
                "address": "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
                "addressState": 4,
            },
            "id": 1,
        }

    @staticmethod
    def peer_state_normal():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "b99034c552e9c0fd34eb95c1cdf17f5e",
                "address": "wss://seed1.nimiq-testnet.com:8080/b99034c552e9c0fd34eb95c1cdf17f5e",
                "addressState": 2,
                "connectionState": 5,
                "version": 2,
                "timeOffset": 186,
                "headHash": "910a78e761034e0655bf01b13336793c809f598194a1b841269600ef8b84fe18",
                "latency": 550,
                "rx": 3440,
                "tx": 2696,
            },
            "id": 1,
        }
