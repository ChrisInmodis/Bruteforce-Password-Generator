import itertools
import time

alphabet_1 = 'abcdefghijklmnopqrstuvwxyz' #26
alphabet_2 = 'abcdefghijklmnopqrstuvwxyzäöüß' #30
alphabet_3 = 'abcdefghijklmnopqrstuvwxyzäöüß0123456789' #40
alphabet_4 = 'abcdefghijklmnopqrstuvwxyzäöüß0123456789!+*@=$&' #47

#change the word length to see how the runtime increases --> be aware of memory errors
repeat = 5 #length of words


#26-letter alphabet and word lenght of 5
start = time.time()
bruteforce = [''.join(x) for x in itertools.product(alphabet_1, repeat=repeat)]
end = time.time()
print("Runtime: ", end-start)


#30-letter alphabet and word lenght of 5
start = time.time()
bruteforce = [''.join(x) for x in itertools.product(alphabet_2, repeat=repeat)]
end = time.time()
print("Normal Alphabet + äöüß: ", end-start)


#40-letter alphabet and word lenght of 5
start = time.time()
bruteforce = [''.join(x) for x in itertools.product(alphabet_3, repeat=repeat)]
end = time.time()
print("Normal Alphabet + äüöß + 0-9: ", end-start)


#47-letter alphabet and word lenght of 5
start = time.time()
bruteforce = [''.join(x) for x in itertools.product(alphabet_4, repeat=repeat)]
end = time.time()
print("Normal Alphabet+ äüöß + 0-9 + Special Chars: ", end-start)

