import pandas as pd
import random
col_list = ["attribute","value","laptop","tablet"]
data = pd.read_csv(r'D:\Worksapce\VSWorksapce\prob_data.csv')
   
class mymodel:
    #gender [0]
    # faculty[1]
    # price[2]
    #purpose1[3]
    # purpose2[4]
    # purpose3[5]
    #freaquency[6]
     
     def __init__(self, selected):
        self.selected=selected
        self.faculty_num=-1
        self.price_num=-1
        self.purpose1_num=-1
        self.purpose2_num=-1
        self.purpose3_num=-1
        self.freaquency_num=-1
        self.gender_num=-1
        
        
                    
     def set_faculty(self,selected):
        if self.selected[1] == "ครุศาสตร์อุตสาหกรรมและเทคโนโลยี":
            self.faculty_num=0
        elif self.selected[1]== "บริหารธุรกิจ":
            self.faculty_num=1
        elif self.selected[1] == "วิทยาศาสตร์":
            self.faculty_num=2
        elif self.selected[1] == "วิศวกรรมศาสตร์":
            self.faculty_num=3
        elif self.selected[1] == "ศิลปศาสตร์":
            self.faculty_num=4
        elif self.selected[1] == "สถาปัตยกรรมศาสตร์":
            self.faculty_num=5
        elif self.selected[1] == "อุตสาหกรรมอาหาร":
            self.faculty_num=6
        elif self.selected[1] == "เทคโนโลยีการเกษตร":
            self.faculty_num=7
        elif self.selected[1] == "เทคโนโลยีสารสนเทศ":
            self.faculty_num=8
        elif self.selected[1] == "วิทยาลัยนวัตกรรมการผลิตขั้นสูง":
            self.faculty_num=9
        elif self.selected[1] == "วิทยาลัยนาโนเทคโนโลยีพระจอมเกล้าลาดกระบัง":
            self.faculty_num=10
        elif self.selected[1] == "วิทยาลัยวิศวกรรมสังคีต":
            self.faculty_num=11
        return self.faculty_num
                    
     def set_price(self,selected):       
        if self.selected[2] == "10,001 - 15,000 บาท":
            self.price_num=0
        elif self.selected[2]== "15,001 - 20,000 บาท":
            self.price_num=1
        elif self.selected[2] == "20,001 - 25,000 บาท":
            self.price_num=2
        elif self.selected[2] == "25,001 - 30,000 บาท":
            self.price_num=3
        elif self.selected[2]== "5,001 - 10,000 บาท":
            self.price_num=4
        elif self.selected[2] == "น้อยกว่า 5,000 บาท":
            self.price_num=5
        elif self.selected[2] == "มากกว่า 30,000 บาท":
            self.price_num=6
        return self.price_num
                    
     def set_purpose1(self,selected):   
        if self.selected[3] == "การศึกษา":
            self.purpose1_num=0
        elif self.selected[3]== "ตัดต่อวิดีโอ":
            self.purpose1_num=1
        elif self.selected[3] == "วาดรูป":
            self.purpose1_num=2
        elif self.selected[3] == "สื่อบันเทิง (สตรีมมิ่งเพลงและวิดีโอต่าง ๆ)":
            self.purpose1_num=3
        elif self.selected[3]== "เขียนแบบ , ออกแบบแผนผังต่าง ๆ":
            self.purpose1_num=4
        elif self.selected[3] == "เขียนโปรแกรม":
            self.purpose1_num=5
        elif self.selected[3] == "เล่นเกม":
            self.purpose1_num=6
        return self.purpose1_num
            
     def set_purpose2(self,selected):   
        if self.selected[4] == "การศึกษา":
            self.purpose2_num=0
        elif self.selected[4]== "ตัดต่อวิดีโอ":
            self.purpose2_num=1
        elif self.selected[4] == "ทำเพลง":
            self.purpose2_num=2
        elif self.selected[4] == "วาดรูป":
            self.purpose2_num=3
        elif self.selected[4]== "สื่อบันเทิง (สตรีมมิ่งเพลงและวิดีโอต่าง ๆ)":
            self.purpose2_num=4
        elif self.selected[4] == "เขียนแบบ , ออกแบบแผนผังต่าง ๆ":
            self.purpose2_num=5
        elif self.selected[4] == "เขียนโปรแกรม":
            self.purpose2_num=6
        elif self.selected[4] == "เล่นเกม":
            self.purpose2_num=7
        return self.purpose2_num
            
     def set_purpose3(self,selected):   
        if self.selected[5] == "การศึกษา":
            self.purpose3_num=0
        elif self.selected[5]== "ตัดต่อวิดีโอ":
            self.purpose3_num=1
        elif self.selected[5] == "ทำเพลง":
            self.purpose3_num=2
        elif self.selected[5] == "วาดรูป":
            self.purpose3_num=3
        elif self.selected[5]== "สื่อบันเทิง (สตรีมมิ่งเพลงและวิดีโอต่าง ๆ)":
            self.purpose3_num=4
        elif self.selected[5] == "เขียนแบบ , ออกแบบแผนผังต่าง ๆ":
            self.purpose3_num=5
        elif self.selected[5] == "เขียนโปรแกรม":
            self.purpose3_num=6
        elif self.selected[5] == "เล่นเกม":
            self.purpose3_num=7
        return self.purpose3_num
                    
     def set_freaquency(self,selected):   
        if self.selected[6] == "1 - 2 วัน":
            self.freaquency_num=0
        elif self.selected[6]== "3 - 5 วัน":
            self.freaquency_num=1
        elif self.selected[6] == "ทุกวัน":
            self.freaquency_num=2
        elif self.selected[6] == "ไม่พกพาเลย":
            self.freaquency_num=3
        return self.freaquency_num
               
     def set_gender(self,selected):   
        if self.selected[0] == "LGBTQ+":
            self.gender_num=0
        elif self.selected[0]== "ชาย":
            self.gender_num=1
        elif self.selected[0] == "หญิง":
            self.gender_num=2 
        return self.gender_num
        
  
     def calculate(self):
        self.faculty_num=self.set_faculty(self.selected)
        self.price_num=self.set_price(self.selected)
        self.purpose1_num=self.set_purpose1(self.selected)
        self.purpose2_num=self.set_purpose2(self.selected)
        self.purpose3_num=self.set_purpose3(self.selected)
        self.freaquency_num=self.set_freaquency(self.selected)
        self.gender_num=self.set_gender(self.selected)
        self.ans_list = [self.faculty_num,self.price_num,self.purpose1_num,self.purpose2_num,
                    self.purpose3_num,self.freaquency_num,self.gender_num]
            
    #Group data to calculate 
        self.att_list = ["faculty","price","purpose1","purpose2","purpose3","freaquency","gender"]
        self.table_all= []
        self.i=0
        for self.var in self.att_list :
            self.table_all.append(self.var)
            self.table_all[self.i] = data.groupby(['attribute']).get_group(self.var)
            self.i=self.i+1
            
    #calculate
        
        self.laptop = []
        self.tablet = []
            
        for self.j in range(len(self.ans_list)) :
            self.temp_value = self.table_all[self.j][(self.table_all[self.j]['value']==self.ans_list[self.j])]
            self.temp_value = self.temp_value.iloc[0]
            self.laptop.append(self.temp_value['laptop'])
            self.tablet.append(self.temp_value['tablet'])
            
        self.sum_laptop=1
        self.sum_tablet=1 
        for self.k in range(len(self.laptop)) :
            print(self.laptop[self.k])
            print(self.tablet[self.k])
            self.sum_laptop=self.sum_laptop*self.laptop[self.k]
            self.sum_tablet=self.sum_tablet*self.tablet[self.k]
            
        print (self.sum_laptop)
        print (self.sum_tablet) 
            #send final answer
        self.final_ans=-1
        if(self.sum_laptop>self.sum_tablet) :
            self.final_ans=0#laptop
        elif (self.sum_laptop<self.sum_tablet) :
            self.final_ans=1#tablet
        else : self.final_ans=random.randint(0,1)#equal pridict class lable
        
        return self.final_ans
        
            