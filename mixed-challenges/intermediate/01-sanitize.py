"""
Objective: write two functions, slugify and safe_filename. Each takes a string and returns a cleaned up copy of it. You may assume the text only holds plain ASCII characters.

slugify turns text into a lowercase identifier made of letters, digits, and hyphens. The text is lowercased, then every run of characters that are not a lowercase letter or a digit becomes a single hyphen, and hyphens at either end are removed. "Hello, World!" becomes "hello-world". If nothing usable is left, it returns an empty string.

safe_filename turns text into a name that is safe to use for a single file or folder on any operating system. The characters < > : " / | ? *, the backslash, and every control character (character codes 0 through 31, and 127) each become an underscore, so the name can never point into another folder. Then whitespace is trimmed from both ends, and any periods and spaces are trimmed from the end. If the part of the name before its first period, ignoring capitalization and surrounding spaces, is a name Windows reserves for devices (CON, PRN, AUX, NUL, COM1 through COM9, or LPT1 through LPT9), an underscore is added to the front, so "CON.txt" becomes "_CON.txt". If nothing is left, it returns a single underscore.
"""

