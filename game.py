import json
from quiz import Quiz

class Game:

    def __init__(self):
        self.data = self.safe_file_load()

        self.quizzes = []
        for q in self.data["quizzes"]:
            quiz = Quiz(q["question"], q["choices"], q["answer"])
            quiz.question = q["question"]
            quiz.choices = q["choices"]
            quiz.answer = q["answer"]
            self.quizzes.append(quiz)
        self.bestscore = self.data["bestscore"]
        

    def show_menu(self):
        print("퀴즈게임")
        print("1.퀴즈풀기")
        print("2.퀴즈추가")
        print("3.퀴즈 목록보기")
        print("4.점수확인")
        print("5.종료")
        
    def solve_quiz(self, data):
        temp_score = 0
        for q in self.quizzes:
            print(q.question)
            for j in range(0,4):
                print(f"{j+1}. {q.choices[j]}")
            answer = self.get_user_input_number("답변을 입력하세요1~4: ",1,4)
            if answer == q.answer:
                print("정답")
                temp_score +=1
            else:
                print("오답")

        print(f"점수 :{temp_score}")
        if temp_score > self.bestscore:
            print("최고점수 갱신")
            self.bestscore = temp_score
            self.data["bestscore"] = self.bestscore
            self.safe_file_save(self.data)

    def add_quiz(self):
        print("문제입력")
        input_first =self.get_user_input_str()
        print("선택지 제시 4번 입력")
        input_second_list = []
        for i in range(0,4):
            print(f"{i+1}번 선택지 입력")

            input_temp=self.get_user_input_str()
            input_second_list.append(input_temp)
        print("정답 입력")
        input_third=self.get_user_input_number("정답 번호를 입력하세요1~4: ",1,4)
        quiz = Quiz(input_first, input_second_list, input_third)
        quiz["question"] = input_first
        quiz["choices"] = input_second_list
        quiz["answer"] = input_third
        # dict_quiz = {
        #     "question" : input_first,
        #     "choices" : input_second_list,
        #     "answer" : input_third
        # }
        self.quizzes.append(quiz)
        self.data["quizzes"].append(quiz.__dict__)
        self.safe_file_save(self.data)

    def show_quiz_list(self):
        
        if self.quizzes == []:
            print("퀴즈없음")
            return

        for i, q in enumerate(self.quizzes):
            print(f"[{i+1}]. {q['question']}")
            print("선택지")
            for j, c in enumerate(q["choices"]):
                print(f"{j+1}. {c}")
            print(f"정답 : {q['answer']}")
            


    def show_bestscore(self):
        if self.bestscore == 0:
            print("퀴즈를 풀지않았거나 0점입니다")
            return
        
        print(f"최고점수 : {self.bestscore}")

    def get_user_input_number(self, string="숫자입력", min_val=0, max_val=5):
        while(True):
            try:
                input_number_only = input(string)
                if input_number_only == '':
                    print("빈입력")
                    continue
                input_number_only = input_number_only.strip()
                input_number_int = int(input_number_only)
                if input_number_int < min_val or input_number_int > max_val:
                    print("범위밖")
                    continue
                else:
                    return input_number_int
            except KeyboardInterrupt:
                print("KeyboardInterrupt 안전종료")
                self.safe_file_save(self.data)
                quit()
            except EOFError:
                print("EOFError 안전종료")
                self.safe_file_save(self.data)
                quit()
            except ValueError:
                print("숫자입력")
                continue

    def get_user_input_str(self, string="문자입력"):
        while(True):
            try:
                input_str = input(string)
                if input_str == '':
                    print("빈입력")
                    continue
                return input_str
            except EOFError:
                print("EOFError 안전종료")
                self.safe_file_save(self.data)
                quit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt 안전종료")
                self.safe_file_save(self.data)
                quit()


    def safe_file_load(self):
        try:
            
            with open('./state.json', encoding='utf-8') as f:
                data = json.load(f)
            
            return data
        except FileNotFoundError:
            print("파일없음")
            with open('./basic.json', encoding='utf-8') as f:
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
            with open('./state.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        except json.JSONDecodeError:
            print("json형식오류")
            print("기본데이터로 저장")
            with open('./basic.json') as f:
                data = json.load(f)
            with open('./state.json', 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)
        
        except:
            print("기타에러")
            quit()
        
    def run(self):
        while True:
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
                    print("종료")
                    self.safe_file_save(self.data)
                    quit()

            except EOFError:
                print("EOFError 안전종료")
                self.safe_file_save(self.data)
                quit()
            except KeyboardInterrupt:
                print("KeyboardInterrupt 안전종료")
                self.safe_file_save(self.data)
                quit()
            except Exception as e:
                print(f"알 수 없는 오류 발생: {e}")
                self.safe_file_save(self.data)
                quit()

        

