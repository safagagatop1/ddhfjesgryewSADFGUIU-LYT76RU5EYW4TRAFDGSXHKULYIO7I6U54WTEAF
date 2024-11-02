# x=300
# z=300
# def setup():
#     size(600,600)
# def draw():
#     global z
#     global x
#     background(100)
#     fill(random(1,255))
#     ellipse(z,z,random(1,200),random(1,200))
#     ellipse(x,z,random(1,200),random(1,200))
#     ellipse(z,x,random(1,200),random(1,200))
#     ellipse(x,x,random(1,200),random(1,200))
#     z+=-1
#     x+=1
#drthdtrrdyfuiuop[piuyftrsrytuydfigohpj[k]lpkojihugytrurifughojp[kpiukjyhtgr
# x=300
# z=300
# def setup():
#     size(600,600)
# def draw():
#     global z
#     global x
#     background(100)
#     fill(random(1,255))
#     line(300,300,x,z)
#     line(300,300,x,x)
#     line(300,300,z,z)
#     line(300,300,z,x)
#     z+=-1
#     x+=1
#;gkergegerkl;re;kglerjlerk;lgekr;eogrl;erlkjelirkg;lrl;erer;lglermklejhpeorgrre
x=0
def setup():
     size(600,600)
def draw():
     global z
     global x
     background(100)
     translate(x,x)
     rect(20,20,40,40)
     triangle(20,20,60,20,40,0)
     x+=1
