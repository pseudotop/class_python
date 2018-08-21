import os

path = os.path.dirname("C:/Users/student/PycharmProjects/class_python/day08")

for b_path, dirs, files in os.walk(path):
    for filename in files:
        # filepath = b_path + '/'+ filename
        # print(filepath)
        filepath = os.path.join(b_path, filename)
        try:
            with open(filepath, 'r', encoding='cp949') as f_in:
                with open(os.path.join(b_path, '_' + filename),
                          'w', encoding='utf-8') as f_out:
                    for line in f_in:
                        f_out.write(line)
        except:
            pass