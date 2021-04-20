#07. 基于模板的句子生成Permalink
#实现一个函数，接收三个参数x，y，z作为输入，并返回字符串"{y} is {z} at {x}"作为输出，其中”{x}”， “{y}”， “{z}”分别代表参数x，y ，z的值。
#进一步地，以x=12，y="temperature" ， z=22.4作为输入，确认该函数的输出结果。

def make(x,y,z):
    print(f'{y} is {z} at {x}')

make(12,'temperature',22.4)