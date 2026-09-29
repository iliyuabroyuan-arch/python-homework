import keyword

name = input()

is_valid = (
    name.isidentifier()
    and not keyword.iskeyword(name)
    and not any(character.isupper() for character in name)
    and "__" not in name
)

print(is_valid)
