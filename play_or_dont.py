# write a random game

def play_or_dont(question, tries=5, footnote="We hope you will make the best decision!"):
    while True:
        ans = input(question)
        if ans in ['Y', 'y', 'ya', 'yes', 'ofc']:
            # print(footnote)             #maybe change variable name?
            print()
            print("Good to see you stay")
            return True
        if ans in ['N', 'n', 'no', 'nope', 'ofc not']:
            # print(footnote)
            print()
            print("Sad to see you go")
            return False
        tries -= 1
        if tries < 0:
            raise ValueError('Invalid User Response')
        # print(footnote)

play_or_dont('Will you keep on playing?')
