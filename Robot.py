#!/usr/bin/env python


class Robot(object):
    population=0

    def __init__(self,name,age):
        self.name=name
        self.age=age
        Robot.population+=1
        # print("我的名字是{0}:".format(self.name))
        print("{0}的年龄是{1}:".format(self.name,self.age))

    def Skill_walk(self):
        print("{0} can walk".format(self.name))

    def Skill_speak(self):
        print("{0} can speck".format(self.name))

    def Die(self):
        print("{0} died".format(self.name))
        Robot.population -= 1

    @classmethod
    def How_many(cls):
        print("Robot population have {0}".format(Robot.population))
        if (Robot.population == 0):
            print("Robot has no one left!")

if __name__=="__main__":
    R=Robot("Rock",3)
    R.Skill_walk()
    R.Skill_speak()
    R.How_many()


    J=Robot("Jack",4)
    J.Skill_speak()
    J.How_many()
    J.Die()
    J.How_many()



