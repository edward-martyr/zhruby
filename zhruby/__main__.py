import argparse
from os import system
import opencc
from zhruby.dict import d


def main():
    cc = opencc.OpenCC('s2t')

    parser = argparse.ArgumentParser(description='Input: Chinese text file, output: TeX file with Shanghainese ruby.')
    parser.add_argument('files', metavar='text files separated by space', type=str, nargs='+', help='Please input a Traditional Chinese text file.')
    args = parser.parse_args()
    files=args.files

    for file in files:
        f = open(file, "r")
        txt = cc.convert(f.read())
        f.close()
        
        counter=0
        out=[]
        while counter<len(txt):
            if txt[counter] in d:
                tr=7
                while not txt[counter:counter+tr] in d:
                    tr-=1
                out.append( [txt[counter:counter+tr], d[txt[counter:counter+tr]]] )
                counter+=tr
            else: 
                out.append([txt[counter],[['']]])
                counter+=1

        out=[(e[0], e[1][0][0]) for e in out]
        outt=''
        for tp in out:
            if tp[-1] == '':
                outt+=tp[0]
            else:
                if len(tp[0]) == len(tp[1].split()):
                    for i in range(len(tp[0])):
                        outt+=r'\ruby{'+tp[0][i]+r'}{'+tp[1].split()[i]+r'}'
                else:
                    outt+=r'\ruby{'+tp[0]+r'}{'+tp[1]+r'}'
        
        fo=open(file+'.ruby.tex', 'w')
        fo.writelines(r'''% !TEX program = xelatex

\documentclass{ctexart}

\punctstyle{kaiming}
\usepackage{ruby}
\renewcommand{\rubysize}{0.5}
\renewcommand\rubysep{-0.3em}

\usepackage{setspace}
\AtBeginDocument{\onehalfspacing}

\begin{document}

'''+ outt + '''

\end{document}''')
        fo.close()


        system(f"xelatex {file}.ruby.tex && rm {file}.ruby.aux && rm {file}.ruby.log")


if __name__ == "__main__":
    main()