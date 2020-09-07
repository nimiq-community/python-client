class MinerFixtures:
    @staticmethod
    def miner_address():
        return {
            "jsonrpc": "2.0",
            "result": "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
            "id": 1,
        }

    @staticmethod
    def miner_threads():
        return {"jsonrpc": "2.0", "result": 2, "id": 1}

    @staticmethod
    def mining_state():
        return {"jsonrpc": "2.0", "result": False, "id": 1}

    @staticmethod
    def hashrate():
        return {"jsonrpc": "2.0", "result": 52982.2731, "id": 1}

    @staticmethod
    def pool_confirmed_balance():
        return {"jsonrpc": "2.0", "result": 12000, "id": 1}

    @staticmethod
    def pool_connection_state():
        return {"jsonrpc": "2.0", "result": 2, "id": 1}

    @staticmethod
    def pool_no_pool():
        return {"jsonrpc": "2.0", "result": None, "id": 1}

    @staticmethod
    def pool_sushipool():
        return {"jsonrpc": "2.0", "result": "us.sushipool.com:443", "id": 1}

    @staticmethod
    def get_work_block_template():
        return {
            "jsonrpc": "2.0",
            "result": {
                "header": {
                    "version": 1,
                    "prevHash": "b6d0644d171957dfc5e85ec36fcb4772a7783c6c47da23d0b7fe9ceb1a6b85f1",
                    "interlinkHash": "960b72c50828837782b92698555e23492e4f75018a2ba5dffea0b89df436e3b0",
                    "accountsHash": "78f442b1962bf9dd07e1b25bf4c42c59e3e40eec7fedf6853c579b6cc56330c1",
                    "nBits": 503371226,
                    "height": 901883,
                },
                "interlink": "11ead9805a7d47ddf5152a7d06a14ea291831c3fc7af20b88240c5ae839683021bcee3e26b8b4167517c162fa113c09606b44d24f8020804a0f756db085546ff585adfdedad9085d36527a8485b497728446c35b9b6c3db263c07dd0a1f487b1639aa37ff60ba3cf6ed8ab5146fee50a23ebd84ea37dca8c49b31e57d05c9e6c57f09a3b282b71ec2be66c1bc8268b5326bb222b11a0d0a4acd2a93c9e8a8713fe4383e9d5df3b1bf008c535281086b2bcc20e494393aea1475a5c3f13673de2cf7314d2",
                "target": 503371226,
                "body": {
                    "hash": "17e250f1977ae85bdbe09468efef83587885419ee1074ddae54d3fb5a96e1f54",
                    "minerAddr": "b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f5",
                    "extraData": "",
                    "transactions": [
                        "009207144f80a4a479b6954c342ef61747c018d368b4bb86dcb70bfc19381e0c9323c5b9092959ee29b05394e184685e3ff7d3c2a60000000029f007a6000000000000008a000dc2fa0144eccc3af5be34553193aacd543b39b21a79d32c975a9e3f958a9516ff92f134f15ae5a70cadcfcf89d3ced84dd9569d04e40d6d138e9e504ed8e70f31a3d407"
                    ],
                    "merkleHashes": [
                        "6039a78b6be96bd0b539c6b2bf52fe6e5970571e0ee3afba798f701eee561ea2"
                    ],
                    "prunedAccounts": [],
                },
            },
            "id": 1,
        }

    @staticmethod
    def get_work():
        return {
            "jsonrpc": "2.0",
            "result": {
                "data": "00015a7d47ddf5152a7d06a14ea291831c3fc7af20b88240c5ae839683021bcee3e279877b3de0da8ce8878bf225f6782a2663eff9a03478c15ba839fde9f1dc3dd9e5f0cd4dbc96a30130de130eb52d8160e9197e2ccf435d8d24a09b518a5e05da87a8658ed8c02531f66a7d31757b08c88d283654ed477e5e2fec21a7ca8449241e00d620000dc2fa5e763bda00000000",
                "suffix": "11fad9806b8b4167517c162fa113c09606b44d24f8020804a0f756db085546ff585adfdedad9085d36527a8485b497728446c35b9b6c3db263c07dd0a1f487b1639aa37ff60ba3cf6ed8ab5146fee50a23ebd84ea37dca8c49b31e57d05c9e6c57f09a3b282b71ec2be66c1bc8268b5326bb222b11a0d0a4acd2a93c9e8a8713fe4383e9d5df3b1bf008c535281086b2bcc20e494393aea1475a5c3f13673de2cf7314d201b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f50000000000",
                "target": 503371296,
                "algorithm": "nimiq-argon2",
            },
            "id": 1,
        }
