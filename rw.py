import random

count = 1; score = 0
exercises =  {
    "1+1 = ?":  2,
    "5+5 = ?": 10,
    "10+25 = ?": 35,
    "50+50 = ?": 100,
    "90+90 = ?": 180,
}
stu_num = int(input("กรุณาระบบรหัสนักเรียน => "))
if stu_num == 34265:
    print("ยินต้อนรับคุณ กรัณย์ภัทร พรหมวิสุทธิ์ ม.6/4 เลขที่ 2")
    print("เรามาเริ่มทำข้อสอบปลายภาคกันเถอะ\n")
else:
    print("รหัสนักเรียนไม่ถูกต้อง")
    exit()
keys = list(exercises.keys())
random.shuffle(keys)
ShuffledExercisesDict = dict()
for key in keys:
    ShuffledExercisesDict.update({key: exercises[key]})
for keys, values in ShuffledExercisesDict.items():
    print('{0}. {1}'.format(count, keys))
    answers = [values]
    j = 0
    while True:
        if j == 3: break
        rand = random.randrange(0, 100)
        if rand != answers[0]:
            answers.append(rand)
            j = j + 1
    j = 0
    random.shuffle(answers)
    map_ans = {"A": 0, "B": 1, "C": 2, "D": 3}
    for i in answers:
        print(chr(65+j) + ". ", i)
        if j == 3:
            choose = str(input("\nChoose Answer => "))
            int_ans = map_ans.get(choose)
            check_ans = answers[int_ans]
            if check_ans == values:
                score = score + 1
        j = j + 1
    count = count + 1
    print()
print('คุณได้คะแนน => {0} / 5'.format(score))
