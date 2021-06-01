import textwrap


def wrap(string, max_width):
    my_wrap = textwrap.TextWrapper(width=max_width)
    return "\n".join(my_wrap.wrap(text=string))
