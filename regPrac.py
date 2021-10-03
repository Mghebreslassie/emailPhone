def find_phone_email():
    '''
    after copy some text to clipboard run function to print out emails and phone numbers.
    '''
    import re
    import pyperclip as clip
    phoneReg = re.compile(r'''(
(\(?\d{3}\)?)?
(\s|-|\.)?
(\d{3})
(\s|-|\.|\*)
(\d{4})
)''', re.VERBOSE)
    text = clip.paste()
    emailReg = re.compile(r'(\w+@\w+\.\w{3})')
    phoneMatches = phoneReg.findall(text)
    for match in phoneMatches:
        print(match[0])
    emailMatches = emailReg.findall(text)
    for match in emailMatches:
        print(match)