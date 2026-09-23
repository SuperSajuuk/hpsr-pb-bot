#
# Exceptions
#
# This file contains a custom Exceptions class for
# raising errors in the code. This makes it far simpler
# for identifying the source of an error, rather than
# raising ValueError generically.
#
# Make sure to raise errors in the sub-exceptions and not
# UserInputException itself. Only raise on UserInputException
# if there is no defined sub-exception.
#
class UserInputException(Exception):
	pass


class InvalidGame(UserInputException):
	pass


class InvalidCategory(UserInputException):
	pass


class InvalidPlatform(UserInputException):
	pass


class UnsupportedGame(UserInputException):
	pass


class MissingInternalData(Exception):
	pass
