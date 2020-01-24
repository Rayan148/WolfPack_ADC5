from django.db.models import Q


def get_data_queryset(query=None):
	queryset=[]
	queries = query.split(" ") #split: this will convert the strings into list
	for q in queries:
		questions = Question.objects.filter( #filter will help to search multiple values. but get will not
		Q(question_title__icontains=q) |
		Q(question__icontains=q)
		)

		for ques in questions:
			queryset.append(ques)

	return list(set(queryset))  #typecasting: changing the type of a variable