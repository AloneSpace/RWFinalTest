count = 1
exercises = {}
while True:
    question = str(input('ข้อ {}. '.format(count)))
    exercises.update({question: ""})
    correct = str(input("คำตอบที่ถูกต้อง => "))
    exercises.update({question: correct})
    answers = [correct]
    for i in range(1,4):
        answers.append(str(input("คำตอบที่ไม่ถูกต้อง => ")))
    choose = str(input("คุณจะกรอกข้อต่อไปหรือไหม [Y/N]?: "))
    if choose == 'N' or choose == 'n':
        print("ทำการบันทึกแบบข้อสอบลงในระบบแล้ว\n\n")
        j = 1
        for key, value in exercises.items():
            print("ข้อที่ {}. {}".format(j,key))
            print("คำตอบ => {}".format(value))
            print("ตัวเลือกที่ผิด: ")
            for i in range(1,4):
                print("• ",answers[i])
            j = j + 1
        break
    count = count + 1

