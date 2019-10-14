# Dictionaries
# dict

my_dictionary = {
    "key": "value",
    "key2": 78
}

product = {
    "id"            : 865446665,
    "description"   : "A yellow submarine for swimming with sharks",
    "price"         : 9.99,
    "weight"        : 9001,
    "department"    : "grocery",
    "aisle"         : 3,
    "shelf"         : "B"
}

print(product["price"])
location = (product["aisle"], product["shelf"])
print(location)

print(product.get("quantity"))

product["aisle"] += 1
product["department"] = "guy's grocery games"

for key in product:
    print(product[key])

# A list of the values
print(product.values())
print(product.keys())
# product["whatever"] = "the value"
product.update({ "whatever": "the value" })



you = {}

data = [ ("name", "your name"), ("age", 90), ("class", "Python") ]

# for k, v in data:
#     you[k] = v

# for dat in data:
    # you.update({ dat[0]: dat[1] })

you.update(data)

print(you)

f'Your age is { you["you"] }'

#                   Collections
# Type          Mutable     Ordered     Denotation
# ------------------------------------------------
# List          Yes         Yes         [,]
# Set           Yes         No          {,}
# Tuple         No          Yes         (,)
# Dictionary    Yes         No          { KEY : VALUE, }
