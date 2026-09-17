#
# Cache
#
# Handles the requirements of communicating with a Redis
# or Valkey server for caching.
#


class Caching:
	def __init__(self, redis):
		self.redis = redis

	# Get a generic key from a name
	def get_key(self, key_name):
		return self.redis.get(key_name)

	# Set a string value to a generic key name
	def create_key(self, key_name, key_value):
		return self.redis.set(key_name, key_value)

	# Get a dictionary of key/value pairs for a hash key.
	def get_hash_data(self, key_name):
		return self.redis.hgetall(key_name)

	# Get the value of a specific field in a hash key.
	def get_hash_field_val(self, key_name, field_name):
		return self.redis.hget(key_name, field_name)

	# Create a new key/value pair in a defined hash
	def create_field_in_hash(self, key_name, field_name, field_value):
		return self.redis.hset(key_name, field_name, field_value)

	# Create multiple key/value pairs in a defined hash
	def create_multiple_in_hash(self, key_name, mapping):
		if not isinstance(mapping, dict):
			raise RuntimeError("Could not insert data to Redis: the value of 'mapping' in method is not a dictionary.")
		return self.redis.hset(key_name, mapping=mapping)

	# Set an expiry time on a key.
	def key_expiry(self, key_name, expiry_time):
		return self.redis.expire(key_name, expiry_time)
