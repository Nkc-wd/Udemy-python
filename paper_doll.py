'''
Created on May 26, 2020

@author: samsung
'''
def paper_doll(text):
    str=""
    for i in range(0,len(text)):
      str=str+"".join(3*text[i])
    print(str)     
       

paper_doll('Hello')
paper_doll('Mississippi')