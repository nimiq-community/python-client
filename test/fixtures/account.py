class AccountFixtures:
    @staticmethod
    def accounts():
        return {
            "jsonrpc": "2.0",
            "result": [
                {
                    "id": "f925107376081be421f52d64bec775cc1fc20829",
                    "address": "NQ33 Y4JH 0UTN 10DX 88FM 5MJB VHTM RGFU 4219",
                    "balance": 0,
                    "type": 0,
                },
                {
                    "id": "ebcbf0de7dae6a42d1c12967db9b2287bf2f7f0f",
                    "address": "NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF",
                    "balance": 52500000000000,
                    "type": 1,
                    "owner": "fd34ab7265a0e48c454ccbf4c9c61dfdf68f9a22",
                    "ownerAddress": "NQ62 YLSA NUK5 L3J8 QHAC RFSC KHGV YPT8 Y6H2",
                    "vestingStart": 1,
                    "vestingStepBlocks": 259200,
                    "vestingStepAmount": 2625000000000,
                    "vestingTotalAmount": 52500000000000,
                },
                {
                    "id": "4974636bd6d34d52b7d4a2ee4425dc2be72a2b4e",
                    "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                    "balance": 1000000000,
                    "type": 2,
                    "sender": "d62d519b3478c63bdd729cf2ccb863178060c64a",
                    "senderAddress": "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA",
                    "recipient": "f5ad55071730d3b9f05989481eefbda7324a44f8",
                    "recipientAddress": "NQ41 XNNM A1QP 639T KU2R H541 VTVV LUR4 LH7Q",
                    "hashRoot": "df331b3c8f8a889703092ea05503779058b7f44e71bc57176378adde424ce922",
                    "hashAlgorithm": 1,
                    "hashCount": 1,
                    "timeout": 1105605,
                    "totalAmount": 1000000000,
                },
            ],
            "id": 1,
        }

    @staticmethod
    def create_account():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "b6edcc7924af5a05af6087959c7233ec2cf1a5db",
                "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                "publicKey": "4f6d35cc47b77bf696b6cce72217e52edff972855bd17396b004a8453b020747",
            },
            "id": 1,
        }

    @staticmethod
    def get_account_basic():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "b6edcc7924af5a05af6087959c7233ec2cf1a5db",
                "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                "balance": 1200000,
                "type": 0,
            },
            "id": 1,
        }

    @staticmethod
    def get_account_vesting():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "ebcbf0de7dae6a42d1c12967db9b2287bf2f7f0f",
                "address": "NQ09 VF5Y 1PKV MRM4 5LE1 55KV P6R2 GXYJ XYQF",
                "balance": 52500000000000,
                "type": 1,
                "owner": "fd34ab7265a0e48c454ccbf4c9c61dfdf68f9a22",
                "ownerAddress": "NQ62 YLSA NUK5 L3J8 QHAC RFSC KHGV YPT8 Y6H2",
                "vestingStart": 1,
                "vestingStepBlocks": 259200,
                "vestingStepAmount": 2625000000000,
                "vestingTotalAmount": 52500000000000,
            },
            "id": 1,
        }

    @staticmethod
    def get_account_vesting_htlc():
        return {
            "jsonrpc": "2.0",
            "result": {
                "id": "4974636bd6d34d52b7d4a2ee4425dc2be72a2b4e",
                "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                "balance": 1000000000,
                "type": 2,
                "sender": "d62d519b3478c63bdd729cf2ccb863178060c64a",
                "senderAddress": "NQ53 SQNM 36RL F333 PPBJ KKRC RE33 2X06 1HJA",
                "recipient": "f5ad55071730d3b9f05989481eefbda7324a44f8",
                "recipientAddress": "NQ41 XNNM A1QP 639T KU2R H541 VTVV LUR4 LH7Q",
                "hashRoot": "df331b3c8f8a889703092ea05503779058b7f44e71bc57176378adde424ce922",
                "hashAlgorithm": 1,
                "hashCount": 1,
                "timeout": 1105605,
                "totalAmount": 1000000000,
            },
            "id": 1,
        }

    @staticmethod
    def get_balance():
        return {"id": 1, "jsonrpc": "2.0", "result": 1200000}
