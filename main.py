def merged_file(path1, path2, path3):
    out_file = "merged_file.txt"

    with open(path1, 'r', encoding='utf-8') as f1:
        file1 = f1.readlines()
    with open(path2, 'r', encoding='utf-8') as f2:
        file2 = f2.readlines()
    with open(path3, 'r', encoding='utf-8') as f3:
        file3 = f3.readlines()
    with open(out_file, 'w', encoding='utf-8') as m_f:
        if len(file1) < len(file2) and len(file1) < len(file3):
            m_f.write(path1 + '\n')
            m_f.write(str(len(file1)) + '\n')
            m_f.writelines(file1)
            m_f.write('\n')
        elif len(file2) < len(file1) and len(file2) < len(file3):
            m_f.write(path2 + '\n')
            m_f.write(str(len(file2)) + '\n')
            m_f.writelines(file2)
            m_f.write('\n')
        elif len(file3) < len(file1) and len(file3) < len(file2):
            m_f.write(path3 + '\n')
            m_f.write(str(len(file3)) + '\n')
            m_f.writelines(file3)
            m_f.write('\n')
        if len(file2) > len(file1) > len(file3) or len(file2) < len(file1) < len(file3):
            m_f.write(path1 + '\n')
            m_f.write(str(len(file1)) + '\n')
            m_f.writelines(file1)
            m_f.write('\n')
        elif len(file1) > len(file2) > len(file3) or len(file2) > len(file1) and len(file2) < len(file3):
            m_f.write(path2 + '\n')
            m_f.write(str(len(file2)) + '\n')
            m_f.writelines(file2)
            m_f.write('\n')
        elif len(file1) > len(file3) > len(file2) or len(file3) > len(file1) and len(file3) < len(file2):
            m_f.write(path3 + '\n')
            m_f.write(str(len(file3)) + '\n')
            m_f.writelines(file3)
            m_f.write('\n')
        if len(file1) > len(file2) and len(file1) > len(file3):
            m_f.write(path1 + '\n')
            m_f.write(str(len(file1)) + '\n')
            m_f.writelines(file1)
            m_f.write('\n')
        elif len(file2) > len(file1) and len(file2) > len(file3):
            m_f.write(path2 + '\n')
            m_f.write(str(len(file2)) + '\n')
            m_f.writelines(file2)
            m_f.write('\n')
        elif len(file3) > len(file1) and len(file3) > len(file2):
            m_f.write(path3 + '\n')
            m_f.write(str(len(file3)) + '\n')
            m_f.writelines(file3)
            m_f.write('\n')
    return


merged_file('1.txt', '2.txt', '3.txt')
