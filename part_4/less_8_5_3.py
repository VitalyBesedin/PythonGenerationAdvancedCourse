# the number of unique words in the text
words = (input().lower()).split()
st= set()
for word in words:
    st.add(word.strip('.,;:-?!'))

print(len(st))

