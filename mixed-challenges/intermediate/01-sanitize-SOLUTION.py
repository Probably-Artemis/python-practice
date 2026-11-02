"""
Objective: write two functions, slugify and safe_filename. Each takes a string and returns a cleaned up copy of it. You may assume the text only holds plain ASCII characters.

slugify turns text into a lowercase identifier made of letters, digits, and hyphens. The text is lowercased, then every run of characters that are not a lowercase letter or a digit becomes a single hyphen, and hyphens at either end are removed. "Hello, World!" becomes "hello-world". If nothing usable is left, it returns an empty string.

safe_filename turns text into a name that is safe to use for a single file or folder on any operating system. The characters < > : " / | ? *, the backslash, and every control character (character codes 0 through 31, and 127) each become an underscore, so the name can never point into another folder. Then whitespace is trimmed from both ends, and any periods and spaces are trimmed from the end. If the part of the name before its first period, ignoring capitalization and surrounding spaces, is a name Windows reserves for devices (CON, PRN, AUX, NUL, COM1 through COM9, or LPT1 through LPT9), an underscore is added to the front, so "CON.txt" becomes "_CON.txt". If nothing is left, it returns a single underscore.

The code below consists of a stub for each of the two functions, followed by some example calls you can use to test your work. You may delete whatever you please if you do not wish to use it.
"""

import re  # re is python's regular expression module. a regular expression is a small pattern language for finding text, and it does in one line what would otherwise take a loop over every character.

_NOT_SLUG = re.compile(r'[^a-z0-9]+') # [^a-z0-9] matches any one character that is not a lowercase letter or digit, and + extends the match over a whole run of them.

# characters Windows forbids in file names, plus control characters and delete
_FILENAME_FORBIDDEN = re.compile(r'[<>:"/\\|?*\x00-\x1f\x7f]') # \x00-\x1f is the range of character codes 0 through 31, and \x7f is 127.

# names Windows reserves for devices, with or without an extension
_DEVICE_NAMES = {"con", "prn", "aux", "nul"} | {
    f"{port}{number}" for port in ("com", "lpt") for number in "123456789"
}


def slugify(content):
    """Turn text into a lowercase identifier made of letters, digits, and hyphens.

    "Hello, World!" becomes "hello-world".

    :param content: the string to convert.
    :return: the slug. An empty string is returned if nothing usable is left.
    """
    return _NOT_SLUG.sub('-', content.lower()).strip('-') # sub() replaces every match with its first argument.


def safe_filename(content):
    """Turn text into a name that is safe to use for one file or folder on any system.

    Path separators, the other characters Windows forbids, and control characters each
    become an underscore, so the result can never point into another directory. Whitespace
    at both ends and periods at the end are trimmed. Names Windows reserves for devices,
    such as "CON" or "NUL.txt", get an underscore in front. Length is not limited.

    :param content: the proposed name. Pass a single name, not a path.
    :return: the safe name. An underscore is returned if nothing usable is left.
    """
    content = _FILENAME_FORBIDDEN.sub('_', content)
    content = content.strip().rstrip('. ') # rstrip('. ') removes any mix of periods and spaces from the end, not the two characters as a pair.
    if content.split('.', 1)[0].strip().lower() in _DEVICE_NAMES: # split('.', 1) splits at the first period only.
        content = '_' + content
    return content or '_' # an empty string is falsy, so or returns '_' in its place.


print(slugify("Hello, World!")) # hello-world
print(slugify("  Python 3.13 -- Release Notes  ")) # python-3-13-release-notes
print(repr(slugify("!!!"))) # '', since nothing usable is left. repr() shows the quotes, so the empty string is visible.

print(safe_filename("notes: draft 2?.txt")) # notes_ draft 2_.txt
print(safe_filename("../secret")) # .._secret, which can no longer point into the folder above.
print(safe_filename("CON.txt")) # _CON.txt
print(safe_filename(" com1 .log")) # _com1 .log
print(safe_filename("report. . ")) # report
print(safe_filename("tab\there")) # tab_here, since a tab is a control character.
print(safe_filename("...")) # _