# AVALIAÇÃO 30 PONTOS - PRÁTICA

SELECT * FROM pedidos;

# minha consulta
SELECT c.nome, SUM(p.valor_total) AS valor_total # já que iremos agrupar, somamos o valor total
FROM clientes c
INNER JOIN pedidos p
ON c.id_cliente = p.id_cliente
GROUP BY c.id_cliente; # agrupamos pelo nome, o unico valor nao agregado (valor total está sendo somado)

# consulta otimizada pelo claude
SELECT c.nome, t.valor_total
FROM (
    SELECT id_cliente, SUM(valor_total) AS valor_total
    FROM pedidos
    GROUP BY id_cliente
) t
INNER JOIN clientes c ON c.id_cliente = t.id_cliente;
# Nessa consulta o SUM já é definido no FROM, que vem do FROM pedidos (que colocamos como T) já com o group by dentro

