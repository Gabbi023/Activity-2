exam_scores = {"Jonathan": 85, "Erica": 99,"Rose": 83, "Henry": 92, "Missy": 77, "Ashleigh": 88, "Paul": 68,
               "Gordon": 86, "Lisa": 90, "Kelly": 77, "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

print(exam_scores["Paul"])

exam_scores = {"Jonathan": 85, "Erica": 99,"Rose": 83, "Henry": 92, "Missy": 77, "Ashleigh": 88, "Paul": 68,
               "Gordon": 86, "Lisa": 90, "Kelly": 77, "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

check_key = "Andrew"

if check_key in exam_scores:
    print(check_key, "took the test")

else:
    print(check_key, "didn't take the test")


exam_scores = {"Jonathan": 85, "Erica": 99,"Rose": 83, "Henry": 92, "Missy": 77, "Ashleigh": 88, "Paul": 68,
               "Gordon": 86, "Lisa": 90, "Kelly": 77, "Joe": 65, "Tiffany": 67, "Wesley": 97, "Gail": 71}

print(exam_scores.get("Lisa"))
print(exam_scores.get("Wesley"))
print(exam_scores.get("Queenie"))


neighbors = {"Ms. Santos": "fruitcake", "Mr. Reyes": "cookies", "Mrs. Dela Cruz": "cupcakes",
             "Mr. Tiu": "gingerbread man"}
done = neighbors.pop("Mr. Reyes")
y = neighbors.keys()

print(y)


neighbors = {"Ms. Santos": "fruitcake", "Mr. Reyes": "cookies", "Mrs. Dela Cruz": "cupcakes",
             "Mr. Tiu": "gingerbread man"}

w = neighbors.values()

print(w)

z = neighbors.items()

print(z)