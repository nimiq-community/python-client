__all__ = ["MempoolInfo"]


class MempoolInfo:
    """
    Mempool information returned by the server.
    """

    def __init__(self, **kwargs):
        self.total = kwargs.pop("total")
        """Total number of pending transactions in mempool."""
        self.buckets = kwargs.pop("buckets")
        """List containing a subset of fee per byte buckets from [10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1, 0] that currently have more than one transaction."""
        transactionsPerBucket = {}
        for attr, value in kwargs.items():
            transactionsPerBucket[int(attr)] = value
        self.transactionsPerBucket = transactionsPerBucket
        """Number of transaction in the bucket. A transaction is assigned to the highest bucket of a value lower than its fee per byte value."""
