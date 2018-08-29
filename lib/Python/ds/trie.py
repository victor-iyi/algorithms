"""Data Structures: Trie.

   @structure
     A tree-like structure where each node represents a single character
     of a given string. Unlike binary trees, a node may have more than two
     children.
                                 (*)
                                /  \\
                              /     \\
                            /        \\
                          /           \\
                        /              \\
                      /                 \\
                     B                   S
                  /  |  \\             /  \\
                /    |   \\           /    \\
              E      I     U         E       T
            /  \\    |    / \\       |       |
          /     \\   |   /   \\      |       |
         A       L   D   L    Y      L       O
         |       | (bid) |  (buy)    |      / \\
         |       |       |           |     /   \\
         R       L       L           L    C     P
      (bear)   (bell)  (bull)      (sell) |   (stop)
                                          |
                                          K
                                       (stock)

   @author
     Victor I. Afolabi
     Artificial Intelligence & Software Engineer.
     Email: javafolabi@gmail.com
     GitHub: https://github.com/victor-iyiola

   @project
     File: ds/tree.py
     Created on 29 August, 2018 @ 2:37 AM.

   @license
     MIT License
     Copyright (c) 2018. Victor I. Afolabi. All rights reserved.
"""


class TrieNode(object):

    def __init__(self, char):
        # Current node's character.
        self._char = char

        # Children.
        self._children = []

        # Number of words you can make from this node.
        self._count = 1

        # Flags that indicates reaching a complete word.
        self._is_word = False

    def __repr__(self):
        return "TrieNode(char=\'{}\')".format(self._char)

    def add_child(self, child):
        self._children.append(child)

    def child_count(self):
        return len(self._children)

    @property
    def char(self):
        return self._char

    @property
    def children(self):
        return self._children

    @property
    def count(self):
        return self._count

    # Alias for count.
    word_count = count

    @property
    def is_word(self):
        return self._is_word

    @count.setter
    def count(self, value):
        self._count = value

    @is_word.setter
    def is_word(self, value):
        self._is_word = value


class Trie(object):

    def __init__(self):
        self._root = TrieNode('*')

    def __contains__(self, word):
        return self.find(word)[0]

    def add(self, word):
        # Start at the root node.
        node = self._root

        # Loop through each character in the given word.
        for char in word.lower():

            # Has char been found in the Trie?
            found = False

            # Go through current node's children.
            for child in node.children:
                # If the current `node.char` == `char`,
                # increment node count
                if char == child.char:
                    # Found charcter in the Trie.
                    found = True

                    # Increment possible words counter & update next node.
                    child.count = child.count + 1
                    node = child

                    break

            if not found:
                # Add child node to current node.
                new_node = TrieNode(char)
                node.add_child(new_node)

                # Update the node.
                node = new_node

        # After adding all characters to the Trie, mark the last char as
        # a complete word.
        node.is_word = True

    def find(self, prefix, node=None):
        node = node or self._root

        # If start node doesn't have any children, prefix doesn't exist!
        if not node.children:
            return False, 0

        # Go through the prefix
        for char in prefix.lower():
            # We haven't found it yet!
            found = False

            # Traverse the Trie & check if char is in any node.
            for child in node.children:
                if child.char == char:
                    # We found a character!
                    found = True
                    node = child
                    break
            # Return False if char wasn't found.
            if not found:
                return False, 0

        # Character was found.
        return True, node.count

    @property
    def root(self):
        return self._root


if __name__ == '__main__':
    trie = Trie()
    trie.add('Vic')
    trie.add('Victor')
    trie.add('Victoria')

    trie.add('Python')
    trie.add('Programming')
    trie.add('programmer')
    trie.add('program')

    print('p' in trie)
    print(trie.find('victor'))
    print(trie.find('prog'))
    print(trie.find('program'))
    print(trie.find('programm'))
