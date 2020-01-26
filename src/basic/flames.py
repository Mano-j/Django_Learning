
'''
    def flames(name11, name22):

        # Gets two names and converts them to uppercase and stores them.
        # name11 = input('Enter Your name: ').upper()
        # name22 = input('Enter Your dream partner\'s name: ').upper()
        name11 = name11.upper()
        name22 = name22.upper()

        # Removing spaces
        name1 = ''.join(name11.split())
        name2 = ''.join(name22.split())
        i, j = 0, 0
        print('\n')
        flag = None

        # Removing common letters in the names.
        print("\tRemoving common letters \n\t\t", name11, '&', name22)
        while i < len(name1):

            for j in range(0, len(name2), 1):
                flag = False
                if name1[i] == name2[j]:
                    print("Removing -", name1[i], end=' ')
                    name2 = name2[:j] + name2[j+1:]
                    name1 = name1[:i] + name1[i+1:]
                    print("\t-->\t", name1, '-', name2)
                    flag = True
                    break

            if not flag:
                i += 1

        # Calculating the finalLength for the FLAMES calculation.
        finalLength = len(name1) + len(name2)
        print(" FinalLength = ", finalLength)

        flames = "FLAMES"
        i = 0
        print("\n Calculating FLAMES for", name11, "&", name22, end='\n')
        print("\t\t ", flames)

        # Calculating the relationship.
        while len(flames) != 1:
            count = 0
            while count != finalLength:
                if i < len(flames):
                    i += 1
                    count += 1
                else:
                    i = 0
            i -= 1
            print("Removing - ", flames[i], end=' ')
            flames = flames[:i] + flames[i+1:]
            print("\t-->\t", flames)

        result = {'F': "are Best Friends.",
                  'L': "are in Love.",
                  'A': "are Attracted towards each other.",
                  'M': "are going to be/ are Married.",
                  'E': "are Enemies.",
                  'S': "are Siblings."
                  }

        # Printing the prediction.
        print("\n   Prediction : \n", name11, '&', name22, result.get(flames))

        return result.get(flames)
'''


def flames(name11, name22):

    # Gets two names and converts them to uppercase and stores them.
    name11 = name11.upper()
    name22 = name22.upper()

    # Removing spaces
    name1 = ''.join(name11.split())
    name2 = ''.join(name22.split())
    i, j = 0, 0
    print('\n')
    flag = None

    if len(name1) > len(name2):
      name1, name2 = name2, name1

    # Removing common letters in the names.
    print("\tRemoving common letters \n\t\t", name11, '&', name22)
    while i < len(name1):

        for j in range(0, len(name2)):
            flag = False
            if name1[i] == name2[j]:
                print("Removing -", name1[i], end=' ')
                name2 = name2[:j] + name2[j+1:]
                name1 = name1[:i] + name1[i+1:]
                print("\t-->\t", name1, '-', name2)
                flag = True
                break

        if not flag:
            i += 1

    # Calculating the finalLength for the FLAMES calculation.
    finalLength = len(name1) + len(name2)
    print(" FinalLength = ", finalLength)

    if finalLength == 0:
      print("You're either a pure narcissist or both your name are anagrams!.")
      return "\n\nYou're either a pure narcissist or both your name are anagrams!."

    else:
      flames = "FLAMES"
      i = 0
      print("\n Calculating FLAMES for", name11, "&", name22, end='\n')
      print("\t\t ", flames)

      # Calculating the relationship.
      while len(flames) != 1:
          count = 0
          while count != finalLength:
              if i < len(flames):
                  i += 1
                  count += 1
              else:
                  i = 0
          i -= 1
          print("Removing - ", flames[i], end=' ')
          flames = flames[:i] + flames[i+1:]
          print("\t-->\t", flames)

      result = {'F': "are Best Friends. :D ",
                'L': "are in Love. ♥",
                'A': "are Attracted towards each other. *_*",
                'M': "are going to be/ are Married. :)",
                'E': "are Enemies. ._.",
                'S': "are Siblings. :P"
                }

      # Printing the prediction.
      print("\n   Prediction : \n", name11, '&', name22, result.get(flames))
      return result.get(flames)