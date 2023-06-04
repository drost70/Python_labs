class NegativeAttributeValue(ValueError):
    """
    Exception class for representing a negative attribute value.

    This exception is raised when an attribute value is expected to be non-negative,
    but a negative value is encountered.

    Attributes:
        attribute_name (str): The name of the attribute with the negative value.
    """

    def __init__(self, attribute_name):
        self.attribute_name = attribute_name

    def __str__(self):
        return f"Invalid value for attribute {self.attribute_name}: {self.attribute_name} cannot be negative."
