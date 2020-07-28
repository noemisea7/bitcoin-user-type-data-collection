from blockstream import blockexplorer

# get transaction by id
tx_id = '56a5b477182cddb6edb460b39135a3dc785eaf7ea88a572052a761d6983e26a2'
tx = blockexplorer.get_transaction(tx_id)

print(tx)

print("V IN")
for info in tx.vin:
    print(info)
    print("\n")
print("\n")

print("V OUT")
for indo in tx.vout:
    print(indo)
    print("\n")
print("\n")

# within the transaction i can find where value was split between, but i cannot
# tell which addresses indicate sendback or "change," becuase i cannot determine
# the send address from the transaction id.
