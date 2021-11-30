class Transaction:
    def __init__(self, name: str, transaction: str, alphabet: set[str]):
        """
        :param name: transaction name
        :param transaction: String repr of transaction i.e. "x = x+y",
                            "=" is required, only letters are preserved
                            all symbols are length = 1 only
        :param alphabet: Alphabet :D
        """
        self.name = name
        self.left = transaction[:transaction.index("=")].strip()
        self.right = [char for char in transaction[transaction.index("=") + 1:] if char in alphabet]

    def __repr__(self):
        return self.name
