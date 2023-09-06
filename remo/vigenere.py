
import sys

class VigenereCipher:
    """Vigenere Cipher class"""

    @staticmethod
    def _implement(msg, sign, *args, **kwargs):
        # All printable ASCII characters
        total = [chr(i) for i in range(32, 127)]
        len_total = len(total)

        if len({i in total for i in msg}) != 1:
            sys.exit(1)

        key = kwargs["key"]
        len_key = len(key)

        text = ""
        for i, char in enumerate(msg):
            # Return same character if it's not printable ASCII
            if char not in total:
                text += char
            else:
                # Find the exact key character in repeating key
                # e.g attackatdawn-->LEMONLEMONLE
                # i.e w == L
                k = key[i % len_key]

                # Index of character and key
                char_id = total.index(char)
                key_id = total.index(k)

                text += (total[(char_id + (sign*key_id)) % len_total])
        return text

    def encrypt(self, msg: str, *args, **kwargs) -> str:
        """Encrypt plaintext to ciphertext using key"""
        return self._implement(msg=msg, sign=1, *args, **kwargs)

    def decrypt(self, ciphertext: str, *args, **kwargs) -> str:
        """Decrypt ciphertext to plaintext using key"""
        
        return self._implement(msg=ciphertext, sign=-1, *args, **kwargs)


def test_decrypt(msg, key):
    cipher = VigenereCipher()
    text = cipher.decrypt(msg, key=key)
    print("Text: " + text)

# world, remos, task, hello!, instantly 
# Text: world
# Text: Remos
# Text: Task
# Text: Hello!
# Text: instantly

# Example 1
test_decrypt("dU`\S", "lemon")

# Example 2
test_decrypt("COSSY", "piece")

# Example 3
test_decrypt("ICgW", "task")

# Example 4
test_decrypt("2ZR_bl", "iterrk")

# Example 5
test_decrypt("Tbg_C]YXf", "jssjandkl")

