'''
Instructions:

1. Instantiate an indexing object by using the Index() function from recordlinkage.
2. Block your pairing on cuisine_type by using indexer's' .block() method.
3. Generate pairs by indexing restaurants and restaurants_new in that order.

'''

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('cuisine_type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)
