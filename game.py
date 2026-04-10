import json
from quiz import Quiz

class Game:

    def __init__(self):
        self.data = self.safe_file_load()

        self.quizzes = self.data["quizzes"]
        self.bestscore = self.data["bestscore"]
        

    def show_menu(self):
        print("퀴즈게임")
        print("1.퀴즈풀기")
        print("2.퀴즈추가")
        print("3.퀴즈 목록보기")
        print("4.점수확인")
        print("5,종료")
        
    def solve_quiz(self, data):
        temp_score = 0
        for i in data.quizzes:
            quiz = Quiz(i.question, i.choice, i.answer)
            print(quiz.question)
            print(quiz.choices)
            answer = self.get_user_input_number()
            if answer == quiz.answer:
                print("정담")
                temp_score +=1
            else:
                print("오답")

        print(f"점수 :{temp_score}")
        if temp_score > data.bestscore:
            print("최고점수 갱신")
            self.bestscore = temp_score
            self.data["bestscore"] = self.bestscore

    def add_quiz(self):
        print("문제입력")
        input_first =self.get_user_input_str()
        print("선택지 제시 4번 입력")
        input_second = []
        for i in range(0,4):

            input_temp=self.get_user_input_number()
            input_second.append(input_temp)
        print("정답")
        input_third=self.get_user_input_number()
        quiz = Quiz(input_first, input_second, input_third)
        dict_quiz = {
            "question:" : input_first,
            "choices:" : input_second,
            "answer:" : input_third
        }
        self.data["quizzes"].append[dict_quiz]
        self.safe_file_save(self.data)

    def show_quiz_list(self):
        
        if self.quizzes == []:
            print("퀴즈없음")
            return

        for i, q in enumerate(self.quizzes):
            print(f"[{i}]. {q.question}")


    def show_bestscore(self):
        if self.bestscore == 0:
            print("퀴즈를 풀지않았거나 0점입니다")
            return
        
        print(self.bestscore)

    def get_user_input_number(self):
        while(True):

            input_number_only = input()
            if input_number_only == '':
                print("빈입력")
                continue
            if input_number_only not in (1,2,3,4,5):
                print("범위밖")
                continue
            if input_number_only.isdigit():

                strip_input = input_number_only.strip()
                return strip_input
            else:
                print("변환실패")
                continue

    def get_user_input_str(self):
        while(True):

            input_str = input()
            if input_str == '':
                print("빈입력")
                continue
            if input_str.isdigit():
                print("숫자뿐입니다.")
                continue
            input_str = input()
            return input

    def safe_file_load(self):
        try:
            
            with open('state.json') as f:
                data = json.load(f)
            
            return data
        except FileNotFoundError:
            print("파일없음")
            with open('basic.json') as f:
                data = json.load(f)
            return data
        
        except json.JSONDecodeError:
            print("json형식오류")
            with open('basic.json') as f:
                data = json.load(f)
            return data
        except:
            print("기타 에러")
            quit()

    def safe_file_save(self, data):
        try:
            with open('state.json') as f:
                json.dump(data, f)
        except json.JSONDecodeError:
            print("json형식오류")
            print("기본데이터로 저장")
            with open('basic.json') as f:
                data = json.load(f)
            with open('state.json') as f:
                json.dump(data, f)
        except:
            print("기타에러")
            quit()
        
    def run(self):
        try:
            self.show_menu()
            input_number = self.get_user_input_number()
            if input_number == 1:
                self.solve_quiz(self.data)
            elif input_number == 2:
                self.add_quiz()
            elif input_number == 3:
                self.show_quiz_list()
            elif input_number == 4:
                self.show_bestscore()
            elif input_number == 5:
                quit()

        except EOFError:
            print("안전종료")
            quit()
        except:
            pass
        

