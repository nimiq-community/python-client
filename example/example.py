from nimiqclient import *

client = NimiqClient()

print(client.consensus())

for account in client.accounts():
	print(account.address)
