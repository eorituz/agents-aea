<a name="aea.crypto.base"></a>
# aea.crypto.base

Abstract module wrapping the public and private key cryptography and ledger api.

<a name="aea.crypto.base.Crypto"></a>
## Crypto Objects

```python
class Crypto(Generic[EntityClass],  ABC)
```

Base class for a crypto object.

<a name="aea.crypto.base.Crypto.__init__"></a>
#### `__`init`__`

```python
 | __init__(private_key_path: Optional[str] = None, **kwargs: Any) -> None
```

Initialize the crypto object.

The actual behaivour of this constructor is determined by the abstract
methods 'generate_private_key()' and 'load_private_key_from_path().
Either way, the entity object will be accessible as a property.

**Arguments**:

- `private_key_path`: the path to the private key.
If None, the key will be generated by 'generate_private_key()'.
If not None, the path will be processed by 'load_private_key_from_path()'.
- `kwargs`: keyword arguments.

<a name="aea.crypto.base.Crypto.generate_private_key"></a>
#### generate`_`private`_`key

```python
 | @classmethod
 | @abstractmethod
 | generate_private_key(cls) -> EntityClass
```

Generate a private key.

**Returns**:

the entity object. Implementation dependent.

<a name="aea.crypto.base.Crypto.load_private_key_from_path"></a>
#### load`_`private`_`key`_`from`_`path

```python
 | @classmethod
 | @abstractmethod
 | load_private_key_from_path(cls, file_name: str) -> EntityClass
```

Load a private key in hex format from a file.

**Arguments**:

- `file_name`: the path to the hex file.

**Returns**:

the entity object.

<a name="aea.crypto.base.Crypto.entity"></a>
#### entity

```python
 | @property
 | entity() -> EntityClass
```

Return an entity object.

**Returns**:

an entity object

<a name="aea.crypto.base.Crypto.private_key"></a>
#### private`_`key

```python
 | @property
 | @abstractmethod
 | private_key() -> str
```

Return a private key.

**Returns**:

a private key string

<a name="aea.crypto.base.Crypto.public_key"></a>
#### public`_`key

```python
 | @property
 | @abstractmethod
 | public_key() -> str
```

Return a public key.

**Returns**:

a public key string

<a name="aea.crypto.base.Crypto.address"></a>
#### address

```python
 | @property
 | @abstractmethod
 | address() -> str
```

Return the address.

**Returns**:

an address string

<a name="aea.crypto.base.Crypto.sign_message"></a>
#### sign`_`message

```python
 | @abstractmethod
 | sign_message(message: bytes, is_deprecated_mode: bool = False) -> str
```

Sign a message in bytes string form.

**Arguments**:

- `message`: the message to be signed
- `is_deprecated_mode`: if the deprecated signing is used

**Returns**:

signature of the message in string form

<a name="aea.crypto.base.Crypto.sign_transaction"></a>
#### sign`_`transaction

```python
 | @abstractmethod
 | sign_transaction(transaction: JSONLike) -> JSONLike
```

Sign a transaction in dict form.

**Arguments**:

- `transaction`: the transaction to be signed

**Returns**:

signed transaction

<a name="aea.crypto.base.Crypto.dump"></a>
#### dump

```python
 | @abstractmethod
 | dump(fp: BinaryIO) -> None
```

Serialize crypto object as binary stream to `fp` (a `.write()`-supporting file-like object).

**Arguments**:

- `fp`: the output file pointer. Must be set in binary mode (mode='wb')

**Returns**:

None

<a name="aea.crypto.base.Helper"></a>
## Helper Objects

```python
class Helper(ABC)
```

Interface for helper class usable as Mixin for LedgerApi or as standalone class.

<a name="aea.crypto.base.Helper.is_transaction_settled"></a>
#### is`_`transaction`_`settled

```python
 | @staticmethod
 | @abstractmethod
 | is_transaction_settled(tx_receipt: JSONLike) -> bool
```

Check whether a transaction is settled or not.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.

**Returns**:

True if the transaction has been settled, False o/w.

<a name="aea.crypto.base.Helper.is_transaction_valid"></a>
#### is`_`transaction`_`valid

```python
 | @staticmethod
 | @abstractmethod
 | is_transaction_valid(tx: JSONLike, seller: Address, client: Address, tx_nonce: str, amount: int) -> bool
```

Check whether a transaction is valid or not.

**Arguments**:

- `tx`: the transaction.
- `seller`: the address of the seller.
- `client`: the address of the client.
- `tx_nonce`: the transaction nonce.
- `amount`: the amount we expect to get from the transaction.

**Returns**:

True if the random_message is equals to tx['input']

<a name="aea.crypto.base.Helper.generate_tx_nonce"></a>
#### generate`_`tx`_`nonce

```python
 | @staticmethod
 | @abstractmethod
 | generate_tx_nonce(seller: Address, client: Address) -> str
```

Generate a unique hash to distinguish txs with the same terms.

**Arguments**:

- `seller`: the address of the seller.
- `client`: the address of the client.

**Returns**:

return the hash in hex.

<a name="aea.crypto.base.Helper.get_address_from_public_key"></a>
#### get`_`address`_`from`_`public`_`key

```python
 | @classmethod
 | @abstractmethod
 | get_address_from_public_key(cls, public_key: str) -> str
```

Get the address from the public key.

**Arguments**:

- `public_key`: the public key

**Returns**:

str

<a name="aea.crypto.base.Helper.recover_message"></a>
#### recover`_`message

```python
 | @classmethod
 | @abstractmethod
 | recover_message(cls, message: bytes, signature: str, is_deprecated_mode: bool = False) -> Tuple[Address, ...]
```

Recover the addresses from the hash.

**Arguments**:

- `message`: the message we expect
- `signature`: the transaction signature
- `is_deprecated_mode`: if the deprecated signing was used

**Returns**:

the recovered addresses

<a name="aea.crypto.base.Helper.recover_public_keys_from_message"></a>
#### recover`_`public`_`keys`_`from`_`message

```python
 | @classmethod
 | @abstractmethod
 | recover_public_keys_from_message(cls, message: bytes, signature: str, is_deprecated_mode: bool = False) -> Tuple[str, ...]
```

Get the public key used to produce the `signature` of the `message`

**Arguments**:

- `message`: raw bytes used to produce signature
- `signature`: signature of the message
- `is_deprecated_mode`: if the deprecated signing was used

**Returns**:

the recovered public keys

<a name="aea.crypto.base.Helper.get_hash"></a>
#### get`_`hash

```python
 | @staticmethod
 | @abstractmethod
 | get_hash(message: bytes) -> str
```

Get the hash of a message.

**Arguments**:

- `message`: the message to be hashed.

**Returns**:

the hash of the message.

<a name="aea.crypto.base.Helper.is_valid_address"></a>
#### is`_`valid`_`address

```python
 | @classmethod
 | @abstractmethod
 | is_valid_address(cls, address: Address) -> bool
```

Check if the address is valid.

**Arguments**:

- `address`: the address to validate

<a name="aea.crypto.base.Helper.load_contract_interface"></a>
#### load`_`contract`_`interface

```python
 | @classmethod
 | @abstractmethod
 | load_contract_interface(cls, file_path: Path) -> Dict[str, str]
```

Load contract interface.

**Arguments**:

- `file_path`: the file path to the interface

**Returns**:

the interface

<a name="aea.crypto.base.LedgerApi"></a>
## LedgerApi Objects

```python
class LedgerApi(Helper,  ABC)
```

Interface for ledger APIs.

<a name="aea.crypto.base.LedgerApi.api"></a>
#### api

```python
 | @property
 | @abstractmethod
 | api() -> Any
```

Get the underlying API object.

This can be used for low-level operations with the concrete ledger APIs.
If there is no such object, return None.

<a name="aea.crypto.base.LedgerApi.get_balance"></a>
#### get`_`balance

```python
 | @abstractmethod
 | get_balance(address: Address) -> Optional[int]
```

Get the balance of a given account.

This usually takes the form of a web request to be waited synchronously.

**Arguments**:

- `address`: the address.

**Returns**:

the balance.

<a name="aea.crypto.base.LedgerApi.get_state"></a>
#### get`_`state

```python
 | @abstractmethod
 | get_state(callable_name: str, *args: Any, **kwargs: Any) -> Optional[JSONLike]
```

Call a specified function on the underlying ledger API.

This usually takes the form of a web request to be waited synchronously.

**Arguments**:

- `callable_name`: the name of the API function to be called.
- `args`: the positional arguments for the API function.
- `kwargs`: the keyword arguments for the API function.

**Returns**:

the ledger API response.

<a name="aea.crypto.base.LedgerApi.get_transfer_transaction"></a>
#### get`_`transfer`_`transaction

```python
 | @abstractmethod
 | get_transfer_transaction(sender_address: Address, destination_address: Address, amount: int, tx_fee: int, tx_nonce: str, **kwargs: Any, ,) -> Optional[JSONLike]
```

Submit a transfer transaction to the ledger.

**Arguments**:

- `sender_address`: the sender address of the payer.
- `destination_address`: the destination address of the payee.
- `amount`: the amount of wealth to be transferred.
- `tx_fee`: the transaction fee.
- `tx_nonce`: verifies the authenticity of the tx

**Returns**:

the transfer transaction

<a name="aea.crypto.base.LedgerApi.send_signed_transaction"></a>
#### send`_`signed`_`transaction

```python
 | @abstractmethod
 | send_signed_transaction(tx_signed: JSONLike) -> Optional[str]
```

Send a signed transaction and wait for confirmation.

Use keyword arguments for the specifying the signed transaction payload.

**Arguments**:

- `tx_signed`: the signed transaction

<a name="aea.crypto.base.LedgerApi.get_transaction_receipt"></a>
#### get`_`transaction`_`receipt

```python
 | @abstractmethod
 | get_transaction_receipt(tx_digest: str) -> Optional[JSONLike]
```

Get the transaction receipt for a transaction digest.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.

**Returns**:

the tx receipt, if present

<a name="aea.crypto.base.LedgerApi.get_transaction"></a>
#### get`_`transaction

```python
 | @abstractmethod
 | get_transaction(tx_digest: str) -> Optional[JSONLike]
```

Get the transaction for a transaction digest.

**Arguments**:

- `tx_digest`: the digest associated to the transaction.

**Returns**:

the tx, if present

<a name="aea.crypto.base.LedgerApi.get_contract_instance"></a>
#### get`_`contract`_`instance

```python
 | @abstractmethod
 | get_contract_instance(contract_interface: Dict[str, str], contract_address: Optional[str] = None) -> Any
```

Get the instance of a contract.

**Arguments**:

- `contract_interface`: the contract interface.
- `contract_address`: the contract address.

**Returns**:

the contract instance

<a name="aea.crypto.base.LedgerApi.get_deploy_transaction"></a>
#### get`_`deploy`_`transaction

```python
 | @abstractmethod
 | get_deploy_transaction(contract_interface: Dict[str, str], deployer_address: Address, **kwargs: Any, ,) -> Optional[JSONLike]
```

Get the transaction to deploy the smart contract.

**Arguments**:

- `contract_interface`: the contract interface.
- `deployer_address`: The address that will deploy the contract.
:returns tx: the transaction dictionary.

<a name="aea.crypto.base.LedgerApi.update_with_gas_estimate"></a>
#### update`_`with`_`gas`_`estimate

```python
 | @abstractmethod
 | update_with_gas_estimate(transaction: JSONLike) -> JSONLike
```

Attempts to update the transaction with a gas estimate

**Arguments**:

- `transaction`: the transaction

**Returns**:

the updated transaction

<a name="aea.crypto.base.FaucetApi"></a>
## FaucetApi Objects

```python
class FaucetApi(ABC)
```

Interface for testnet faucet APIs.

<a name="aea.crypto.base.FaucetApi.get_wealth"></a>
#### get`_`wealth

```python
 | @abstractmethod
 | get_wealth(address: Address, url: Optional[str] = None) -> None
```

Get wealth from the faucet for the provided address.

**Arguments**:

- `address`: the address.
- `url`: the url

**Returns**:

None

