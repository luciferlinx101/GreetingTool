from stackapi import StackAPI

class StackOverflowAPIWrapper:
    def __init__(self, k: int):
        self.client = StackAPI('stackoverflow')
        self.client.page_size = k
        self.client.max_pages = 1

        self.get_questions_endpoint = 'search/advanced'
        self.get_answers_endpoint = 'questions/{ids}/answers'
        self.filter = 'withbody'

    def __get_questions(self, SITE, q, title, tags):
        questions_resp = SITE.fetch(
            self.get_questions_endpoint,
            q=q,
            title=title,
            accepted=True,
            filter=self.filter,
            tags=tags
        )
        questions = {}
        for item in questions_resp['items']:
            questions[item['question_id']] = (item['title'], item['body'])
        return questions

    def __get_answers(self, SITE, QIDs):
        if len(QIDs) == 0:
            return {}
        answers_resp = SITE.fetch(
            self.get_answers_endpoint,
            ids=QIDs,
            filter=self.filter
        )
        answers = {}
        for answer in answers_resp['items']:
            answers[answer['question_id']] = answer['body']
        return answers

    def __prepare_qa_output(self, questions, answers):
        output = ""

        for i, key in enumerate(questions.keys()):
            output += f"""
                Question {i+1}: {questions[key][0]} \n \
                Description: {questions[key][1]} \n \
                Answer: {answers[key]}
            """

        return output

    def search_advanced(self, q: str, title: str, tags):
        questions = self.__get_questions(self.client, q, title, tags)
        print(f"Questions found: {len(questions)}")
        print(questions)
        answers = self.__get_answers(self.client, list(questions.keys()))
        print(answers)
        print(f"Answers found: {len(answers)}")
        return self.__prepare_qa_output(questions, answers)

# client = StackOverflowAPIWrapper(2)
# print(client.search_advanced("invalid argument", "Java.net.SocketException", ["java", "request"]))