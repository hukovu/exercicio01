#%%
import random

pessoas = []

for _ in range(15):
    altura = round(random.uniform(1.3, 1.92), 2)

    pessoas.append({'altura': altura})

for i, pessoa in enumerate(pessoas,1):
    print(f'pessoa {i}: {pessoa["altura"]}m')

menor_altura = min(pessoa['altura'] for pessoa in pessoas)
maior_altura = max(pessoa['altura'] for pessoa in pessoas)

print(f'a menor altura na lista é: {menor_altura}m')
print(f'a maior altura na lista é: {maior_altura}m')


#%%
homens = [pessoa['altura'] for pessoa in pessoas if pessoa ['sexo'] == 'homem']

if homens: 
    media_altura_homens = sum(homens) / len(homens)
    print(f'A média de altura dos homens é: {media_altura_homens:.2f}m')

else:
    print('não há homens na lista de pessoas')

#%%
    mulheres = [pessoa for pessoa in pessoas if pessoa ['sexo'] == 'mulher']

numero_mulheres = len (mulheres)

print(f'número de mulheres na lista é: {numero_mulheres}')

