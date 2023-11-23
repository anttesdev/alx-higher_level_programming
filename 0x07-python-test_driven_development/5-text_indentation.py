def text_indentation(text):
    """
    A function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    Args:
        text (str): The input text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiter = ['.', '?', ':']
    line = ""

    for char in text:
        line += char
        if char in delimiter:
            print(line.strip())
            print()
            line = ""
    if line:
        print(line.strip())
