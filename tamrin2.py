# tamrin1:

num1 = int(input("number one ... "))
num2 = int(input("number tow .... "))
num3 = int(input("number three .... "))

gam = (num1 + num2 + num3)

print("majmo adad hast : ",gam)


# tamrin2:

num1 = int(input("number one ... "))
vazn1 = int(input("vazn aval ..."))

num2 = int(input("number tow ... "))
vazn2 = int(input("vazn dovom ..."))

num3 = int(input("number three ... "))
vazn3 = int(input("vazn sevom ..."))

miyangin_vazni = ((num1*vazn1 + num2*vazn2 + num3*vazn3)/
                  (vazn1 + vazn2 + vazn3))

print(miyangin_vazni)


# tamrin3:

rozha = int(input("tedad roz ra vared konid : "))

sahat = (rozha * 24)
dagigeh = (sahat * 60)
sanieh = (dagigeh * 60)

print("{} sahat \n{} daigeh \n{} sanieh".format(
    sahat,dagigeh,sanieh
))


# tamrin4:

geymat = float(input("geymat ra vared konid :  "))

darsad_takhfif = int(input("darsad takhfif ra vared konid : "))

geymat_nahayi = (geymat - (darsad_takhfif * geymat)/100)
print("geymat nahayi : ",geymat_nahayi)



# tamein5:


circle_r =  float(input("give me r : "))
pi = 3.14159
masahat = ((circle_r**2)*pi)
mohit = (2*circle_r*pi)
print("masahat : {:.3f} m**2\nmohit : {:.3f} m".format(masahat,mohit))


# tamrin6:

num1 = float(input("give me M : "))
klm = (num1/1000)
ctm = (num1*100)
mlm = (ctm * 10)

print("kilomet : {} \ncantimetr : {} \nmilimet : {}".format(klm,ctm,mlm))


# tamrin7:

zele = float(input("tool zele mokeab ra vared konid : "))
masahat = ((zele**2)*6)
hajm = (zele**3)
print("masahat mokab : {} m**2 \nhajmeh mokab : {} m**3".format(masahat,hajm))


# tamrin8:

a = float(input("zele 1 : "))
b = float(input("zele 2 : "))
c = float(input("zele 3 : "))

s = ((a*b*c)/2)
masahat = ((s*(s-a)*(s-b)*(s-c)) ** 0.5)
print("masahat mosalas heron : ",masahat)


# tamrin9:

a ,b ,c = map(float,input("se adad ra vared konid : ").split())

jam = (a + b + c)
miyangin = (jam/2)

print(f"jam : {jam} \nmiyangin : {miyangin}")
                    

# tamrin10:

sarmaye = float(input("sarmaye :"))
nerkh = float(input("nerkh : "))
sal = float(input("sal : "))
tedade_mohasebe = float(input("tedad mohaswbe : "))

mablag_nahayi = (sarmaye*(((nerkh+1)/(tedade_mohasebe * 100)
                          )**(tedade_mohasebe * sal)
                         )
                        )

print(f"mablage nahayi : {mablag_nahayi}")