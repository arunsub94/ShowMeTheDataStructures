# BLOCKCHAIN IMPLEMENTATION

import hashlib
from datetime import timezone
import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        if(self.data is not None):
            sha = hashlib.sha256()
            hash_str = self.data.encode('utf-8')
            sha.update(hash_str)
            return sha.hexdigest()
        else:
            return None

    def __repr__(self):
        return str(self.timestamp) + str(" | ") + str(self.data) + str(" | ") + str(self.previous_hash) + str(" | ") + str(self.hash)

class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, timestamp, data):
        if(self.head is None):
            new_block = Block(timestamp, data, None)
            self.head = new_block
            self.tail = self.head
        else:
            self.tail.next = Block(timestamp, data, self.tail.hash)
            self.tail = self.tail.next

    def tolist(self):
        BlockChain_List = []
        block_node = self.head
        while block_node:
            BlockChain_List.append(block_node)
            block_node = block_node.next
        return BlockChain_List

dt = datetime.datetime.now()
utc_time = dt.replace(tzinfo = timezone.utc)

# TEST CASE 1

BC1 = BlockChain()
BC1.append(utc_time.timestamp() , "This is encrypted code")
BC1.append(utc_time.timestamp() , None)
BC1.append(utc_time.timestamp() , "End of BlockChain!")
print(BC1.tolist())
print('----END------OF-------TEST-------CASE------')

# TEST CASE 2

BC2 = BlockChain()
BC2.append(utc_time.timestamp() , "Check this out!")
BC2.append(utc_time.timestamp() , "No, check this out!")
BC2.append(utc_time.timestamp() , "Shut up previous blocks! Block 3 rules!")
BC2.append(utc_time.timestamp() , "Block 4 begs to differ.")
print(BC2.tolist())
print('----END------OF-------TEST-------CASE------')

# TEST CASE 3

BC3 = BlockChain()
BC3.append(utc_time.timestamp() , " ")
print(BC3.tolist())
print('----END------OF-------TEST-------CASE------')
