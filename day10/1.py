'''
1.读取codon.txt⽂件，将所有密码⼦信息存储到字典codon_dict中，键为密码⼦，值为对应的氨基酸缩写（终⽌密码⼦为stop）
2.定义⼀个函数transcript，输⼊DNA序列，转录成为mRNA序列
3.定义⼀个函数translate，输⼊DNA序列，先利⽤transcript转录为mRNA，再将mRNA翻译为氨基酸序列，输出氨基酸序列（字符串）
注意事项如下：
1.起始密码⼦为AUG，从第⼀个起始密码⼦开始翻译，起始密码⼦也对应氨基酸，作为氨基酸序列第⼀位。
2.如果没有起始密码⼦，return空字符串
3.每三个碱基翻译成codon_dict对应的氨基酸，遇到第⼀个终⽌密码⼦停⽌
4.读取seq.fa⽂件读取到字典seq_dict中，键为序列名（如第⼀条名称为seq1），值为对应的
序列。
5.建⽴字典protein_dict,键为seq_dict中序列名称，值为对应序列翻译出的氨基酸序列
（translate函数输出结果）
'''
import os


def read_dic(path):
    codon_dict = {}
    with open(path, 'r') as f:
        for line in f:
            codon, animo = line.split()
            if len(codon) == 3:
                codon_dict[codon] = animo
    return codon_dict


def transcript(dna):
    res = ""
    trans = {"A": "U", "T": "A", "C": "G", "G": "C"}
    for i in range(len(dna)):
        res += trans[i]
    return res


def translate(dna, codon_dict):
    amino = ''
    mrna = transcript(dna)
    start_index = mrna.find("AUG")
    while start_index < len(mrna):
        codon = mrna[start_index:start_index+3]
        if codon_dict[codon] == "STOP":
            break
        amino += codon_dict[codon]
        start_index += 3
    return amino


def read_fa(path):
    seq_dict = {}
    with open(path, 'r') as f:
        text = f.readlines()
        for i in range(0, len(text), 2):
            seq_dict[text[i][1:-1]] = text[i+1][:-1]
    return seq_dict


def protein(codon_path, seq_path):
    codon_dict = read_dic(codon_path)
    seq_dict = read_fa(seq_path)
    protein_dict = {}
    for i, j in seq_dict.items():
        protein_dict[i] = translate(j, codon_dict)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    protein_path = os.path.join(current_dir, 'protein.txt')
    with open(protein_path, 'w') as f:
        for i, j in protein_dict.items():
            f.write(i+'\n')
            f.write(j+'\n')


current_dir = os.path.dirname(os.path.abspath(__file__))
codon_path = os.path.join(current_dir, 'codon.txt')
seq_path = os.path.join(current_dir, 'seq.fa')
protein(codon_path, seq_path)
