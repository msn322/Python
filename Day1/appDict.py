monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July"

}
# Default return value is None
print(monthConversion.get("Feb", "Not a valid key"))
print(monthConversion.values())
print(monthConversion.keys())
print(monthConversion.items())