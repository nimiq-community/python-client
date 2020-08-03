Nimiq Python Client
===================

> Python implementation of the Nimiq RPC client specs.

## Usage

Send requests to a Nimiq node with `NimiqClient` object.

```python
import nimiqclient

client = NimiqClient(
	scheme = "http",
	user = "luna",
	password = "moon",
	host = "127.0.0.1",
	port = 8648
)
```

Once the client have been set up, we can call the methods with the appropiate arguments to make requests to the Nimiq node.

When no `config` object is passed in the initialization it will use the default values in the Nimiq node.

```python
client = NimiqClient()

# make rpc call to get the block number
blockNumber = client.blockNumber()

print(blockNumber) # displays the block number, for example 748883
```

## API

The complete [API documentation](docs) is available in the `/docs` folder.

Check out the [Nimiq RPC specs](https://github.com/nimiq/core-js/wiki/JSON-RPC-API) for behind the scene RPC calls.

## Installation

### From GitHub repository

Clone the repository then intall the package.

```sh
$ git clone https://github.com/nimiq-community/python-client
$ cd python-client
$ python setup.py install
```

### From Python Package Index (PyPI)

```sh
$pip install nimiqclient
```

## Contributions

This implementation was originally contributed by [rraallvv](https://github.com/rraallvv/).

Please send your contributions as pull requests.

Refer to the [issue tracker](https://github.com/nimiq-community/python-client/issues) for ideas.

### Develop

After cloning the repository intall the package.

```sh
$ git clone https://github.com/nimiq-community/python-client
$ cd python-client
$ python setup.py install
```

All done, happy coding!

### Testing

Tests are stored in the `/tests` folder and can be run from the command line like this:

```sh
$ python -m unittest discover -v
```

### Documentation

The documentation is generated automatically running [Doxygen](https://www.doxygen.nl/download.html#srcbin) from the repository root directory.

```sh
doxygen doxygenfile
```

## License

[Apache 2.0](LICENSE.md)
