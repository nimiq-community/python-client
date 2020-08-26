class MemPoolFixtures:
    @staticmethod
    def mempool_empty():
        return {"jsonrpc": "2.0", "result": {"buckets": [], "total": 0}, "id": 1}

    @staticmethod
    def mempool():
        return {
            "jsonrpc": "2.0",
            "result": {"1": 3, "buckets": [1], "total": 3},
            "id": 1,
        }

    @staticmethod
    def mempool_content_full_transactions():
        return {
            "jsonrpc": "2.0",
            "result": [
                {
                    "hash": "5bb722c2afe25c18ba33d453b3ac2c90ac278c595cc92f6188c8b699e8fb006a",
                    "from": "f3a2a520967fb046deee40af0c68c3dc43ef3238",
                    "fromAddress": "NQ04 XEHA A84N FXQ4 DPPE 82PG QS63 TH1X XCHQ",
                    "to": "ca9e687c4e760e5d6dd4a789c577cefe1338ad2c",
                    "toAddress": "NQ77 RAF6 GY2E EQ75 STEL LX4U AVXE YQ9K HB9C",
                    "value": 9286543536,
                    "fee": 1380,
                    "data": None,
                    "flags": 0,
                },
                {
                    "hash": "f59a30e0a7e3348ef569225db1f4c29026aeac4350f8c6e751f669eddce0c718",
                    "from": "f3a2a520967fb046deee40af0c68c3dc43ef3238",
                    "fromAddress": "NQ04 XEHA A84N FXQ4 DPPE 82PG QS63 TH1X XCHQ",
                    "to": "1a5ac816ace8ee339f7ec80f580ef9ea17b8b32b",
                    "toAddress": "NQ85 39DC G5MC V3P3 77TX R07M G3PR V8BT HCRB",
                    "value": 5314650699,
                    "fee": 1380,
                    "data": None,
                    "flags": 0,
                },
                {
                    "hash": "9cd9c1d0ffcaebfcfe86bc2ae73b4e82a488de99c8e3faef92b05432bb94519c",
                    "from": "f3a2a520967fb046deee40af0c68c3dc43ef3238",
                    "fromAddress": "NQ04 XEHA A84N FXQ4 DPPE 82PG QS63 TH1X XCHQ",
                    "to": "d497b15fe0857394f3e485c87e00fa44270fcd4d",
                    "toAddress": "NQ60 SJBT 2PY0 GMRR 9UY4 GP47 U07S 8GKG YKAD",
                    "value": 1038143325,
                    "fee": 1380,
                    "data": None,
                    "flags": 0,
                },
            ],
            "id": 1,
        }

    @staticmethod
    def mempool_content_hashes_only():
        return {
            "jsonrpc": "2.0",
            "result": [
                "5bb722c2afe25c18ba33d453b3ac2c90ac278c595cc92f6188c8b699e8fb006a",
                "f59a30e0a7e3348ef569225db1f4c29026aeac4350f8c6e751f669eddce0c718",
                "9cd9c1d0ffcaebfcfe86bc2ae73b4e82a488de99c8e3faef92b05432bb94519c",
            ],
            "id": 1,
        }
