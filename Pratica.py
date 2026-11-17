##10. Você foi escolhido(a) para participar da equipe responsável pelo desenvolvimento do Sistema Integrado de Atendimento ao Cidadão.
##Elabore uma proposta inicial de modelagem para esse sistema. Em sua resposta, apresente: (a) o escopo e os limites da primeira versão;
##(b) pelo menos dois requisitos funcionais e dois não funcionais; (c) duas regras de negócio;
##(d) os principais atores e suas responsabilidades;
##(e) duas premissas, duas restrições e dois riscos do projeto, apresentando possíveis soluções;
##(f) explique como utilizaria os diagramas UML de casos de uso, classes, sequência, atividades, estados e componentes;
##(g) explique como a orientação a objetos e uma ferramenta CASE podem apoiar o desenvolvimento.
##Finalize justificando como a modelagem contribui para reduzir erros, custos e retrabalho.

a) O escopo da primeira versão focaria no sistema básico, focando na interatividade base entre o cidadão e o atendente. Um sistema simples, de abertura, fiscalização e fechamento de ocorrências/manifestações.
b) Como requisitos não funcionais temos a disponibilidade 24 horas do serviço e a portabilidade para todos os tipos de dispostivos. Como Funcionais temos a entrega de emails de confirmação/fechamento de ocorrências por email, e a possibilidade de poder encontrar a localidade do usuário automaticamente com base na localização do dispositivo.
c) A primeira regra é a necessidade de inserir o CPF para fazer cadastro, a segunda é a de não poder abrir mais de 3 solicitações para a mesma categoria e o mesmo endereço ao mesmo tempo.
d) Os principais atores são os atendentes, que visualizam e podem fechar ou responder ocorrências, os administradores, que tem acesso de atendente e com recursos a mais para fazer manutenção do sistema, e o usuário final, que pode abrir e acompanhar ocorrências.
e) Uma premissa é de que os atendentes serão previamente instruídos de como usar a plataforma, a outra é de que os administradores saberão utilizar os acessos da plataforma. As restrições são parecidas com as do ponto C: Limite de 3 solicitações para o mesmo endereço e o fechamento de uma solicitação só pelo atendente, e não o usuário. De risco temos diversos, os principais sendo: Brechas de segurança, que podem ser resolvidas com autenticação de dois fatores no login, e a sobrecarga de ocorrências, que será resolvida com o limite estabelecido acima.
f) O diagrama de caso de uso será utilizado para o escopo do projeto, o de classes para uma base da organização dos dados do sistema, o de sequência, estado e de atividades para mapearmos o processo de abertura de ocorrências, e o diagrama de componentes para mapearmos o espaço físico que o sistema ocupará.
g) Podem ser utilizadas no desenvolvimento e na implementação dos recursos do sistema, para os desenvolvedores terem uma visão total do processo, por exemplo.
Uma boa modelagem reduz o retrabalho, nos entregando um mapa correto dos procedimentos a serem feitos na construção do sistema. Erros podem sempre serem cometidos, mas com uma boa modelagem fica mais fácil de "recalcular a rota" nesses casos.
