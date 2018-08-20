import fraise
import re

# Should return four space seperated lowercase words
def test_generate_with_no_parameters():
    passphrase = fraise.generate()
    match = re.match("^([a-z]+\s){3}[a-z]+$", passphrase)
    print("Generated passphrase: {}".format(passphrase))
    assert match

# Should return eight space seperated lowercase words
def test_generate_with_word_count():
    passphrase = fraise.generate(word_count=8)
    match = re.match("^([a-z]+\s){7}[a-z]+$", passphrase)
    print("Generated passphrase: {}".format(passphrase))
    assert match
