class Fixtures():
    @staticmethod
    def accounts():
        return {
                "jsonrpc": "2.0",
                "result": [
                    {
                        "id": "f925107376081be421f52d64bec775cc1fc20829",
                        "address": "NQ33 Y4JH 0UTN 10DX 88FM 5MJB VHTM RGFU 4219",
                        "balance": 0,
                        "type": 0
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
                        "vestingTotalAmount": 52500000000000
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
                        "totalAmount": 1000000000
                    }
                ],
                "id": 1
            }

    @staticmethod
    def blockNumber():
        return {
                "jsonrpc": "2.0",
                "result": 748883,
                "id": 1
            }

    @staticmethod
    def blockTransactionCountFound():
        return {
                "jsonrpc": "2.0",
                "result": 2,
                "id": 1
            }

    @staticmethod
    def blockTransactionCountNotFound():
        return {
                "jsonrpc": "2.0",
                "result": None,
                "id": 1
            }

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
    def createAccount():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "id": "b6edcc7924af5a05af6087959c7233ec2cf1a5db",
                    "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                    "publicKey": "4f6d35cc47b77bf696b6cce72217e52edff972855bd17396b004a8453b020747"
                },
                "id": 1
            }

    @staticmethod
    def createRawTransactionBasic():
        return {
                "jsonrpc": "2.0",
                "result": "00c3c0d1af80b84c3b3de4e3d79d5c8cc950e044098c969953d68bf9cee68d7b53305dbaac7514a06dae935e40d599caf1bd8a243c00000000000186a00000000000000001000af84c01239b16cee089836c2af5c7b1dbb22cdc0b4864349f7f3805909aa8cf24e4c1ff0461832e86f3624778a867d5f2ba318f92918ada7ae28d70d40c4ef1d6413802",
                "id": 1
            }

    @staticmethod
    def getAccountBasic():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "id": "b6edcc7924af5a05af6087959c7233ec2cf1a5db",
                    "address": "NQ46 NTNU QX94 MVD0 BBT0 GXAR QUHK VGNF 39ET",
                    "balance": 1200000,
                    "type": 0
                },
                "id": 1
            }

    @staticmethod
    def getAccountVesting():
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
                    "vestingTotalAmount": 52500000000000
                },
                "id": 1
            }

    @staticmethod
    def getAccountVestingHtlc():
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
                    "totalAmount": 1000000000
                },
                "id": 1
            }

    @staticmethod
    def getBalance():
        return {
                "id": 1,
                "jsonrpc": "2.0",
                "result": 1200000
            }

    @staticmethod
    def getBlockFound():
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
                        "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e"
                    ]
                },
                "id": 1
            }

    @staticmethod
    def getBlockNotFound():
        return {
                "jsonrpc": "2.0",
                "result": None,
                "id": 1
            }

    @staticmethod
    def getBlockWithTransactions():
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
                            "flags": 0
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
                            "flags": 0
                        }
                    ]
                },
                "id": 1
            }

    @staticmethod
    def getRawTransactionInfoBasic():
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
                    "inMempool": False
                },
                "id": 1
            }

    @staticmethod
    def getTransactionContractCreation():
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
                    "flags": 1
                },
                "id": 1
            }

    @staticmethod
    def getTransactionFull():
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
                    "flags": 0
                },
                "id": 1
            }

    @staticmethod
    def getTransactionNotFound():
        return {
                "jsonrpc": "2.0",
                "result": None,
                "id": 1
            }

    @staticmethod
    def getTransactionReceiptNotFound():
        return {
                "jsonrpc": "2.0",
                "result": None,
                "id": 1
            }

    @staticmethod
    def getTransactionReceiptFound():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "transactionHash": "fd8e46ae55c5b8cd7cb086cf8d6c81f941a516d6148021d55f912fb2ca75cc8e",
                    "transactionIndex": -1,
                    "blockNumber": 11608,
                    "blockHash": "bc3945d22c9f6441409a6e539728534a4fc97859bda87333071fad9dad942786",
                    "confirmations": 718846,
                    "timestamp": 1523412456
                },
                "id": 1
            }

    @staticmethod
    def getTransactionsNotFound():
        return {
                "jsonrpc": "2.0",
                "result": [],
                "id": 1
            }

    @staticmethod
    def getTransactionsFound():
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
                        "flags": 0
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
                        "flags": 0
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
                        "flags": 0
                    }
                ],
                "id": 1
            }

    @staticmethod
    def getWorkBlockTemplate():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "header": {
                        "version": 1,
                        "prevHash": "b6d0644d171957dfc5e85ec36fcb4772a7783c6c47da23d0b7fe9ceb1a6b85f1",
                        "interlinkHash": "960b72c50828837782b92698555e23492e4f75018a2ba5dffea0b89df436e3b0",
                        "accountsHash": "78f442b1962bf9dd07e1b25bf4c42c59e3e40eec7fedf6853c579b6cc56330c1",
                        "nBits": 503371226,
                        "height": 901883
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
                        "prunedAccounts": []
                    }
                },
                "id": 1
            }

    @staticmethod
    def getWork():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "data": "00015a7d47ddf5152a7d06a14ea291831c3fc7af20b88240c5ae839683021bcee3e279877b3de0da8ce8878bf225f6782a2663eff9a03478c15ba839fde9f1dc3dd9e5f0cd4dbc96a30130de130eb52d8160e9197e2ccf435d8d24a09b518a5e05da87a8658ed8c02531f66a7d31757b08c88d283654ed477e5e2fec21a7ca8449241e00d620000dc2fa5e763bda00000000",
                    "suffix": "11fad9806b8b4167517c162fa113c09606b44d24f8020804a0f756db085546ff585adfdedad9085d36527a8485b497728446c35b9b6c3db263c07dd0a1f487b1639aa37ff60ba3cf6ed8ab5146fee50a23ebd84ea37dca8c49b31e57d05c9e6c57f09a3b282b71ec2be66c1bc8268b5326bb222b11a0d0a4acd2a93c9e8a8713fe4383e9d5df3b1bf008c535281086b2bcc20e494393aea1475a5c3f13673de2cf7314d201b7cc7f01e0e6f0e07dd9249dc598f4e5ee8801f50000000000",
                    "target": 503371296,
                    "algorithm": "nimiq-argon2"
                },
                "id": 1
            }

    @staticmethod
    def hashrate():
        return {
                "jsonrpc": "2.0",
                "result": 52982.2731,
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
    def mempoolEmpty():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "buckets": [],
                    "total": 0
                },
                "id": 1
            }

    @staticmethod
    def mempool():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "1": 3,
                    "buckets": [1],
                    "total": 3
                },
                "id": 1
            }

    @staticmethod
    def mempoolContentFullTransactions():
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
                        "flags": 0
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
                        "flags": 0
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
                        "flags": 0
                    }
                ],
                "id": 1
            }

    @staticmethod
    def mempoolContentHashesOnly():
        return {
                "jsonrpc": "2.0",
                "result": [
                    "5bb722c2afe25c18ba33d453b3ac2c90ac278c595cc92f6188c8b699e8fb006a",
                    "f59a30e0a7e3348ef569225db1f4c29026aeac4350f8c6e751f669eddce0c718",
                    "9cd9c1d0ffcaebfcfe86bc2ae73b4e82a488de99c8e3faef92b05432bb94519c"
                ],
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
    def minerAddress():
        return {
                "jsonrpc": "2.0",
                "result": "NQ39 NY67 X0F0 UTQE 0YER 4JEU B67L UPP8 G0FM",
                "id": 1
            }

    @staticmethod
    def minerThreads():
        return {
                "jsonrpc": "2.0",
                "result": 2,
                "id": 1
            }

    @staticmethod
    def miningState():
        return {
                "jsonrpc": "2.0",
                "result": False,
                "id": 1
            }

    @staticmethod
    def peerCount():
        return {
                "jsonrpc": "2.0",
                "result": 6,
                "id": 1
            }

    @staticmethod
    def peerListEmpty():
        return {
                "jsonrpc": "2.0",
                "result": [],
                "id": 1
            }

    @staticmethod
    def peerList():
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
                        "tx": 1265
                    },
                    {
                        "id": "e37dca72802c972d45b37735e9595cf0",
                        "address": "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
                        "addressState": 4
                    }
                ],
                "id": 1
            }

    @staticmethod
    def peerStateError():
        return {
                "jsonrpc": "2.0",
                "error": {
                    "code": 1,
                    "message": "Invalid or unknown peer address"
                },
                "id": 1
            }

    @staticmethod
    def peerStateFailed():
        return {
                "jsonrpc": "2.0",
                "result": {
                    "id": "e37dca72802c972d45b37735e9595cf0",
                    "address": "wss://seed4.nimiq-testnet.com:8080/e37dca72802c972d45b37735e9595cf0",
                    "addressState": 4
                },
                "id": 1
            }

    @staticmethod
    def peerStateNormal():
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
                    "tx": 2696
                },
                "id": 1
            }

    @staticmethod
    def poolConfirmedBalance():
        return {
                "jsonrpc": "2.0",
                "result": 12000,
                "id": 1
            }

    @staticmethod
    def poolConnectionState():
        return {
                "jsonrpc": "2.0",
                "result": 2,
                "id": 1
            }

    @staticmethod
    def poolNoPool():
        return {
                "jsonrpc": "2.0",
                "result": None,
                "id": 1
            }

    @staticmethod
    def poolSushipool():
        return {
                "jsonrpc": "2.0",
                "result": "us.sushipool.com:443",
                "id": 1
            }

    @staticmethod
    def sendTransaction():
        return {
                "jsonrpc": "2.0",
                "result": "81cf3f07b6b0646bb16833d57cda801ad5957e264b64705edeef6191fea0ad63",
                "id": 1
            }

    @staticmethod
    def submitBlock():
        return {
                "jsonrpc": "2.0",
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
