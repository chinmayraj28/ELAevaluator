"""
The code needs to be able to iterate through all possible values 
efficiently"""
"! ^ | -> <->"
class Formula():
    def __init__(self,startString = "",splitString = []):
        self.vars = []
        if startString != "":
            self.formula = startString.split(" ")
        else:
            self.formula = splitString
        self.setSymbol = ["(",")","!","^","|","->","<->"]
        self.recurse()
    def recurse(self):
        stack = []
        skipTo = 0
        for i in range(len(self.formula)):
            if i<skipTo:
                continue
            val = self.formula[i]
            if val == self.setSymbol[0]:
                new_stack = []
                for j in range(i+1,len(self.formula)):
                    if self.formula[j] != self.setSymbol[1]:
                        new_stack.append(self.formula[j])
                    else:
                        stack.append(self.setSymbol[0])
                        stack.append(Formula(splitString = new_stack))
                        for vars in stack[-1].vars:
                            if vars not in self.vars:
                                self.vars.append(vars)
                        stack.append(self.setSymbol[1])
                        skipTo = j+1
                        break
            else:
                if (val not in self.setSymbol) and (val not in self.vars):
                    self.vars.append(val)
                stack.append(val)    
        self.stack = stack
    def __str__(self):
        answerString = ""
        for i in self.stack:
            answerString += str(i) + " "
        return answerString
    def evaluate(self,ground_truth):
        new_stack = []
        for i in self.stack:
            if i in [self.setSymbol[0],self.setSymbol[1]]:
                continue
            elif type(i) != str:
                new_stack.append(i.evaluate(ground_truth))
            elif i in self.setSymbol:
                new_stack.append(i)
            else:
                new_stack.append(ground_truth[i])
        index = 0
        while index <len(new_stack):
            if new_stack[index] == self.setSymbol[2]:
                if new_stack[index+1] == "!":
                    new_stack.pop(index+1)
                    new_stack.pop(index)
                elif new_stack[index+1] in [0,1]:
                    new_stack[index+1] = 1-new_stack[index+1]
                else:
                    raise Exception(self.stack, "is an invalid formula")
            index +=1
        #Fuck this isnt the proper modular way to code this
        index = 0
        while index <len(new_stack):
            if new_stack[index] == self.setSymbol[3]:
                a = new_stack[index-1]
                b = new_stack[index+1]
                new_stack.pop(index)
                new_stack.pop(index)
                new_stack[index-1] = a&b
            index +=1
        index = 0
        while index <len(new_stack):
            if new_stack[index] == self.setSymbol[4]:
                a = new_stack[index-1]
                b = new_stack[index+1]
                new_stack.pop(index)
                new_stack.pop(index)
                new_stack[index-1] = a|b
            index +=1
        index = 0
        while index <len(new_stack):
            if new_stack[index] == self.setSymbol[5]:  # -> (IMPLIES)
                a = new_stack[index-1]
                b = new_stack[index+1]
                new_stack.pop(index)
                new_stack.pop(index)
                # IMPLIES: False only when a=True and b=False
                if a == 1 and b == 0:
                    new_stack[index-1] = 0
                else:
                    new_stack[index-1] = 1
            index +=1
        index = 0
        while index <len(new_stack):
            if new_stack[index] == self.setSymbol[6]:  # <-> (BICONDITIONAL)
                a = new_stack[index-1]
                b = new_stack[index+1]
                new_stack.pop(index)
                new_stack.pop(index)
                # BICONDITIONAL: True when both values are equal
                new_stack[index-1] = 1 if (a==b) else 0
            index +=1
        return new_stack[0]
                
class Evaluator():
    def __init__(self,startString = "",splitString = [],outputfile="answers.txt"):
        self.formula = Formula(startString=startString,splitString=splitString)
        self.vars = self.formula.vars
        self.n = len(self.vars)
        self.outputfile = outputfile
    def generate_truth_table(self):
        file = open(self.outputfile,"w")
        file.write(" ".join(self.vars))
        file.write("\n")
        for combination in range(pow(2,self.n)):
            ground_truth = {}
            for id,var in enumerate(self.vars):
                ground_truth[var] = (combination>>id)&1
            answer = self.formula.evaluate(ground_truth)
            for id,var in enumerate(self.vars):
                file.write(str((combination>>id)&1))
                file.write(len(var)*" ")
            file.write(str(answer))
            file.write("\n")
        file.close()
            
if __name__=="__main__":
    temp = Evaluator(input("Input formula"))
    print(temp.vars)
    temp.generate_truth_table()