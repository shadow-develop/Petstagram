def validate_only_letters(value):
    if not all(x.isalpha() for x in value):
        raise ValueError('Name must contain ony letters!')
