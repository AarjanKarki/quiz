import pgzrun
TITLE='quiz'
WIDTH=900
HEIGHT=650

marqueebox=Rect(0,0,500,80)
questionbox=Rect(0,0,660,150)
timer_box=Rect(0,0,150,150)
answer1=Rect(0,0,300,150)
answer2=Rect(0,0,300,150)
answer3=Rect(0,0,300,150)
answer4=Rect(0,0,300,150)
skipbox=Rect(0,0,150,330)

score=0
time_left=10
question_file_name='questions.txt'
marquee_message=''
game_over=False

answerboxes=[answer1,answer2,answer3,answer4]
questions=[]
question_count=0
question_index=0

marqueebox.move_ip(0,0)
questionbox.move_ip(20,100)
timer_box.move_ip(700,100)
answer1.move_ip(20,270)
answer2.move_ip(370,270)
answer3.move_ip(20,450)
answer4.move_ip(370,450)
skipbox.move_ip(700,270)

def draw():
    global marquee_message
    screen.clear()
    screen.fill(255,0,0)
    screen.draw.filled_rect(marqueebox,'black')
    screen.draw.filled_rect(questionbox,'black')
    screen.draw.filled_rect(timer_box,'black')
    screen.draw.filled_rect(skipbox,'black')
    for answerbox in answerboxes:
        screen.draw.filled_rect(answerboxes,'black')
    marquee_message='welcome to quizmaster'
    marquee_message=marquee_message+f'Q:{question_index}of{question_count}'
