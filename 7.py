def  pasos_robot(paso):
    if paso ==1 or paso ==2:
        return paso
    elif paso == 3:
        return paso + 1
    pasos_caminar= pasos_robot(paso -1)+pasos_robot(paso -2) + pasos_robot(paso-3)
    return pasos_caminar

pasos =int(input('ingrese los pasos que el robot va caminar: '))
for i in range(1,pasos +1):
    print(pasos_robot(i))


    