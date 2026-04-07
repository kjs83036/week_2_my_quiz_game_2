import json

class Game:

    def __init__(self,quizzes, bestscore):
        self.quizzes = quizzes
        self.bestscore = bestscore
        

    def show_menu(self):
        print("퀴즈게임")
        print("1.퀴즈풀기")
        print("2.퀴즈추가")
        print("3.퀴즈 목록보기")
        print("4.점수확인")
        print("5,종료")
        

    def solve_quiz(self, data):
        temp_score == 0
        for i in data.quizzes:
            print(i.question)
            print(i.choice)
            answer = self.get_user_input()
            if answer == i.answer:
                print("정담")
                temp_score +=1
            else:
                print("오답")

        print(f"점수 :{temp_score}")
        if temp_score > data.bestscore:
            print("최고점수 갱신")

    def add_quiz(self):
        
        pass

    def show_quiz_list(self):
        pass

    def show_bestscore(self):
        pass

    def get_user_input(self):
        while(True):

            input = input()
            if input == '':
                print("빈입력")
                continue
            if input not in (1,2,3,4,5):
                print("범위밖")
                continue
            if input.digit():

                strip_input = input.strip()
                return strip_input
            else:
                print("변환실패")
                continue

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
        
    def run(self):
        try:
            self.show_menu()
            input_number = self.get_user_input()
            if input_number == 1:
                self.solve_quiz()
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
        

