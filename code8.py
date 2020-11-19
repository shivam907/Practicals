import collections
fin = open('email.txt','r')
a= fin.read()
d={ }
l=a.lower().split()
for word in l:
     word = word.replace(".","")
     word = word.replace(",","")
     word = word.replace(":","")
     word = word.replace("\"","")
     word = word.replace("!","")
     word = word.replace("&","")
     word = word.replace("*","")
for k in l:
     key=k
     if key not in d:
           count=L.count(key)
           d[key]=count

n_print = int(input("How many most common words to print: "))
print("\nOK. The {} most common words are as follows\n".format(n_print))
word_counter = collections.Counter(d)
for word, count in word_counter.most_common(n_print):
      print(word, ": ", count)
fin.close()
