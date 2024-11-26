records = []

while True:
    record = input("Enter book record in format (book title - days) and done to finish  \n")
    if record =="done":
        break
    records.append(record)  # Harry Potter   
print(records)

bookDic = {}   #[a - 5,b - 6,c - 7 , a - 7]
uniqueTitle = set() 

for record in records:
    title, days = record.split(" - ")
    days = int(days)

    if title in bookDic:
        bookDic[title] += days
    else:
        bookDic[title] = days


    uniqueTitle.add(title)

print(bookDic)
print(uniqueTitle)

mostBorrowed = max(bookDic, key=bookDic.get)
print(f"Most borrowed book: {mostBorrowed} ({bookDic[mostBorrowed]} days)")
leastBorrowed = min(bookDic, key=bookDic.get)
print(f"Least borrowed book: {leastBorrowed} ({bookDic[leastBorrowed]} days)")

avg = sum(bookDic.values()) / len(bookDic)
print("Average borrowing time: "+str(avg))

sortedBooks = sorted(bookDic,reverse=True)
print(f"Books sorted by borrowing duration descending: {sortedBooks}")
# print("Books sorted by borrowing duration descending: "+str(sortedBooks))