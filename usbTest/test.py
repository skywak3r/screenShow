from FX_PLC_ctl import config_ser,Set_Reset,read_onoff_element,read_register
import time
up = {1:"X005",2:"X006",3:"X010",4:"X012",5:"X014"}
down = {2:"X007",3:"X011",4:"X013",5:"X015",6:"X016"}

button = {1:"X023",2:"X024",3:"X025",4:"X026",5:"X027",6:"X030"}

fun = {"open":"M10","close":"X004","stop":"X035"}
ser = config_ser()

tmpDic = {1:up, 2:down, 3:button, 4:fun}
res = input("input 1:up,2:down,3:button or 4:fun")
tmpDic1 = tmpDic[int(res)]


if tmpDic1 == fun:

    tmp = input("input open, close or stop")
    Set_Reset(ser,fun[tmp],1)
else:
    tmp = input("number:1-6")
    
    Set_Reset(ser,tmpDic1[int(tmp)],1)

    
    





