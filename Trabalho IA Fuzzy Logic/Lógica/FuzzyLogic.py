import numpy as np
import matplotlib.pyplot as plt
import skfuzzy as fuzz
from skfuzzy import control as ctrl

qtde_pessoas = ctrl.Antecedent(np.arange(0,500,1),'pessoas')
qtde_pessoas.automf(number=3, names=["baixo", "medio", "alto"])

qtde_vagas = ctrl.Antecedent(np.arange(0,300,1),'vagas')
qtde_vagas.automf(number=3, names=["baixo", "medio", "alto"])

prioridade = ctrl.Antecedent(np.arange(0,1),'prioridade')
prioridade.automf(number=3, names=["baixo", "medio", "alto"])

encaminhamento = ctrl.Consequent(np.arange(0,100,1),'encaminhamento')
encaminhamento.automf(number=3, names=["Recusado", "Neutro", "Aprovado"])

qtde_pessoas['baixo'] = fuzz.trapmf(qtde_pessoas.universe, [0,0,50,100])
qtde_pessoas['medio'] = fuzz.trimf(qtde_pessoas.universe, [50,125,200])
qtde_pessoas['alto'] = fuzz.trapmf(qtde_pessoas.universe, [200,300,500,500])

qtde_vagas['baixo'] = fuzz.trapmf(qtde_vagas.universe, [0,0,30,70])
qtde_vagas['medio'] = fuzz.trimf(qtde_vagas.universe, [30,90,150])
qtde_vagas['alto'] = fuzz.trapmf(qtde_vagas.universe, [150,200,300,300])

prioridade['baixo'] = fuzz.trapmf(prioridade.universe, [0, 0, 0.3, 0.5])
prioridade['medio'] = fuzz.trimf(prioridade.universe, [0.3 , 0.5, 0.7])
prioridade['alto'] = fuzz.trapmf(prioridade.universe, [0.5, 0.7, 1.0 , 1.0])

encaminhamento['Recusado'] = fuzz.trapmf(encaminhamento.universe, [0,0,30,50])
encaminhamento['Neutro'] = fuzz.trimf(encaminhamento.universe, [30,50,70])
encaminhamento['Aprovado'] = fuzz.trapmf(encaminhamento.universe, [50,70,100,100])

regra1 = ctrl.Rule(qtde_pessoas['alto'] & qtde_vagas['baixo'] & prioridade['alto'], encaminhamento['Aprovado'])
regra2 = ctrl.Rule(qtde_pessoas['alto'] & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Recusado'])
regra3 = ctrl.Rule(qtde_pessoas['alto'] & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra4 = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['alto'], encaminhamento['Aprovado'])
regra5 = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Neutro'])
regra6 = ctrl.Rule(qtde_pessoas['medio'] & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra7 = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['alto'], encaminhamento['Aprovado'])
regra8 = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['medio'], encaminhamento['Neutro'])
regra9 = ctrl.Rule(qtde_pessoas['baixo'] & qtde_vagas['baixo'] & prioridade['baixo'], encaminhamento['Recusado'])
regra10 = ctrl.Rule(qtde_vagas['medio'] & prioridade['alto'], encaminhamento['Aprovado'])
regra11 = ctrl.Rule(qtde_vagas['medio'] & prioridade['medio'], encaminhamento['Aprovado'])
regra12 = ctrl.Rule(qtde_vagas['medio'] & prioridade['baixo'], encaminhamento['Neutro'])
regra13 = ctrl.Rule(qtde_vagas['alto'], encaminhamento['Aprovado'])

sistema_ctrl = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5,
                                  regra6, regra7, regra8, regra9, regra10, regra11, regra12, regra13 ])
sistema = ctrl.ControlSystemSimulation(sistema_ctrl)

sistema.input['pessoas'] = int(input("Digite o número de pessoas: "))
sistema.input['vagas'] = int(input("Digite o número de vagas: "))
sistema.input['prioridade'] = float(input("Digite o número de prioridade: "))

sistema.compute()
print(sistema.output['encaminhamento'])
encaminhamento.view(sim=sistema)
plt.show()

